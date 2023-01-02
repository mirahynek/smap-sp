from gpiozero import MotionSensor
from picamera import PiCamera
import time

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"
cas = 0
while True:
    pir.wait_for_motion()
    print(f"Pohyb {cas} ")
    time.sleep(1)
    cas += 1
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_preview()
