from enum import Enum
from .variables import *
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


class Voice(Enum):
    PASSIVE = PASSIVE
    ACTIVE = ACTIVE


voiceType = NewType("VoiceType", Voice)


class Aspect(Enum):
    PERF = PERF
    IMPERF = IMPERF


aspectType = NewType("aspectType", Aspect)


class PresentConjugation(Enum):
    EIMAI = EIMAI
    CON2AB = CON2AB
    CON1_ACT = CON1_ACT
    CON1_PASS_ARCHAIC = CON1_PASS_ARCHAIC
    CON2A_ACT = CON2A_ACT
    CON2AK_ACT = CON2AK_ACT
    CON2B_ACT = CON2B_ACT
    CON2B_PASS_ARCHAIC = CON2B_PASS_ARCHAIC
    CON2C_ACT = CON2C_ACT
    CON2D_ACT = CON2D_ACT
    CON1_ACT_MODAL = CON1_ACT_MODAL
    CON2_ACT_MODAL = CON2_ACT_MODAL
    CON1_PASS = CON1_PASS
    CON2A_PASS = CON2A_PASS
    CON2AK_PASS = CON2AK_PASS
    CON2B_PASS = CON2B_PASS
    CON2C_PASS = CON2C_PASS
    CON2F_PASS = CON2F_PASS
    CON2D_PASS = CON2D_PASS
    CON2E_PASS = CON2E_PASS


presentConjugationType = NewType("presentConjugationType", PresentConjugation)


class Numbers(Enum):
    PL = dict
    SG = dict


class Genders(Enum):
    FEM = Numbers
    MASC = Numbers
    NEUT = Numbers


class Adjective(Enum):
    GENDER = Genders


class Tenses(Enum):
    FIN = FIN
    PAST = PAST


tenseType = NewType("tenseType", Tenses)

cases = dict[NOM: Union[str, tuple], VOC: Union[str, tuple], ACC: Union[str, tuple], GEN: Union[str, tuple]]

numbers = dict[SG: cases, PL: cases]

declension_forms_type = dict[FEM: numbers, MASC: numbers, NEUT: numbers]

adjective_basic_forms = dict[ADJ: str, COMPARATIVE: str, ADVERB: str, ADVERB_COMPARATIVE: str]

noun_basic_forms = dict[NOM_SG: str, GEN_SG: str, NOM_PL: str, GENDERS: list[genderType], PROPER_NAME: bool]

recognized_conjugation_type = dict[ASPECT: aspectType, VOICE: voiceType, TENSE: tenseType,
                                   ROOT: str, CONJUGATION_IND: str, CONJUGATION_IMP: str, CONJUGATION_PART: str]


basic_forms_type = dict[ACT_PRES_PARTICIPLE: set[str],
                        ACTIVE_AORIST_PARTICIPLE: set[str],
                        AORIST: dict[ACTIVE: set[str],
                                     PASSIVE: set[str]],
                        ARCH_ACT_PRES_PARTICIPLE: set[str],
                        CONJUNCTIVE: dict[ACTIVE: set[str], PASSIVE: set[str]],
                        MODAL: bool,
                        PRES_CONJUGATION: str,
                        PARATATIKOS: dict[ACTIVE: set[str], PASSIVE: set[str]],
                        PASSIVE_AORIST_PARTICIPLE: set[str],
                        PASSIVE_PERFECT_PARTICIPLE: set[str],
                        PRESENT: dict[ACTIVE: set[str], PASSIVE: set[str]]]

personal_forms_type = dict[SG: dict[PRI: list[str], SEC: list[str], TER: list[str]],
                           PL: dict[PRI: list[str], SEC: list[str], TER: list[str]]]

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
