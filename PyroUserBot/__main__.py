import asyncio
import importlib
from pyrogram import Client, idle
from PyroUserBot.helper import join
from PyroUserBot.modules import ALL_MODULES
from PyroUserBot import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("PyroUserBot.modules" + all_module)
        print(f"Successfully Imported {all_module} ðŸ’¥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} ðŸ”¥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

