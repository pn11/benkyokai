cmake_minimum_required(VERSION 2.8)

project(socket)
add_executable(${PROJECT_NAME}_server server.cpp)
add_executable(${PROJECT_NAME}_client client.cpp)

# enable C++11
if(CMAKE_COMPILER_IS_GNUCXX)
  add_definitions(-std=gnu++0x)
endif()
