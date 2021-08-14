from Elevator.Elevator import Elevator
from Controllers.MotorController import MotorController
from Vision.Vision import Vision
from time import sleep
from Utils.Enums.State import State
from Utils.CustomLogger import CustomLogger
from Utils.Constants import *
from Utils.ArgumentParserHelper import GetArgs

def main():
  output, level = GetArgs()

  elevator = Elevator(output, level)
  motor_controller = MotorController(output, level)
  vision = Vision(output, level)
  logger = CustomLogger("Main", output, level)

  try:
    
    while True:

      if elevator.is_still():
        vision.update()
        if vision.moving:
          logger.debug("Something changed... Moving the elevator.")
          elevator.move()
          motor_controller.update(elevator)
        else:
          logger.debug("Nothing changed. Stay still.")

      else:
        elevator.check()
        if elevator.is_still():
          logger.debug("Elevator stopped moving")
          vision.reset()
        else:
          logger.debug("Elevator keep moving")
          motor_controller.update(elevator)

      sleep(DELAY_BETWEEN_CAPTURES)

  except KeyboardInterrupt:
    motor_controller.cleanup()

if __name__ == "__main__":
    main()
