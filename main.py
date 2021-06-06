from goldo_main.zmq_broker import ZmqBroker
import nucleo_topics
import asyncio

from pathlib import Path

import sys

def rm_tree(path: Path):
    for child in path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()

    
async def config_put(config_name, msg):
    config_path = Path(f'config/{config_name}')
    config_path.mkdir(parents=True, exist_ok=True)
    open(config_path / 'robot_config.bin', 'wb').write(msg.SerializeToString())
    for sequences_file in msg.sequences_files:
        open(config_path / sequences_file.path, 'w').write(sequences_file.body)
    robot.loadConfig(config_path)
    
async def config_delete(config_name, msg):
    config_path = Path(f'config/{config_name}')
    rm_tree(config_path)
    
async def config_set_default(config_name, msg):
    config_path = Path('config/')
    config_path.mkdir(exist_ok=True)
    open(config_path / 'default', 'w').write(config_name)
    
async def main():
    from goldo_main.robot_main import RobotMain
    global robot
    
    broker = ZmqBroker()
    robot = RobotMain(broker)
    if 'simulation' in sys.argv:
        robot._simulation_mode = True
    broker.registerCallback('config/*/put', config_put)
    broker.registerCallback('config/*/delete', config_delete)
    broker.registerCallback('config/*/set_default', config_set_default)
    broker.registerCallback('robot/config_nucleo', robot.configNucleo)
    broker.registerCallback('camera/out/image', lambda msg: broker.publishTopic('gui/in/camera/image', msg))
    broker.registerCallback('camera/out/detections', lambda msg: broker.publishTopic('gui/in/camera/detections', msg))
    broker.registerCallback('nucleo/out/propulsion/telemetry', lambda msg: broker.publishTopic('rplidar/in/robot_pose', msg.pose)) 
    broker.registerCallback('nucleo/out/match/timer', lambda msg: broker.publishTopic('gui/in/match_timer', msg))         
    broker.registerCallback('nucleo/out/os/heartbeat', lambda msg: broker.publishTopic('gui/in/heartbeat', msg))
    await broker.run()
        
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())