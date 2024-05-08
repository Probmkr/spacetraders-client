from typing import TypedDict

from type.agent import AgentData
from type.waypoint import WayPointData

"""
{
  "data": {
    "cargo": {
      "capacity": 40,
      "inventory": [],
      "units": 0
    },
    "cooldown": {
      "remainingSeconds": 0,
      "shipSymbol": "PROBM-1",
      "totalSeconds": 0
    },
    "crew": {
      "capacity": 80,
      "current": 57,
      "morale": 100,
      "required": 57,
      "rotation": "STRICT",
      "wages": 0
    },
    "engine": {
      "condition": 1,
      "description": "An advanced propulsion system that uses ionized particles to generate high-speed, low-thrust acceleration, with improved efficiency and performance.",
      "integrity": 1,
      "name": "Ion Drive II",
      "requirements": {
        "crew": 8,
        "power": 6
      },
      "speed": 30,
      "symbol": "ENGINE_ION_DRIVE_II"
    },
    "frame": {
      "condition": 1,
      "description": "A medium-sized, multi-purpose spacecraft, often used for combat, transport, or support operations.",
      "fuelCapacity": 400,
      "integrity": 1,
      "moduleSlots": 8,
      "mountingPoints": 5,
      "name": "Frigate",
      "requirements": {
        "crew": 25,
        "power": 8
      },
      "symbol": "FRAME_FRIGATE"
    },
    "fuel": {
      "capacity": 400,
      "consumed": {
        "amount": 0,
        "timestamp": "2024-05-06T18:44:23.757Z"
      },
      "current": 400
    },
    "modules": [
      {
        "capacity": 40,
        "description": "An expanded cargo hold module that provides more efficient storage space for a ship's cargo.",
        "name": "Expanded Cargo Hold",
        "requirements": {
          "crew": 2,
          "power": 2,
          "slots": 2
        },
        "symbol": "MODULE_CARGO_HOLD_II"
      },
      {
        "capacity": 40,
        "description": "A module that provides living space and amenities for the crew.",
        "name": "Crew Quarters",
        "requirements": {
          "crew": 2,
          "power": 1,
          "slots": 1
        },
        "symbol": "MODULE_CREW_QUARTERS_I"
      },
      {
        "capacity": 40,
        "description": "A module that provides living space and amenities for the crew.",
        "name": "Crew Quarters",
        "requirements": {
          "crew": 2,
          "power": 1,
          "slots": 1
        },
        "symbol": "MODULE_CREW_QUARTERS_I"
      },
      {
        "description": "Crushes and processes extracted minerals and ores into their component parts, filters out impurities, and containerizes them into raw storage units.",
        "name": "Mineral Processor",
        "requirements": {
          "crew": 0,
          "power": 1,
          "slots": 2
        },
        "symbol": "MODULE_MINERAL_PROCESSOR_I"
      },
      {
        "description": "Filters and processes extracted gases into their component parts, filters out impurities, and containerizes them into raw storage units.",
        "name": "Gas Processor",
        "requirements": {
          "crew": 0,
          "power": 1,
          "slots": 2
        },
        "symbol": "MODULE_GAS_PROCESSOR_I"
      }
    ],
    "mounts": [
      {
        "description": "An advanced sensor array that improves a ship's ability to detect and track other objects in space with greater accuracy and range.",
        "name": "Sensor Array II",
        "requirements": {
          "crew": 2,
          "power": 2
        },
        "strength": 4,
        "symbol": "MOUNT_SENSOR_ARRAY_II"
      },
      {
        "description": "An advanced gas siphon that can extract gas from gas giants and other gas-rich bodies more efficiently and at a higher rate.",
        "name": "Gas Siphon II",
        "requirements": {
          "crew": 2,
          "power": 2
        },
        "strength": 20,
        "symbol": "MOUNT_GAS_SIPHON_II"
      },
      {
        "description": "An advanced mining laser that is more efficient and effective at extracting valuable minerals from asteroids and other space objects.",
        "name": "Mining Laser II",
        "requirements": {
          "crew": 2,
          "power": 2
        },
        "strength": 5,
        "symbol": "MOUNT_MINING_LASER_II"
      },
      {
        "deposits": [
          "QUARTZ_SAND",
          "SILICON_CRYSTALS",
          "PRECIOUS_STONES",
          "ICE_WATER",
          "AMMONIA_ICE",
          "IRON_ORE",
          "COPPER_ORE",
          "SILVER_ORE",
          "ALUMINUM_ORE",
          "GOLD_ORE",
          "PLATINUM_ORE",
          "DIAMONDS",
          "URANITE_ORE"
        ],
        "description": "An advanced survey probe that can be used to gather information about a mineral deposit with greater accuracy.",
        "name": "Surveyor II",
        "requirements": {
          "crew": 4,
          "power": 3
        },
        "strength": 2,
        "symbol": "MOUNT_SURVEYOR_II"
      }
    ],
    "nav": {
      "flightMode": "CRUISE",
      "route": {
        "arrival": "2024-05-06T18:44:23.757Z",
        "departureTime": "2024-05-06T18:44:23.757Z",
        "destination": {
          "symbol": "X1-ZQ60-A1",
          "systemSymbol": "X1-ZQ60",
          "type": "PLANET",
          "x": 10,
          "y": 25
        },
        "origin": {
          "symbol": "X1-ZQ60-A1",
          "systemSymbol": "X1-ZQ60",
          "type": "PLANET",
          "x": 10,
          "y": 25
        }
      },
      "status": "DOCKED",
      "systemSymbol": "X1-ZQ60",
      "waypointSymbol": "X1-ZQ60-A1"
    },
    "reactor": {
      "condition": 1,
      "description": "A basic fission power reactor, used to generate electricity from nuclear fission reactions.",
      "integrity": 1,
      "name": "Fission Reactor I",
      "powerOutput": 31,
      "requirements": {
        "crew": 8
      },
      "symbol": "REACTOR_FISSION_I"
    },
    "registration": {
      "factionSymbol": "COSMIC",
      "name": "PROBM-1",
      "role": "COMMAND"
    },
    "symbol": "PROBM-1"
  }
}
"""


