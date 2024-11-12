cmake_minimum_required(VERSION 3.12)
project(VideoConverter)

set(CMAKE_CXX_STANDARD 14)

# Указываем путь до pybind11 и FFmpeg
find_package(pybind11 REQUIRED)
find_package(FFmpeg REQUIRED)

add_library(video_converter MODULE video_converter.cpp bindings.cpp)
target_link_libraries(video_converter PRIVATE pybind11::module avcodec avformat avutil swscale)
