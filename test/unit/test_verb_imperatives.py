from unittest import TestCase

from modern_greek_inflexion import verb
from modern_greek_inflexion.resources.variables import CONJUNCTIVE, ACTIVE, IMP, PASSIVE, PRESENT


def imp_conj_act(v):
    return verb.Verb(v).create_conjunctive()[ACTIVE][IMP]


def imp_conj_pass(v):
    return verb.Verb(v).create_conjunctive()[PASSIVE][IMP]


def imp_cont_act(v):
    return verb.Verb(v).create_imperfect_forms()[PRESENT][ACTIVE][IMP]


def imp_cont_pass(v):
    return verb.Verb(v).create_imperfect_forms()[PRESENT][PASSIVE][IMP]


class VerbTestImperAct(TestCase):

    # IMPER_ACT_CONT_1
    def test_pinw(self):
        self.assertDictEqual(
            imp_cont_act('πίνω'),
            {'pl': {'sec': {'πίνετε'}}, 'sg': {'sec': {'πίνε'}}}

        )

    def test_verb_xairw_imper(self):
        self.assertDictEqual(
            imp_cont_act('χαίρω'),
            {'sg': {'sec': {'χαίρε'}}, 'pl': {'sec': {'χαίρετε'}}}

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
            {'pl': {'sec': {'πληρούτε'}}}

        )

    # IMPER_ACT_CONT_2C
    def test_klaiw(self):
        self.assertDictEqual(
            imp_cont_act('κλαίω'),
            {'pl': {'sec': {'κλαίγετε', 'κλαίτε'}}, 'sg': {'sec': {'κλαίγε'}}}

        )

    def test_odhgw(self):
        self.assertDictEqual(
            imp_cont_act('οδηγώ'),
            {'pl': {'sec': {'οδηγάτε', 'οδηγείτε'}}, 'sg': {'sec': {'οδήγα', 'οδήγει'}}}

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

    def test_parembainw(self):
        self.assertDictEqual(
            imp_conj_act('παρεμβαίνω'),
            {'pl': {'sec': {'παρέμβετε'}}}
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

    def test_verb_antilambanomai_imp(self):
        self.assertDictEqual(
            imp_conj_pass('αντιλαμβάνομαι'),
            {'sg': {'sec': {'αντιλήψου'}}, 'pl': {'sec': {'αντιληφθείτε'}}}
        )

    def test_briskw(self):
        self.assertDictEqual(
            imp_conj_pass('βρίσκω'),
            {'pl': {'sec': {'βρεθείτε'}}, 'sg': {'sec': {''}}}

        )