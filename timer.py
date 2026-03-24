from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import time

api_id = 33222575
api_hash = "30e5784b4f338125540c2a4c98974cc0"

NAME = "T4yxt"

client = TelegramClient('session', api_id, api_hash)

async def main():
    while True:
        current_time = time.strftime("%H:%M")  # только часы и минуты

        await client(UpdateProfileRequest(
            first_name=f"{NAME} | {current_time}"
        ))

        await asyncio.sleep(61)  # обновление раз в минуту

with client:
    client.loop.run_until_complete(main())