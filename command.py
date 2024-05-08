from bot import SpaceTradersBot
from client import SpaceTradersClient
from env import TOKEN
import json


bot = SpaceTradersBot(TOKEN)


def json_formatter(data):
    return json.dumps(data, indent=4, sort_keys=True)


def get_system_from_waypoint(waypoint):
    return "-".join(waypoint.split("-")[:2])


def symbols(multi_data):
    return [data["symbol"] for data in multi_data["data"]]


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
    waypoint = await client.fetch_waypoint(get_system_from_waypoint(waypoint), waypoint)
    print(json_formatter(waypoint))


@bot.command()
async def get_waypoints(
    client: SpaceTradersClient, system: str = "", *query: list[str]
):
    if not system:
        print("Usage: get_waypoints <system> [*query]")
        return
    waypoints = await client.fetch_waypoints(system, query)
    print(symbols(waypoints))


@bot.command()
async def get_shipyard_waypoints(
    client: SpaceTradersClient, system: str = "", *query: list[str]
):
    if not system:
        print("Usage: get_shipyard_waypoints <system> [*query]")
        return
    waypoints = await client.fetch_waypoints(system, ["traits=SHIPYARD", *query])
    print(symbols(waypoints))


@bot.command()
async def get_shipyard(client: SpaceTradersClient, waypoint: str = ""):
    if not waypoint:
        print("Usage: get_shipyard <system> <waypoint>")
        return
    shipyard = await client.fetch_shipyard(get_system_from_waypoint(waypoint), waypoint)
    print(json_formatter(shipyard))


@bot.command()
async def get_ships(client: SpaceTradersClient):
    ships = await client.fetch_ships()
    print(symbols(ships))
