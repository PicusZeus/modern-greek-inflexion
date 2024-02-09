from unittest import TestCase

from icecream import ic

from modern_greek_inflexion import verb


def parat_act(v):
    return verb.create_all_forms(v)['paratatikos']['active']['ind']


def parat_pass(v):
    return verb.create_all_forms(v)['paratatikos']['passive']['ind']


class VerbTestParatAct(TestCase):

    # PARAT1_ACT
    def test_blepw(self):
        self.assertDictEqual(
            parat_act('βλέπω'),
            {'pl': {'pri': {'βλέπαμε'}, 'sec': {'βλέπατε'}, 'ter': {'έβλεπαν', 'βλέπανε'}},
             'sg': {'pri': {'έβλεπα'}, 'sec': {'έβλεπες'}, 'ter': {'έβλεπε'}}}

        )

    def test_elpizw(self):
        self.assertDictEqual(
            parat_act('ελπίζω'),
            {'pl': {'pri': {'ελπίζαμε'},
                    'sec': {'ελπίζατε'},
                    'ter': {'έλπιζαν', 'ήλπιζαν', 'ελπίζανε'}},
             'sg': {'pri': {'ήλπιζα', 'έλπιζα'},
                    'sec': {'ήλπιζες', 'έλπιζες'},
                    'ter': {'έλπιζε', 'ήλπιζε'}}}
        )

    # sinizisi
    def test_teleiwnw(self):
        self.assertDictEqual(
            parat_act('τελειώνω'),
            {'pl': {'pri': {'τελειώναμε'},
                    'sec': {'τελειώνατε'},
                    'ter': {'τέλειωναν', 'τελείωναν', 'τελειώνανε'}},
             'sg': {'pri': {'τελείωνα', 'τέλειωνα'},
                    'sec': {'τελείωνες', 'τέλειωνες'},
                    'ter': {'τελείωνε', 'τέλειωνε'}}}
            ,
        )

    # esoteriki auksisi

    def test_enkrinw(self):
        self.assertDictEqual(
            parat_act('εγκρίνω'),
            {'pl': {'pri': {'εγκρίναμε'},
                    'sec': {'εγκρίνατε'},
                    'ter': {'ενέκριναν', 'εγκρίνανε'}},
             'sg': {'pri': {'ενέκρινα'},
                    'sec': {'ενέκρινες'},
                    'ter': { 'ενέκρινε'}}}
            ,
        )

    def test_syllambanw(self):
        self.assertDictEqual(
            parat_act('συλλαμβάνω'),
            {'pl': {'pri': {'συλλαμβάναμε', 'συνελαμβάναμε'},
                    'sec': {'συλλαμβάνατε', 'συνελαμβάνατε'},
                    'ter': {'συλλάμβαναν',
                            'συλλαμβάνανε',
                            'συνελάμβαναν',
                            'συνελαμβάνανε'}},
             'sg': {'pri': {'συλλάμβανα', 'συνελάμβανα'},
                    'sec': {'συλλάμβανες', 'συνελάμβανες'},
                    'ter': {'συνελάμβανε', 'συλλάμβανε'}}}
            ,
            # ic(parat_act('συλλαμβάνω'))
        )

    # CON2A
    def test_rotaw(self):
        self.assertDictEqual(
            parat_act('ρωτάω'),
            {'pl': {'pri': {'ρωτούσαμε', 'ρωτάγαμε'},
                    'sec': {'ρωτάγατε', 'ρωτούσατε'},
                    'ter': {'ρωτούσαν', 'ρώταγαν', 'ρωτάγανε', 'ρωτούσανε'}},
             'sg': {'pri': {'ρώταγα', 'ρωτούσα'},
                    'sec': {'ρώταγες', 'ρωτούσες'},
                    'ter': {'ρώταγε', 'ρωτούσε'}}}

        )

    # CON2B
    def test_zw(self):
        self.assertDictEqual(
            parat_act('ζω'),
            {'pl': {'pri': {'ζούσαμε'}, 'sec': {'ζούσατε'}, 'ter': {'ζούσανε', 'ζούσαν'}},
             'sg': {'pri': {'ζούσα'}, 'sec': {'ζούσες'}, 'ter': {'ζούσε'}}}

        )

    # CON2A + CON2B
    def test_lalw(self):
        self.assertDictEqual(
            parat_act('λαλώ'),
            {'pl': {'pri': {'λαλάγαμε', 'λαλούσαμε'},
                    'sec': {'λαλάγατε', 'λαλούσατε'},
                    'ter': {'λάλαγαν', 'λαλούσανε', 'λαλάγανε', 'λαλούσαν'}},
             'sg': {'pri': {'λαλούσα', 'λάλαγα'},
                    'sec': {'λάλαγες', 'λαλούσες'},
                    'ter': {'λαλούσε', 'λάλαγε'}}}

        )


