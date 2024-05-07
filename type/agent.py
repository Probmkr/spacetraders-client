from typing import Literal, TypedDict
from .literal import Faction


class AgentData(TypedDict):
    accountId: str
    symbol: str
    headquarters: str
    credits: int
    startingFaction: Faction
    shipCount: int


class AgentResponse(TypedDict):
    data: AgentData
