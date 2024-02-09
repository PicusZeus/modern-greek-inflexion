from dataclasses import dataclass
from icecream import ic

from modern_greek_inflexion.adjective.basic.create_basic_adj import create_all_basic_forms
from modern_greek_inflexion.adjective.all.create_all_adj import create_all_adj_forms
from .._exceptions import NotInGreekException
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources.resources import ADJ, ADVERB, COMP, COMP_ADV, ADV, COMPARATIVE, ADVERB_COMPARATIVE, SUPERL, SUPERL_ADV
import re

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)


@dataclass
class Cases:
    nom: tuple[str]
    gen: tuple[str]
    acc: tuple[str]
    voc: tuple[str]


@dataclass
class Genders:
    fem: Cases
    masc: Cases
    neut: Cases


@dataclass
class Numbers:
    sg: Genders
    pl: Genders


@dataclass
class Adjective:
    adj: Numbers
    comp: Numbers
    superl: Numbers
    adv: tuple[str]
    comp_adv: tuple[str]
    superl_adv: tuple[str]


class Adj:

    def __init__(self, adj: str, aklito: bool = False, basic_forms: dict = None):
        self.adjective = adj
        adj = convert_to_monotonic(adj, one_syllable_rule=False)

        if not greek_pattern.match(adj):
            raise NotInGreekException
        if basic_forms:
            self.basic_forms = basic_forms
        else:
            self.basic_forms = create_all_basic_forms(adj, aklito)

    @staticmethod
    def _adj(basic, adverb):
        forms, alternative_forms = create_all_adj_forms(basic)

        if alternative_forms:
            adj = merging_all_dictionaries(forms, alternative_forms)
        else:
            adj = merging_all_dictionaries(forms, forms)

        if adverb:
            adv = set(adverb.split(','))
        else:
            adv = set()

        return adj, adv

    def positive_degree(self):
        adj, adv = self._adj(self.basic_forms[ADJ], self.basic_forms[ADVERB])
        return {ADJ: adj, ADV: adv}

    def _comp_degree(self, bas_compars):
        all_compars = []
        all_adverbs = set()
        # if self.adjective == 'καλός':
            # ic(all_adverbs, self.basic_forms[ADVERB_COMPARATIVE])
        for compar in bas_compars.split(','):
            base = create_all_basic_forms(compar)
            adj, adv = self._adj(base[ADJ], base[ADVERB])
            all_compars.append(adj)

            all_adverbs.update(adv)
        all_comp_forms = merging_all_dictionaries(*all_compars)

        return all_comp_forms, all_adverbs

    def comparative_degree(self):
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if compars != '-':
                comparative_forms, comparative_adv = self._comp_degree(compars)
                return {COMP: comparative_forms, COMP_ADV: set(advs_compar.split(','))}

    def superlative_degree(self):
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if superlatives != '-':
                comparative_forms, comparative_adv = self._comp_degree(superlatives)
                return {SUPERL: comparative_forms, SUPERL_ADV: set(advs_superlative.split(','))}

    def all(self):
        _all = {}
        adj, adv = self._adj(self.basic_forms[ADJ], self.basic_forms[ADVERB])
        _all[ADJ] = adj
        if adv:
            _all[ADV] = adv

        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if compars != '-':
                comparative_forms, _ = self._comp_degree(compars)
                _all[COMP] = comparative_forms
                # if comparative_adv:
                _all[COMP_ADV] = set(advs_compar.split(','))
            if superlatives != '-':
                superlative_forms, _ = self._comp_degree(superlatives)
                _all[SUPERL] = superlative_forms
                # if superlative_adv:
                _all[SUPERL_ADV] = set(advs_superlative.split(','))

        return _all


def create_all(adj: str, aklito=False) -> dict:
    """
    :param aklito: boolean
    :param adj: masc sg nom form
    :return: dictionary with keys:
    'adj': array with dictionaries of forms and alternative forms
    'comp'. array with dictionaries of all comparative forms and alternative forms (if exists monolektik type)
    'superl': array with dictionaries of all superlative forms and alternative forms (if exists)
    'adv': array of all possible adverbs
    'comp_adv': array of all possible comparative adverbs (if exists)
    'comp_superl': array of all possible superlative adverbs (if exists)

    """
    adj = convert_to_monotonic(adj, one_syllable_rule=False)
    if not greek_pattern.match(adj):
        raise NotInGreekException

    forms = []
    comp_forms = []
    super_forms = []
    adverbs = []
    comp_adv = []
    super_adv = []

    all_basic_adj_forms = create_all_basic_forms(adj, aklito=aklito)
    if all_basic_adj_forms[ADJ]:

        all_adj_infl_forms = create_all_adj_forms(all_basic_adj_forms[ADJ])

        forms.append(all_adj_infl_forms[0])

        if all_adj_infl_forms[1]:
            forms.append(all_adj_infl_forms[1])

    basic_compar = all_basic_adj_forms[COMPARATIVE]
    if basic_compar:

        compars, superlatives = basic_compar.split('/')
        if compars != '-':
            for compar in compars.split(','):

                base = create_all_basic_forms(compar)
                all_inf_comp_forms, alternatives = create_all_adj_forms(base[ADJ])

                if all_inf_comp_forms:
                    comp_forms.append(all_inf_comp_forms)
                if alternatives:
                    comp_forms.append(alternatives)
        if superlatives and superlatives != '-':
            for superlative in superlatives.split(','):
                base = create_all_basic_forms(superlative)
                all_inf_superl_forms, alternatives = create_all_adj_forms(base[ADJ])
                if all_inf_superl_forms:
                    super_forms.append(all_inf_superl_forms)
                if alternatives:
                    super_forms.append(alternatives)

    if all_basic_adj_forms[ADVERB]:
        for adverb in all_basic_adj_forms[ADVERB].split(','):
            adverbs.append(adverb)

    if all_basic_adj_forms[ADVERB_COMPARATIVE]:
        adv_comparatives, adv_superlatives = all_basic_adj_forms[ADVERB_COMPARATIVE].split('/')
        if adv_comparatives != '-':
            for adv_comparative in adv_comparatives.split(','):
                comp_adv.append(adv_comparative)
        if adv_superlatives != '-':
            for adv_superlative in adv_superlatives.split(','):
                super_adv.append(adv_superlative)
    result = {}
    if forms:
        forms = merging_all_dictionaries(*forms)

        result[ADJ] = forms
    if comp_forms:

        comp_forms = merging_all_dictionaries(*comp_forms)
        if not comp_forms:
            raise ValueError
        result[COMP] = comp_forms
    if super_forms:
        super_forms = merging_all_dictionaries(*super_forms)
        result[SUPERL] = super_forms
    if adverbs:
        adverbs = set(adverbs)
        result[ADV] = adverbs
    if comp_adv:
        comp_adv = set(comp_adv)
        result[COMP_ADV] = comp_adv
    if super_adv:
        super_adv = set(super_adv)
        result[SUPERL_ADV] = super_adv

    return result
