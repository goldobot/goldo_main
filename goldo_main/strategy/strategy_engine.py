from enum import Enum, IntEnum
import astar
import asyncio
import logging
import math
# import pb2 as _pb2
# from goldo_main.enums import *
import google.protobuf.wrappers_pb2
import google.protobuf as _pb

from .strategy_engine_base import StrategyEngineBase, Action, Path
from .strategy_engine_base import ObstacleRectangle, ObstaclePolygon

_sym_db = _pb.symbol_database.Default()

LOGGER = logging.getLogger(__name__)


class StrategyEngine(StrategyEngineBase):
    def __init__(self, robot):
        super().__init__()
        self._robot = robot
        self._astar = astar.AStarWrapper()
        self.adversary_radius = 0.5

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
        self.create_timer_callback(timer, callback)

    @property
    def robot_state(self):
        return self._robot._state_proto

    def _get_sequence(self, sequence):
        return self._robot._sequences[sequence]

    def _update_path_planner(self):
        # reset astar costs
        # background
        self._astar.fillRect((0, -1.5), (2.0, 1.5), 1)

        # borders
        self._astar.fillRect((0, -1.5), (0.1, 1.5), 0)
        self._astar.fillRect((1.9, -1.5), (2.0, 1.5), 0)
        self._astar.fillRect((0, -1.5), (2.0, -1.4), 0)
        self._astar.fillRect((0, 1.4), (2.0, 1.5), 0)

        # angle corners
        self._astar.fillPoly([(1.3, -1.5), (2.0, -0.7), (2.0, -1.5)], 0)
        self._astar.fillPoly([(1.3, 1.5), (2.0, 0.7), (2.0, 1.5)], 0)

        for k, v in self.obstacles.items():
            if not v.enabled:
                continue
            if isinstance(v, ObstaclePolygon):
                self._astar.fillPoly(v.points, 0)
            if isinstance(v, ObstacleRectangle):
                self._astar.fillRect(v.p1, v.p2, 0)

        for d in self._robot._state_proto.rplidar_detections:
            self._astar.fillDisk((d.x, d.y), self.adversary_radius, 0)

        msg = _sym_db.GetSymbol('google.protobuf.BytesValue')(value=self._astar.getArr())
        self._create_task(self._robot._broker.publishTopic('strategy/debug/astar_arr', msg))

    def _compute_path(self, action: Action) -> Path:
        pose_proto = self._robot._state_proto.robot_pose

        # clamp pose to table size
        begin_x = pose_proto.position.x
        begin_y = pose_proto.position.y

        if begin_x < 0:
            begin_x = 0
        if begin_x > 2.0:
            begin_x = 2.0
        if begin_y < -1.5:
            begin_y = -1.5
        if begin_y > 1.5:
            begin_y = 1.5

        astar_path = self._astar.computePath((begin_x, begin_y),
                                             (action.begin_pose[0], action.begin_pose[1]))
        if len(astar_path) < 2:
            print('NO PATH', action)
            return None
        return Path(points=astar_path, begin_yaw=pose_proto.yaw, end_yaw=action.begin_pose[2] * math.pi / 180)

    async def _execute_move(self, path):
        LOGGER.info('execute move to action: %s', self._target_action.name)
        propulsion = self._robot.propulsion
        try:
            await propulsion.pointTo(path.points[1])
            await propulsion.trajectorySpline(path.points)
            await propulsion.faceDirection(path.end_yaw * 180 / math.pi)
        except:
            await propulsion.clearError()
            raise

    def _onMatchTimer(self, value):
        self._on_match_timer(value)
