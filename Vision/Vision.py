from picamera import PiCamera
from skimage.metrics import structural_similarity as compare_ssim
from Utils.CustomLogger import CustomLogger
from picamera.array import PiRGBArray
import cv2

class Vision:

  # Constructor
  def __init__(self, output, level):
    self.l = CustomLogger("Vision", output, level)
    self.last_image = []
    self.moving = False
    self.camera = PiCamera()
    self.l.info("Initialization of Vision")
    
    # Save raw capture to allow us to grab image from the stream and for perf : https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
    self.raw_capture = PiRGBArray(self.camera)

    #self.camera.start_preview()

  # --------- private functions --------------------------

  # Captures an images from the pi camera
  def _capture_image(self):
    self.l.debug("Capturing image...")
    self.camera.capture(self.raw_capture, format="bgr")
    return self.raw_capture.array

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

    cv2.imshow("Image", self.last_image)
