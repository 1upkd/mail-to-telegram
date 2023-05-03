from smtplib import SMTP as Client
client = Client("::1", 8025)
r = client.sendmail('a@1upkd.localhost', ['b@1upkd.localhost'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>

Hi Bart, this is Anne.
""")