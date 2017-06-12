cmake_minimum_required(VERSION 2.8.3)
project(qt_gui_cpp)

# Add support for C++11
if(NOT WIN32)
  add_definitions(-std=c++11)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(pluginlib REQUIRED)
find_package(TinyXML REQUIRED)

ament_python_install_package(${PROJECT_NAME})

set(INCLUDE_DIRS include ${ament_cmake_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS} ${TinyXML_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})

set(LIBRARY_DIRS ${ament_cmake_LIBRARY_DIRS} ${pluginlib_LIBRARY_DIRS} ${TinyXML_LIBRARY_DIRS})

link_directories(${LIBRARY_DIRS})

set(LIBS ${ament_cmake_LIBRARIES} ${pluginlib_LIBRARIES} ${TinyXML_LIBRARIES})

find_package(Boost REQUIRED COMPONENTS filesystem system)

add_subdirectory(src)

install(DIRECTORY include/qt_gui_cpp/
  DESTINATION include/${PROJECT_NAME})
install(FILES plugin.xml DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(ament_cmake)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
