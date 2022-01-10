from unittest import TestCase, main

from src.numerals import numerals

qa = numerals.create_all_adj_num('οχτώ')
qn = numerals.create_all_noun_num('χιλιάδες')


class NumeralsNounTest(TestCase):

    def test_noun_xiliades(self):
        self.assertEqual(
            numerals.create_all_noun_num('χιλιάδες'),
            {'fem': {'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}},
                     'pl': {'voc': {'χιλιάδες'}, 'acc': {'χιλιάδες'}, 'gen': {'χιλιάδων'}, 'nom': {'χιλιάδες'}}}}
        )


class NumeralsAdjectiveTest(TestCase):

    def test_num_diakosia(self):
        self.assertEqual(
            numerals.create_all_adj_num('διακόσια'),
            {'adj': {'sg': {'fem': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'masc': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'neut': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}}}, 'pl': {
                'fem': {'gen': {'διακοσίων'}, 'acc': {'διακόσιες'}, 'voc': {'διακόσιες'}, 'nom': {'διακόσιες'}},
                'masc': {'gen': {'διακοσίων'}, 'acc': {'διακόσιους'}, 'voc': {'διακόσιοι'}, 'nom': {'διακόσιοι'}},
                'neut': {'gen': {'διακοσίων'}, 'acc': {'διακόσια'}, 'voc': {'διακόσια'}, 'nom': {'διακόσια'}}}}}

        )

    def test_num_deuteros(self):
        self.assertEqual(
            numerals.create_all_adj_num('δεύτερος'),
            {'adj': {'sg': {'masc': {'nom': {'δεύτερος'}, 'acc': {'δεύτερο'}, 'gen': {'δεύτερου'}, 'voc': {'δεύτερε'}},
                            'fem': {'nom': {'δεύτερη'}, 'acc': {'δεύτερη'}, 'gen': {'δεύτερης'}, 'voc': {'δεύτερη'}},
                            'neut': {'nom': {'δεύτερο'}, 'acc': {'δεύτερο'}, 'gen': {'δεύτερου'}, 'voc': {'δεύτερο'}}},
                     'pl': {
                         'masc': {'nom': {'δεύτεροι'}, 'acc': {'δεύτερους'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτεροι'}},
                         'fem': {'nom': {'δεύτερες'}, 'acc': {'δεύτερες'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτερες'}},
                         'neut': {'nom': {'δεύτερα'}, 'acc': {'δεύτερα'}, 'gen': {'δεύτερων'}, 'voc': {'δεύτερα'}}}},
             'adv': {'δεύτερον'}}

        )

    def test_num_protos(self):
        self.maxDiff = None
        self.assertEqual(
            numerals.create_all_adj_num('πρώτος'),
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

    def test_num_dekatria(self):
        self.assertEqual(
            numerals.create_all_adj_num('δεκατρία'),
            {'adj': {
                'pl': {'masc': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'fem': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'neut': {'voc': {'δεκατρία'}, 'acc': {'δεκατρία'}, 'nom': {'δεκατρία'}, 'gen': {'δεκατριών'}}},
                'sg': {'masc': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'fem': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'neut': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}}}}}

        )

    def test_num_oxto(self):
        self.assertEqual(
            numerals.create_all_adj_num('οχτώ'),
            {'adj': {'pl': {'masc': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}},
                            'fem': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}},
                            'neut': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}}},
                     'sg': {'masc': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}},
                            'fem': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}},
                            'neut': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}}}}}

        )

    def test_num_enamisi(self):
        self.assertEqual(
            numerals.create_all_adj_num('ενάμισι'),
            {'adj': {'sg': {'masc': {'gen': {'ενάμιση'}, 'nom': {'ενάμισης'}, 'acc': {'ενάμιση'}, 'voc': {'ενάμιση'}},
                            'neut': {'gen': {'ενάμισι'}, 'nom': {'ενάμισι'}, 'acc': {'ενάμισι'}, 'voc': {'ενάμισι'}},
                            'fem': {'gen': {'μιάμισης'}, 'nom': {'μιάμιση'}, 'acc': {'μιάμιση'}, 'voc': {'μιάμιση'}}},
                     'pl': {'masc': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'neut': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'fem': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}}}}}

        )
if __name__ == '__main__':
    main()
