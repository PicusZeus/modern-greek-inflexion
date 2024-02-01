from unittest import TestCase

from modern_greek_inflexion import verb


def aorist_act(v):
    return verb.create_all_forms(v)['aorist']['active']['ind']


def aorist_pass(v):
    return verb.create_all_forms(v)['aorist']['passive']['ind']


class VerbTestAorAct(TestCase):
    def test_menw(self):
        self.assertDictEqual(
            aorist_act('μένω'),
            {'pl': {'pri': {'μείναμε'}, 'sec': {'μείνατε'}, 'ter': {'έμειναν', 'μείνανε'}},
             'sg': {'pri': {'έμεινα'}, 'sec': {'έμεινες'}, 'ter': {'έμεινε'}}}
            ,
        )
    # sinizisi

    def test_teleiwnw(self):
        self.assertDictEqual(
            aorist_act('τελειώνω'),
            {'pl': {'pri': {'τελειώσαμε'},
                    'sec': {'τελειώσατε'},
                    'ter': {'τελείωσαν', 'τέλειωσαν', 'τελειώσανε'}},
             'sg': {'pri': {'τέλειωσα', 'τελείωσα'},
                    'sec': {'τέλειωσες', 'τελείωσες'},
                    'ter': {'τελείωσε', 'τέλειωσε'}}}

        )

    # esoteriki auksisi

    def test_ekdidw(self):
        self.assertDictEqual(
            aorist_act('εκδίδω'),
            {'pl': {'pri': {'εκδώσαμε'},
                    'sec': {'εκδώσατε'},
                    'ter': {'εξέδωσαν', 'εκδώσανε'}},
             'sg': {'pri': {'εξέδωσα'}, 'sec': {'εξέδωσες'}, 'ter': {'εξέδωσε'}}}

        )

    def test_paragw(self):
        self.assertDictEqual(
            aorist_act('παράγω'),
            {'pl': {'pri': {'παραγάγαμε'},
                    'sec': {'παραγάγατε'},
                    'ter': {'παρήγαγαν', 'παραγάγανε'}},
             'sg': {'pri': {'παρήγαγα'}, 'sec': {'παρήγαγες'}, 'ter': {'παρήγαγε'}}}
            ,
        )

class VerbTestAorPass(TestCase):
    def test_dexomai(self):
        self.assertDictEqual(
            aorist_pass('εκδίδω'),
            {'pl': {'pri': {'εξεδόθημεν', 'εκδοθήκαμε'},
                    'sec': {'εκδοθήκατε', 'εξεδόθητε'},
                    'ter': {'εκδόθηκαν', 'εκδοθήκανε', 'εξεδόθησαν'}},
             'sg': {'pri': {'εξεδόθην', 'εκδόθηκα'},
                    'sec': {'εξεδόθης', 'εκδόθηκες'},
                    'ter': {'εκδόθηκε', 'εξεδόθη'}}}

        )