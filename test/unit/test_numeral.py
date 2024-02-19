from unittest import TestCase, main

from icecream import ic

from modern_greek_inflexion import numerals
from modern_greek_inflexion.numerals import Numeral
from modern_greek_inflexion.resources.variables import NOUN


class NumeralsNounTest(TestCase):

    def test_noun_xiliades(self):
        self.assertDictEqual(
            Numeral('χιλιάδες', pos=NOUN).all(),
            {'fem': {'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}},
                     'pl': {'voc': {'χιλιάδες'}, 'acc': {'χιλιάδες'}, 'gen': {'χιλιάδων'}, 'nom': {'χιλιάδες'}}}}
        )


class NumeralsAdjectiveTest(TestCase):

    def test_num_diakosia(self):
        self.assertDictEqual(
            Numeral('διακόσια').all(),
            {'adj': {'sg': {'fem': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'masc': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}},
                            'neut': {'gen': {''}, 'acc': {''}, 'voc': {''}, 'nom': {''}}}, 'pl': {
                'fem': {'gen': {'διακοσίων'}, 'acc': {'διακόσιες'}, 'voc': {'διακόσιες'}, 'nom': {'διακόσιες'}},
                'masc': {'gen': {'διακοσίων'}, 'acc': {'διακόσιους'}, 'voc': {'διακόσιοι'}, 'nom': {'διακόσιοι'}},
                'neut': {'gen': {'διακοσίων'}, 'acc': {'διακόσια'}, 'voc': {'διακόσια'}, 'nom': {'διακόσια'}}}}}
        )

    def test_num_deuteros(self):
        self.assertDictEqual(
            Numeral('δεύτερος').all(),
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
        self.assertDictEqual(
            Numeral('πρώτος').all(),
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

                       'fem': {'acc': {'πρώτιστη', 'πρωτίστη'},
                                                                      'gen': {'πρωτίστης', 'πρώτιστης'},
                                                                      'nom': {'πρώτιστη', 'πρωτίστη'},
                                                                      'voc': {'πρώτιστη', 'πρωτίστη'}}},

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
                       'fem': {'voc': {'πρώτες'}, 'nom': {'πρώτες'}, 'gen': {'πρώτων'}, 'acc': {'πρώτες'}}}}},
        )

    def test_num_dekatria(self):
        self.assertDictEqual(
            Numeral('δεκατρία').all(),
            {'adj': {
                'pl': {'masc': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'fem': {'voc': {'δεκατρείς'}, 'acc': {'δεκατρείς'}, 'nom': {'δεκατρείς'}, 'gen': {'δεκατριών'}},
                       'neut': {'voc': {'δεκατρία'}, 'acc': {'δεκατρία'}, 'nom': {'δεκατρία'}, 'gen': {'δεκατριών'}}},
                'sg': {'masc': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'fem': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}},
                       'neut': {'voc': {''}, 'acc': {''}, 'nom': {''}, 'gen': {''}}}}}
        )

    def test_num_oxto(self):
        self.assertDictEqual(
            Numeral('οχτώ').all(),
            {'adj': {'pl': {'masc': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}},
                            'fem': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}},
                            'neut': {'gen': {'οχτώ'}, 'nom': {'οχτώ'}, 'voc': {'οχτώ'}, 'acc': {'οχτώ'}}},
                     'sg': {'masc': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}},
                            'fem': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}},
                            'neut': {'gen': {''}, 'nom': {''}, 'voc': {''}, 'acc': {''}}}}}
        )

    def test_num_enamisi(self):
        self.assertDictEqual(
            Numeral('ενάμισι').all(),
            {'adj': {'sg': {'masc': {'gen': {'ενάμιση'}, 'nom': {'ενάμισης'}, 'acc': {'ενάμιση'}, 'voc': {'ενάμιση'}},
                            'neut': {'gen': {'ενάμισι'}, 'nom': {'ενάμισι'}, 'acc': {'ενάμισι'}, 'voc': {'ενάμισι'}},
                            'fem': {'gen': {'μιάμισης'}, 'nom': {'μιάμιση'}, 'acc': {'μιάμιση'}, 'voc': {'μιάμιση'}}},
                     'pl': {'masc': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'neut': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'fem': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}}}}}
        )

    def test_num_enamisis(self):
        self.assertDictEqual(
            Numeral('ενάμισι').all(),
            {'adj': {'sg': {'masc': {'gen': {'ενάμιση'}, 'nom': {'ενάμισης'}, 'acc': {'ενάμιση'}, 'voc': {'ενάμιση'}},
                            'neut': {'gen': {'ενάμισι'}, 'nom': {'ενάμισι'}, 'acc': {'ενάμισι'}, 'voc': {'ενάμισι'}},
                            'fem': {'gen': {'μιάμισης'}, 'nom': {'μιάμιση'}, 'acc': {'μιάμιση'}, 'voc': {'μιάμιση'}}},
                     'pl': {'masc': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'neut': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}},
                            'fem': {'gen': {''}, 'nom': {''}, 'acc': {''}, 'voc': {''}}}}},
        )

    def test_num_treisimisi(self):
        self.assertDictEqual(
            Numeral('τρεισήμισι').all(),
            {'adj': {'pl': {'fem': {'acc': {'τρεισήμισι'},
                                    'gen': {'τρεισήμισι'},
                                    'nom': {'τρεισήμισι'},
                                    'voc': {'τρεισήμισι'}},
                            'masc': {'acc': {'τρεισήμισι'},
                                     'gen': {'τρεισήμισι'},
                                     'nom': {'τρεισήμισι'},
                                     'voc': {'τρεισήμισι'}},
                            'neut': {'acc': {'τρεισήμισι'},
                                     'gen': {'τρεισήμισι'},
                                     'nom': {'τρεισήμισι'},
                                     'voc': {'τρεισήμισι'}}},
                     'sg': {'fem': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                            'masc': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                            'neut': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}}}}}

        )

