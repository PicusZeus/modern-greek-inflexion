from unittest import TestCase, main

from modern_greek_inflexion.quantifiers import quantifiers

qa = quantifiers.create_all_adj_quant('οχτώ')
qn = quantifiers.create_all_noun_quant('χιλιάδες')
print(qa)

class QuntifiersNounTest(TestCase):

    def test_noun_xiliades(self):
        self.assertEqual(
            quantifiers.create_all_noun_quant('χιλιάδες'),
            {'fem': {'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}},
                     'pl': {'voc': {'χιλιάδες'}, 'acc': {'χιλιάδες'}, 'gen': {'χιλιάδων'}, 'nom': {'χιλιάδες'}}}}
        )


class QuantifiersAdjectiveTest(TestCase):

    def test_quant_diakosia(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('διακόσια'),
            {'adj': {'sg': {'fem': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'masc': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'neut': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}}}, 'pl': {
                'fem': {'gen': {'διακοσίων'}, 'acc': {'διακόσιες'}, 'voc': {'διακόσιες'}, 'nom': {'διακόσιες'}},
                'masc': {'gen': {'διακοσίων'}, 'acc': {'διακόσιους'}, 'voc': {'διακόσιοι'}, 'nom': {'διακόσιοι'}},
                'neut': {'gen': {'διακοσίων'}, 'acc': {'διακόσια'}, 'voc': {'διακόσια'}, 'nom': {'διακόσια'}}}}}

        )

    def test_quant_dekatria(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('δεκατρία'),
            {'adj': {
                'pl': {'masc': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'fem': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'neut': {'voc': {'δεκατρία'}, 'acc': {'δεκατρία'}, 'nom': {'δεκατρία'}, 'gen': {'δεκατριών'}}},
                'sg': {'masc': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'fem': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'neut': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}}}}}

        )

    def test_quant_oxto(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('οχτώ'),
            {'adj': {'sg': {'fem': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'neut': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'masc': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}}}, 'pl': {
                'fem': {'gen': {'οχτώ', 'οκτώ'}, 'acc': {'οχτώ', 'οκτώ'}, 'voc': {'οχτώ', 'οκτώ'},
                        'nom': {'οχτώ', 'οκτώ'}},
                'neut': {'gen': {'οχτώ', 'οκτώ'}, 'acc': {'οχτώ', 'οκτώ'}, 'voc': {'οχτώ', 'οκτώ'},
                         'nom': {'οχτώ', 'οκτώ'}},
                'masc': {'gen': {'οχτώ', 'οκτώ'}, 'acc': {'οχτώ', 'οκτώ'}, 'voc': {'οχτώ', 'οκτώ'},
                         'nom': {'οχτώ', 'οκτώ'}}}}}
        )


if __name__ == '__main__':
    main()