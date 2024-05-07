from typing import TypedDict
from type.agent import AgentData
from type.alias import DateTimeString
from type.common import MetaData
from type.literal import Faction


class DeliverData(TypedDict):
    tradeSymbol: str
    destinationSymbol: str
    unitsRequired: int
    unitsFulfilled: int


class PaymentData(TypedDict):
    onAccepted: int
    onFulfilled: int


class TermData(TypedDict):
    deadline: DateTimeString
    payment: PaymentData
    deliver: list[DeliverData]


class ContractData(TypedDict):
    id: str
    factionSymbol: Faction
    type: str
    terms: TermData
    accepted: bool
    fulfilled: bool
    expiration: DateTimeString
    deadlineToAccept: DateTimeString


class ContractResponse(TypedDict):
    data: ContractData
    meta: MetaData


class AcceptContractData(TypedDict):
    contract: ContractData
    agent: AgentData


class AcceptContractResponse(TypedDict):
    data: AcceptContractData
