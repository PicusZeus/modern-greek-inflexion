from unittest import TestCase

from modern_greek_inflexion import verb


def imp_conj_act(v):
    return verb.create_all_forms(v)['conjunctive']['active']['imp']


def imp_conj_pass(v):
    return verb.create_all_forms(v)['conjunctive']['passive']['imp']


def imp_cont_act(v):
    return verb.create_all_forms(v)['present']['active']['imp']


def imp_cont_pass(v):
    return verb.create_all_forms(v)['present']['passive']['imp']


class VerbTestImperAct(TestCase):

    # IMPER_ACT_CONT_1
    def test_pinw(self):
        self.assertDictEqual(
            imp_cont_act('πίνω'),
            {'pl': {'sec': {'πίνετε'}}, 'sg': {'sec': {'πίνε'}}}

        )

    # IMPER_ACT_CONT_2A + IMPER_ACT_CONT_2B
    def test_milaw(self):
        self.assertDictEqual(
            imp_cont_act('μιλάω'),
            {'pl': {'sec': {'μιλάτε', 'μιλείτε'}},
             'sg': {'sec': {'μίλει', 'μίλαγε', 'μίλα'}}}

        )

    # IMER_ACT_CONT_2A
    def test_kathistw(self):
        self.assertDictEqual(
            imp_cont_act('καθιστώ'),
            {'pl': {'sec': {'καθιστάτε'}}, 'sg': {'sec': {'καθίστα'}}}
        )

    # IMPER_ACT_CONT_2D
    def test_plhrw(self):
        self.assertDictEqual(
            imp_cont_act('πληρώ'),
            {'pl': {'sec': {'πληροίτε'}}}

        )

    # IMPER_ACT_CONT_2C
    def test_klaiw(self):
        self.assertDictEqual(
            imp_cont_act('κλαίω'),
            {'pl': {'sec': {'κλαίγετε', 'κλαίτε'}}, 'sg': {'sec': {'κλαίγε'}}}

        )

    def test_lego(self):
        self.assertDictEqual(
            imp_conj_act('λέω'),
            {'pl': {'sec': {'πείτε', 'πέστε'}}, 'sg': {'sec': {'πες'}}}

        )

    def test_katebainw(self):
        self.assertDictEqual(
            imp_conj_act('κατεβαίνω'),
            {'pl': {'sec': {'κατεβείτε'}}, 'sg': {'sec': {'κατέβα'}}}

        )

    def test_paraggelnw(self):
        self.assertDictEqual(
            imp_conj_act('παραγγέλνω'),
            {'pl': {'sec': {'παραγγείλτε'}}, 'sg': {'sec': {'παράγγειλε'}}}

        )

class VerbTestImperPass(TestCase):
    def test_skeftomai(self):
        self.assertDictEqual(
            imp_cont_pass('σκέφτομαι'),
            {'pl': {'sec': {'σκέφτεστε'}}, 'sg': {'sec': {'σκέφτου'}}}
        )

    def test_dexomai(self):
        self.assertDictEqual(
            imp_conj_pass('δέχομαι'),
            {'pl': {'sec': {'δεχθείτε', 'δεχτείτε'}}, 'sg': {'sec': {'δέξου'}}}

        )

    def test_briskw(self):
        self.assertDictEqual(
            imp_conj_pass('βρίσκω'),
            {'pl': {'sec': {'βρεθείτε'}}, 'sg': {'sec': {''}}}

        )