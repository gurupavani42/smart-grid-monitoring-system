# Smart Grid Monitoring System

## Overview

The Smart Grid Monitoring System is a Python-based project designed to monitor important electrical parameters of a smart grid.

The system reads grid measurements from a CSV file and checks parameters such as:

- Voltage
- Current
- Frequency
- Power Factor
- Temperature

It calculates active power and identifies abnormal conditions such as:

- Overvoltage
- Undervoltage
- Overcurrent
- Under-frequency
- Over-frequency
- Low power factor
- High temperature

The system finally displays the condition of the grid as NORMAL, WARNING, or FAULT.

## Objectives

1. Monitor electrical parameters.
2. Detect abnormal grid conditions.
3. Calculate active power.
4. Generate alerts when limits are exceeded.
5. Provide a simple and low-cost grid monitoring solution.
6. Demonstrate smart-grid monitoring using software simulation.

## Technologies Used

- Python 3
- CSV
- unittest
- Mathematical calculations

## Parameters Monitored

| Parameter | Normal Range |
|-----------|--------------|
| Voltage | 220–240 V |
| Current | 0–100 A |
| Frequency | 49–51 Hz |
| Power Factor | 0.8–1.0 |
| Temperature | Below 80 °C |

## Project Structure

smart-grid-monitoring-system/

├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── monitoring.py
│   └── fault_detection.py
├── data/
│   └── grid_data.csv
├── tests/
│   └── test_monitoring.py
└── output/
    └── expected_output.txt

## Installation

Install Python 3 from:

https://www.python.org/

Clone the repository:

git clone https://github.com/YOUR_USERNAME/smart-grid-monitoring-system.git

Move into the project directory:

cd smart-grid-monitoring-system

Install dependencies:

pip install -r requirements.txt

## Running the Project

Run:

python src/main.py

## Testbench

The project includes automated test cases using Python unittest.

Run:

python -m unittest tests/test_monitoring.py

## Expected Result

The program reads the grid data and identifies the condition of each measurement.

Example:

Voltage      : 232.5 V
Current      : 42.3 A
Frequency    : 50.02 Hz
Power Factor : 0.94
Active Power : 9.25 kW
Temperature  : 45.6 °C

Grid Status  : NORMAL

For abnormal values, the system generates an alert.

Example:

ALERT: OVERVOLTAGE DETECTED

Grid Status: WARNING

## Future Improvements

- Real-time IoT sensor integration
- ESP32/Arduino integration
- Cloud monitoring
- Mobile application
- Real-time dashboard
- Automatic fault notification
- Machine-learning-based fault prediction

## Author

B.Tech Electrical Engineering Student

## License

This project is developed for educational and academic purposes.
