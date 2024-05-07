from bot import SpaceTradersBot
from client import SpaceTradersClient
from env import TOKEN


bot = SpaceTradersBot(TOKEN)


@bot.command(name="get-agent")
async def get_agent(client: SpaceTradersClient):
    agent = await client.fetch_agent()
    print(agent)
