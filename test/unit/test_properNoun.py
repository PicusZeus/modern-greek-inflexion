from unittest import TestCase

# from icecream import ic

from modern_greek_inflexion.resources.resources import MASC, SURNAME, FEM, FEM_SG, greek_corpus
from modern_greek_inflexion import noun


class ProperNounTests(TestCase):
    def test_Nikos(self):
        self.assertDictEqual(
            noun.create_all('Νίκος', proper_name=True),
            {'masc': {'pl': {'nom': {'Νίκοι'}, 'acc': {'Νίκους'}, 'voc': {'Νίκοι'}, 'gen': {'Νίκων'}},
                      'sg': {'gen': {'Νίκου'}, 'nom': {'Νίκος'}, 'acc': {'Νίκο'}, 'voc': {'Νίκο'}}}},
        )

    def test_Axilleus(self):
        self.assertDictEqual(
            noun.create_all('Αχιλλεύς', proper_name=True),
            {'masc': {'pl': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                      'sg': {'acc': {'Αχιλλέα'},
                             'gen': {'Αχιλλέως'},
                             'nom': {'Αχιλλεύς'},
                             'voc': {'Αχιλλεύ'}}}},

        )

    def test_Leas(self):
        self.assertDictEqual(noun.create_all('Λέας', proper_name=True),
                             {'masc': {'pl': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                                       'sg': {'acc': {'Λέα'},
                                              'gen': {'Λέα'},
                                              'nom': {'Λέας'},
                                              'voc': {'Λέα'}}}}
                             )

    def test_Gnwmwn(self):
        self.assertDictEqual(
            noun.create_all('Γνώμων', proper_name=True),
            {'masc': {'pl': {'acc': {'Γνώμονες'},
                             'gen': {'Γνωμόνων'},
                             'nom': {'Γνώμονες'},
                             'voc': {'Γνώμονες'}},
                      'sg': {'acc': {'Γνώμονα'},
                             'gen': {'Γνώμονος'},
                             'nom': {'Γνώμων'},
                             'voc': {'Γνώμων'}}}}

        )

    def test_Yios(self):
        self.assertDictEqual(

            noun.create_all('Υιός', proper_name=True),
            {'masc': {'pl': {'acc': {'Υιούς'},
                             'gen': {'Υιών'},
                             'nom': {'Υιοί'},
                             'voc': {'Υιοί'}},
                      'sg': {'acc': {'Υιό'},
                             'gen': {'Υιού'},
                             'nom': {'Υιός'},
                             'voc': {'Υιέ'}}}}
        )

    def test_Thetis(self):
        self.assertDictEqual(
            noun.create_all('Θέτις', proper_name=True),
            {'fem': {'pl': {'acc': {'Θέτιδες'},
                            'gen': {'Θετίδων'},
                            'nom': {'Θέτιδες'},
                            'voc': {'Θέτιδες'}},
                     'sg': {'acc': {'Θέτιδα'},
                            'gen': {'Θέτιδος'},
                            'nom': {'Θέτις'},
                            'voc': {'Θέτι'}}}},
        )

    def test_Polonos(self):
        self.assertDictEqual(
            noun.create_all('Πολωνός', proper_name=True),
            {'masc': {'pl': {'acc': {'Πολωνούς'},
                             'gen': {'Πολωνών'},
                             'nom': {'Πολωνοί'},
                             'voc': {'Πολωνοί'}},
                      'sg': {'acc': {'Πολωνό'},
                             'gen': {'Πολωνού'},
                             'nom': {'Πολωνός'},
                             'voc': {'Πολωνέ'}}}}

        )

    def test_Paxu(self):
        self.assertDictEqual(
            noun.create_all('Παχύ', proper_name=True, gender=SURNAME),
            {'surname': {'pl': {'gen': {'Παχύ'}, 'acc': {'Παχύ'}, 'nom': {'Παχύ'}, 'voc': {'Παχύ'}},
                         'sg': {'acc': {'Παχύ'}, 'gen': {'Παχύ'}, 'nom': {'Παχύ'}, 'voc': {'Παχύ'}}}},

        )

    def test_Ellas(self):
        self.assertDictEqual(
            noun.create_all('Ελλάς', proper_name=True, gender=FEM),
            {'fem': {'pl': {'acc': {'Ελλάδες'},
                            'gen': {'Ελλάδων'},
                            'nom': {'Ελλάδες'},
                            'voc': {'Ελλάδες'}},
                     'sg': {'acc': {'Ελλάδα'},
                            'gen': {'Ελλάδος'},
                            'nom': {'Ελλάς'},
                            'voc': {'Ελλάς'}}}}

        )

    def test_Papandreou(self):
        self.assertDictEqual(
            noun.create_all('Παπανδρέου', proper_name=True, gender=SURNAME),

            {'surname': {
                'pl': {'gen': {'Παπανδρέου'}, 'acc': {'Παπανδρέου'}, 'nom': {'Παπανδρέου'}, 'voc': {'Παπανδρέου'}},
                'sg': {'acc': {'Παπανδρέου'}, 'gen': {'Παπανδρέου'}, 'nom': {'Παπανδρέου'}, 'voc': {'Παπανδρέου'}}}}
        )

    def test_Dimas(self):
        self.assertDictEqual(
            noun.create_all('Δημάς', proper_name=True, gender=SURNAME),
            {'surname': {'pl': {'acc': {'Δημάδες'}, 'gen': {'Δημάδων'}, 'nom': {'Δημάδες'}, 'voc': {'Δημάδες'}},
                         'sg': {'acc': {'Δημά'}, 'gen': {'Δημά'}, 'nom': {'Δημάς'}, 'voc': {'Δημά'}}}}

        )

    def test_Mykonos(self):
        self.assertDictEqual(
            noun.create_all('Μύκονος', proper_name=True, gender=FEM_SG),
            {'fem': {'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}},
                     'sg': {'nom': {'Μύκονος'}, 'gen': {'Μυκόνου'}, 'acc': {'Μύκονο'}, 'voc': {'Μύκονε'}}}}
        )

    def test_Bandaloi(self):
        self.assertDictEqual(
            noun.create_all('Βάνδαλοι', proper_name=True),
            {'masc': {'pl': {'nom': {'Βάνδαλοι'}, 'gen': {'Βανδάλων'}, 'voc': {'Βάνδαλοι'}, 'acc': {'Βάνδαλους'}},
                      'sg': {'nom': {''}, 'gen': {''}, 'voc': {''}, 'acc': {''}}}}
        )

    def test_Ghs(self):
        self.assertDictEqual(
            noun.create_all('Γης', proper_name=True),
            {'fem': {'pl': {'nom': {'Γαίες'}, 'gen': {'Γαίων'}, 'voc': {'Γαίες'}, 'acc': {'Γαίες'}},
                     'sg': {'nom': {'Γης'}, 'gen': {'Γης'}, 'voc': {'Γη'}, 'acc': {'Γη'}}}}
        )

    def test_Athhnai(self):
        self.assertDictEqual(
            noun.create_all('Αθήναι', proper_name=True),
            {'fem': {'pl': {'acc': {'Αθήναι'},
                            'gen': {'Αθηνών'},
                            'nom': {'Αθήναι'},
                            'voc': {'Αθήναι'}},
                     'sg': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}}}},
        )

    def test_Simwn(self):
        self.assertDictEqual(
            noun.create_all('Σίμων'),
            {'masc': {'pl': {'acc': {'Σίμωνες'},
                             'gen': {'Σιμώνων'},
                             'nom': {'Σίμωνες'},
                             'voc': {'Σίμωνες'}},
                      'sg': {'acc': {'Σίμωνα'},
                             'gen': {'Σίμωνος'},
                             'nom': {'Σίμων'},
                             'voc': {'Σίμων'}}}}

        )

    def test_Baios(self):
        self.assertDictEqual(
            noun.create_all('Βάιος', proper_name=True),
            {'masc': {'pl': {'acc': {'Βάιους'},
                             'gen': {'Βάιων'},
                             'nom': {'Βάιοι'},
                             'voc': {'Βάιοι'}},
                      'sg': {'acc': {'Βάιον', 'Βάιο'},
                             'gen': {'Βάιου'},
                             'nom': {'Βάιος'},
                             'voc': {'Βάιε', 'Βάιο'}}}}

        )

    def test_Ihsous(self):
        self.assertDictEqual(
            noun.create_all('Ιησούς', proper_name=True, gender=MASC),
            {'masc': {'sg': {'voc': {'Ιησού'}, 'gen': {'Ιησού'}, 'nom': {'Ιησούς'}, 'acc': {'Ιησού'}},
                      'pl': {'voc': {''}, 'gen': {''}, 'nom': {''}, 'acc': {''}}}}
        )

    def test_Filippos(self):
        self.assertDictEqual(
            noun.create_all('Φίλιππος', proper_name=True),
            {'masc': {
                'sg': {'nom': {'Φίλιππος'}, 'acc': {'Φίλιππο'}, 'voc': {'Φίλιππε'}, 'gen': {'Φιλίππου', 'Φίλιππου'}},
                'pl': {'nom': {'Φίλιπποι'}, 'acc': {'Φιλίππους'}, 'voc': {'Φίλιπποι'},
                       'gen': {'Φιλίππων'}}}}
        )

    def test_Froso(self):
        self.assertDictEqual(
            noun.create_all('Φρόσω', gender=FEM_SG, proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'nom': {'Φρόσω'}, 'voc': {'Φρόσω'}, 'gen': {'Φρόσως'}, 'acc': {'Φρόσω'}}}}
        )

    def test_Barsobia(self):
        self.assertDictEqual(
            noun.create_all('Βαρσοβία', proper_name=True, gender=FEM_SG),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'gen': {''}, 'voc': {''}},
                     'sg': {'acc': {'Βαρσοβία'}, 'nom': {'Βαρσοβία'}, 'gen': {'Βαρσοβίας'}, 'voc': {'Βαρσοβία'}}}}
        )

    def test_Polonos(self):
        self.assertDictEqual(
            noun.create_all('Πολωνός', gender=MASC),
            {'masc': {'sg': {'gen': {'Πολωνού'},
                             'nom': {'Πολωνός'},
                             'voc': {'Πολωνέ'},
                             'acc': {'Πολωνό'}},
                      'pl': {'gen': {'Πολωνών'},
                             'nom': {'Πολωνοί'},
                             'voc': {'Πολωνοί'},
                             'acc': {'Πολωνούς'}}}}
        )

    def test_Alexandrou(self):
        self.assertDictEqual(
            noun.create_all('Αλεξαντρού', proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'acc': {'Αλεξαντρού'}, 'gen': {'Αλεξαντρούς'},
                            'nom': {'Αλεξαντρού'}, 'voc': {'Αλεξαντρού'}}}}
        )

    def test_Angelos(self):
        self.assertDictEqual(
            noun.create_all('Άγγελος', proper_name=True),
            {'masc': {'pl': {'acc': {'Άγγελους'},
                             'gen': {'Άγγελων'},
                             'nom': {'Άγγελοι'},
                             'voc': {'Άγγελοι'}},
                      'sg': {'acc': {'Άγγελο'},
                             'gen': {'Άγγελου'},
                             'nom': {'Άγγελος'},
                             'voc': {'Άγγελε'}}}}
        )
