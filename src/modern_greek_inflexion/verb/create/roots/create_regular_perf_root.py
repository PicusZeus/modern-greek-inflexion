from modern_greek_inflexion.resources.typing import voiceType, presentConjugationType
from modern_greek_inflexion.resources.variables import ACTIVE, PASSIVE
from modern_greek_inflexion.verb.create.roots.create_regular_perf_active_root import create_regular_perf_active_root
from modern_greek_inflexion.verb.create.roots.create_regular_perf_passive_root import create_regular_perf_passive_root


def create_regular_perf_root(pres_form: str,
                             voice: voiceType = ACTIVE,
                             pres_conjugation: presentConjugationType = None,
                             root: str = None) -> str:

    """
    This function creates regular aorist roots from present root.
    :param pres_form: 1st person sg present simple form
    :param voice: ACTIVE or PASSIVE
    :param pres_conjugation: present conjugation type
    :param root: present tense stem
    :return: perfect stem active or passive, if multiple separated by coma
    """

    if pres_form.endswith('έρχομαι') or pres_form.endswith('γίνομαι') or pres_form.endswith('κάθομαι') or pres_form.endswith('ξανάρχομαι'):
        voice = ACTIVE

    if voice == PASSIVE:
        perf_root = create_regular_perf_passive_root(pres_form, pres_conjugation, root)

    else:
        perf_root = create_regular_perf_active_root(pres_form, pres_conjugation, root)

    if perf_root:
        return perf_root
