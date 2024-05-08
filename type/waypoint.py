from typing import TypedDict
from type.common import MultiData
from type.literal import Faction
from type.alias import DateTimeString


class OrbitalData(TypedDict):
    symbol: str


class TraitData(TypedDict):
    symbol: str
    name: str
    description: str


class ModifierData(TypedDict):
    pass


class ChartData(TypedDict):
    submittedBy: Faction
    submittedOn: DateTimeString


class FactionData(TypedDict):
    symbol: Faction


class WayPointData(TypedDict):
    systemSymbol: str
    symbol: str
    type: str
    x: int
    y: int
    orbitals: list[OrbitalData]
    traits: list[TraitData]
    modifiers: list[ModifierData]
    chart: ChartData
    faction: FactionData
    isUnderConstruction: bool


class WayPointResponse(TypedDict):
    data: WayPointData


class WayPointsResponse(MultiData):
    data: list[WayPointData]
