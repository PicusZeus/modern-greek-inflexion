from unittest import TestCase

from modern_greek_inflexion import noun


class ProperNounTests(TestCase):
    def test_Nikos(self):
        self.assertDictEqual(
            noun.create_all('Νίκος', proper_name=True),
            {'masc': {'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}},
                      'sg': {'gen': {'Νίκου'}, 'nom': {'Νίκος'}, 'acc': {'Νίκο'}, 'voc': {'Νίκο'}}}}
        )

    def test_Papandreou(self):
        self.assertDictEqual(
            noun.create_all('Παπανδρέου', proper_name=True, gender='surname'),
            {'surname': {'pl': {'nom': {'Παπανδρέου'}, 'voc': {'Παπανδρέου'}, 'gen': {'Παπανδρέου'},
                                'acc': {'Παπανδρέου'}}, 'sg': {'nom': {'Παπανδρέου'}, 'gen': {'Παπανδρέου'},
                                                               'voc': {'Παπανδρέου'}, 'acc': {'Παπανδρέου'}}}}
        )

    def test_Mykonos(self):
        self.assertDictEqual(
            noun.create_all('Μύκονος', proper_name=True, gender='fem_sg'),
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
            {'masc': {'pl': {'voc': {''}, 'acc': {''}, 'nom': {''}},
                      'sg': {'voc': {'Βάιε', 'Βάιο'}, 'acc': {'Βάιο'}, 'nom': {'Βάιος'}, 'gen': {'Βαΐου', 'Βάιου'}}}}
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
            noun.create_all('Φρόσω', proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'nom': {'Φρόσω'}, 'voc': {'Φρόσω'}, 'gen': {'Φρόσως'}, 'acc': {'Φρόσω'}}}}
        )

    def test_Barsobia(self):
        self.assertDictEqual(
            noun.create_all('Βαρσοβία', proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'gen': {''}, 'voc': {''}},
                     'sg': {'acc': {'Βαρσοβία'}, 'nom': {'Βαρσοβία'}, 'gen': {'Βαρσοβίας'}, 'voc': {'Βαρσοβία'}}}}
        )

    def test_Paolo(self):
        self.assertDictEqual(
            noun.create_all('Μύκονος', proper_name=True, gender='fem'),
            {'fem': {'sg': {'voc': {'Μύκονε'}, 'gen': {'Μύκονου', 'Μυκόνου'}, 'nom': {'Μύκονος'}, 'acc': {'Μύκονο'}},
                     'pl': {'voc': {''}, 'nom': {''}, 'acc': {''}}}}
        )



