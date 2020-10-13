from unittest import TestCase, main

from modern_greek_inflexion.quantifiers import quantifiers

qa = quantifiers.create_all_adj_quant('δεύτερος')
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

    def test_quant_deuteros(self):
        self.assertEqual(
            quantifiers.create_all_adj_quant('δεύτερος'),
            {'adj': {'sg': {'masc': {'nom': {'δεύτερος'}, 'acc': {'δεύτερο'}, 'gen': {'δεύτερου'}, 'voc': {'δεύτερε'}},
                            'fem': {'nom': {'δεύτερη'}, 'acc': {'δεύτερη'}, 'gen': {'δεύτερης'}, 'voc': {'δεύτερη'}},
                            'neut': {'nom': {'δεύτερο'}, 'acc': {'δεύτερο'}, 'gen': {'δεύτερου'}, 'voc': {'δεύτερο'}}},
                     'pl': {
                         'masc': {'nom': {'δεύτεροι'}, 'acc': {'δεύτερους'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτεροι'}},
                         'fem': {'nom': {'δεύτερες'}, 'acc': {'δεύτερες'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτερες'}},
                         'neut': {'nom': {'δεύτερα'}, 'acc': {'δεύτερα'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτερα'}}}},
             'adv': {'δεύτερον'}}

        )

    def test_quant_protos(self):
        self.maxDiff = None
        self.assertEqual(
            quantifiers.create_all_adj_quant('πρώτος'),
            {'adv': {'πρώτον', 'πρώτα'}, 'comp': {'sg': {
                'neut': {'voc': {'πρωτύτερο'}, 'nom': {'πρωτύτερο'}, 'gen': {'πρωτύτερου'}, 'acc': {'πρωτύτερο'}},
                'masc': {'voc': {'πρωτύτερε'}, 'nom': {'πρωτύτερος'}, 'gen': {'πρωτύτερου'}, 'acc': {'πρωτύτερο'}},
                'fem': {'voc': {'πρωτύτερη'}, 'nom': {'πρωτύτερη'}, 'gen': {'πρωτύτερης'}, 'acc': {'πρωτύτερη'}}},
                                                                       'pl': {'neut': {'voc': {'πρωτύτερα'},
                                                                                       'nom': {'πρωτύτερα'},
                                                                                       'gen': {'πρωτύτερων'},
                                                                                       'acc': {'πρωτύτερα'}},
                                                                              'masc': {'voc': {'πρωτύτεροι'},
                                                                                       'nom': {'πρωτύτεροι'},
                                                                                       'gen': {'πρωτύτερων'},
                                                                                       'acc': {'πρωτύτερους'}},
                                                                              'fem': {'voc': {'πρωτύτερες'},
                                                                                      'nom': {'πρωτύτερες'},
                                                                                      'gen': {'πρωτύτερων'},
                                                                                      'acc': {'πρωτύτερες'}}}},
             'superl_adv': {'πρώτιστα'}, 'superl': {
                'sg': {'neut': {'voc': {'πρώτιστο'}, 'nom': {'πρώτιστο'}, 'gen': {'πρώτιστου'}, 'acc': {'πρώτιστο'}},
                       'masc': {'voc': {'πρώτιστε'}, 'nom': {'πρώτιστος'}, 'gen': {'πρώτιστου'}, 'acc': {'πρώτιστο'}},
                       'fem': {'voc': {'πρώτιστη'}, 'nom': {'πρώτιστη'}, 'gen': {'πρώτιστης'}, 'acc': {'πρώτιστη'}}},
                'pl': {'neut': {'voc': {'πρώτιστα'}, 'nom': {'πρώτιστα'}, 'gen': {'πρώτιστων'}, 'acc': {'πρώτιστα'}},
                       'masc': {'voc': {'πρώτιστοι'}, 'nom': {'πρώτιστοι'}, 'gen': {'πρώτιστων'},
                                'acc': {'πρώτιστους'}},
                       'fem': {'voc': {'πρώτιστες'}, 'nom': {'πρώτιστες'}, 'gen': {'πρώτιστων'},
                               'acc': {'πρώτιστες'}}}}, 'comp_adv': {'πρωτύτερα'}, 'adj': {
                'sg': {'neut': {'voc': {'πρώτο'}, 'nom': {'πρώτο'}, 'gen': {'πρώτου'}, 'acc': {'πρώτο'}},
                       'masc': {'voc': {'πρώτε'}, 'nom': {'πρώτος'}, 'gen': {'πρώτου'}, 'acc': {'πρώτο'}},
                       'fem': {'voc': {'πρώτη'}, 'nom': {'πρώτη'}, 'gen': {'πρώτης'}, 'acc': {'πρώτη'}}},
                'pl': {'neut': {'voc': {'πρώτα'}, 'nom': {'πρώτα'}, 'gen': {'πρώτων'}, 'acc': {'πρώτα'}},
                       'masc': {'voc': {'πρώτοι'}, 'nom': {'πρώτοι'}, 'gen': {'πρώτων'}, 'acc': {'πρώτους'}},
                       'fem': {'voc': {'πρώτες'}, 'nom': {'πρώτες'}, 'gen': {'πρώτων'}, 'acc': {'πρώτες'}}}}}

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