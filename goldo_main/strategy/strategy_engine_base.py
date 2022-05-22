from enum import Enum, IntEnum

import asyncio
import logging
import math

from typing import Sequence, Optional, Tuple, Mapping, Callable, Awaitable
from dataclasses import dataclass, field

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class MovementState(IntEnum):
    # not moving
    Idle = 0
    # in prepare_sequence
    Moving = 1
    # ready
    Ready = 2
    # has had an error
    Error = 3


class SequenceState(IntEnum):
    # not executing sequence
    Idle = 0
    # in prepare_sequence
    Prepare = 1
    # ready
    PrepareFinished = 2
    # in prepare_cancel_sequence
    Cancel = 3
    # sequence
    Sequence = 4
    # sequence abort
    Abort = 5
    # finalize
    Finalize = 6


@dataclass
class Action:
    name: str
    enabled: bool = False
    priority: int = 0
    # robot will move to begin_pose before executing action. (x, y, yaw in degrees)
    begin_pose: Tuple[float, float, float] = (0, 0, 0)
    # sequence to execute when robot has arrived at begin_pose
    sequence: Optional[str] = None
    # sequence to execute during move to begin_pose
    sequence_prepare: Optional[str] = None
    # sequence to execute after sequence_prepare if action is cancelled (because an adversary moved)
    sequence_cancel: Optional[str] = None
    # sequence to execute after sequence_prepare if action is aborted (because an adversary moved)
    sequence_abort: Optional[str] = None
    # sequence to execute after sequence, during move to next action
    sequence_finalize: Optional[str] = None


@dataclass
class Path:
    points: Sequence[Tuple[float, float]] = field(default_factory=lambda: [])
    begin_yaw: float = 0
    end_yaw: float = 0

    @property
    def valid(self):
        return len(self.points) >= 2


@dataclass
class ObstaclePolygon:
    name: str
    enabled: bool = False
    points: Sequence[Tuple[float, float]] = field(default_factory=lambda: [])


@dataclass
class ObstacleRectangle:
    name: str
    enabled: bool = False
    p1: [Tuple[float, float]] = (0, 0)
    p2: [Tuple[float, float]] = (0, 0)


