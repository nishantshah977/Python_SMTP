
import smtplib
server = smtplib.SMTP('smtp server', 587)
server.starttls()
server.login("Your Username", "your password")
msg = "Your email"
server.sendmail("Sender Email","Receiver email", msg)
server.quit()
