from env import LOG_LEVEL
from type import *
import aiohttp
import logging
import coloredlogs


class bcolors:
    # https://godoc.org/github.com/whitedevops/colors
    BGRED = "\033[41m"
    BGGREEN = "\033[42m"
    BGYELLOW = "\033[43m"
    BGBLUE = "\033[44m"
    BGMAGENDA = "\033[45m"
    BGCYAN = "\033[46m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENDA = "\033[95m"
    CYAN = "\033[96m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


logger = logging.getLogger(__name__)
# logging.basicConfig(level=LOG_LEVEL)
coloredlogs.install(logger=logger, level=LOG_LEVEL)


class SpaceTradersBot:
    token: str
    symbol: str
    baseurl: str

    def __init__(
        self, token: str, endpoint: str = "https://api.spacetraders.io/v2"
    ) -> None:
        self.token = token
        self.baseurl = endpoint

    def get_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            headers={
                "Authorization": f"Bearer {self.token}",
            }
        )

    def get_json_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }
        )

    async def get_agent(self) -> agent.AgentData:
        async with self.get_session() as session:
            endpoint = f"{self.baseurl}/my/agent"
            logger.debug(f"GET {endpoint}")
            async with session.get(endpoint) as response:
                logger.debug(f"GET {endpoint} -> {response.status}")
                return await response.json()
