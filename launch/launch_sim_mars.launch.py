import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    # Change this to your actual package name
    package_name = 'Test_bot'

    # Path to the gazebo parameters file
    gazebo_params_path = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'gazebo_params.yaml'
    )

    # Path to your mars.world file
    mars_world_path = os.path.join(
        get_package_share_directory(package_name),
        'worlds',
        'mars.world'
    )

    # Robot state publisher launch file
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')
        ]),
        launch_arguments={
            'use_sim_time': 'true',
            'use_ros2_control': 'true'
        }.items()
    )

    # Include the Gazebo launch file and load mars.world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={
            'world': mars_world_path,
            'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_path
        }.items()
    )

    # Spawner node for the robot
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_bot',
            '-x', '5', '-y', '5', '-z', '6.0'  # Adjust spawn position if needed
        ],
        output='screen'
    )

    rtabmap = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rtabmap.launch.py')
        ])
    )
    # Optional: Load your controllers here
    # diff_drive_spawner = Node(
    #     package='controller_manager',
    #     executable='spawner',
    #     arguments=['diff_cont']
    # )

    # joint_broad_spawner = Node(
    #     package='controller_manager',
    #     executable='spawner',
    #     arguments=['joint_broad']
    # )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        # diff_drive_spawner,
        # joint_broad_spawner
    ])

