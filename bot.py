from client import SpaceTradersClient, logger
from typing import Any, Awaitable, Callable, Coroutine

CommandFunction = Callable[[SpaceTradersClient], Coroutine[Any, Any, None]]


class CommandNotFoundException(Exception):
    pass


class Command:
    command_func: CommandFunction

    def __init__(self, func: CommandFunction) -> None:
        self.command_func = func


class SpaceTradersBot:
    client: SpaceTradersClient
    command_list: dict[str, Command]

    def __init__(self, token: str) -> None:
        self.client = SpaceTradersClient(token)
        self.command_list = {}

    def command(self, name: str = None, *args, **kwargs):

        def wrapper(func: CommandFunction):
            funcName = name.lower() if name else func.__name__
            logger.debug(f"Command added: {funcName}")
            self.command_list[funcName] = Command(func)
            return self.command_list[funcName]

        return wrapper

    async def run_command(self, command: str, args: list[str] = []):
        if command in self.command_list:
            await self.command_list[command].command_func(self.client, *args)
        else:
            raise CommandNotFoundException(f"Command not found `{command}`")

    async def async_run(self):
        raw = None
        while True:
            try:
                raw = input("bot > ")
            except KeyboardInterrupt:
                break
            except EOFError:
                print()
                continue
            if (raw == "") or (raw.isspace()):
                continue
            command, *args = raw.split()
            if (command := command.lower()) in ["exit", "quit"]:
                break
            try:

                await self.run_command(command, args)
            except CommandNotFoundException as e:
                print(e)
