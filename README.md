# IBT ROS2 description
Nomenclature: 
- Name of the product + DOF (6) + payload (18 kg) + reach (14, 1400 mm) + version of URDF (v2)

## Folder structure
The entrypoint is `robofox.urdf.xacro` and it contains the kinematic chain of robofox with the parameters getted from the files `.yaml` contained in the correspoding config folder
```
ibt_ros2_description
├── config
│   ├── config.rviz
│   └── robofox_61814v3
│       ├── joint_limits.yaml
│       └── physical_parameters.yaml
├── launch
│   └── robofox_display.launch.py
├── meshes
│   └── robofox_61814v3
│       └── visual
│           ├── *.STL
└── xacro
    ├── robofox.urdf
    ├── robofox.urdf.xacro
    └── robofox.xacro

```

## How to use
If you want to use `*.urdf` file remeber to regenerate it after changing of parameters `joint_limits.yaml` and `physical_parameters.yaml` using the command
```bash
~/ibt_ros2_description/xacro$ . ../install/setup.bash 
~/ibt_ros2_description/xacro$ xacro robofox.urdf.xacro > robofox.urdf
```