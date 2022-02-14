import pyrogram
from pyrogram import Client

friday_ = """
╔═══╗───╔═╗─╔═╗
║ ══╬═╦═╬═╬═╝ ╠═══╦═╦═╗
║ ╔═╣ ╔═╣ ║╔╗ ║╔╗ ╠══ ║
╚═╝ ╚═╝ ╚═╩═══╩═╩═╩═══╝
Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/DevsExpo/blob/master/LICENSE >
All rights reserved.
"""

print(friday_)

api_id = input("11539587: \n")
api_hash = input("7e243ca4dbf28af17e7239a0447cc6b1 : \n")


with Client("FridayUB", api_id=api_id, api_hash=api_hash) as bot_:
    first_name = (bot_.get_me()).first_name
    string_session_ = f"<b><u>String Session For {first_name}</b></u> \n<code>{bot_.export_session_string()}</code>"
    bot_.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
