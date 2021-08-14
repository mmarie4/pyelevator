from Utils.CustomLogger import CustomLogger
from Utils.Enums.State import State
from Utils.Constants import *
import RPi.GPIO as gp  
from time import sleep

class MotorController:

  """
  Class MotorController that handles the commands to the servomotor

  """

  # Constructor
  def __init__(self, output, level):
    self.l = CustomLogger("MotorController", output, level)
    self.step = ANGLE_STEP_DEGREES

    gp.setmode(gp.BOARD)  
    gp.setup(GPIO_PWM_PIN, gp.OUT)  
    self.pwm = gp.PWM(GPIO_PWM_PIN, PWM_FREQUENCY_HZ)
    self.pwm.start(MIN_POSITION)

    self.l.info("MotorController initialized.")

  # --------- private functions --------------------------
  def _angle_to_PWM(SELF, value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

  def _rotate(self, angle):
      angle = MAX_POSITION if angle > MAX_POSITION else angle
      angle = MIN_POSITION if angle < MIN_POSITION else angle
      sig = self._angle_to_PWM(angle, MIN_POSITION, MAX_POSITION, SERVO_MIN_DUTY, SERVO_MAX_DUTY)
      self.pwm.ChangeDutyCycle(sig)

  # ----------------------------------------------------

  # Cleanup GPIO
  def cleanup(self):
    self.l.info("Cleaning up GPIO...")
    gp.cleanup()

  # Activate motor based on elevator state
  def update(self, elevator):
    self.l.debug("elevator position = " + str(elevator.position))
    if elevator.state == State.MOVING_DOWN:
      self.l.debug("Moving down...")
      self._rotate(elevator.position - self.step)
      elevator.position -= self.step
    elif elevator.state == State.MOVING_UP:
      self.l.debug("Moving up...")
      self._rotate(elevator.position + self.step)
      elevator.position += self.step
    else:
      self.l.debug("Nothing to do")
