cmake_minimum_required(VERSION 3.1)

project(oblig6_task)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y -Wall -Wextra")

if(APPLE)
    if(EXISTS /usr/local/opt/openssl)
        set(OPENSSL_ROOT_DIR /usr/local/opt/openssl)
    elseif(EXISTS /opt/homebrew/opt/openssl)
        set(OPENSSL_ROOT_DIR /opt/homebrew/opt/openssl)
    endif()
endif()

find_package(OpenSSL REQUIRED)
include_directories(${OPENSSL_INCLUDE_DIR})

add_executable(main main.cpp)
target_link_libraries(main ${OPENSSL_CRYPTO_LIBRARY})
