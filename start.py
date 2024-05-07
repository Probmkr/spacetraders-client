from bot import SpaceTradersBot, logger
from env import TOKEN
import asyncio


async def main():
    bot = SpaceTradersBot(TOKEN)
    agent = await bot.fetch_agent()
    logger.debug(type(agent))


asyncio.run(main())
