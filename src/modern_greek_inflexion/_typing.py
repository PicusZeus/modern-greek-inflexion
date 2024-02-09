from enum import Enum
from .resources import (ULTIMATE, ANTEPENULTIMATE, PENULTIMATE, MASC, MASC_PL,
                        MASC_SG, FEM_SG, FEM, FEM_PL, NEUT_SG, NEUT, NEUT_PL,
                        MASC_FEM)
from typing import NewType


class Accent(Enum):
    ULTIMATE = ULTIMATE
    PENULTIMATE = PENULTIMATE
    ANTEPENULTIMATE = ANTEPENULTIMATE


AccentType = NewType('Accents', Accent)


class Gender(Enum):
    MASC = MASC
    MASC_PL = MASC_PL
    MASC_SG = MASC_SG
    FEM_SG = FEM_SG
    FEM = FEM
    FEM_PL = FEM_PL
    NEUT_SG = NEUT_SG
    NEUT = NEUT
    NEUT_PL = NEUT_PL
    MASC_FEM = MASC_FEM
    NONE = None


GenderType = NewType("Genders", Gender)
