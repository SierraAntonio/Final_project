# Final_project
Proyecto final de la materia de diseño de sistemas roboticas UDLAP LRT4102-1

**WATER CLEANING ROBOT**
----------------------------
I designed AquaCleaner as an autonomous floating robot to tackle water pollution and support UN Sustainable Development Goal 6.6 (protecting and restoring freshwater ecosystems). My goal was to create an affordable, scalable solution to remove trash from lakes and rivers while monitoring water quality—using ROS2 for intelligent autonomy and Arduino for robust hardware control.
Developed by student from Universidad de las Américas Puebla (UDLAP)
![Image](https://github.com/user-attachments/assets/20d7e44a-f680-4475-9b4c-3b9e72525e9b)
![Image](https://github.com/user-attachments/assets/290dbe6c-30f9-46b8-9c4c-bcf27c9b200d)
![Image](https://github.com/user-attachments/assets/058b3000-cdf5-4cec-b9f0-9aea06dea040)
---------------------------------------------------------------------
1. Vision System
USB Camera

Purpose: Real-time color detection (red/green objects) using OpenCV in ROS2.

Processing: HSV color space segmentation with thresholds (lower_red1, upper_red1, lower_green, etc.).

Output: Publishes detection status to ROS2 topics (e.g., "red_detected", "green_detected").

2. Motor Control
Arduino Mega

Role: Low-level motor control via H-bridge (L298N).

Actuators:

2x DC Motors (12V) for propulsion.

3D-Printed Propellers (iterated for thrust optimization).

ROS2 Integration: Serial communication (/dev/ttyACM0) with Python ROS nodes sending commands (b'A', b'S', b'B').

3. Power Management
Power Bank + 2x 9V Batteries

Purpose: Dual power supply for Raspberry Pi (ROS2) and Arduino/motors.

4. Structural Components
PVC Pipes + Styrofoam

Design: Lightweight floating base with net storage for debris.

Buoyancy: Validated through pool testing.

5. Software Stack
ROS2 Humble (Ubuntu 22.04)

Nodes:

vision_node: Color detection (Python/OpenCV).

control_node: Serial communication with Arduino.

main_node: State machine logic (INITIAL, BOTH_ON, POST_COLOR_WAIT).

Dependencies: pyserial, numpy, opencv-python.

6. Testing & Validation
Success Metrics:

90% detection accuracy for red/green objects.

2-second motor response latency.

Limitations:

Propeller thrust insufficient for strong currents.

Lighting conditions affected detection reliability
