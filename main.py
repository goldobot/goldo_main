from goldo_main.zmq_broker import ZmqBroker
import nucleo_topics
import asyncio

import os
import os.path

async def foo(config_name, msg):
    config_path = f'config/{config_name}'
    if not os.path.isdir(config_path):
        os.mkdir(config_path)
    open(config_path+'/robot_config.bin'.format(config_name), 'wb').write(msg.SerializeToString())
    
if __name__ == '__main__':
    broker = ZmqBroker()
    broker.registerCallback('config/*/put', foo)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(broker.run())