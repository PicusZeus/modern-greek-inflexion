from __future__ import annotations

from modern_greek_inflexion.resources.typing import voiceType, presentConjugationType
from modern_greek_inflexion.resources.variables import ACTIVE, PASSIVE
from modern_greek_inflexion.verb.create.roots.create_regular_perf_active_root import create_regular_perf_active_root
from modern_greek_inflexion.verb.create.roots.create_regular_perf_passive_root import create_regular_perf_passive_root


def create_regular_perf_root(verb: str,
                             voice: voiceType = ACTIVE,
                             act_perf_root: str = None,
                             pres_conjugation: presentConjugationType = None,
                             root: str = None) -> str | None:

    """
    create regular aorist roots from present root. For obvious reasons it's only useful for verbs you don't have
    supplied aorist forms and so it is prone to errors that cannot be eliminated
    :param verb:
    :param voice:
    :param act_perf_root:
    :param pres_conjugation:
    :param root:
    :return:
    """

    if verb.endswith('έρχομαι') or verb.endswith('γίνομαι') or verb.endswith('κάθομαι') or verb.endswith('ξανάρχομαι'):
        voice = ACTIVE

    if voice == PASSIVE:
        perf_root = create_regular_perf_passive_root(verb, act_perf_root, pres_conjugation, root)

    else:
        perf_root = create_regular_perf_active_root(verb, pres_conjugation, root)

    if perf_root:
        return perf_root
