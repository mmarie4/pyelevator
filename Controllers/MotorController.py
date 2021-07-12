from Utils.CustomLogger import CustomLogger

class MotorController:

  """
  Class MotorController that handles the commands to the servomotor

  """

  # --------- private functions --------------------------

  def _rotate(angle):
    l.debug("Rotating motor with angle = ", angle)

  # ----------------------------------------------------

  # Constructor
  def __init__(self, output, level):
    self.l = CustomLogger("MotorController", output, level)
    self.l.info("Initialization of MotorController")
    self.step_angle = 10

  # Activate motor based on elevator state
  def update(elevator):
    if elevator.state == State.MOVING_DOWN:
      self.l.debug("Moving down...")
      _rotate(-1 * self.step_angle)
    elif elevator.state == State.MOVING_UP:
      self.l.debug("Moving up...")
      _rotate(self.step_angle)
    else:
      self.l.debug("Nothing to do")
