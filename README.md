## pyelevator
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
Other tools and helpers

## Setup
- **Picamera** : no need to install any library but the camera must be enabled : type `sudo raspi-config` , go to the 3rd option **Interface option** and enable camera, then reboot
- Install scikit-image : `pip3 install --upgrade scikit-image` (need numpy >= 1.16.5)
- In casethe import of scikit-image causes an error : `sudo apt install libatlas-base-dev`
- Install opencv : `pip3 install python-opencv`