from client import logger
from command import bot
from env import TOKEN
import asyncio


async def main():
    await bot.async_run()


asyncio.run(main())
