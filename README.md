# AI-Driven Predictive Maintenance System for Rotating Machinery using Multisensory Data

## Overview

This project presents a real-time predictive maintenance system for rotating machinery using multisensory industrial data. The system continuously monitors machine conditions using multiple sensors and detects abnormal operating behavior using a machine learning model.

The objective is to reduce unexpected machine failure, minimize downtime, and improve maintenance efficiency through continuous monitoring and intelligent fault detection.

The system combines:

* Arduino-based sensor acquisition
* Real-time serial communication
* Python-based machine learning
* Decision Tree fault classification
* Automated email alert system
* IoT-ready architecture

---

## Features

* Real-time machine health monitoring
* Multisensor data acquisition
* Abnormal condition detection using Machine Learning
* Automatic email alerts during faults
* Serial communication between Arduino and Python
* Industrial parameter monitoring:

  * Tilt/Vibration
  * Temperature
  * Sound
  * Current
  * Voltage
* Edge-level fault detection
* IoT integration ready

---

## Technologies Used

### Hardware

* Arduino UNO
* MPU6050 Accelerometer & Gyroscope
* LM35 Temperature Sensor
* ACS712 Current Sensor
* Voltage Sensor Module
* Sound Sensor
* ESP8266 WiFi Module
* 16x2 LCD Display

### Software

* Python
* Arduino IDE
* Scikit-learn
* Pandas
* PySerial

---

## Machine Learning Model

The project uses a `DecisionTreeClassifier` from Scikit-learn to classify machine conditions as:

* Normal
* Abnormal

### Input Features

* Tilt
* Temperature
* Sound
* Current
* Voltage

### Output

* `0` → Normal
* `1` → Abnormal

The model is trained using sensor data stored in `Machine.csv`.

---

## System Architecture

```text
Sensors → Arduino UNO → Serial Communication → Python ML Model
       → Fault Detection → Email Alert → IoT/Cloud Monitoring
```

---

## Working Process

1. Sensors collect real-time machine parameters.
2. Arduino sends sensor values through serial communication.
3. Python reads incoming sensor data.
4. Data is processed using the Decision Tree model.
5. Machine status is classified.
6. If abnormality is detected:

   * Alert is printed
   * Signal is sent back to Arduino
   * Email notification is triggered

---

## Email Alert System

The system automatically sends an email notification when abnormal machine behavior is detected.

Alert includes:

* Tilt value
* Temperature
* Sound level
* Current
* Voltage
* Fault status


---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### Install Dependencies

```bash
pip install pandas scikit-learn pyserial
```

---

## Run the Project

1. Connect Arduino to PC
2. Upload Arduino code
3. Update correct COM port in Python code

Example:

```python
ser = serial.Serial('COM7', 9600, timeout=1)
```

4. Run Python script

```bash
python main.py
```

---

## Example Serial Data Format

```text
X10T35S40C3V12
```

Where:

* X → Tilt
* T → Temperature
* S → Sound
* C → Current
* V → Voltage

---

## Future Improvements

* Deep Learning-based fault prediction
* Remaining Useful Life (RUL) estimation
* Cloud dashboard integration
* MQTT/ThingSpeak support
* Real-time graph visualization
* Mobile app alerts
* Advanced anomaly detection models

---

## Applications

* Industrial motor monitoring
* Pump monitoring systems
* Conveyor systems
* Manufacturing industries
* Smart factories
* Industrial IoT systems

---

## Team Members

* Francies T
* Bal Abisheak C
* Vinay Prasath R

---

## License

This project is developed for academic and educational purposes.
