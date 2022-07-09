import zmq
import time
import sys
import struct
import pathlib

_msg_type_struct = struct.Struct('<BBHIi')
_prop_event_struct = struct.Struct('<IHBB')

def main():
    #open log file
    #log_file = open(out_path, 'wb')
    start_ts = time.time()
    last_flush_ts = start_ts
    
    context = zmq.Context()    
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect('tcp://{}:3002'.format("192.168.0.211"))
    socket_sub.setsockopt(zmq.SUBSCRIBE,b'')
    
    while True:
        msg_header,payload = socket_sub.recv_multipart()
        ts = time.time()
        
        #header = struct.pack('<IIII', int((ts - start_ts) * 1000), len(topic), len(full_name), len(payload))
        comm_id, reserved, msg_type, t_seconds, t_nanoseconds = _msg_type_struct.unpack(msg_header)
        if (msg_type!=0) and (msg_type!=1) and (msg_type!=2) and (msg_type!=10) and (msg_type!=33) and (msg_type!=44) and (msg_type!=120) and (msg_type!=122) and (msg_type!=180) and (msg_type!=181) and (msg_type!=182) and (msg_type!=300) and (msg_type!=301) and (msg_type!=302):
            print ("msg_type={}".format(msg_type))
            if (msg_type==130):
                #print ("len(payload)={}".format(len(payload)))
                ev_ts, ev_seq, ev_event, ev_error = _prop_event_struct.unpack(payload)
                print ("ev_ts={}, ev_seq={}, ev_event={}, ev_error={}".format(ev_ts, ev_seq, ev_event, ev_error))
        
        if ts - last_flush_ts >= 1:
            last_flush_ts = ts
            #log_file.flush()
    
if __name__ == '__main__':
    main()
