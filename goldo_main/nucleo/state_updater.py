import asyncio

class NucleoStateUpdater(object):
    def __init__(self, robot):
        self._robot = robot
        self._broker = robot._broker
        self._nucleo_proto = self._robot._state_proto.nucleo
        self._heartbeat_received = False
        self._broker.registerCallback('nucleo/out/os/heartbeat', self.onHeartbeatMsg)
        self._broker.registerCallback('nucleo/out/os/reset', self.onResetMessage)
        self._broker.registerCallback('nucleo/out/os/task_statistics/uart_comm', self.onUartCommStatsMsg)
        self._broker.registerCallback('nucleo/out/robot/config/load_status', self.onConfigStatusMsg)
        self._broker.registerCallback('nucleo/out/os/task_statistics/uart_comm', self.onUartCommStatsMsg)
        self._broker.registerCallback('nucleo/out/os/task_statistics/odrive_comm', self.onODriveCommStatsMsg)

        self._last_uart_comm_stats_ts = 0

        self._watchdog_task = asyncio.create_task(self.runWatchdog())

    def setBroker(self, broker):
        self._broker = broker


    async def runWatchdog(self):
        while True:
            await asyncio.sleep(1)
            if not self._heartbeat_received:
                self._nucleo_proto.connected = False                
            self._heartbeat_received = False            

    async def onNucleoReset(self):
        self._nucleo_proto.Clear()

    async def onHeartbeatMsg(self, msg):
        if msg.timestamp < self._nucleo_proto.heartbeat:
            await self.onNucleoReset()
        self._nucleo_proto.heartbeat = msg.timestamp
        self._nucleo_proto.connected = True
        self._heartbeat_received = True

    async def onResetMessage(self, msg):
        await self.onNucleoReset()

    async def onConfigStatusMsg(self, msg):
        # config status is inverted in nucleo code
        self._nucleo_proto.configured = not msg.status

    async def onUartCommStatsMsg(self, msg):
        self._last_uart_comm_stats_ts = self._nucleo_proto.heartbeat
        self._nucleo_proto.tasks_statistics.uart_comm.CopyFrom(msg)

    async def onODriveCommStatsMsg(self, msg):
        self._last_odrive_comm_stats_ts = self._nucleo_proto.heartbeat
        self._nucleo_proto.tasks_statistics.odrive_comm.CopyFrom(msg)

    async def onFpgaStatsMsg(self, msg):
        pass