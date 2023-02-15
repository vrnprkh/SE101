# Overview

The goal of this project was to design an interactive chessboard that tracks moves and acts as a teaching tool for beginners.
Each piece would have a magnet underneath which then could be detected using a 
4x4 grid of halls sensors to track where the piece was on the board.
In software, the changes in the sensor data is processed and then tracked.

This project was a first year design project for the course SE101 at the University Of Waterloo.

Group members: Emily Wang, Justin Lin, Jacqueline Ho, Nandan Patel, Varun Parikh.

# Process



## Planning


## Implementation

![Block Diagram](/images/block%20diagram.png)


### Software

#### Interfacing
To interface with the arduino, we used a python library called 
[pyFirmata](https://github.com/tino/pyFirmata),
which is a python interface for the firmata protocol. 
This allowed us to use python to send data to the arduino, 
and read the raw sensor data from the arduino.

#### Sensor Processing
To add info on sensorProcessor


#### GUI
The GUI for this project was made using pygame. It is capable of highlighting squares 
for legal moves, 

add info





### Hardware

#### Breadboard organization

#### Hall sensors

#### Multiplexing



## Challenges


