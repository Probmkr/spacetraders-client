from bot import SpaceTradersBot
from client import SpaceTradersClient
from env import TOKEN
import json


bot = SpaceTradersBot(TOKEN)


def json_formatter(data):
    return json.dumps(data, indent=4, sort_keys=True)


@bot.command()
async def get_agent(client: SpaceTradersClient):
    agent = await client.fetch_agent()
    print(json_formatter(agent))


@bot.command()
async def get_contracts(client: SpaceTradersClient):
    contract = await client.fetch_contracts()
    print(json_formatter(contract))
