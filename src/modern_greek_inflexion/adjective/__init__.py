from modern_greek_inflexion.adjective.basic.create_basic_adj import create_all_basic_forms
from .all.create_all_adj import create_all_adj_forms
from ..exceptions import NotInGreekException
from modern_greek_inflexion.verb.helpers import merging_all_dictionaries
from modern_greek_accentuation.accentuation import convert_to_monotonic

from ..resources.typing import adj_basic_forms_type, genders_declensions_type, adj_declension_degree_type
from ..resources.variables import ADJ, ADVERB, COMP, COMP_ADV, ADV, COMPARATIVE, ADVERB_COMPARATIVE, SUPERL, SUPERL_ADV
from modern_greek_inflexion.resources import greek_pattern


class Adjective:
    """
    This class can be used to create adjective forms, all or only in certain degree, you can do it by instantiating the class with a single basic form (nom sg masc), you can also add already prepared basic forms.

    :param adj: A single form nominative singular masculine.
    :type adj: str
    :param aklito: If you know the noun is indeclinable, set it to True
    :type aklito: bool, optional
    :param basic_forms: a dictionary with the following shape ``{ADJ: "masc/fem/neut", COMPARATIVE: "parathetiko,alt_parathetiko/uperthetiko,alt_uperthetiko, ADVERB: "adverb,alt_adverb", ADVERB_COMPARATIVE: "adverb_parathetiko,alt_adverb_parathetiko/adverb_uperthetiko,alt_adverb_uperthetiko"}``
    :type basic_forms: dict, optional
    """

    def __init__(self, adj: str, aklito: bool = False, basic_forms: adj_basic_forms_type = None):

        self.adjective = adj
        adj = convert_to_monotonic(adj, one_syllable_rule=False)

        if not greek_pattern.match(adj):
            raise NotInGreekException
        if basic_forms:
            self.basic_forms = basic_forms
        else:
            self.basic_forms = create_all_basic_forms(adj, aklito)

    @staticmethod
    def _adj(basic: str, adverb: str) -> tuple[adj_declension_degree_type, set[str]]:
        """
        :param basic: "masc/fem/neut"
        :param adverb: set adverb, alt_adverb
        :return: two element tuple, the first is a dictionary with all inflexion adjective forms with the following
        structure:{SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, the second one is a set containing adverbs
        """
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

    def positive_degree(self) -> {ADJ: adj_declension_degree_type, ADV: set[str]}:
        """
        Creates positive degree forms

        :return: A dictionary of adjective forms in positive degree with the following shape: ``{ADJ: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, ADV: set(forms)}``
        :rtype: dict
        """
        adj, adv = self._adj(self.basic_forms[ADJ], self.basic_forms[ADVERB])
        return {ADJ: adj, ADV: adv}

    def _comp_degree(self, bas_compars: str) -> tuple[adj_declension_degree_type, set[str]]:
        """
        Creates comparative degree forms

        :param bas_compars: adj: masc nom sg form (`ωραιότερος`)
        :return: two element tuple, the first is a dictionary with all inflexion adjective forms with the following
        structure:{SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, the second one is a set containing adverbs
        """
        all_compars = []
        all_adverbs = set()

        for compar in bas_compars.split(','):
            base = create_all_basic_forms(compar)
            adj, adv = self._adj(base[ADJ], base[ADVERB])
            all_compars.append(adj)

            all_adverbs.update(adv)
        all_comp_forms = merging_all_dictionaries(*all_compars)

        return all_comp_forms, all_adverbs

    def comparative_degree(self) -> {COMP: adj_declension_degree_type, COMP_ADV: set[str]}:
        """
        Creates comparative degree forms

        :return: A dictionary of adjective forms in the comparative degree with the following shape: ``COMP: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, COMP_ADV: set(forms)``
        :rtype: dict
        """
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if compars != '-':
                comparative_forms, comparative_adv = self._comp_degree(compars)
                return {COMP: comparative_forms, COMP_ADV: set(advs_compar.split(','))}

    def superlative_degree(self) -> {SUPERL: adj_declension_degree_type, SUPERL_ADV: set[str]}:

        """
        Create superlative degree forms

        :return: A dictionary of adjective forms in the superlative degree with the following shape ``SUPERL: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, SUPERL_ADV: set(forms)}``
        :rtype: dict
        """
        basic_compar = self.basic_forms[COMPARATIVE]
        if basic_compar:
            compars, superlatives = basic_compar.split('/')
            advs_compar, advs_superlative = self.basic_forms[ADVERB_COMPARATIVE].split('/')
            if superlatives != '-':
                comparative_forms, comparative_adv = self._comp_degree(superlatives)
                return {SUPERL: comparative_forms, SUPERL_ADV: set(advs_superlative.split(','))}

    def all(self) -> {ADJ: adj_declension_degree_type, ADV: set[str], COMP: adj_declension_degree_type, COMP_ADV: set[str],
                      SUPERL: adj_declension_degree_type, SUPERL_ADV: set[str]}:
        """
        Create all forms from a basic adjective form

        :return: a dictionary with the following shape ``{ADJ: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, ADV: set(forms), COMP: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, COMP_ADV: set(forms), SUPERL: {SG: {MASC: {NOM: set(forms), ...}, ...}, ...}, SUPERL_ADV: set(forms)}``
        :rtype: dict
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
