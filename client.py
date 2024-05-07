from typing import TypedDict
from env import LOG_LEVEL
from type import *
import aiohttp
import logging
import coloredlogs

from type.agent import AgentResponse
from type.contract import AcceptContractResponse, ContractResponse
from type.literal import Faction
from type.register import RegisterResponse


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


class SpaceTradersClient:
    token: str
    symbol: str
    baseurl: str

    def __init__(
        self, token: str, baseurl: str = "https://api.spacetraders.io/v2"
    ) -> None:
        self.token = token
        self.baseurl = baseurl

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

    # none testing, just written
    async def register(
        symbol: str,
        faction: Faction = "COSMIC",
        baseurl: str = "https://api.spacetraders.io/v2",
    ) -> RegisterResponse:
        async with aiohttp.ClientSession() as session:
            endpoint = f"{baseurl}/register"
            logger.debug(f"POST {endpoint}")
            async with session.post(
                endpoint, json={"symbol": symbol, "faction": faction}
            ) as response:
                logger.debug(f"POST {endpoint} -> {response.status}")
                return await response.json()

    async def fetch_agent(self) -> AgentResponse:
        async with self.get_session() as session:
            endpoint = f"{self.baseurl}/my/agent"
            logger.debug(f"GET {endpoint}")
            async with session.get(endpoint) as response:
                logger.debug(f"GET {endpoint} -> {response.status}")
                return await response.json()

    async def fetch_contracts(self) -> ContractResponse:
        async with self.get_session() as session:
            endpoint = f"{self.baseurl}/my/contracts"
            logger.debug(f"GET {endpoint}")
            async with session.get(endpoint) as response:
                logger.debug(f"GET {endpoint} -> {response.status}")
                return await response.json()

    async def accept_contract(self, contract_id: str) -> AcceptContractResponse:
        async with self.get_session() as session:
            endpoint = f"{self.baseurl}/my/contracts/{contract_id}/accept"
            logger.debug(f"POST {endpoint}")
            async with session.post(endpoint) as response:
                logger.debug(f"POST {endpoint} -> {response.status}")
                return await response.json()
