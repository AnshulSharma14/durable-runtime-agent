cmake_minimum_required(VERSION 3.22)
project(durable_runtime_agent LANGUAGES CXX)
add_executable(dar src/main.cpp)
target_compile_features(dar PRIVATE cxx_std_20)
enable_testing()
find_package(Python3 REQUIRED COMPONENTS Interpreter)

add_test(
    NAME dar_cli_contract
    COMMAND "${Python3_EXECUTABLE}"
            "${CMAKE_CURRENT_SOURCE_DIR}/tests/test_cli.py"
            "$<TARGET_FILE:dar>"
)

