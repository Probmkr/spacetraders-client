from typing import TypedDict

from type.agent import AgentData


class RegisterData(TypedDict):
    token: str
    agent: AgentData


class RegisterResponse(TypedDict):
    data: RegisterData
