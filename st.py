from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# 🔑 Put your own API ID & API HASH from https://my.telegram.org
API_ID = int(input("Enter API ID: "))
API_HASH = input("Enter API HASH: ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("\n✅ Your String Session:\n")
    print(client.session.save())
    print("\n⚠️ Copy and save this string safely. Do NOT share it.")
