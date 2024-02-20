from dataclasses import dataclass

from modern_greek_inflexion.resources import NOM, GEN, ACC, VOC, FEM, MASC, NEUT, SG, PL, ADJ, COMP, SUPERL, \
    COMPARATIVE, ADVERB, ADVERB_COMPARATIVE, NOM_SG, GEN_SG, NOM_PL, GENDERS, PROPER_NAME

from enum import Enum
from .resources import (ULTIMATE, ANTEPENULTIMATE, PENULTIMATE, MASC, MASC_PL,
                        MASC_SG, FEM_SG, FEM, FEM_PL, NEUT_SG, NEUT, NEUT_PL,
                        MASC_FEM)
from typing import NewType, Union


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


genderType = NewType("Genders", Gender)


class GendersBasic(Enum):
    MASC = MASC
    FEM = FEM
    NEUT = NEUT


genderBasicType = NewType("GendersBasic", GendersBasic)


class Numbers(Enum):
    PL = dict
    SG = dict


class Genders(Enum):
    FEM = Numbers
    MASC = Numbers
    NEUT = Numbers


class Adjective(Enum):
    GENDER = Genders


cases = dict[NOM: Union[str, tuple], VOC: Union[str, tuple], ACC: Union[str, tuple], GEN: Union[str, tuple]]

numbers = dict[SG: cases, PL: cases]

declension_forms_type = dict[FEM: numbers, MASC: numbers, NEUT: numbers]

adjective_basic_forms = dict[ADJ: str, COMPARATIVE: str, ADVERB: str, ADVERB_COMPARATIVE: str]

noun_basic_forms = dict[NOM_SG: str, GEN_SG: str, NOM_PL: str, GENDERS: list[genderType], PROPER_NAME: bool]
# adjective_type = dict[]

# ADJ: masc, fem, neut
# forms as a
# string
# divided
# with / ('ωραίος/ωραία/ωραίο') if alternatives, they are added and
# separated
# with a coma
# COMPARATIVE:
# if exists in form parathetiko + ',' + alt_parathetiko + '/' + uperthetiko + ',' + alt_uperthetiko with
# form
# only in masc
# sing
# nom
# ADVERB: adverb
# form,
# if alternatives, then separated with coma
# ADVERB_COMPARATIVE:
# if exists, adverb_parathetiko + ',' + alt_adverb_parathetiko + '/' + adverb_uperthetiko + ',' + alt_adverb_uperthetiko