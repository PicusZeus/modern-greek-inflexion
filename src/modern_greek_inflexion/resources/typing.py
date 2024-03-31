from enum import Enum
from .variables import *
from typing import NewType, Union, Any


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


cases_type = {NOM: set[str], VOC: set[str], ACC: set[str], GEN: set[str]}

# adjective, pronouns itp

genders_adj_type = {MASC: cases_type, FEM: cases_type, NEUT: cases_type}

adj_declension_degree_type = {SG: genders_adj_type, PL: genders_adj_type}

adj_basic_forms_type = {ADJ: str, COMPARATIVE: str, ADVERB: str, ADVERB_COMPARATIVE: str}


tenseType = NewType("tenseType", Tenses)

cases = {NOM: set[str], VOC: set[str], ACC: set[str], GEN: set[str]}

numbers = {SG: cases, PL: cases}

genders_declensions_type = {FEM: numbers, MASC: numbers, NEUT: numbers}

noun_basic_forms = {NOM_SG: str, GEN_SG: str, NOM_PL: str, GENDERS: list[genderType], PROPER_NAME: bool}

recognized_conjugation_type = {ASPECT: aspectType, VOICE: voiceType, TENSE: tenseType,
                               ROOT: str, CONJUGATION_IND: str, CONJUGATION_IMP: str, CONJUGATION_PART: str}

basic_forms_type = {ACT_PRES_PARTICIPLE: set[str],
                    ACTIVE_AORIST_PARTICIPLE: set[str],
                    AORIST: {ACTIVE: set[str],
                            PASSIVE: set[str]},
                    ARCH_ACT_PRES_PARTICIPLE: set[str],
                    CONJUNCTIVE: {ACTIVE: set[str], PASSIVE: set[str]},
                    MODAL: bool,
                    PRES_CONJUGATION: str,
                    PARATATIKOS: {ACTIVE: set[str], PASSIVE: set[str]},
                    PASSIVE_AORIST_PARTICIPLE: set[str],
                    PASSIVE_PERFECT_PARTICIPLE: set[str],
                    PRESENT: {ACTIVE: set[str], PASSIVE: set[str]}}

personal_forms_type = {SG: {PRI: set[str], SEC: set[str], TER: set[str]},
                       PL: {PRI: set[str], SEC: set[str], TER: set[str]}}

voice_forms_imp_type = {ACTIVE: {IND: personal_forms_type, IMP: personal_forms_type}, PASSIVE: {IND: personal_forms_type, IMP: personal_forms_type}}
voice_forms_type = {ACTIVE: {IND: personal_forms_type}, PASSIVE: {IND: personal_forms_type}}

participles_type = {ARCH_ACT_PRES_PARTICIPLE: genders_declensions_type, PASSIVE_PERFECT_PARTICIPLE: genders_declensions_type, PASS_PRES_PARTICIPLE: genders_declensions_type, ACTIVE_AORIST_PARTICIPLE: genders_declensions_type, PASSIVE_AORIST_PARTICIPLE: genders_declensions_type, ACT_PRES_PARTICIPLE: set[str]}



