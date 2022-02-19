all:zmq_broker

zmq_broker:
	g++ zmq_broker.cpp -std=c++11 -I/usr/include/python3.7 -lzmq -lpython3.7m -o zmq_broker

clean:
	rm -f *.o zmq_broker
