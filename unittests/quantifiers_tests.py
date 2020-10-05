from unittest import TestCase, main

from modern_greek_inflexion.quantifiers import quantifiers

qa = quantifiers.create_all_adj_quant('οχτώ')
qn = quantifiers.create_all_noun_quant('χιλιάδες')
print(qa)

class QuntifiersNounTest(TestCase):

    def test_noun_xiliades(self):
        self.assertEqual(
            quantifiers.create_all_noun_quant('χιλιάδες'),
            {'fem': {'sg': {'nom': '', 'gen': '', 'voc': '', 'acc': ''},
                     'pl': {'nom': 'χιλιάδες', 'acc': 'χιλιάδες', 'voc': 'χιλιάδες', 'gen': 'χιλιάδων'}}}
        )



class QuantifiersAdjectiveTest(TestCase):

    def test_quant_diakosia(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('διακόσια'),
            {'adj': [{'sg': {'masc': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'fem': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'neut': {'nom': '', 'gen': '', 'acc': '', 'voc': ''}},
                      'pl': {'masc': {'nom': 'διακόσιοι', 'gen': 'διακοσίων', 'acc': 'διακόσιους', 'voc': 'διακόσιοι'},
                             'fem': {'nom': 'διακόσιες', 'gen': 'διακοσίων', 'acc': 'διακόσιες', 'voc': 'διακόσιες'},
                             'neut': {'nom': 'διακόσια', 'gen': 'διακοσίων', 'acc': 'διακόσια', 'voc': 'διακόσια'}}}]}
        )

    def test_quant_dekatria(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('δεκατρία'),
            {'adj': [{'sg': {'masc': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'fem': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'neut': {'nom': '', 'gen': '', 'acc': '', 'voc': ''}},
                      'pl': {'masc': {'nom': 'δεκατρείς', 'gen': 'δεκατριών', 'acc': 'δεκατρείς', 'voc': 'δεκατρείς'},
                             'fem': {'nom': 'δεκατρείς', 'gen': 'δεκατριών', 'acc': 'δεκατρείς', 'voc': 'δεκατρείς'},
                             'neut': {'nom': 'δεκατρία', 'gen': 'δεκατριών', 'acc': 'δεκατρία', 'voc': 'δεκατρία'}}}]}
        )

    def test_quant_oxto(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('οχτώ'),
            {'adj': [{'sg': {'masc': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'fem': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                             'neut': {'nom': '', 'gen': '', 'acc': '', 'voc': ''}},
                      'pl': {'masc': {'nom': 'οχτώ,οκτώ', 'gen': 'οχτώ,οκτώ', 'acc': 'οχτώ,οκτώ', 'voc': 'οχτώ,οκτώ'},
                             'fem': {'nom': 'οχτώ,οκτώ', 'gen': 'οχτώ,οκτώ', 'acc': 'οχτώ,οκτώ', 'voc': 'οχτώ,οκτώ'},
                             'neut': {'nom': 'οχτώ,οκτώ', 'gen': 'οχτώ,οκτώ', 'acc': 'οχτώ,οκτώ',
                                      'voc': 'οχτώ,οκτώ'}}}]}

        )


if __name__ == '__main__':
    main()