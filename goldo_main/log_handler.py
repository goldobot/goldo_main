import logging
import pb2 as _pb2
LogMessage = _pb2.get_symbol('goldo.log.LogMessage')
import asyncio
import queue

class GoldoLogHandler(logging.Handler):
    def __init__(self, zmq_client):        
        logging.Handler.__init__(self)
        self.zmq_client = zmq_client
        self.loop = asyncio.get_event_loop()
        self.queue = queue.Queue()
        self._task = asyncio.create_task(self.run())
        
    async def run(self):
        while True:
            await asyncio.sleep(0.1)            
            try:
                while True:
                    msg = self.queue.get(False) # non blocking
                    await self.zmq_client.publishTopic('goldo_main/log', msg)
            except queue.Empty:
                    pass   

    def prepare(self, record):       
        msg = self.format(record)
        proto = LogMessage()
        proto.name = record.name
        proto.message = msg
        proto.pathname = record.pathname
        proto.lineno  = record.lineno
        proto.levelno  = record.levelno
        proto.func = record.funcName        
       
        #record.args = None
        #record.exc_info = None
        #record.exc_text = None
        return proto

    def emit(self, record):
        try:
            self.queue.put_nowait(self.prepare(record))
        except Exception:
            self.handleError(record)