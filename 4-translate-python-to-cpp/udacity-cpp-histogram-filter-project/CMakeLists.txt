project(udacity_cpp_histogram_filter_project)

cmake_minimum_required(VERSION 3.5)

add_definitions(-std=c++11)

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")

set(sources helpers.cpp localizer.cpp simulate.cpp tests.cpp)

add_executable(udacity_cpp_histogram_filter_project ${sources})
