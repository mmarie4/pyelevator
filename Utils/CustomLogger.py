from datetime import datetime
from Utils.Enums.Level import Level

class CustomLogger:

  """
  Custom logger

  Parameters:
  - name : name for this logger
  - output : can be CONSOLE or any other string that will be the filename where the log are printed
  _ level : reading level. DEBUG shows all logs, INFO only info and error, and ERROR only errors

  """

  # Constructor
  def __init__(self, name, output = "CONSOLE", level = Level.DEBUG):
    self.level = level
    self.name = name
    self.output = output
    if self.output != "CONSOLE":
      print("Initialization of " + name + " logger. Writing output in " + self.output)
      self.f = open(self.output, "a")

  # --------- private functions --------------------------

  def _format_log(self, msg, level):
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return level.name + ":" + "[" + self.name + "] - (" + time + ") " + msg

  def _log(self, msg, level):
    text = self._format_log(msg, level)

    if self.output == 'CONSOLE':
      print(str(text))
    else:
      self.f.write(text + "\n")

# -------------------------------------------------------

  # Log at ERROR level
  def error(self, msg):
    self._log(msg, Level.ERROR)

  # Log at INFO level
  def info(self, msg):
    if self.level == Level.DEBUG or self.level == Level.INFO:
      self._log(msg, Level.INFO)

  # Log at DEBUG level
  def debug(self, msg):
    if self.level == Level.DEBUG:
      self._log(msg, Level.DEBUG)