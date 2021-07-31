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




# Conception
Need to transform the rotation movement of the motor to a translation movement. Could have done it with a rack and pinion, but I figured the easiest way would be to use a wheel and a string, especially because I want to place the raspberry Pi on top of the hamster cage that avoid taking too much space inside.
Then the platform will needs movement constraints on the rotations and on the translations horizontally, to allow only vertical movements. We will need to add a basis and 4 pillars to guide the platform. At the end, the elevator will work like this :

We can calculate the radius of the wheel depending on the amplitude we want for our platform. I am using a servomotor that can rotate on 180°, which means the maximum amplitude of the elevator corresponds to half the perimeter : 2*PI*R / 2 = h => R = h / PI

I am using a SG90 servomotor, that requires 5V alimentation and use PWM signals. Plug it as followed:
- Yellow cable on a GPIO pin that uses PWM signal
- Red cable on a 5V pin
- Black/brown cable on the ground

My servomotor has his wires attached so I bought a bunch of jumper wires to connect to the relevant pins on the Pi:
[Picture]

Here is the deatils about each pin of the raspberry pi 4 that I am using: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F4128%2F0*VsaGvGskvJa20hZa.png&f=1&nofb=1

#### References
[Accessing Picamera with openCV and python](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
[Image differences with openCV and python](https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/)