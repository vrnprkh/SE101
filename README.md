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
*Block diagram.*

### Software

#### Interfacing
To interface with the arduino, we used a python library called 
[pyFirmata](https://github.com/tino/pyFirmata),
which is a python interface for the firmata protocol. 
This allowed us to use python to send data to the arduino, 
and read the raw sensor data from the arduino.

#### Sensor Processing

Processing and interpretting sensor data was probably one of the trickiest aspects of this entire project.
There were two parts to processing the data, reading and clamping the data values, then update the board depending on the changes.

The sensor reading was done as follows:
1. Read data from each multiplexer, for each possible pin (0.1 seconds between each read).
2. Place each input to a 4x4 grid of values.
3. Map values above or below a certain thershold to 0 or 1
    - Sensor values from 0 to 0.49 and 0.53 to 1 were mapped to 1
    - Otherwise the values would be mapped to 0.
    - More details in hardware section.
4. Sleep for 0.1 seconds to prevent any multiplexer issues.



The tricky part, was managing the board state using sensor data.
Since the sensors could only read if a piece was their and not its color, it was tricky to manage the state of the board.

The board management was implemented as follows:
1. Take processed sensor values (from above).
2. Count the number of changes from the previous state the board was in.
3. If more than 2 changes are detected, throw an error.
4. If no change is detected, do nothing.
5. If exactly 1 change is detected:
    1. If a piece is picked up:
        - If the player is holding one of their own pieces, and then picked up another of their own pieces, throw an error.
        - If the player is holding one of their own pieces, and then picked up their opponents piece anticipate a capture.
        - If the player has no pieces and picks up their own, add the piece to their hand, and update the board state by removing the piece.
        - If the player has no pieces and picks up thier opponents piece, throw and error.
    2. If a piece is placed:
        - If the players hand is currently empty, throw an error.
        - If the player places a piece in an illegal posistion, throw an error.
        - If a capture is being anticipated, and a piece is not placed on the square of square of capture, throw an error.
        - If a piece is placed back on it original square from the players hand, put the piece back down and clear the players hand.
        - Otherwise, update the board based on the legal move / capture, and clear the players hand.

Due to the limitations of our hardware implementation, this approach worked, but could be difficult at times, and was error prone. Therefore when an error was thrown, the board processor would wait until the player undoed the move, and would continue when the sensor data matched the last state. This obviously did not work at all times, but was the most effective implementation that we could do.

#### GUI
The GUI for this project was made using pygame. It is capable of highlighting squares 
for legal moves, 

add info





### Hardware

#### Breadboard organization

#### Hall sensors

#### Multiplexing



## Challenges


