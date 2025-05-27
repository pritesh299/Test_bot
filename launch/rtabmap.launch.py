# Requirements:
#   A realsense D455series
#   Install realsense2 ros2 package (make sure you have this patch: https://github.com/IntelRealSense/realsense-ros/issues/2564#issuecomment-1336288238)
# Example:
#   $ ros2 launch rtabmap_examples realsense_d400.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    parameters=[{
          'frame_id':'base_footprint',
          'subscribe_depth':True,
          'subscribe_odom_info':True,
          'wait_imu_to_init':True,
          'approx_sync':False}]

    remappings=[
          ('/odom', '/visual_odom'),
          ('/imu', '/imu/out'),
          ('rgb/image', '/camera/image_raw'),
          ('rgb/camera_info', '/camera/depth/camera_info'),
          ('depth/image', '/camera/depth/image_raw')]    
    
 

    return LaunchDescription([

        Node(
            package='rtabmap_odom', executable='rgbd_odometry', output='screen',
            parameters=parameters,
            remappings=remappings,
            arguments=['--ros-args', '--log-level', 'error']),

        # Node(
        #     package='rtabmap_slam', executable='rtabmap', output='screen',
        #     parameters=parameters,
        #     remappings=remappings,
        #     arguments=['--ros-args', '--log-level', 'error']),

        Node(
            package='rtabmap_viz', executable='rtabmap_viz', output='screen',
            parameters=parameters,
            remappings=remappings,
            arguments=['--ros-args', '--log-level', 'error']),
    ])