from modern_greek_inflexion.adjective.basic.create_basic_adj import create_all_basic_forms
from .all.create_all_adj import create_all_adj_forms
from .._exceptions import NotInGreekException
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.typing import adjective_basic_forms, adjective_forms_type
from ..resources.variables import ADJ, ADVERB, COMP, COMP_ADV, ADV, COMPARATIVE, ADVERB_COMPARATIVE, SUPERL, SUPERL_ADV
from modern_greek_inflexion.resources import greek_pattern


class Adjective:
    """

    """

    def __init__(self, adj: str, aklito: bool = False, basic_forms: adjective_basic_forms = None):
        """
        :param adj:
        :param aklito:
        :param basic_forms:
        """
        self.adjective = adj
        adj = convert_to_monotonic(adj, one_syllable_rule=False)

        if not greek_pattern.match(adj):
            raise NotInGreekException
        if basic_forms:
            self.basic_forms = basic_forms
        else:
            self.basic_forms = create_all_basic_forms(adj, aklito)

    @staticmethod
    def _adj(basic: str, adverb: str) -> tuple[adjective_forms_type, set[str]]:
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

    def positive_degree(self) -> dict[ADJ: adjective_forms_type, ADV: set[str]]:
        adj, adv = self._adj(self.basic_forms[ADJ], self.basic_forms[ADVERB])
        return {ADJ: adj, ADV: adv}

    def _comp_degree(self, bas_compars: str) -> tuple[adjective_forms_type, set[str]]:
        all_compars = []
        all_adverbs = set()

        for compar in bas_compars.split(','):
            base = create_all_basic_forms(compar)
            adj, adv = self._adj(base[ADJ], base[ADVERB])
            all_compars.append(adj)

            all_adverbs.update(adv)
        all_comp_forms = merging_all_dictionaries(*all_compars)

        return all_comp_forms, all_adverbs

    def comparative_degree(self) -> dict[COMP: adjective_forms_type, COMP_ADV: set[str]]:
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if compars != '-':
                comparative_forms, comparative_adv = self._comp_degree(compars)
                return {COMP: comparative_forms, COMP_ADV: set(advs_compar.split(','))}

    def superlative_degree(self) -> dict[SUPERL: adjective_forms_type, SUPERL_ADV: set[str]]:
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if superlatives != '-':
                comparative_forms, comparative_adv = self._comp_degree(superlatives)
                return {SUPERL: comparative_forms, SUPERL_ADV: set(advs_superlative.split(','))}

    def all(self) -> dict[ADJ: adjective_forms_type, ADV: set[str], COMP: adjective_forms_type, COMP_ADV: set[str],
                          SUPERL: adjective_forms_type, SUPERL_ADV: set[str]]:
        """

        :return:
        """
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
