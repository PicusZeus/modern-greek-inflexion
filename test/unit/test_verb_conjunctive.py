from unittest import TestCase


from modern_greek_inflexion import verb


def conj_act(v):
    return verb.create_all_forms(v)['conjunctive']['active']['ind']


def conj_pass(v):
    return verb.create_all_forms(v)['conjunctive']['passive']['ind']


class VerbTestConAct(TestCase):
    def test_douleuw(self):
        self.assertDictEqual(
            conj_act('δουλεύω'),
            {'pl': {'pri': {'δουλεύσουμε', 'δουλεύσομε', 'δουλέψομε', 'δουλέψουμε'},
                    'sec': {'δουλέψετε', 'δουλεύσετε'},
                    'ter': {'δουλέψουνε', 'δουλεύσουν', 'δουλεύσουνε', 'δουλέψουν'}},
             'sg': {'pri': {'δουλεύσω', 'δουλέψω'},
                    'sec': {'δουλέψεις', 'δουλεύσεις'},
                    'ter': {'δουλέψει', 'δουλεύσει'}}}
            ,
        )

    def test_trww(self):
        self.assertDictEqual(
            conj_act('τρώω'),
            {'pl': {'pri': {'φάγομε', 'φάμε', 'φάγουμε'},
                    'sec': {'φάγετε', 'φάτε'},
                    'ter': {'φάγουν', 'φαν', 'φάνε', 'φάγουνε'}},
             'sg': {'pri': {'φάω', 'φάγω'},
                    'sec': {'φάγεις', 'φας'},
                    'ter': {'φάγει', 'φάει'}}}

        )

    def test_kathomai(self):
        self.assertDictEqual(
            conj_act('κάθομαι'),
            {'pl': {'pri': {'καθίσουμε', 'κάτσομε', 'κάτσουμε', 'καθίσομε'},
                    'sec': {'κάτσετε', 'καθίσετε'},
                    'ter': {'καθίσουν', 'κάτσουνε', 'κάτσουν', 'καθίσουνε'}},
             'sg': {'pri': {'καθίσω', 'κάτσω'},
                    'sec': {'κάτσεις', 'καθίσεις'},
                    'ter': {'καθίσει', 'κάτσει'}}}

        )

    def test_blepw(self):
        self.assertDictEqual(
            conj_act('βλέπω'),
            {'pl': {'pri': {'δούμε'}, 'sec': {'δείτε'}, 'ter': {'δούνε', 'δουν'}},
             'sg': {'pri': {'δω'}, 'sec': {'δεις'}, 'ter': {'δει'}}}

        )
class VerbTestConPass(TestCase):

    def test_lego(self):
        self.assertDictEqual(
            conj_pass('λέγω'),
            {'pl': {'pri': {'ειπωθούμε', 'λεχθούμε'},
                    'sec': {'λεχθείτε', 'ειπωθείτε'},
                    'ter': {'λεχθούν', 'ειπωθούν', 'λεχθούνε', 'ειπωθούνε'}},
             'sg': {'pri': {'λεχθώ', 'ειπωθώ'},
                    'sec': {'ειπωθείς', 'λεχθείς'},
                    'ter': {'λεχθεί', 'ειπωθεί'}}}
            ,
        )
