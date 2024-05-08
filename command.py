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


@bot.command()
async def accept_contract(client: SpaceTradersClient, contract_id: str):
    if not contract_id:
        print("Usage: accept_contract <contract_id>")
        return
    contract = await client.accept_contract(contract_id)
    print(json_formatter(contract))


@bot.command()
async def get_waypoint(client: SpaceTradersClient, waypoint: str = ""):
    if not waypoint:
        print("Usage: get_waypoint <system> <waypoint>")
        return
    waypoint = await client.fetch_waypoint("-".join(waypoint.split("-")[:2]), waypoint)
    print(json_formatter(waypoint))


@bot.command()
async def get_waypoints(
    client: SpaceTradersClient, system: str = "", *query: list[str]
):
    if not system:
        print("Usage: get_waypoints <system> [*query]")
        return
    waypoints = await client.fetch_waypoints(system, query)
    print([waypoint["symbol"] for waypoint in waypoints["data"]])
