from Elevator.Elevator import Elevator
from Controllers.MotorController import MotorController
from Vision.Vision import Vision
from time import sleep
from Utils.CustomLogger import CustomLogger
from Utils.Constants import *
from Utils.ArgumentParserHelper import GetArgs

def main():
  output, level = GetArgs()

  elevator = Elevator(output, level)
  motor_controller = MotorController(output, level)
  vision = Vision(output, level)
  logger = CustomLogger("Main", output, level)

  while True:

    if vision.moving:
      logger.debug("Vision detected movement last iteration")
      vision.update()
      if vision.moving:
        logger.debug("Vision detected movement again... Do nothing.")
      else:
        logger.debug("Vision found no movement. Activating controller")
        elevator.update()

    else:
      logger.debug("Vision detected no movement last iteration")
      vision.update()
      if vision.moving:
        logger.debug("Vision detected movement. Wait next iteration.")
      else:
        logger.debug("Vision still detects no movement")

    sleep(DELAY_BETWEEN_CAPTURES)

if __name__ == "__main__":
    main()
