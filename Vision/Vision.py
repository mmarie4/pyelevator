from Utils.CustomLogger import CustomLogger

class Vision:

  # Constructor
  def __init__(self, output, level):
    self.l = CustomLogger("Vision", output, level)
    self.last_image = []
    self.moving = False
    self.l.info("Initialization of Vision")

  # --------- private functions --------------------------

  # Captures an images from the pi camera
  def _capture_image(self):
    self.l.debug("Capturing image...")
    return []

  # Compare previous image and new one to detect differences
  def _compare_images(self, new_image):
    self.l.debug("Comparing images...")
    return self.last_image != new_image

  # ------------------------------------------------------

  # Detect movement and update Vision instance
  def update(self):
    self.l.debug("Updating vision...")
    new_image = self._capture_image()

    self.l.debug("Compare images to detect movement...")
    result = self._compare_images(new_image)

    self.last_image = new_image
    self.moving = result
    self.l.debug("Vision updated: " + "Something moved" if self.moving else "Nothing moved")