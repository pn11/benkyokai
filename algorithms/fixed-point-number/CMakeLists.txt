
cmake_minimum_required(VERSION 2.8)

project(fixed-point-number CXX)
add_executable(${PROJECT_NAME} src/main.cpp)
include_directories(./inc)

# enable C++11
if(CMAKE_COMPILER_IS_GNUCXX)
  add_definitions(-std=gnu++0x)
endif()


if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
