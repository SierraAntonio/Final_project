# Final_project
 
 UDLAP LRT4102-1

**WATER CLEANING ROBOT**
----------------------------
I designed AquaCleaner as an autonomous floating robot to tackle water pollution and support UN Sustainable Development Goal 6.6 (protecting and restoring freshwater ecosystems). My goal was to create an affordable, scalable solution to remove trash from lakes and rivers while monitoring water quality—using ROS2 for intelligent autonomy and Arduino for robust hardware control.
Autonomous robot for UN SDG 6.6, built with:
- ROS2 Humble (Python)
- Arduino Mega
- OpenCV color detection

## Gallery
| Software | Hadware | Language |
|----------|-------------|---------|
| ![Image](https://github.com/user-attachments/assets/ba29d53e-6dfa-47d1-b6b1-9304f1ada48d) | ![image](https://github.com/user-attachments/assets/dede4016-bc5f-4181-8ec5-300de8afe694)
 | ![Image](https://github.com/user-attachments/assets/058b3000-cdf5-4cec-b9f0-9aea06dea040) 
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

## 🛠️ Hardware & Software Components

| Category          | Component               | Specification/Model              | Purpose                                                                 | Notes                              |
|-------------------|-------------------------|----------------------------------|-------------------------------------------------------------------------|------------------------------------|
| **Computing**     | Raspberry Pi 4          | Model B (4GB RAM)                | Runs ROS2 Humble (Ubuntu 22.04) for autonomy and vision processing.     | Borrowed from UDLAP lab.           |
|                   | Arduino Mega 2560       | ATmega2560                       | Controls motors via H-bridge (L298N).                                   | Communicates with ROS2 via serial. |
| **Sensors**       | USB Camera              | Generic (e.g., Raspberry Pi Cam) | Detects red/green objects using OpenCV (HSV color space).               | Thresholds: `lower_red1=[0,100,100]`, `upper_green=[80,255,255]`. |
| **Actuators**     | DC Motors               | 12V, 2x                          | Propels the robot in water.                                             | Connected via L298N H-bridge.      |
|                   | 3D-Printed Propellers   | Custom design                    | Converts motor rotation to thrust.                                      | Iterated for better efficiency.    |
| **Power**         | Power Bank              | 10,000mAh+                       | Powers Raspberry Pi.                                                    | Purchased.                         |
|                   | 9V Batteries            | 2x                               | Supplies Arduino and motors.                                            | 60 MXN each.                       |
| **Structure**     | PVC Pipes               | 3m length                        | Lightweight frame for buoyancy.                                         | Cost: 300 MXN.                     |
|                   | Styrofoam               | 2x2m sheet                       | Provides additional floatation.                                         | Cost: 120 MXN.                     |
|                   | Float Tube              | 2m                               | Auxiliary buoyancy aid.                                                 | Cost: 50 MXN.                      |
| **Software**      | ROS2 Humble             | Ubuntu 22.04                     | Autonomy stack (SLAM-free, color-based navigation).                     | Nodes: `vision_node`, `control_node`, `main_node`. |
|                   | OpenCV                  | 4.5+ (Python)                    | Real-time color detection (`cv2.inRange`).                              | Thresholds calibrated for red/green. |
|                   | PySerial                | 3.5+                             | Serial communication with Arduino.                                      | Commands: `b'A'`, `b'S'`, `b'B'`.  |
---

## 🧱 Structure Design

The physical structure of the robot was designed with two main priorities in mind: **buoyancy** and **environmental safety**. The selected materials—**PVC pipes**, **styrofoam sheets**, and **floating tubes**—were chosen for their lightweight properties and resistance to water absorption, ensuring the robot remains afloat during operation.

### 🛠️ Materials Used

- **PVC Pipes and Elbows:** Form the rigid frame of the robot. PVC is durable, lightweight, and waterproof.
- **Styrofoam Panels (Expanded Polystyrene):** Provide buoyant force by displacing water and resisting saturation.
- **Floating Tube (Foam Pool Noodle or Similar):** Enhances stability and helps keep the robot balanced even when collecting debris.

These materials together ensure that the robot maintains positive buoyancy, meaning the **total weight of the system is less than the weight of the water displaced**. This principle, based on Archimedes' law, guarantees that the robot floats and remains stable, even under partial load.
![Image](https://github.com/user-attachments/assets/c8843805-dd73-40cd-8192-74dbe48ce407)

We also printed the blades:

![Image](https://github.com/user-attachments/assets/bb540c26-d89f-4c2c-9225-c167b5cfe0e9)
---

### 📸 Structure Image

#### 🔲 Front View
![Image](https://github.com/user-attachments/assets/57bc1fd0-6536-457f-b4ce-df89768875f6)


# ⚙️ Installation Guide

This guide explains how to install Ubuntu, ROS 2 Humble, OpenCV, and configure Arduino communication for your autonomous water-cleaning robot system.

---

## 🐧 Ubuntu 22.04 Installation (Jammy Jellyfish)

Download the official Ubuntu 22.04 ISO from the following link:  
🔗 [Ubuntu 22.04 Jammy Downloads](https://releases.ubuntu.com/jammy/)

> 💡 **Note:** For Raspberry Pi or ARM-based systems, use the ARM64 version.

---

## 🤖 Installing ROS 2 Humble Hawksbill on Ubuntu 22.04

```bash
# Update your system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install software-properties-common -y
sudo add-apt-repository universe

# Add ROS 2 GPG key
sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

# Add ROS 2 repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list

# Update and install ROS 2 Humble (desktop version)
sudo apt update
sudo apt install ros-humble-desktop -y

# Source ROS 2 environment automatically
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
````
📦 Installing OpenCV, PySerial, and NumPy
```bash

# Install OpenCV (Python3 version) and pip
sudo apt install python3-opencv python3-pip -y

# Install Python libraries for ROS-Arduino communication
pip3 install pyserial numpy
````
🔌 Setting Up Serial Communication with Arduino
```bash
# Check the Arduino port (usually /dev/ttyACM0)
ls /dev/ttyACM*

# Grant serial port permissions
sudo chmod 666 /dev/ttyACM0
````
📝 Important Notes for ROS 2 Workspace
Make sure your ROS 2 project is inside a proper ROS workspace, for example:
```bash
~/ros2_ws/src/your_project/
````
Each package should include as the following image: 
![Image](https://github.com/user-attachments/assets/c8ad046e-e900-4094-b225-c8afa93b1338)
If you have a structure like this, the proyect will work correctly
# 💻 You can find the Codes Used in the Project

---

## 🧠 System Architecture: Python and Arduino Serial Communication

The system is composed of two main parts: the **Python script running on a Raspberry Pi (or computer with ROS 2)**, and the **Arduino microcontroller** connected via USB.

### 🐍 Python (OpenCV + PySerial)

The Python script is responsible for:

- **Capturing video frames** from a USB camera.
- **Detecting red and green colors** using HSV thresholding.
- **Sending commands to Arduino** via the serial port (`/dev/ttyACM0`) based on detection results.
- **State management**, to decide when to start or stop the motors.

#### 🔍 Color Detection Logic

- Red and green color ranges are defined in HSV space.
- If more than a certain number of pixels match those ranges (e.g. 5000+), it is considered "detected".
- The logic reacts immediately to detected objects to engage the collection process.

#### 🧬 State Machine Overview

| State               | Condition                  | Action                                 |
|--------------------|----------------------------|----------------------------------------|
| `INITIAL`          | No color                   | Send `'A'` → Motors Off                |
|                    | Color detected             | Send `'S'` → Stop → wait → `'B'` On    |
| `AMBOS_ENCENDIDOS` | Color disappears           | Start timer → Switch to `WAITING`     |
| `WAITING`          | After 4 seconds            | Return to `INITIAL`                   |

---

### 🔌 Arduino (L298N Motor Control)

The Arduino sketch waits for **single-character commands** received via Serial (USB) from Python. The supported commands are:

| Command | Meaning             | Arduino Action                         |
|---------|---------------------|----------------------------------------|
| `A`     | Initialization       | Stop all motors                        |
| `S`     | Stop                | Immediately turn off motors            |
| `B`     | Activate            | Start motors to move forward           |

Arduino uses a **L298N H-Bridge** to control two DC motors. Each command from the Python script corresponds to a digital signal change on the motor driver pins.

---

### 🔄 How They Work Together

1. The camera captures live video.
2. The Python script detects if a red or green object is present.
3. Depending on the result:
   - It sends a command like `'S'` or `'B'` to the Arduino.
4. Arduino receives the command and updates the motor control logic accordingly.
5. Feedback is visualized on the camera window and terminal.

> ✅ This architecture enables real-time reactive control, where **vision guides motion**.

---
# 🧹 Uninstall OpenCV and Camera-Related Packages in Python 3

```bash
pip3 uninstall opencv-python opencv-contrib-python
sudo apt remove libopencv* python3-opencv
sudo apt autoremove
```

> These commands remove OpenCV installed via `pip3` and `apt`, which can be necessary if you're experiencing issues with the camera losing connection after running Python program. Once there are uninstalled you have to install them again and be carefull where you connect the usb Camara, must have to be on the second usb flash raspberry, if you connected them on the first one you have to change only the code where the usb c lo puedes verificar con:
 ```bash
 ls /dev/video*
```



## ✅ Conclusion

The development of this autonomous aquatic robot successfully demonstrated the feasibility of using ROS 2 and OpenCV for real-time color-based object detection and motor control through Arduino communication. The robot achieved a high detection accuracy for red and green floating objects and responded correctly by activating its motors to collect them. The modular software architecture, based on ROS 2 nodes, enabled easy integration and testing of vision and control subsystems. This project contributes to sustainable solutions for water pollution and highlights the potential of low-cost robotics in environmental applications.

---

## 🚀 Future Improvements

- **Structural Design:** Replace the current PVC and styrofoam structure with a more hydrodynamic and waterproof frame to improve stability and maneuverability in real aquatic environments.
- **Advanced Detection:** Incorporate deep learning models or advanced computer vision techniques to improve object detection under varying lighting and environmental conditions.
- **Contact-Based Collection:** Add a mechanical collection mechanism that physically interacts with the detected debris for better waste retention and efficiency.
- **Battery & Power:** Integrate a solar charging system or higher-capacity power bank to allow longer autonomous operation time.

---

## 📬 Contact

For questions, suggestions, or collaboration opportunities, please contact:

**Antonio Martínez Sierra**  
📧 antonio.martinezsa@udlap.mx
