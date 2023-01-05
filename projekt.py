from gpiozero import MotionSensor, Button
from email.message import EmailMessage
import time, smtplib
import datetime

pir = MotionSensor(4)
cas = 0

button = Button(5)

button.wait_for_press()

x = datetime.datetime.now()
text = x.strftime("%Y-%m-%d_%H-%M-%S0_%a")

# připojovací smtp údaje
email_address = "eduraspberry@seznam.cz"
email_password = "Meganek5."

# vytvoření e-mailu
msg = EmailMessage()
msg['Subject'] = "RPi notifikace"
msg['From'] = email_address
msg['To'] = "mira.hynek@seznam.cz"
msg.set_content("Toto je druhý e-mail z RPi " + text)

# poslání e-mailu
with smtplib.SMTP_SSL('smtp.seznam.cz', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)

print("Email odeslán")

while True:
    pir.wait_for_motion()
    print(f"Pohyb {cas} ")
    time.sleep(1)
    cas += 1
