from client import SpaceTradersClient, logger
from env import TOKEN
import asyncio


async def main():
    bot = SpaceTradersClient(TOKEN)
    while True:
        raw = None
        try:
            raw = input("client > ")
        except KeyboardInterrupt:
            break
        except EOFError:
            print("")
            continue
        splited = raw.split(" ")
        command = splited[0]
        args = splited[1:]
        if command == "register":
            if len(args) == 1:
                symbol = args[0]
                response = await bot.register(symbol)
                print(response)
            else:
                print("Usage: register <symbol>")
        elif command == "get-agent":
            response = await bot.fetch_agent()
            print(response)
        elif command == "get-contracts":
            response = await bot.fetch_contracts()
            print(response)
        elif command == "accept-contract":
            if len(args) == 1:
                contract_id = args[0]
                response = await bot.accept_contract(contract_id)
                print(response)
            else:
                print("Usage: accept-contract <contract_id>")
        elif command in ["exit", "quit"]:
            break
        else:
            print("Unknown command")


asyncio.run(main())
