cmake_minimum_required(VERSION 3.5)

project(awtube31814v2)

# find dependencies
find_package(ament_cmake REQUIRED)
install(
  DIRECTORY
    config
    launch
    meshes
    xacro
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
