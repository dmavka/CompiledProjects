cmake_minimum_required(VERSION 3.10)
project(imager C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic")
endif()

add_executable(${PROJECT_NAME} imager.c)

set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME ${PROJECT_NAME})
target_link_libraries(${PROJECT_NAME} LINK_PRIVATE curl)
target_link_libraries(${PROJECT_NAME} LINK_PRIVATE SDL2)
target_link_libraries(${PROJECT_NAME} LINK_PRIVATE SDL2_image)

include(GNUInstallDirs)
install(TARGETS imager RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

install(FILES imager.desktop
    DESTINATION ${CMAKE_INSTALL_DATADIR}/applications)


