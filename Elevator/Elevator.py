from .Enums.State import State
from Utils.CustomLogger import CustomLogger

class Elevator:

  """
  Class Elevator that handles abstraction of the state of the elevator

  """

  # Constructor
  def __init__(self, output, level):
    self.state = State.DOWN
    self.limit = 10
    self.position = 0
    self.l = CustomLogger("Elevator", output, level)
    self.l.info("Initialization of Elevator")

  # --------- private functions --------------------------

  # Set state on DOWN
  def _stop_down():
    self.l = CustomLogger("Elevator")
    self.state = State.DOWN
    self.l.info("Elevator stopping on down position...")

  # Set state on UP
  def _stop_up():
    self.state = State.UP
    self.l.info("Elevator stopping on top position...")

  # ------------------------------------------------------

  # Set state on MOVING_DOWN or MOVING_UP based on current state
  def move():
    if self.state == State.UP:
      self.state = State.MOVING_DOWN
      self.l.info("Elevator moving down...")
    elif self.state == State.DOWN:
      self.state = State.MOVING_UP
      self.l.info("Elevator moving up...")
    else:
      self.l.error("Incorrect action : tried to move", self.state, "moving state.")

  # Check if elevator needs to stop
  def update():
    if self.state == State.MOVING_DOWN and position <= 0:
      self.state = State.DOWN
    if self.state == State.MOVING_UP and position >= limit:
      self.state = State.UP