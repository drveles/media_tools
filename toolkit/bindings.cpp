#include <pybind11/pybind11.h>
#include "video_converter.cpp"

namespace py = pybind11;

PYBIND11_MODULE(video_converter, m) {
    m.def("convert_to_x264", &convert_to_x264, "Convert video to x264 format");
}
