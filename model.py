from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Die:
    value: int
    kept: bool

@dataclass(frozen=True)
class Turn:
    dice: list[Die]
    player: int         # spieler id
    rolls: int
@dataclass(frozen=True)
class Kniffel:
    current: Turn
