
cmake_minimum_required(VERSION 2.8)

project(fixed-point-number CXX)
add_executable(${PROJECT_NAME} src/main.cpp)
include_directories(./inc)

# enable C++11
if(CMAKE_COMPILER_IS_GNUCXX)
  add_definitions(-std=gnu++0x)
endif()

add_definitions(-DDEBUG_LEVEL=4)
