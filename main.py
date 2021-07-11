from Elevator.Elevator import Elevator
from Controllers.MotorController import MotorController
from Vision.Vision import Vision
from time import sleep



def main():
    elevator = Elevator()
    motor_controller = MotorController()
    vision = Vision()

    while true:
      if vision.detect_movement():
        elevator.move()

      sleep(0.5)

if __name__ == "__main__":
    main()
