#include "zmq.hpp"
#include "zmq_addon.hpp"

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cstdint>

#include <iostream>
#include <string>

void *zmq_context;

void *pub_socket;
void *sub_socket;

void *pub_socket_comm_uart;
void *sub_socket_comm_uart;

void *pub_socket_lidar;
void *sub_socket_lidar;

zmq_pollitem_t poll_items[3];

zmq::context_t mCtx;
std::vector<zmq::socket_t> mSocketsPub;
std::vector<zmq::socket_t> mSocketsSub;

std::vector<zmq_pollitem_t> mPollItems;

void publishTopic(const std::string &topic_name,
                  const std::string &message_type, const std::string &payload){
    // if(topic_name.

};

bool initZmqSockets() {
  // main publish socket
  zmq::socket_t sock_pub(mCtx, zmq::socket_type::pub);
  sock_pub.bind("tcp://*:3801");

  // main subscribe socket
  zmq::socket_t sock_sub(mCtx, zmq::socket_type::sub);
  sock_sub.bind("tcp://*:3802");
  sock_sub.set(zmq::sockopt::subscribe, "");

  // nucleo publish socket
  zmq::socket_t sock_pub_nucleo(mCtx, zmq::socket_type::pub);
  sock_pub.bind("tcp://*:3803");

  // nucleo subscribe socket
  zmq::socket_t sock_sub_nucleo(mCtx, zmq::socket_type::sub);
  sock_sub_nucleo.bind("tcp://*:3804");
  sock_sub_nucleo.set(zmq::sockopt::subscribe, "");

  mSocketsPub.emplace_back(std::move(sock_pub));
  mSocketsPub.emplace_back(std::move(sock_pub_nucleo));

  mSocketsSub.emplace_back(std::move(sock_sub));
  mSocketsSub.emplace_back(std::move(sock_sub_nucleo));

  mPollItems.reserve(mSocketsSub.size());
  for (auto &socket : mSocketsSub) {
    mPollItems.push_back(zmq_pollitem_t{(void *)socket, 0, ZMQ_POLLIN, 0});
  }

  return true;
}

int main(int argc, char *argv[]) {

  Py_Initialize();

  std::cout << "init";
  initZmqSockets();

  while (true) {
    zmq_poll(mPollItems.data(), mPollItems.size(), 10);
    for (int i = 0; i < mPollItems.size(); i++) {
      if (mPollItems[i].revents && ZMQ_POLLIN) {
        auto &socket = mSocketsSub[i];

        std::vector<zmq::message_t> recv_msgs;
        const auto ret =
            zmq::recv_multipart(socket, std::back_inserter(recv_msgs));
        std::cout << recv_msgs[0].to_string() << std::endl;
      };
    }
  };

  // generic sockets
  /*




      while(true)
      {
              std::string topic_name;
              std::string message_type;
              std::string payload;

              topic_name.resize(1024);
              message_type.resize(1024);
              payload.resize(1024*1024*16);

              zmq_poll(poll_items, 2, 10);

      // Read data from uart
      if(poll_items[0].revents && ZMQ_POLLIN)
      {
          int rdlen;

          rdlen = read(fd, tmp_buffer, sizeof(tmp_buffer));
          deserializer.push_data(tmp_buffer, rdlen);

          while(deserializer.message_ready())
          {
              uint16_t recv_message_type = deserializer.message_type();
              size_t recv_message_size = deserializer.message_size();
              deserializer.pop_message(tmp_buffer, sizeof(tmp_buffer));

              zmq_send(pub_socket, (const char*)(&recv_message_type), 2,
  ZMQ_SNDMORE); zmq_send(pub_socket, (const char*)(tmp_buffer),
  recv_message_size, 0);
          }
      }
      }	*/
}