class ShipCargoData(TypedDict):
    capacity: int
    inventory: list[str]
    units: int


class ShipCooldownData(TypedDict):
    remainingSeconds: int
    shipSymbol: str
    totalSeconds: int


class ShipCrewData(TypedDict):
    capacity: int
    current: int
    morale: int
    required: int
    rotation: str
    wages: int


class RequirementsData(TypedDict, total=False):
    crew: int
    slots: int
    power: int


class ShipEngineData(TypedDict):
    condition: int
    description: str
    integrity: int
    name: str
    requirements: RequirementsData
    speed: int
    symbol: str


class ShipFrameData(TypedDict):
    condition: int
    description: str
    fuelCapacity: int
    integrity: int
    moduleSlots: int
    mountingPoints: int
    name: str
    requirements: RequirementsData
    symbol: str


class FuelConsumedData(TypedDict):
    amount: int
    timestamp: str


class ShipFuelData(TypedDict):
    capacity: int
    consumed: FuelConsumedData
    current: int


class ShipModuleData(TypedDict):
    capacity: int
    description: str
    name: str
    requirements: RequirementsData
    symbol: str
    deposits: list[str]


class RouteDestinationData(WayPointData):
    pass


class RouteOriginData(WayPointData):
    pass


class NavRouteData(TypedDict):
    arrival: str
    departureTime: str
    destination: RouteDestinationData
    origin: RouteOriginData


class NavRouteData(TypedDict):
    arrival: str
    departureTime: str
    destination: RouteDestinationData
    origin: RouteOriginData


class ShipNavData(TypedDict):
    flightMode: str
    route: NavRouteData
    status: str
    systemSymbol: str
    waypointSymbol: str


class ShipReactorData(TypedDict):
    condition: int
    description: str
    integrity: int
    name: str
    powerOutput: int
    requirements: RequirementsData
    symbol: str


class ShipRegistrationData(TypedDict):
    factionSymbol: str
    name: str
    role: str


class ShipData(TypedDict):
    symbol: str
    cargo: ShipCargoData
    cooldown: ShipCooldownData
    crew: ShipCrewData
    engine: ShipEngineData
    frame: ShipFrameData
    fuel: ShipFuelData
    modules: list[ShipModuleData]
    nav: list[ShipNavData]
    reactor: ShipReactorData
    registration: ShipRegistrationData


class ShipResponse(TypedDict):
    data: ShipData


class ShipsResponse(TypedDict):
    data: list[ShipData]


class BuyShipData(TypedDict):
    agent: AgentData
    ship: ShipData


class BuyShipResponse(TypedDict):
    data: BuyShipData
