# pyelevator
Python script for Rabpberry Pi to command elevator based on computer vision


## Code Architecture

### Modules
#### Elevator
Abstraction of the elevator. Basically a state machine, handling the transitions between states.
#### Vision
The camera module, handling the detection of movement
#### Controllers
Handle the commands to the motor
#### Utils
Other tools and libraries