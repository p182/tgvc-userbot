import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, filters
from pyrogram.types import Message


self_or_contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s - %(levelname)s] - %(name)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[
                        RotatingFileHandler(
                            "tgvcuserbot.txt", maxBytes=2048000, backupCount=10),
                        logging.StreamHandler()
                    ])
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.dispatcher").setLevel(logging.INFO)


@Client.on_message(self_or_contact_filter & filters.command('logs', prefixes='!'))
async def logzzz(client, m: Message):
    try:
        await client.send_document(m.chat.id, "tgvcuserbot.txt")
    except Exception as e:
        await m.reply(f"**Error** \n`{e}`")
        return