class VerbTestParPass(TestCase):

    # PARAT1_PASS

    def test_erxomai(self):
        self.assertDictEqual(
            parat_pass('έρχομαι'),
            {'pl': {'pri': {'ερχόμασταν', 'ερχόμαστε'},
                    'sec': {'ερχόσαστε', 'ερχόσασταν'},
                    'ter': {'έρχονταν', 'ερχόντουσαν'}},
             'sg': {'pri': {'ερχόμουν', 'ερχόμουνα'},
                    'sec': {'ερχόσουν', 'ερχόσουνα'},
                    'ter': {'ερχότανε', 'ερχόταν'}}}
            ,

        )

    def test_anamenw(self):
        self.assertDictEqual(
            parat_pass('αναμένω'),
            {'pl': {'pri': {'αναμενόμαστε', 'αναμενόμασταν'},
                    'sec': {'αναμενόσαστε', 'αναμενόσασταν'},
                    'ter': {'αναμένονταν', 'αναμενόντουσαν'}},
             'sg': {'pri': {'αναμενόμουνα', 'αναμενόμουν'},
                    'sec': {'αναμενόσουνα', 'αναμενόσουν'},
                    'ter': {'αναμενότανε', 'αναμένετο', 'αναμενόταν'}}}

        )

    # PARAT2A_PASS
    def test_anarwtiemai(self):
        self.assertDictEqual(
            parat_pass('αναρωτιέμαι'),
            {'pl': {'pri': {'αναρωτιόμαστε', 'αναρωτιόμασταν'},
                    'sec': {'αναρωτιόσαστε', 'αναρωτιόσασταν'},
                    'ter': {'αναρωτιόνταν', 'αναρωτιούνταν', 'αναρωτιόντουσαν'}},
             'sg': {'pri': {'αναρωτιόμουν', 'αναρωτιόμουνα'},
                    'sec': {'αναρωτιόσουνα', 'αναρωτιόσουν'},
                    'ter': {'αναρωτιόταν', 'αναρωτιότανε'}}}

        )

    def test_eksarwmai(self):
        self.assertDictEqual(
            parat_pass('εξαρτώ'),
            {'pl': {'pri': {'εξαρτιόμασταν', 'εξαρτιόμαστε'},
                    'sec': {'εξαρτιόσαστε', 'εξαρτιόσασταν'},
                    'ter': {'εξαρτιόντουσαν', 'εξαρτιούνταν', 'εξαρτιόνταν', 'εξαρτώντο'}},
             'sg': {'pri': {'εξαρτιόμουν', 'εξαρτιόμουνα'},
                    'sec': {'εξαρτιόσουνα', 'εξαρτιόσουν'},
                    'ter': {'εξαρτιόταν', 'εξαρτάτο', 'εξαρτιότανε'}}}

        )

    # PARAT2AK_PASS
    def test_kataxrwmai(self):
        self.assertDictEqual(
            parat_pass('καταχρώμαι'),
            {'pl': {'pri': {'καταχρόμασταν', 'καταχρόμαστε'},
                    'sec': {'καταχρόσαστε', 'καταχρόσασταν'},
                    'ter': {'καταχρόνταν', 'καταχρώντο'}},
             'sg': {'pri': {'καταχρόμουν'},
                    'sec': {'καταχρόσουν'},
                    'ter': {'καταχρόταν', 'καταχράτο'}}}

        )
    # PARAT2B_PASS
    def test_apotelw(self):
        self.assertDictEqual(
            parat_pass('αποτελώ'),
            {'pl': {'pri': {'αποτελούμασταν', 'αποτελούμαστε'},
                    'sec': {'αποτελούσαστε', 'αποτελούσασταν'},
                    'ter': {'αποτελούνταν', 'αποτελούντο'}},
             'sg': {'pri': {'αποτελούμουν'},
                    'sec': {'αποτελούσουν'},
                    'ter': {'αποτελούνταν', 'αποτελείτο'}}}

        )

    # PARAT2B_PASS + PARAT2B_PASS

    def test_kubernw(self):
        self.assertDictEqual(
            parat_pass('κυβερνώ'),
            {'pl': {'pri': {'κυβερνιόμασταν',
                            'κυβερνιόμαστε',
                            'κυβερνούμασταν',
                            'κυβερνούμαστε'},
                    'sec': {'κυβερνιόσασταν',
                            'κυβερνιόσαστε',
                            'κυβερνούσασταν',
                            'κυβερνούσαστε'},
                    'ter': {'κυβερνιούνταν',
                            'κυβερνιόνταν',
                            'κυβερνιόντουσαν',
                            'κυβερνούνταν'}},
             'sg': {'pri': {'κυβερνούμουν', 'κυβερνιόμουνα', 'κυβερνιόμουν'},
                    'sec': {'κυβερνιόσουν', 'κυβερνιόσουνα', 'κυβερνούσουν'},
                    'ter': {'κυβερνιόταν', 'κυβερνούνταν', 'κυβερνιότανε'}}},
            # ic(parat_pass('πηγάζω'))

        )
    # PARAT2C_PASS
    def test_lupamai(self):
        self.assertDictEqual(
            parat_pass('λυπάμαι'),
            {'pl': {'pri': {'λυπόμαστε', 'λυπόμασταν'},
                    'sec': {'λυπόσαστε', 'λυπόσασταν'},
                    'ter': {'λυπόντουσαν', 'λυπούνταν', 'λυπόνταν'}},
             'sg': {'pri': {'λυπόμουνα', 'λυπόμουν'},
                    'sec': {'λυπόσουνα', 'λυπόσουν'},
                    'ter': {'λυπόταν', 'λυπότανε'}}},

        )
    # PARAT2D_PASS
    def test_epitithemai(self):
        self.assertDictEqual(
            parat_pass('επιτίθεμαι'),
            {'pl': {'pri': {'επιτιθέμαστε', 'επιτιθέμασταν', 'επιτιθέμεθα'},
                    'sec': {'επιτίθεσθε', 'επιτίθεστε'},
                    'ter': {'επιτίθεντο'}},
             'sg': {'pri': {'επιτιθέμην'},
                    'sec': {'επιτίθεσο'},
                    'ter': {'επιτίθετο', 'επετίθετο'}}}

        )
    # PARAT2E_PASS

    def test_kathistamai(self):
        self.assertDictEqual(
            parat_pass('καθίσταμαι'),
            {'pl': {'pri': {'καθιστόμασταν', 'καθιστάμεθα', 'καθιστόμαστε'},
                    'sec': {'καθίσταστε', 'καθίστασθε'},
                    'ter': {'καθίσταντο'}},
             'sg': {'pri': {'καθιστάμην'}, 'sec': {'καθίστασο'}, 'ter': {'καθίστατο'}}}

        )








