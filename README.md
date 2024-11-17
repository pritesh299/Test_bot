
**Test_bot: An Implementation of Autonomous Navigation**

To run the simulation, source the workspace in the terminal:

```bash
source install/setup.bash
ros2 launch Test_bot launch_sim.launch.py use_sim_time:=true
```

For RViz visualization of the LiDAR, open another terminal and run:

```bash
rviz2 -d src/Test_bot/config/drive_bot.rviz
```

You can use teleop commands to control the Test_bot. Run the following in another terminal:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

For SLAM, open another terminal and run the following command. Then, tick the map option in RViz, which subscribes to the `/map` topic:

```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=src/Test_bot/config/mapper_params_online_async.yaml use_sim_time:=true
```

For Nav2, open another terminal and run the following. Then, tick the other map option in RViz, which subscribes to the `/global_costmap/costmap` topic:

```bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true
```

--- 
