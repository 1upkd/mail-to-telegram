from aiosmtpd.controller import Controller
import asyncio
import config
from email.parser import BytesParser
import email.policy
import os
import telegram
from telegram.constants import ParseMode
import time
import uuid


parser = BytesParser(policy=email.policy.default)
os.makedirs("received_mails", exist_ok=True)
bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)

class MailHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        domain = address.split("@")[1]
        if domain not in config.ALLOWED_DOMAINS:
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'
    
    async def handle_DATA(self, server, session, envelope):
        try:
            sender = envelope.mail_from
            receiver = envelope.rcpt_tos[0]
            receiver_id = receiver.split("@")[0].split("+")[0][2:]
            msg_id = str(uuid.uuid1())
            print(msg_id, sender, receiver)
            message = parser.parsebytes(envelope.original_content)
            content = message.get_body("html",).get_content()
            text = "<b>" + message["From"] + "</b>\n"
            text += message["Subject"] + "\n\n"
            url = config.DOMAIN + msg_id + ".html"
            text += f'<a href="{url}">Read</a>'
            with open("received_mails/"+msg_id+".html", "w") as f:
                f.write(content)
                f.close()
            await bot.send_message(chat_id=receiver_id, text=text, parse_mode=ParseMode.HTML)
        except:
            pass
        return '250 Message accepted for delivery'

if __name__=="__main__":
    controller = Controller(MailHandler(), hostname="", port=25, decode_data=True)
    controller.start()
    print("Server Listening On", controller.hostname, controller.port)
    while True:
        time.sleep(600)
    #a = input("PRESS ENTER TO STOP\n")
    #controller.stop()