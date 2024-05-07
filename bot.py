from client import SpaceTradersClient, logger
from typing import Awaitable, Callable

CommandFunction = Callable[[SpaceTradersClient], Awaitable[None]]


class SubCommand:
    command_func: CommandFunction

    def __init__(self, func: CommandFunction) -> None:
        self.command_func = func


class Command(SubCommand):
    sub_command_list: dict[str, SubCommand]

    def __init__(self, func: Callable[[SpaceTradersClient], Awaitable[None]]) -> None:
        super().__init__(func)
        self.sub_command_list = {}

    def sub_command(self, name: str, *args, **kwargs):

        def wrapper(func: CommandFunction, *args, **kwargs):
            funcName = name.lower() if name else func.__name__
            logger.debug(f"Subcommand added: {funcName}")
            self.sub_command_list[name] = SubCommand(func)

        return wrapper


class SpaceTradersBot:
    client: SpaceTradersClient
    command_list: dict[str, Command]

    def __init__(self, token: str) -> None:
        self.client = SpaceTradersClient(token)
        self.command_list = {}

    def command(self, name: str, *args, **kwargs):

        def wrapper(func: CommandFunction, *args, **kwargs):
            funcName = name.lower() if name else func.__name__
            logger.debug(f"Command added: {funcName}")
            self.command_list[name] = Command(func)

        return wrapper

    async def run_command(self, command: str, args: list[str] = []):
        if command in self.command_list:
            await self.command_list[command].command_func(self.client, *args)
            if args:
                sub_command = args[0].lower()
                if sub_command in self.command_list[command].sub_command_list:
                    await self.command_list[command].sub_command_list[
                        sub_command
                    ].command_func(self.client, *args[1:])
                else:
                    return "Subcommand not found"
        else:
            return "Command not found"

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
            await self.run_command(command, args)
