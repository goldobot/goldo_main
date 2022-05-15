from enum import Enum, IntEnum
import astar
import asyncio
import logging
import math
import pb2 as _pb2
from goldo_main.enums import *
import google.protobuf as _pb

from .strategy_engine_base import StrategyEngineBase, Action, Path

_sym_db = _pb.symbol_database.Default()

LOGGER = logging.getLogger(__name__)


class StrategyEngine(StrategyEngineBase):
    def __init__(self, robot):
        super().__init__()
        self._robot = robot
        self._astar = astar.AStarWrapper()

    async def try_astar(self):
        # return
        self._astar.resetCosts()
        # self._astar.fillRect(35,0,125, 55)
        if self._robot.side == Side.Blue or True:
            # port
            # self._astar.fillRect(200-55,90,200, 150)
            # adversary start area
            # self._astar.fillRect(35,300-55,125, 300)
            # self._astar.fillRect(0,300-55,35, 300)
            # self._astar.fillRect(125,300-55,165, 300)
            pass

        self._astar.setDisk((1.7, -0.3), 30)

        msg = _sym_db.GetSymbol('google.protobuf.BytesValue')(value=self._astar.getArr())

        await self._robot._broker.publishTopic('strategy/debug/astar_arr', msg)
        print(self._astar.computePath((1.8, -1.3), (1.8, 1.3)))

    async def display_astar(self):
        msg = _sym_db.GetSymbol('google.protobuf.BytesValue')(value=self._astar.getArr())
        await self._robot._broker.publishTopic('strategy/debug/astar_arr', msg)

    def addTimerCallback(self, timer, callback):
        self._timer_callbacks.append((timer, callback))

    @property
    def robot_state(self):
        return self._robot._state_proto

    def _get_sequence(self, sequence):
        return self._robot._sequences[sequence]

    def _compute_path(self, action: Action) -> Path:
        pose_proto = self._robot._state_proto.robot_pose
        # reset astar costs
        # background
        self._astar.fillRect((0, -1.5), (2.0, 1.5), 1)

        # borders
        self._astar.fillRect((0, -1.5), (0.1, 1.5), 0)
        self._astar.fillRect((1.9, -1.5), (2.0, 1.5), 0)
        self._astar.fillRect((0, -1.5), (2.0, -1.4), 0)
        self._astar.fillRect((0, 1.4), (2.0, 1.5), 0)

        astar_path = self._astar.computePath((pose_proto.position.x, pose_proto.position.y),
                                             (action.begin_pose[0], action.begin_pose[1]))
        return Path(points=astar_path, begin_yaw=pose_proto.yaw, end_yaw=action.begin_pose[3] * math.pi / 180)

    async def _execute_move(self):
        await asyncio.sleep(2)

    def _onMatchTimer(self, value):
        l = []
        for timer, callback in self._timer_callbacks:
            if value <= timer:
                task = asyncio.create_task(callback())
                self._tasks[id(task)] = task
            else:
                l.append((timer, callback))
        self._timer_callbacks = l
