from unittest import TestCase

from modern_greek_inflexion import verb
from modern_greek_inflexion.resources import ACTIVE, IND, PASSIVE


def aorist_act(v):
    # return verb.create_all_forms(v)['aorist']['active']['ind']
    return verb.Verb(v).create_aorist()[ACTIVE][IND]


def aorist_pass(v):
    return verb.Verb(v).create_aorist()[PASSIVE][IND]


class VerbTestAorAct(TestCase):
    def test_menw(self):
        self.assertDictEqual(
            aorist_act('μένω'),
            {'pl': {'pri': {'μείναμε'}, 'sec': {'μείνατε'}, 'ter': {'έμειναν', 'μείνανε'}},
             'sg': {'pri': {'έμεινα'}, 'sec': {'έμεινες'}, 'ter': {'έμεινε'}}}
            ,
        )

    def test_verb_sympitw_aor(self):
        self.assertDictEqual(
            aorist_act('συμπίπτω'),
            {'sg': {'pri': {'συνέπεσα'}, 'sec': {'συνέπεσες'}, 'ter': {'συνέπεσε'}},
             'pl': {'pri': {'συμπέσαμε'}, 'sec': {'συμπέσατε'},
                    'ter': {'συνέπεσαν', 'συμπέσανε'}}}

        )

    def test_verb_synisto(self):
        self.assertDictEqual(
            aorist_act('συνιστώ'),
            {'pl': {'pri': {'συστήσαμε'},
                    'sec': {'συστήσατε'},
                    'ter': {'συνέστησαν', 'συστήσανε', 'σύστησαν'}},
             'sg': {'pri': {'συνέστησα', 'σύστησα'},
                    'sec': {'σύστησες', 'συνέστησες'},
                    'ter': {'συνέστησε', 'σύστησε'}}}

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

    def test_aorist_verb_eisago(self):
        self.assertDictEqual(
            aorist_act('εισάγω'),
            {'sg': {'pri': {'εισήγαγα'}, 'sec': {'εισήγαγες'}, 'ter': {'εισήγαγε'}},
             'pl': {'pri': {'εισαγάγαμε'}, 'sec': {'εισαγάγατε'},
                    'ter': {'εισήγαγαν', 'εισαγάγανε'}}}

        )

    def test_aorist_verb_anago(self):
        self.assertDictEqual(
            aorist_act('ανάγω'),
            {'sg': {'pri': {'ανήγαγα'}, 'sec': {'ανήγαγες'}, 'ter': {'ανήγαγε'}},
             'pl': {'pri': {'αναγάγαμε'}, 'sec': {'αναγάγατε'}, 'ter': {'ανήγαγαν', 'αναγάγανε'}}}

        )

    def test_verb_symbainw(self):
        # self.maxDiff = None
        self.assertDictEqual(
            aorist_act('συμβαίνω'),
            {'pl': {'pri': {'συνέβημεν'},
                    'sec': {'συνέβητε'},
                    'ter': {'συνέβησαν'}},
             'sg': {'pri': {'συνέβην'},
                    'sec': {'συνέβης'},
                    'ter': {'συνέβη'}}}

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

    def test_aorist_verb_anago(self):
        self.assertDictEqual(
            aorist_pass('ανάγω'),
            {
                'sg': {'pri': {'ανήχθην', 'ανάχθηκα'}, 'sec': {'ανήχθης', 'ανάχθηκες'}, 'ter': {'ανάχθηκε', 'ανήχθη'}},
                'pl': {'pri': {'ανήχθημεν', 'αναχθήκαμε'}, 'sec': {'αναχθήκατε', 'ανήχθητε'},
                       'ter': {'ανήχθησαν', 'ανάχθηκαν', 'αναχθήκανε'}}}

        )

    def test_aorist_verb_eisago(self):
        self.assertDictEqual(
            aorist_pass('εισάγω'),
             {
                'sg': {'pri': {'εισάχθηκα', 'εισήχθην'}, 'sec': {'εισάχθηκες', 'εισήχθης'},
                       'ter': {'εισάχθηκε', 'εισήχθη'}},
                'pl': {'pri': {'εισαχθήκαμε', 'εισήχθημεν'}, 'sec': {'εισήχθητε', 'εισαχθήκατε'},
                       'ter': {'εισάχθηκαν', 'εισαχθήκανε', 'εισήχθησαν'}}}

        )

    def test_verb_synisto(self):
        self.assertDictEqual(
            aorist_pass('συνιστώ'),
            {'pl': {'pri': {'συσταθήκαμε', 'συνεστάθημεν'},
                    'sec': {'συνεστάθητε', 'συσταθήκατε'},
                    'ter': {'συνεστάθησαν',
                            'συστάθηκαν',
                            'συσταθήκανε'}},
             'sg': {'pri': {'συστάθηκα', 'συνεστάθην'},
                    'sec': {'συνεστάθης', 'συστάθηκες'},
                    'ter': {'συστάθηκε', 'συνεστάθη'}}}

        )
