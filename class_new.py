from dataclasses import dataclass
from dataclasses import make_dataclass
from typing import Any, List
from math import asin, cos, radians, sin, sqrt
# import attr


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Desk:
    cards: List[PlayingCard]


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


Position = make_dataclass('Position', ['name', 'lat', 'lon'])


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


@dataclass
class Capital(Position):
    country: str = 'Unknown'
    lat: float = 40.0


# @attr.s
# class AttrsCard:
#     rank = attr.ib()
#     suit = attr.ib()


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return  NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


@dataclass
class DataClassCard:
    rank: str
    suit: str
