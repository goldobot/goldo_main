from goldo_main.zmq_broker import ZmqBroker
import nucleo_topics
import asyncio

import os
import os.path

import goldo_main.commands
from goldo_main import robot

async def foo(config_name, msg):
    config_path = f'config/{config_name}'
    if not os.path.isdir(config_path):
        os.mkdir(config_path)
    open(config_path+'/robot_config.bin'.format(config_name), 'wb').write(msg.SerializeToString())
    print(msg)


        
if __name__ == '__main__':
    broker = ZmqBroker()
    robot._setBroker(broker)
    broker.registerCallback('config/*/put', foo)
    broker.registerCallback('camera/out/image', lambda msg: broker.publishTopic('gui/in/camera/image', msg))
    broker.registerCallback('camera/out/detections', lambda msg: broker.publishTopic('gui/in/camera/detections', msg))
    broker.registerCallback('nucleo/out/propulsion/telemetry', lambda msg: broker.publishTopic('rplidar/in/robot_pose', msg.pose)) 
    broker.registerCallback('nucleo/out/match/timer', lambda msg: broker.publishTopic('gui/in/match_timer', msg))         
    broker.registerCallback('nucleo/out/os/heartbeat', lambda msg: broker.publishTopic('gui/in/heartbeat', msg))          
    goldo_main.commands._broker = broker
    loop = asyncio.get_event_loop()
    loop.run_until_complete(broker.run())