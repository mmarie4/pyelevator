from Elevator.Elevator import Elevator
from Controllers.MotorController import MotorController
from Vision.Vision import Vision
from time import sleep
from Utils.CustomLogger import CustomLogger
from Utils.Enums.Level import Level
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
        logger.debug("Vision detected moving again... Do nothing")
      else:
        logger.debug("Vision found stable image. Activating controller")
        elevator.update()

    else:
      logger.debug("Vision detected no movement last iteration")
      vision.update()
      if vision.moving:
        logger.debug("Vision detected movement. Wait next iteration.")
      else:
        logger.debug("Vision still detects no movement")

    sleep(0.2)

if __name__ == "__main__":
    main()
