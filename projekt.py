from gpiozero import MotionSensor
import time

pir = MotionSensor(4)
cas = 0
while True:
    pir.wait_for_motion()
    print(f"Pohyb {cas} ")
    time.sleep(1)
    cas += 1