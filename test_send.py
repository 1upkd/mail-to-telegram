import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
from smtplib import SMTP as Client

sender_email = "a@1upkd.com"
receiver_email = config.TEST_RECEIVER_ID


msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"
msg["From"] = sender_email
msg["To"] = receiver_email

html = """\
<html>
  <body>
    <p><b>Python Mail Test</b>
    <br>
       This is HTML email with attachment.<br>
       Click on <a href="https://fedingo.com">Fedingo Resources</a> 
       for more python articles.
    </p>
  </body>
</html>
"""

part = MIMEText(html, "html")
msg.attach(part)

#encoders.encode_base64(part)

client = Client("localhost", 25)
r = client.sendmail(sender_email, receiver_email, msg.as_string())