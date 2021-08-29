import zmq
import time
import struct
import pathlib


def main():
    ip = 'robot01'
    
    #find next filename
    i = 0
    while True:        
        log_path = pathlib.Path('recordings/rec_{}.bin'.format(i))
        if not log_path.is_file():
            break
        i += 1
    
    #open log file
    file = open(log_path, 'wb')
    start_ts = time.time()
    last_flush_ts = start_ts
    
    context = zmq.Context()    
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect('tcp://{}:3801'.format(ip))
    socket_sub.setsockopt(zmq.SUBSCRIBE,b'')
    
    while True:
        topic, full_name, payload = socket_sub.recv_multipart()
        ts = time.time()
        
        header = struct.pack('<IIII', int((ts - start_ts) * 1000), len(topic), len(full_name), len(payload))
        file.write(header)
        file.write(topic)
        file.write(full_name)
        file.write(payload)
        
        if ts - last_flush_ts >= 1:
            last_flush_ts = ts
            file.flush()
        
        
if __name__ == '__main__':
    main()