# @brief     Launch file for visualizing the models of the robofox robot
#
# @author    Mattia Dei Rossi <mattia.deirossi@innobotics.it>
# @copyright (C) IBT


import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "robofox_type",
            description="Type/series of used IBT robot.",
            choices=["robofox_61814v3"],
            default_value="robofox_61814v3",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value='robofox',
            description="Prefix of the joint names, useful for multi-robot setup."
        )
    )

    robofox_type = LaunchConfiguration("robofox_type")
    prefix = LaunchConfiguration("prefix")
    
    pkg_dir = get_package_share_directory('ibt_ros2_description')

    # Configuration files
    xacro_file = os.path.join(pkg_dir, 'xacro', 'robofox.urdf.xacro')
    robot_description = Command([FindExecutable(name='xacro'),
                                 ' ', xacro_file,
                                 ' ', 'name:=robofox',
                                 ' ', 'robofox_type:=', robofox_type,
                                 ' ', 'prefix:=', prefix
                                 ])
    rviz_config_path = os.path.join(pkg_dir, 'config', 'config.rviz')

    # Nodes
    robot_state_publisher_node = Node(
        name='robot_state_publisher',
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robot_description}
        ]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=[
            '-d', rviz_config_path
        ]
    )
    nodes = [
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ]

    return LaunchDescription(declared_arguments + nodes)
