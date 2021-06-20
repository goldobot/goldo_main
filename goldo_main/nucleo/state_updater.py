
import asyncio

class NucleoStateUpdater(object):
    def __init__(self):
        pass
        
        
    def setBroker(self, broker):
        self._broker = broker
        self._watchdog_task = asyncio.create_task(self.runWatchdog())
        
    async def runWatchdog(self):
        while True:
            await asyncio.sleep(1)
            
        
    def onNucleoReset(self):
        pass
        
    def onHeartbeatMsg(self, msg):
        pass
        
    def onResetMessage(self, msg):
        pass
        
    def onUartCommStatsMsg(self, msg):
        pass
        
    def onODriveCommStatsMsg(self, msg):
        pass
        
    def onFpgaStatsMsg(self, msg):
        pass
        
        