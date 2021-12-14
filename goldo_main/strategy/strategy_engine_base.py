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
    Abort = 5
    # Finalize
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
    


class StrategyEngineBase:
    _actions: Sequence[Action] = []
    _actions_by_name: Mapping[str, Action] = {}
    _current_sequence: Optional[asyncio.Task] = None
    _sequence_state: SequenceState = SequenceState.Idle
    _movement_state: MovementState = MovementState.Idle
    _timer_callbacks: Sequence[Tuple[float, Callable[[None], Awaitable[None]]]] = []
    _tasks: Mapping[int, asyncio.Task] = {}

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
        

    def reset(self):
        self._actions_by_name = {}
        self._actions = []
        self._current_sequence = None
        self._sequence_state = SequenceState.Idle
        self._movement_state = MovementState.Idle

    async def run(self):
        # test
        self._running = True
        try:
            await self._execute_sequence('start_match')
        except asyncio.CancelledError:
            raise
        except Exception:
            LOGGER.exception('error in start_match sequence')

        print('finish start match')
        LOGGER.debug('selected FOO: ')
        action, path = self._select_next_action()
        if action is not None:
            LOGGER.debug('selected action: %s', action.name)
        self._start_go_action(action, path)

        while self._running:
            await asyncio.sleep(1)

    def _start_go_action(self, action, path):
        self.current_action = action
        # todo also start trajectory to new path
        if action.sequence_prepare is not None:
            self._start_sequence(action.sequence_prepare)
            self._current_sequence.add_done_callback(self._on_prepare_done)
            self._sequence_state = SequenceState.Prepare
        else:
            self._sequence_state = SequenceState.PrepareFinished

        self._current_move = asyncio.create_task(self._execute_move(path))
        self._current_move.add_done_callback(self._on_move_done)
        self._movement_state = MovementState.Moving

    def _start_current_action(self):
        """Start executing current action"""
        action = self.current_action
        self._start_sequence(action.sequence)
        self._current_sequence.add_done_callback(self._on_sequence_done)
        self._sequence_state = SequenceState.Sequence

    async def _execute_move(self):
        await asyncio.sleep(2)

    def _select_next_action(self) -> Tuple[Action, Path]:
        self._actions.sort(key=lambda action: -action.priority)
        for action in self._actions:
            if action.enabled:
                path = self._compute_path(action)
                if path is not None:
                    return action, path
        return None, None

    def _compute_path(self, action: Action) -> Path:
        return Path()

    def _on_prepare_done(self, task):
        try:
            if task is not None:
                task.result()
        except:
            LOGGER.exception(f'{self.current_action.name}: exception in prepare')
            return
        LOGGER.debug(f'{self.current_action.name}: prepare done')
        if self._movement_state == MovementState.Ready:
            # movement already finished, start action immediatelly
            self._start_current_action()
        else:
            self._sequence_state = SequenceState.PrepareFinished

    def on_abort_finished(self, task):
        pass

    def _on_finalize_done(self, task):
        try:
            if task is not None:
                task.result()
        except:
            LOGGER.exception(f'{self.previous_action.name}: exception in finalize')
            return
        LOGGER.debug(f'{self.previous_action.name}: finalize done')
        action = self.current_action
        if action is None:
            self._sequence_state = SequenceState.Idle
            return
        if action.sequence_prepare is not None:
            self._start_sequence(action.sequence_prepare)
            self._current_sequence.add_done_callback(self._on_prepare_done)
            self._sequence_state = SequenceState.Prepare
        else:
            self._current_sequence = None
            self._on_prepare_done(None)

    def _on_move_done(self, task):
        try:
            if task is not None:
                task.result()
        except:
            LOGGER.exception(f'{self.previous_action.name}: exception in move')
            return

        LOGGER.debug(f'{self.current_action.name}: move done')
        self._movement_state = MovementState.Ready
        if self._sequence_state == SequenceState.PrepareFinished:
            # movement already finished, start action immediatelly
            self._start_current_action()

    def _on_sequence_done(self, task):
        try:
            task.result()
        except:
            LOGGER.exception(f'{self.current_action.name}: exception in sequence')
            return
        LOGGER.debug(f'{self.current_action.name}: sequence done')

        self.previous_action = self.current_action

        if self.previous_action.sequence_finalize is not None:
            # finalize previous sequence
            self._start_sequence(self.previous_action.sequence_finalize)
            self._current_sequence.add_done_callback(self._on_finalize_done)
            self._sequence_state = SequenceState.Finalize
        else:
            self._sequence_state = SequenceState.Idle

        # select next action
        action, path = self._select_next_action()
        if action is None:
            LOGGER.debug('no new action found')
            return

        self.current_action = action

        # prepare current sequence
        if action.sequence_prepare is not None:
            self._start_sequence(action.sequence_prepare)
            self._current_sequence.add_done_callback(self._on_prepare_done)
            self._sequence_state = SequenceState.Prepare
        else:
            self._sequence_state = SequenceState.PrepareFinished

        self._current_move = asyncio.create_task(self._execute_move(path))
        self._current_move.add_done_callback(self._on_move_done)
        self._movement_state = MovementState.Moving

    def _create_task(self, awaitable):
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
