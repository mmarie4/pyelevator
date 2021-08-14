from picamera import PiCamera
from skimage.metrics import structural_similarity as compare_ssim
from Utils.CustomLogger import CustomLogger
from picamera.array import PiRGBArray
from Utils.Constants import *
import cv2

class Vision:

  # Constructor
  def __init__(self, output, level):
    self.l = CustomLogger("Vision", output, level)
    self.moving = False
    self.camera = PiCamera()
    # Save raw capture to allow us to grab image from the stream and for perf : https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
    self.raw_capture = PiRGBArray(self.camera)
    self.last_image = self._capture_image()
    self.score_threshold = SSIM_THRESHOLD
    #self.camera.start_preview()
    self.l.info("Vision initialized.")

  # --------- private functions --------------------------

  # Captures an images from the pi camera
  def _capture_image(self):
    self.l.debug("Capturing image...")
    self.raw_capture.truncate(0)
    self.camera.capture(self.raw_capture, format="bgr")
    #cv2.imshow("Frame", self.raw_capture.array)
    return self.raw_capture.array

  # Compare previous image and new one to detect differences
  # Returns true if there is a difference between the images
  def _compare_images(self, new_image):
    self.l.debug("Comparing images...")
    gray_last_image = cv2.cvtColor(self.last_image, cv2.COLOR_BGR2GRAY)
    gray_new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(gray_last_image, gray_new_image, full=True)
    diff = (diff * 255).astype("uint8")
    self.l.debug("SSIM: {}".format(score))
    return score < self.score_threshold

  # ------------------------------------------------------

  # Detect movement and update Vision instance
  def update(self):
    new_image = self._capture_image()
    self.moving = self._compare_images(new_image)
    self.last_image = new_image

  # When elevator stops, get ready to detect movement again
  def reset(self):
    self.moving = False
    self.last_image = self._capture_image()
