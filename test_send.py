from smtplib import SMTP as Client
client = Client("p1.1upkd.com", 25)
r = client.sendmail('a@1upkd.com', ['b@inmail.1upkd.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>

Hi Bart, this is Anne.
""")