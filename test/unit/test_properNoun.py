from unittest import TestCase

# from icecream import ic

from modern_greek_inflexion.resources.resources import MASC, SURNAME, FEM, FEM_SG
from modern_greek_inflexion import noun


class ProperNounTests(TestCase):
    def test_Nikos(self):
        self.assertDictEqual(
            noun.create_all('Νίκος', proper_name=True),
            {'masc': {'pl': {'nom': {'Νίκοι'}, 'acc': {'Νίκους'}, 'voc': {'Νίκοι'}, 'gen': {'Νίκων'}},
                      'sg': {'gen': {'Νίκου'}, 'nom': {'Νίκος'}, 'acc': {'Νίκο'}, 'voc': {'Νίκο'}}}},

        )

    def test_Paxu(self):
        self.assertDictEqual(
            noun.create_all('Παχύ', proper_name=True, gender=SURNAME),
            {'surname': {'pl': {'gen': {'Παχύ'}, 'acc': {'Παχύ'}, 'nom': {'Παχύ'}, 'voc': {'Παχύ'}},
             'sg': {'acc': {'Παχύ'}, 'gen': {'Παχύ'}, 'nom': {'Παχύ'}, 'voc': {'Παχύ'}}}}
        )

    def test_Papandreou(self):
        self.assertDictEqual(
            noun.create_all('Παπανδρέου', proper_name=True, gender=SURNAME),


        {'surname': {'pl': {'gen': {'Παπανδρέου'}, 'acc': {'Παπανδρέου'}, 'nom': {'Παπανδρέου'}, 'voc': {'Παπανδρέου'}},
                     'sg': {'acc': {'Παπανδρέου'}, 'gen': {'Παπανδρέου'}, 'nom': {'Παπανδρέου'}, 'voc': {'Παπανδρέου'}}}}
        )

    def test_Dimas(self):
        self.assertDictEqual(
            noun.create_all('Δημάς', proper_name=True, gender=SURNAME),
            {'surname': {'pl': {'acc': {'Δημάδες'},'gen': {'Δημάδων'}, 'nom': {'Δημάδες'},'voc': {'Δημάδες'}},
                         'sg': {'acc': {'Δημά'},'gen': {'Δημά'},'nom': {'Δημάς'}, 'voc': {'Δημά'}}}}

        )
    def test_Mykonos(self):
        self.assertDictEqual(
            noun.create_all('Μύκονος', proper_name=True, gender=FEM_SG),
            {'fem': {'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}},
                     'sg': {'nom': {'Μύκονος'}, 'gen': {'Μύκονου', 'Μυκόνου'}, 'acc': {'Μύκονο'}, 'voc': {'Μύκονε'}}}}
        )

    def test_Bandaloi(self):
        self.assertDictEqual(
            noun.create_all('Βάνδαλοι', proper_name=True),
            {'masc': {'pl': {'nom': {'Βάνδαλοι'}, 'gen': {'Βανδάλων'}, 'voc': {'Βάνδαλοι'}, 'acc': {'Βάνδαλους'}},
                      'sg': {'nom': {''}, 'gen': {''}, 'voc': {''}, 'acc': {''}}}}
        )

    def test_Ghis(self):
        self.assertDictEqual(
            noun.create_all('Γης', proper_name=True),
            {'fem': {'pl': {'nom': {'Γαίες'}, 'gen': {'Γαίων'}, 'voc': {'Γαίες'}, 'acc': {'Γαίες'}},
                     'sg': {'nom': {'Γης'}, 'gen': {'Γης'}, 'voc': {'Γη'}, 'acc': {'Γη'}}}}
        )

    def test_Baios(self):
        self.assertDictEqual(
            noun.create_all('Βάιος', proper_name=True),
            {'masc': {'pl': {'acc': {'Βαΐους', 'Βάιους'},
                             'gen': {'Βάιων', 'Βαΐων'},
                             'nom': {'Βάιοι'},
                             'voc': {'Βάιοι'}},
                      'sg': {'acc': {'Βάιο', 'Βάιον'},
                             'gen': {'Βάιου', 'Βαΐου'},
                             'nom': {'Βάιος'},
                             'voc': {'Βάιο', 'Βάιε'}}}}

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
                'pl': {'nom': {'Φίλιπποι'}, 'acc': {'Φιλίππους', 'Φίλιππους'}, 'voc': {'Φίλιπποι'},
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

    def test_Paolo(self):
        self.assertDictEqual(
            noun.create_all('Μύκονος', proper_name=True, gender=FEM_SG),
            {'fem': {'sg': {'voc': {'Μύκονε'}, 'gen': {'Μύκονου', 'Μυκόνου'}, 'nom': {'Μύκονος'}, 'acc': {'Μύκονο'}},
                     'pl': {'voc': {''}, 'nom': {''}, 'acc': {''}}}}
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
            {'masc': {'pl': {'acc': {'Αγγέλους', 'Άγγελους'},
                                                'gen': {'Αγγέλων'},
                                                'nom': {'Άγγελοι'},
                                                'voc': {'Άγγελοι'}},
                        'sg': {'acc': {'Άγγελο'},
                               'gen': {'Αγγέλου', 'Άγγελου'},
                               'nom': {'Άγγελος'},
                               'voc': {'Άγγελε'}}}}
        )

