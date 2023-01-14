#from gpiozero import Button
from gpiozero import MotionSensor
from picamera import PiCamera
import datetime
from time import sleep
import smtplib
from email.message import EmailMessage
camera = PiCamera()
#button = Button(5)
pir = MotionSensor(4)
#button.wait_for_press()
while True:
    pir.wait_for_motion()
    #button.wait_for_press()
    x = datetime.datetime.now()
    text = x.strftime("%Y-%m-%d_%H-%M-%S0_%a_")
    cesta = '/home/pi/Desktop/kamera/' + text + 'snímek.png'
    camera.capture(cesta)
    print("Snímek OK")
    #camera.close()
    sleep(10)
    filename = text + ".h264"
    camera.start_recording(filename)
    sleep(10)    
    camera.stop_recording()
    print("Video OK")
# ověření
    email_address = "eduraspberry@seznam.cz"
    email_password = "Meganek5."
# vytvoř e-mail
    msg = EmailMessage()
    msg['Subject'] = "RPi notifikace"
    msg['From'] = email_address
    msg['To'] = "mira.hynek@seznam.cz"
    msg.set_content("Toto je notifikace
    z RPi " + text)
# pošli email
    with smtplib.SMTP_SSL('smtp.seznam.cz', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    print("E-mail odeslán")
# print(x.strftime("%Y-%m-%d_%H-%M-%S0_%a"))
