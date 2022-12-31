from gpiozero import MotionSensor
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# E-mail, ze kterého chci odeslat aktualizaci (funguje pouze s gmailem)
fromEmail = 'smap.uhk@gmail.com'
fromEmailPassword = 'Meganek5.'
toEmail = 'miroslav.hynek@uhk.cz'

pir = MotionSensor(4)
cas = 0
while True:
    pir.wait_for_motion()
    print(f"Pohyb {cas} ")
    time.sleep(1)
    cas += 1

def sendEmail():
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Detekován pohyb'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Raspberry pi security system update'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart security system found Motion in your room')
	msgAlternative.attach(msgText)

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()
