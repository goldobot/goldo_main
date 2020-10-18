from zmq_broker import ZmqBroker
import asyncio

if __name__ == '__main__':
    broker = ZmqBroker()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(broker.run())