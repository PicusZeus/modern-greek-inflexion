from unittest import TestCase, main

from modern_greek_inflexion.noun import noun

res = noun.create_all('γη')
# res = noun.create_all_basic_forms('Φρόσω', proper_name=True)
print(res)


class ProperNounTests(TestCase):
    def test_Nikos(self):
        self.assertEqual(
            noun.create_all('Νίκος', proper_name=True),
            {'masc': {'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}},
                      'sg': {'gen': {'Νίκου'}, 'nom': {'Νίκος'}, 'acc': {'Νίκο'}, 'voc': {'Νίκο'}}}}

        )


    def test_Baios(self):
        self.assertEqual(
            noun.create_all('Βάιος', proper_name=True),
            {'masc': {'sg': {'voc': {'Βάιο'}, 'gen': {'Βάιου'}, 'nom': {'Βάιος'}, 'acc': {'Βάιο'}},
                      'pl': {'voc': {''}, 'acc': {''}, 'nom': {''}}}}

        )

    def test_Filippos(self):
        self.assertEqual(
            noun.create_all('Φίλιππος', proper_name=True),
            {'masc': {
                'sg': {'nom': {'Φίλιππος'}, 'acc': {'Φίλιππο'}, 'voc': {'Φίλιππε'}, 'gen': {'Φιλίππου', 'Φίλιππου'}},
                'pl': {'nom': {'Φίλιπποι'}, 'acc': {'Φιλίππους', 'Φίλιππους'}, 'voc': {'Φίλιπποι'},
                       'gen': {'Φιλίππων'}}}}
        )

    def test_Froso(self):
        self.assertEqual(
            noun.create_all('Φρόσω', proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'nom': {'Φρόσω'}, 'voc': {'Φρόσω'}, 'gen': {'Φρόσως'}, 'acc': {'Φρόσω'}}}}

        )

    def test_Barsobia(self):
        self.assertEqual(
            noun.create_all('Βαρσοβία', proper_name=True),
            {'fem': {'pl': {'acc': {''}, 'nom': {''}, 'gen': {''}, 'voc': {''}},
                     'sg': {'acc': {'Βαρσοβία'}, 'nom': {'Βαρσοβία'}, 'gen': {'Βαρσοβίας'}, 'voc': {'Βαρσοβία'}}}}

        )

    def test_Paolo(self):
        self.assertEqual(
            noun.create_all('Μύκονος', proper_name=True, proper_name_gender='fem'),
            {'fem': {'sg': {'voc': {'Μύκονε'}, 'gen': {'Μύκονου', 'Μυκόνου'}, 'nom': {'Μύκονος'}, 'acc': {'Μύκονο'}},
                     'pl': {'voc': {''}, 'nom': {''}, 'acc': {''}}}}

        )

if __name__ == '__main__':
    main()