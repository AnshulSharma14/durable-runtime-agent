cmake_minimum_required(VERSION 3.22)
project(durable_runtime_agent LANGUAGES CXX)
add_executable(dar src/main.cpp)
target_compile_features(dar PRIVATE cxx_std_20)
enable_testing()
add_test(NAME dar_smoke COMMAND dar)


