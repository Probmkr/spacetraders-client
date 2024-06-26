from typing import TypedDict


class MetaData(TypedDict):
    total: int
    page: int
    limit: int


class MultiData(TypedDict):
    meta: MetaData
