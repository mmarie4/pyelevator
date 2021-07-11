from Enums.State import State

class Elevator:

  def __init__(self):
    self.state = State.DOWN

  """
  Set state on MOVING_DOWN or MOVING_UP based on current state
  """
  def move():
    if self.state == State.UP:
      self.state = State.MOVING_DOWN
      print("Elevator moving down...")
    elif self.state == State.DOWN
      self.state = State.MOVING_UP
      print("Elevator moving up...")
    else
      raise Exception("Incorrect action : tried to move", self.state, "moving state.")

  """
  Set state on DOWN or UP based on current state
  """
  def stop():
    if self.state == State.MOVING_UP:
      self.state = State.UP
      print("Elevator stopping on top position...")
    elif self.state == State.MOVING_DOWN
      self.state = State.DOWN
      print("Elevator stopping on down position...")
    else
      raise Exception("Incorrect action : tried to stop from", self.state, "state.")