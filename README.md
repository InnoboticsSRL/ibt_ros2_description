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
│       ├── collision
│       │   ├── *.STL
│       └── visual
│           ├── *.STL
└── xacro
    ├── robofox.urdf
    ├── robofox.urdf.xacro
    └── robofox.xacro

```