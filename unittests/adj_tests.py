from unittest import TestCase, main

from modern_greek_inflexion.adjective import adjective


r = adjective.create_all('βιλλαράς')
print(r)

class AdjectiveTests(TestCase):

    def test_adj_oraios(self):
        self.assertEqual(
            adjective.create_all('ωραίος'),
            {'adj': {'pl': {'fem': {'gen': {'ωραίων'}, 'acc': {'ωραίες'}, 'voc': {'ωραίες'}, 'nom': {'ωραίες'}},
                            'masc': {'gen': {'ωραίων'}, 'acc': {'ωραίους'}, 'voc': {'ωραίοι'}, 'nom': {'ωραίοι'}},
                            'neut': {'gen': {'ωραίων'}, 'acc': {'ωραία'}, 'voc': {'ωραία'}, 'nom': {'ωραία'}}},
                     'sg': {'fem': {'gen': {'ωραίας'}, 'acc': {'ωραία'}, 'voc': {'ωραία'}, 'nom': {'ωραία'}},
                            'masc': {'gen': {'ωραίου'}, 'acc': {'ωραίο'}, 'voc': {'ωραίε'}, 'nom': {'ωραίος'}},
                            'neut': {'gen': {'ωραίου'}, 'acc': {'ωραίο'}, 'voc': {'ωραίο'}, 'nom': {'ωραίο'}}}},
             'comp': {'pl': {
                 'fem': {'gen': {'ωραιότερων'}, 'acc': {'ωραιότερες'}, 'voc': {'ωραιότερες'}, 'nom': {'ωραιότερες'}},
                 'masc': {'gen': {'ωραιότερων'}, 'acc': {'ωραιότερους'}, 'voc': {'ωραιότεροι'}, 'nom': {'ωραιότεροι'}},
                 'neut': {'gen': {'ωραιότερων'}, 'acc': {'ωραιότερα'}, 'voc': {'ωραιότερα'}, 'nom': {'ωραιότερα'}}},
                      'sg': {'fem': {'gen': {'ωραιότερης'}, 'acc': {'ωραιότερη'}, 'voc': {'ωραιότερη'},
                                     'nom': {'ωραιότερη'}},
                             'masc': {'gen': {'ωραιότερου'}, 'acc': {'ωραιότερο'}, 'voc': {'ωραιότερε'},
                                      'nom': {'ωραιότερος'}},
                             'neut': {'gen': {'ωραιότερου'}, 'acc': {'ωραιότερο'}, 'voc': {'ωραιότερο'},
                                      'nom': {'ωραιότερο'}}}},
             'superl': {'pl': {
                'fem': {'gen': {'ωραιότατων'}, 'acc': {'ωραιότατες'}, 'voc': {'ωραιότατες'}, 'nom': {'ωραιότατες'}},
                'masc': {'gen': {'ωραιότατων'}, 'acc': {'ωραιότατους'}, 'voc': {'ωραιότατοι'}, 'nom': {'ωραιότατοι'}},
                'neut': {'gen': {'ωραιότατων'}, 'acc': {'ωραιότατα'}, 'voc': {'ωραιότατα'}, 'nom': {'ωραιότατα'}}},
                                                                          'sg': {'fem': {'gen': {'ωραιότατης'},
                                                                                         'acc': {'ωραιότατη'},
                                                                                         'voc': {'ωραιότατη'},
                                                                                         'nom': {'ωραιότατη'}},
                                                                                 'masc': {'gen': {'ωραιότατου'},
                                                                                          'acc': {'ωραιότατο'},
                                                                                          'voc': {'ωραιότατε'},
                                                                                          'nom': {'ωραιότατος'}},
                                                                                 'neut': {'gen': {'ωραιότατου'},
                                                                                          'acc': {'ωραιότατο'},
                                                                                          'voc': {'ωραιότατο'},
                                                                                          'nom': {'ωραιότατο'}}}},
             'adv': {'ωραία'},
             'comp_adv': {'ωραιότερα'},
             'superl_adv': {'ωραιότατα'}}

        )


    def test_adj_porfyroxrous(self):
        self.assertEqual(
            adjective.create_all('πορφυρόχρους'),
            {'adj': {'pl': {'fem': {'acc': {'πορφυρόχρους'}, 'gen': {'πορφυρόχρων'}, 'nom': {'πορφυρόχροι'},
                                    'voc': {'πορφυρόχροι'}},
                            'masc': {'acc': {'πορφυρόχρους'}, 'gen': {'πορφυρόχρων'}, 'nom': {'πορφυρόχροι'},
                                     'voc': {'πορφυρόχροι'}},
                            'neut': {'acc': {'πορφυρόχροα'}, 'gen': {'πορφυρόχρων'}, 'nom': {'πορφυρόχροα'},
                                     'voc': {'πορφυρόχροα'}}}, 'sg': {
                'fem': {'acc': {'πορφυρόχρου'}, 'gen': {'πορφυρόχρουν'}, 'nom': {'πορφυρόχρους'},
                        'voc': {'πορφυρόχρους'}},
                'masc': {'acc': {'πορφυρόχρου'}, 'gen': {'πορφυρόχρουν'}, 'nom': {'πορφυρόχρους'},
                         'voc': {'πορφυρόχρους'}},
                'neut': {'acc': {'πορφυρόχρουν'}, 'gen': {'πορφυρόχρου'}, 'nom': {'πορφυρόχρουν'},
                         'voc': {'πορφυρόχρουν'}}}}}

        )

    def test_adj_melas(self):
        self.assertEqual(
            adjective.create_all('μέλας'),
            {'adj': {'sg': {'fem': {'voc': {'μέλαν'}, 'gen': {'μέλανος'}, 'acc': {'μέλανα'}, 'nom': {'μέλαινα'}},
                            'masc': {'voc': {'μέλαν'}, 'gen': {'μέλανος'}, 'acc': {'μέλανα'}, 'nom': {'μέλας'}},
                            'neut': {'voc': {'μέλαν'}, 'gen': {'μέλανος'}, 'acc': {'μέλαν'}, 'nom': {'μέλαν'}}},
                     'pl': {'fem': {'voc': {'μέλανες'}, 'gen': {'μελαινών'}, 'acc': {'μέλανες'}, 'nom': {'μέλανες'}},
                            'masc': {'voc': {'μέλανες'}, 'gen': {'μελάνων'}, 'acc': {'μέλανες'}, 'nom': {'μέλανες'}},
                            'neut': {'voc': {'μέλανα'}, 'gen': {'μελάνων'}, 'acc': {'μέλανα'}, 'nom': {'μέλανα'}}}}}

        )

    def test_adj_rodis(self):
        self.assertEqual(
            adjective.create_all('ροδής'),
            {'adj': {'sg': {'fem': {'nom': {'ροδιά'}, 'voc': {'ροδιά'}, 'gen': {'ροδιάς'}, 'acc': {'ροδιά'}},
                            'masc': {'nom': {'ροδής'}, 'voc': {'ροδή'}, 'gen': {'ροδή'}, 'acc': {'ροδή'}},
                            'neut': {'nom': {'ροδί'}, 'voc': {'ροδί'}, 'gen': {'ροδιού'}, 'acc': {'ροδί'}}},
                     'pl': {'fem': {'nom': {'ροδιές'}, 'voc': {'ροδιές'}, 'gen': {'ροδιών'}, 'acc': {'ροδιές'}},
                            'masc': {'nom': {'ροδιοί'}, 'voc': {'ροδιοί'}, 'gen': {'ροδιών'}, 'acc': {'ροδιούς'}},
                            'neut': {'nom': {'ροδιά'}, 'voc': {'ροδιά'}, 'gen': {'ροδιών'}, 'acc': {'ροδιά'}}}},
             'adv': {'ροδιά'}}

        )

    def test_adj_akamatis(self):
        # self.maxDiff = None
        self.assertEqual(
            adjective.create_all('ακαμάτης'),
            {'adj': {'pl': {
                'fem': {'gen': {'ακαμάτισων'}, 'nom': {'ακαμάτισσες'}, 'voc': {'ακαμάτισσες'}, 'acc': {'ακαμάτισσες'}},
                'neut': {'gen': {'ακαμάτικων'}, 'nom': {'ακαμάτικα'}, 'voc': {'ακαμάτικα'}, 'acc': {'ακαμάτικα'}},
                'masc': {'gen': {'ακαμάτηδων'}, 'nom': {'ακαμάτηδες'}, 'voc': {'ακαμάτηδες'}, 'acc': {'ακαμάτηδες'}}},
                     'sg': {'fem': {'gen': {'ακαμάτισσας'}, 'nom': {'ακαμάτισσα'}, 'voc': {'ακαμάτισσα'},
                                    'acc': {'ακαμάτισσα'}},
                            'neut': {'gen': {'ακαμάτικου'}, 'nom': {'ακαμάτικο'}, 'voc': {'ακαμάτικο'},
                                     'acc': {'ακαμάτικο'}},
                            'masc': {'gen': {'ακαμάτη'}, 'nom': {'ακαμάτης'}, 'voc': {'ακαμάτη'}, 'acc': {'ακαμάτη'}}}}}

        )

    def test_adj_argos(self):
        self.assertEqual(
            adjective.create_all('αργός'),
            {'adj': {'pl': {'fem': {'gen': {'αργών'}, 'nom': {'αργές'}, 'acc': {'αργές'}, 'voc': {'αργές'}},
                            'masc': {'gen': {'αργών'}, 'nom': {'αργοί'}, 'acc': {'αργούς'}, 'voc': {'αργοί'}},
                            'neut': {'gen': {'αργών'}, 'nom': {'αργά'}, 'acc': {'αργά'}, 'voc': {'αργά'}}},
                     'sg': {'fem': {'gen': {'αργής'}, 'nom': {'αργή'}, 'acc': {'αργή'}, 'voc': {'αργή'}},
                            'masc': {'gen': {'αργού'}, 'nom': {'αργός'}, 'acc': {'αργό'}, 'voc': {'αργέ'}},
                            'neut': {'gen': {'αργού'}, 'nom': {'αργό'}, 'acc': {'αργό'}, 'voc': {'αργό'}}}}, 'comp': {
                'pl': {'fem': {'gen': {'αργότερων'}, 'nom': {'αργότερες'}, 'acc': {'αργότερες'}, 'voc': {'αργότερες'}},
                       'masc': {'gen': {'αργότερων'}, 'nom': {'αργότεροι'}, 'acc': {'αργότερους'},
                                'voc': {'αργότεροι'}},
                       'neut': {'gen': {'αργότερων'}, 'nom': {'αργότερα'}, 'acc': {'αργότερα'}, 'voc': {'αργότερα'}}},
                'sg': {'fem': {'gen': {'αργότερης'}, 'nom': {'αργότερη'}, 'acc': {'αργότερη'}, 'voc': {'αργότερη'}},
                       'masc': {'gen': {'αργότερου'}, 'nom': {'αργότερος'}, 'acc': {'αργότερο'}, 'voc': {'αργότερε'}},
                       'neut': {'gen': {'αργότερου'}, 'nom': {'αργότερο'}, 'acc': {'αργότερο'}, 'voc': {'αργότερο'}}}},
             'adv': {'αργά'}, 'comp_adv': {'αργότερα'}}

        )

    def test_adj_kalos(self):
        self.assertEqual(
            adjective.create_all('καλός'),
            {'adj': {'pl': {'neut': {'nom': {'καλά'}, 'voc': {'καλά'}, 'acc': {'καλά'}, 'gen': {'καλών'}},
                            'masc': {'nom': {'καλοί'}, 'voc': {'καλοί'}, 'acc': {'καλούς'}, 'gen': {'καλών'}},
                            'fem': {'nom': {'καλές'}, 'voc': {'καλές'}, 'acc': {'καλές'}, 'gen': {'καλών'}}},
                     'sg': {'neut': {'nom': {'καλό'}, 'voc': {'καλό'}, 'acc': {'καλό'}, 'gen': {'καλού'}},
                            'masc': {'nom': {'καλός'}, 'voc': {'καλέ'}, 'acc': {'καλό'}, 'gen': {'καλού'}},
                            'fem': {'nom': {'καλή'}, 'voc': {'καλή'}, 'acc': {'καλή'}, 'gen': {'καλής'}}}}, 'comp': {
                'pl': {'neut': {'nom': {'καλύτερα'}, 'voc': {'καλύτερα'}, 'acc': {'καλύτερα'}, 'gen': {'καλύτερων'}},
                       'masc': {'nom': {'καλύτεροι'}, 'voc': {'καλύτεροι'}, 'acc': {'καλύτερους'},
                                'gen': {'καλύτερων'}},
                       'fem': {'nom': {'καλύτερες'}, 'voc': {'καλύτερες'}, 'acc': {'καλύτερες'}, 'gen': {'καλύτερων'}}},
                'sg': {'neut': {'nom': {'καλύτερο'}, 'voc': {'καλύτερο'}, 'acc': {'καλύτερο'}, 'gen': {'καλύτερου'}},
                       'masc': {'nom': {'καλύτερος'}, 'voc': {'καλύτερε'}, 'acc': {'καλύτερο'}, 'gen': {'καλύτερου'}},
                       'fem': {'nom': {'καλύτερη'}, 'voc': {'καλύτερη'}, 'acc': {'καλύτερη'}, 'gen': {'καλύτερης'}}}},
             'superl': {'pl': {'neut': {'nom': {'άριστα'}, 'voc': {'άριστα'}, 'acc': {'άριστα'}, 'gen': {'άριστων'}},
                               'masc': {'nom': {'άριστοι'}, 'voc': {'άριστοι'}, 'acc': {'άριστους'},
                                        'gen': {'άριστων'}},
                               'fem': {'nom': {'άριστες'}, 'voc': {'άριστες'}, 'acc': {'άριστες'}, 'gen': {'άριστων'}}},
                        'sg': {'neut': {'nom': {'άριστο'}, 'voc': {'άριστο'}, 'acc': {'άριστο'}, 'gen': {'άριστου'}},
                               'masc': {'nom': {'άριστος'}, 'voc': {'άριστε'}, 'acc': {'άριστο'}, 'gen': {'άριστου'}},
                               'fem': {'nom': {'άριστη'}, 'voc': {'άριστη'}, 'acc': {'άριστη'}, 'gen': {'άριστης'}}}},
             'adv': {'καλώς', 'καλά'}, 'comp_adv': {'καλύτερα', 'κάλλιον', 'κάλλιο'}, 'superl_adv': {'άριστα'}}

        )
    def test_adj_portokalis(self):
        self.assertEqual(
            adjective.create_all('πορτοκαλής'),
            {'adj': {'sg': {
                'neut': {'gen': {'πορτοκαλιού'}, 'voc': {'πορτοκαλί'}, 'nom': {'πορτοκαλί'}, 'acc': {'πορτοκαλί'}},
                'masc': {'gen': {'πορτοκαλή'}, 'voc': {'πορτοκαλή'}, 'nom': {'πορτοκαλής'}, 'acc': {'πορτοκαλή'}},
                'fem': {'gen': {'πορτοκαλιάς'}, 'voc': {'πορτοκαλιά'}, 'nom': {'πορτοκαλιά'}, 'acc': {'πορτοκαλιά'}}},
                     'pl': {'neut': {'gen': {'πορτοκαλιών'}, 'voc': {'πορτοκαλιά'}, 'nom': {'πορτοκαλιά'},
                                     'acc': {'πορτοκαλιά'}},
                            'masc': {'gen': {'πορτοκαλιών'}, 'voc': {'πορτοκαλιοί'}, 'nom': {'πορτοκαλιοί'},
                                     'acc': {'πορτοκαλιούς'}},
                            'fem': {'gen': {'πορτοκαλιών'}, 'voc': {'πορτοκαλιές'}, 'nom': {'πορτοκαλιές'},
                                    'acc': {'πορτοκαλιές'}}}}, 'adv': {'πορτοκαλιά'}}

        )

    def test_adj_roz(self):
        self.assertEqual(
            adjective.create_all('ροζ'),
            {'adj': {'sg': {'masc': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}},
                            'neut': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}},
                            'fem': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}}},
                     'pl': {'masc': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}},
                            'neut': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}},
                            'fem': {'nom': {'ροζ'}, 'voc': {'ροζ'}, 'acc': {'ροζ'}, 'gen': {'ροζ'}}}}, 'adv': {'ροζ'}}

        )

    def test_adj_safis(self):
        self.maxDiff = None
        self.assertEqual(
            adjective.create_all('σαφής'),
            {'adj': {'pl': {'fem': {'acc': {'σαφείς'}, 'gen': {'σαφών'}, 'nom': {'σαφείς'}, 'voc': {'σαφείς'}},
                            'neut': {'acc': {'σαφή'}, 'gen': {'σαφών'}, 'nom': {'σαφή'}, 'voc': {'σαφή'}},
                            'masc': {'acc': {'σαφείς'}, 'gen': {'σαφών'}, 'nom': {'σαφείς'}, 'voc': {'σαφείς'}}},
                     'sg': {'fem': {'acc': {'σαφή'}, 'gen': {'σαφούς'}, 'nom': {'σαφής'}, 'voc': {'σαφής'}},
                            'neut': {'acc': {'σαφές'}, 'gen': {'σαφούς'}, 'nom': {'σαφές'}, 'voc': {'σαφές'}},
                            'masc': {'acc': {'σαφή'}, 'gen': {'σαφούς'}, 'nom': {'σαφής'}, 'voc': {'σαφή'}}}}, 'comp': {
                'pl': {
                    'fem': {'acc': {'σαφέστερες'}, 'gen': {'σαφέστερων'}, 'nom': {'σαφέστερες'}, 'voc': {'σαφέστερες'}},
                    'neut': {'acc': {'σαφέστερα'}, 'gen': {'σαφέστερων'}, 'nom': {'σαφέστερα'}, 'voc': {'σαφέστερα'}},
                    'masc': {'acc': {'σαφέστερους'}, 'gen': {'σαφέστερων'}, 'nom': {'σαφέστεροι'},
                             'voc': {'σαφέστεροι'}}},
                'sg': {'fem': {'acc': {'σαφέστερη'}, 'gen': {'σαφέστερης'}, 'nom': {'σαφέστερη'}, 'voc': {'σαφέστερη'}},
                       'neut': {'acc': {'σαφέστερο'}, 'gen': {'σαφέστερου'}, 'nom': {'σαφέστερο'},
                                'voc': {'σαφέστερο'}},
                       'masc': {'acc': {'σαφέστερο'}, 'gen': {'σαφέστερου'}, 'nom': {'σαφέστερος'},
                                'voc': {'σαφέστερε'}}}}, 'superl': {'pl': {
                'fem': {'acc': {'σαφέστατες'}, 'gen': {'σαφέστατων'}, 'nom': {'σαφέστατες'}, 'voc': {'σαφέστατες'}},
                'neut': {'acc': {'σαφέστατα'}, 'gen': {'σαφέστατων'}, 'nom': {'σαφέστατα'}, 'voc': {'σαφέστατα'}},
                'masc': {'acc': {'σαφέστατους'}, 'gen': {'σαφέστατων'}, 'nom': {'σαφέστατοι'}, 'voc': {'σαφέστατοι'}}},
                                                                    'sg': {'fem': {'acc': {'σαφέστατη'},
                                                                                   'gen': {'σαφέστατης'},
                                                                                   'nom': {'σαφέστατη'},
                                                                                   'voc': {'σαφέστατη'}},
                                                                           'neut': {'acc': {'σαφέστατο'},
                                                                                    'gen': {'σαφέστατου'},
                                                                                    'nom': {'σαφέστατο'},
                                                                                    'voc': {'σαφέστατο'}},
                                                                           'masc': {'acc': {'σαφέστατο'},
                                                                                    'gen': {'σαφέστατου'},
                                                                                    'nom': {'σαφέστατος'},
                                                                                    'voc': {'σαφέστατε'}}}},
             'adv': {'σαφώς'}, 'comp_adv': {'σαφέστερα'}, 'superl_adv': {'σαφέστατα'}}

        )

    def test_adj_tempelis(self):
        self.assertEqual(
            adjective.create_all('τεμπέλης'),
            {'adj': {'pl': {
                'masc': {'gen': {'τεμπέληδων'}, 'nom': {'τεμπέληδες'}, 'acc': {'τεμπέληδες'}, 'voc': {'τεμπέληδες'}},
                'neut': {'gen': {'τεμπέλικων'}, 'nom': {'τεμπέλικα'}, 'acc': {'τεμπέλικα'}, 'voc': {'τεμπέλικα'}},
                'fem': {'gen': {'τεμπέων'}, 'nom': {'τεμπέλες'}, 'acc': {'τεμπέλες'}, 'voc': {'τεμπέλες'}}},
                     'sg': {'masc': {'gen': {'τεμπέλη'}, 'nom': {'τεμπέλης'}, 'acc': {'τεμπέλη'}, 'voc': {'τεμπέλη'}},
                            'neut': {'gen': {'τεμπέλικου'}, 'nom': {'τεμπέλικο'}, 'acc': {'τεμπέλικο'},
                                     'voc': {'τεμπέλικο'}},
                            'fem': {'gen': {'τεμπέλας'}, 'nom': {'τεμπέλα'}, 'acc': {'τεμπέλα'}, 'voc': {'τεμπέλα'}}}},
             'adv': {'τεμπέλικα'}}

        )

    def test_adj_baris(self):
        self.assertEqual(
            adjective.create_all('βαρύς'),
            {'adj': {
                'sg': {'neut': {'voc': {'βαρύ'}, 'nom': {'βαρύ'}, 'acc': {'βαρύ'}, 'gen': {'βαρέος', 'βαριού', 'βαρύ'}},
                       'fem': {'voc': {'βαρεία', 'βαριά'}, 'nom': {'βαρεία', 'βαριά'},
                               'acc': {'βαρεία', 'βαριά', 'βαρείαν'}, 'gen': {'βαριάς', 'βαρείας'}},
                       'masc': {'voc': {'βαρύ'}, 'nom': {'βαρύς'}, 'acc': {'βαρύ'},
                                'gen': {'βαρέος', 'βαριού', 'βαρύ'}}}, 'pl': {
                    'neut': {'voc': {'βαριά', 'βαρέα'}, 'nom': {'βαριά', 'βαρέα'}, 'acc': {'βαριά', 'βαρέα'},
                             'gen': {'βαριών', 'βαρέων'}},
                    'fem': {'voc': {'βαριές', 'βαρείες'}, 'nom': {'βαριές', 'βαρείες'}, 'acc': {'βαριές', 'βαρείες'},
                            'gen': {'βαριών', 'βαρειών'}},
                    'masc': {'voc': {'βαρείς', 'βαριόι'}, 'nom': {'βαρείς', 'βαριόι'}, 'acc': {'βαρείς', 'βαριούς'},
                             'gen': {'βαριών', 'βαρέων'}}}}, 'comp': {
                'sg': {'neut': {'voc': {'βαρύτερο'}, 'nom': {'βαρύτερο'}, 'acc': {'βαρύτερο'}, 'gen': {'βαρύτερου'}},
                       'fem': {'voc': {'βαρύτερη'}, 'nom': {'βαρύτερη'}, 'acc': {'βαρύτερη'}, 'gen': {'βαρύτερης'}},
                       'masc': {'voc': {'βαρύτερε'}, 'nom': {'βαρύτερος'}, 'acc': {'βαρύτερο'}, 'gen': {'βαρύτερου'}}},
                'pl': {'neut': {'voc': {'βαρύτερα'}, 'nom': {'βαρύτερα'}, 'acc': {'βαρύτερα'}, 'gen': {'βαρύτερων'}},
                       'fem': {'voc': {'βαρύτερες'}, 'nom': {'βαρύτερες'}, 'acc': {'βαρύτερες'}, 'gen': {'βαρύτερων'}},
                       'masc': {'voc': {'βαρύτεροι'}, 'nom': {'βαρύτεροι'}, 'acc': {'βαρύτερους'},
                                'gen': {'βαρύτερων'}}}}, 'superl': {
                'sg': {'neut': {'voc': {'βαρύτατο'}, 'nom': {'βαρύτατο'}, 'acc': {'βαρύτατο'}, 'gen': {'βαρύτατου'}},
                       'fem': {'voc': {'βαρύτατη'}, 'nom': {'βαρύτατη'}, 'acc': {'βαρύτατη'}, 'gen': {'βαρύτατης'}},
                       'masc': {'voc': {'βαρύτατε'}, 'nom': {'βαρύτατος'}, 'acc': {'βαρύτατο'}, 'gen': {'βαρύτατου'}}},
                'pl': {'neut': {'voc': {'βαρύτατα'}, 'nom': {'βαρύτατα'}, 'acc': {'βαρύτατα'}, 'gen': {'βαρύτατων'}},
                       'fem': {'voc': {'βαρύτατες'}, 'nom': {'βαρύτατες'}, 'acc': {'βαρύτατες'}, 'gen': {'βαρύτατων'}},
                       'masc': {'voc': {'βαρύτατοι'}, 'nom': {'βαρύτατοι'}, 'acc': {'βαρύτατους'},
                                'gen': {'βαρύτατων'}}}}, 'adv': {'βαρέως'}, 'comp_adv': {'βαρύτερα'},
             'superl_adv': {'βαρύτατα'}}

        )

    def test_adj_kakos(self):
        self.assertEqual(
            adjective.create_all('κακός'),
            {'adj': {'sg': {'masc': {'acc': {'κακό'}, 'gen': {'κακού'}, 'voc': {'κακέ'}, 'nom': {'κακός'}},
                            'fem': {'acc': {'κακή', 'κακιά'}, 'nom': {'κακή', 'κακιά'}, 'voc': {'κακή', 'κακιά'},
                                    'gen': {'κακής', 'κακιάς'}},
                            'neut': {'acc': {'κακό'}, 'gen': {'κακού'}, 'voc': {'κακό'}, 'nom': {'κακό'}}},
                     'pl': {'neut': {'acc': {'κακά'}, 'gen': {'κακών'}, 'voc': {'κακά'}, 'nom': {'κακά'}},
                            'fem': {'acc': {'κακές'}, 'gen': {'κακών'}, 'voc': {'κακές'}, 'nom': {'κακές'}},
                            'masc': {'acc': {'κακούς'}, 'gen': {'κακών'}, 'voc': {'κακοί'}, 'nom': {'κακοί'}}}},
             'comp': {'sg': {
                 'neut': {'acc': {'χειρότερο', 'ήσσον'}, 'nom': {'χειρότερο', 'ήσσον'}, 'voc': {'χειρότερο', 'ήσσον'},
                          'gen': {'ήσσονος', 'χειρότερου'}},
                 'fem': {'acc': {'ήσσονα', 'χειρότερη'}, 'nom': {'χειρότερη', 'ήσσων'}, 'voc': {'χειρότερη', 'ήσσων'},
                         'gen': {'ήσσονος', 'χειρότερης'}},
                 'masc': {'acc': {'ήσσονα', 'χειρότερο'}, 'nom': {'χειρότερος', 'ήσσων'}, 'voc': {'ήσσων', 'χειρότερε'},
                          'gen': {'ήσσονα', 'ήσσονος', 'χειρότερου'}}}, 'pl': {
                 'neut': {'acc': {'ήσσονα', 'χειρότερα'}, 'nom': {'ήσσονα', 'χειρότερα'},
                          'voc': {'ήσσονα', 'χειρότερα'}, 'gen': {'χειρότερων', 'ησσόνων'}},
                 'fem': {'acc': {'χειρότερες', 'ήσσονες'}, 'nom': {'χειρότερες', 'ήσσονες'},
                         'voc': {'χειρότερες', 'ήσσονες'}, 'gen': {'χειρότερων', 'ησσονών'}},
                 'masc': {'acc': {'χειρότερους', 'ήσσονες'}, 'nom': {'χειρότεροι', 'ήσσονες'},
                          'voc': {'χειρότεροι', 'ήσσονες'}, 'gen': {'χειρότερων', 'ησσόνων'}}}}, 'superl': {'sg': {
                'masc': {'acc': {'χείριστο', 'ήκιστο'}, 'nom': {'χείριστος', 'ήκιστος'}, 'voc': {'ήκιστε', 'χείριστε'},
                         'gen': {'ήκιστου', 'χείριστου'}},
                'fem': {'acc': {'χείριστη', 'ήκιστη'}, 'nom': {'χείριστη', 'ήκιστη'}, 'voc': {'χείριστη', 'ήκιστη'},
                        'gen': {'χείριστης', 'ήκιστης'}},
                'neut': {'acc': {'χείριστο', 'ήκιστο'}, 'nom': {'χείριστο', 'ήκιστο'}, 'voc': {'χείριστο', 'ήκιστο'},
                         'gen': {'ήκιστου', 'χείριστου'}}}, 'pl': {
                'masc': {'acc': {'ήκιστους', 'χείριστους'}, 'nom': {'χείριστοι', 'ήκιστοι'},
                         'voc': {'χείριστοι', 'ήκιστοι'}, 'gen': {'χείριστων', 'ήκιστων'}},
                'fem': {'acc': {'χείριστες', 'ήκιστες'}, 'nom': {'χείριστες', 'ήκιστες'},
                        'voc': {'χείριστες', 'ήκιστες'}, 'gen': {'χείριστων', 'ήκιστων'}},
                'neut': {'acc': {'ήκιστα', 'χείριστα'}, 'nom': {'ήκιστα', 'χείριστα'}, 'voc': {'ήκιστα', 'χείριστα'},
                         'gen': {'χείριστων', 'ήκιστων'}}}}, 'adv': {'κακώς', 'κακά'},
             'comp_adv': {'ήττον', 'ήσσον', 'χειρότερα'}, 'superl_adv': {'κάκιστα', 'ήκιστα'}}

        )
if __name__ == "__main__":

    main()