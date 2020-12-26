cmake_minimum_required(VERSION 3.5)

project(bmstu_aa_lab_06)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED on)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")

add_executable(lab_06 main.cpp aco.cpp bf.cpp)
target_link_libraries(lab_06 ${PTHREAD_LIBRARY})

add_executable(lab_06_test test.cpp aco.cpp bf.cpp)
target_link_libraries(lab_06_test ${PTHREAD_LIBRARY})