class StrategyEngineBase:
    current_action: Optional[Action] = None
    _target_action: Optional[Action] = None
    _previous_action: Optional[Action] = None
    _obstacles: Mapping[str, object] = {}
    _actions: Sequence[Action] = []
    _actions_by_name: Mapping[str, Action] = {}
    _current_sequence: Optional[asyncio.Task] = None
    _sequence_state: SequenceState = SequenceState.Idle
    _movement_state: MovementState = MovementState.Idle
    _timer_callbacks: Sequence[Tuple[float, Callable[[None], Awaitable[None]]]] = []
    _tasks: Mapping[int, asyncio.Task] = {}
    _closing: bool = False
    _aborting: bool = True


    move_counter: int = 0

    @property
    def actions(self):
        return self._actions_by_name

    def create_action(self, name, **kwargs) -> Action:
        action = Action(name=name, **kwargs)
        self._actions_by_name[action.name] = action
        self._actions.append(action)
        return action

    @property
    def obstacles(self):
        return self._obstacles

    def create_obstacle_polygon(self, name, **kwargs) -> ObstaclePolygon:
        obstacle = ObstaclePolygon(name, **kwargs)
        self._obstacles[name] = obstacle
        return obstacle

    def create_obstacle_rectangle(self, name, **kwargs) -> ObstaclePolygon:
        obstacle = ObstacleRectangle(name, **kwargs)
        self._obstacles[name] = obstacle
        return obstacle

    def reset(self):
        self._actions_by_name = {}
        self._actions = []
        self._obstacles = {}
        self._current_sequence = None
        self._sequence_state = SequenceState.Idle
        self._movement_state = MovementState.Idle


        # todo debug
        self.move_counter = 0

    async def run(self):
        # test
        self._running = True
        self._closing = False
        try:
            await self._execute_sequence('start_match')
        except asyncio.CancelledError:
            raise
        except Exception:
            LOGGER.exception('error in start_match sequence')
        try:
            print('finish start match')
            self._schedule_next_action()

            # todo: await on future
            while self._running:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            LOGGER.debug('strategy engine run cancelled')
            self._closing = True
            for k, v in self._tasks:
                v.cancel()

    def _start_current_action(self):
        """Start executing current action"""
        action = self._target_action
        self.current_action = action
        self._start_sequence(action.sequence)
        self._current_sequence.add_done_callback(self._on_sequence_done)
        self._sequence_state = SequenceState.Sequence

    def _update_path_planner(self):
        pass

    async def _execute_move(self):
        await asyncio.sleep(2)

    def _select_next_action(self) -> Tuple[Action, Path]:
        self._update_path_planner()
        self._actions.sort(key=lambda action: -action.priority)
        for action in self._actions:
            if action.enabled:
                path = self._compute_path(action)
                if path is not None:
                    return action, path
        return None, None

    def _schedule_next_action(self):
        if self._closing:
            return
        self._previous_action = self._target_action
        action, path = self._select_next_action()
        self._target_action = action
        if action != self._previous_action:
            self._start_cancel()

        if action is None:
            loop = asyncio.get_event_loop()
            loop.call_later(0.1, self._schedule_next_action)
        else:
            LOGGER.debug('selected action: %s', action.name)
            self._start_move(path)
            self._start_prepare()

    def _start_prepare(self):
        if self._closing:
            return
        if self._sequence_state != SequenceState.Idle:
            return
        self._previous_action = self._target_action
        # execute prepare sequence if it is defined, else jump PrepareFinished state
        if self._target_action.sequence_prepare is not None:
            self.current_action = self._target_action
            self._start_sequence(self._target_action.sequence_prepare)
            self._current_sequence.add_done_callback(self._on_prepare_done)
            self._sequence_state = SequenceState.Prepare
        else:
            self._on_prepare_done()

    def _start_cancel(self):
        if self._sequence_state != SequenceState.PrepareFinished:
            return
        # execute cancel sequence if it is defined, else jump Idle state
        if self._previous_action.sequence_cancel is not None:
            self.current_action = self._previous_action
            self._start_sequence(self._previous_action.sequence_cancel)
            self._current_sequence.add_done_callback(self._on_cancel_done)
            self._sequence_state = SequenceState.Cancel
        else:
            self._previous_action = None
            self._sequence_state = SequenceState.Idle
            if self._target_action is not None:
                self._start_prepare()

    def _start_move(self, path: Path):
        self._current_move = asyncio.create_task(self._execute_move(path))
        self._current_move.add_done_callback(self._on_move_done)
        self._movement_state = MovementState.Moving

    def _compute_path(self, action: Action) -> Path:
        return Path()

    def _on_prepare_done(self, task: asyncio.Task = None) -> None:
        self.current_action = None
        if self._closing:
            return
        try:
            if task is not None:
                task.result()
        except Exception:
            LOGGER.exception(f'{self._target_action.name}: exception in prepare')
            # todo: cancel move, launch recovery sequence, schedule next action
            return

        LOGGER.debug(f'{self._target_action.name}: prepare done')
        self._sequence_state = SequenceState.PrepareFinished

        # current action changed du to rescheduling, must cancel action that finished preparing
        if self._target_action != self._previous_action:
            self._start_cancel()
            return

        if self._movement_state == MovementState.Ready:
            # movement already finished, start action immediately
            self._start_current_action()

    def _on_cancel_finished(self, task):
        self.current_action = None
        self._previous_action = None
        if self._target_action is not None:
            self._start_prepare()

    def _on_finalize_done(self, task: asyncio.Task = None):
        self.current_action = None
        try:
            if task is not None:
                task.result()
        except Exception:
            LOGGER.exception(f'{self._previous_action.name}: exception in finalize')
            return
        LOGGER.debug(f'{self._previous_action.name}: finalize done')

        self._previous_action = None
        self._sequence_state = SequenceState.Idle

        if self._target_action is not None:
            self._start_prepare()

    def _on_move_error(self):
        self._update_path_planner()
        path = self._compute_path(self._target_action)
        if path is not None:
            # reschedule move with current action
            self._current_move = asyncio.create_task(self._execute_move(path))
            self._current_move.add_done_callback(self._on_move_done)
            # todo: maybe retry counter
            return

        self._schedule_next_action()

    def _on_move_done(self, task):
        try:
            if task is not None:
                task.result()
        except Exception:
            LOGGER.exception(f'{self._target_action.name}: exception in move')
            self._on_move_error()

        LOGGER.debug(f'{self._target_action.name}: move done')
        self._movement_state = MovementState.Ready
        if self._sequence_state == SequenceState.PrepareFinished:
            # movement already finished, start action immediatelly
            self._start_current_action()

    def _on_sequence_done(self, task):
        try:
            task.result()
        except:
            LOGGER.exception(f'{self._target_action.name}: exception in sequence')
            return
        LOGGER.debug(f'{self._target_action.name}: sequence done')

        self._previous_action = self._target_action

        if self._previous_action.sequence_finalize is not None:
            # finalize previous sequence
            self._start_sequence(self._previous_action.sequence_finalize)
            self._current_sequence.add_done_callback(self._on_finalize_done)
            self._sequence_state = SequenceState.Finalize
        else:
            self._sequence_state = SequenceState.Idle

        self._schedule_next_action()

    def _create_task(self, awaitable):
        if self._closing == True:
            LOGGER.error('try to create task while closing')
            return
        task = asyncio.create_task(awaitable)
        self._tasks[id(task)] = task
        task.add_done_callback(self._on_task_done)
        return task

    def _on_task_done(self, task):
        del self._tasks[id(task)]

    def _start_sequence(self, sequence):
        self._current_sequence = asyncio.create_task(self._get_sequence(sequence)())

    async def _execute_sequence(self, sequence):
        await self._get_sequence(sequence)()

    def _execute_trajectory(self, path: Path):
        pass
