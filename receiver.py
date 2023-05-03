import asyncio
from aiosmtpd.controller import Controller

ALLOWED_DOMAINS = ["inmail.1upkd.com", "1upkd.localhost"]

class ExampleHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        domain = address.split("@")[1]
        if domain not in ALLOWED_DOMAINS:
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'
    
    async def handle_DATA(self, server, session, envelope):
        print('Message from %s' % envelope.mail_from)
        print('Message for %s' % envelope.rcpt_tos)
        print('Message data:\n')
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            print(f'> {ln}'.strip())
        print()
        print('End of message')
        return '250 Message accepted for delivery'

if __name__=="__main__":
    controller = Controller(ExampleHandler(), hostname="", port=25)
    controller.start()
    print("Server Listening On", controller.hostname, controller.port)
    a = input("PRESS ENTER TO STOP\n")
    controller.stop()