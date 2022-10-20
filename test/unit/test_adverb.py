from unittest import TestCase

from modern_greek_inflexion import adverb


class AdverbTest(TestCase):
    def test_adv_noris(self):
        self.assertDictEqual(
            adverb.create_all('νωρίς'),
            {'adv': {'νωρίς'}, 'comp_adv': {'νωρίτερα'}, 'superl_adv': {''}}
        )

    def test_adv_pote(self):
        self.assertDictEqual(
            adverb.create_all('ποτέ'),
            {'adv': {'ποτέ'}}
        )

    def test_adv_ano(self):
        self.assertDictEqual(
            adverb.create_all('άνω'),
            {'adv': {'άνω'}, 'comp_adv': {'ανώτερα'}, 'superl_adv': {'ανώτατα'}, 'comp': {
                'pl': {'neut': {'nom': {'ανώτερα'}, 'gen': {'ανώτερων'}, 'voc': {'ανώτερα'}, 'acc': {'ανώτερα'}},
                       'masc': {'nom': {'ανώτεροι'}, 'gen': {'ανώτερων'}, 'voc': {'ανώτεροι'}, 'acc': {'ανώτερους'}},
                       'fem': {'nom': {'ανώτερες'}, 'gen': {'ανώτερων'}, 'voc': {'ανώτερες'}, 'acc': {'ανώτερες'}}},
                'sg': {'neut': {'nom': {'ανώτερο'}, 'gen': {'ανώτερου'}, 'voc': {'ανώτερο'}, 'acc': {'ανώτερο'}},
                       'masc': {'nom': {'ανώτερος'}, 'gen': {'ανώτερου'}, 'voc': {'ανώτερε'}, 'acc': {'ανώτερο'}},
                       'fem': {'nom': {'ανώτερη'}, 'gen': {'ανώτερης'}, 'voc': {'ανώτερη'}, 'acc': {'ανώτερη'}}}},
             'superl': {
                 'pl': {'neut': {'nom': {'ανώτατα'}, 'gen': {'ανώτατων'}, 'voc': {'ανώτατα'}, 'acc': {'ανώτατα'}},
                        'masc': {'nom': {'ανώτατοι'}, 'gen': {'ανώτατων'}, 'voc': {'ανώτατοι'}, 'acc': {'ανώτατους'}},
                        'fem': {'nom': {'ανώτατες'}, 'gen': {'ανώτατων'}, 'voc': {'ανώτατες'}, 'acc': {'ανώτατες'}}},
                 'sg': {'neut': {'nom': {'ανώτατο'}, 'gen': {'ανώτατου'}, 'voc': {'ανώτατο'}, 'acc': {'ανώτατο'}},
                        'masc': {'nom': {'ανώτατος'}, 'gen': {'ανώτατου'}, 'voc': {'ανώτατε'}, 'acc': {'ανώτατο'}},
                        'fem': {'nom': {'ανώτατη'}, 'gen': {'ανώτατης'}, 'voc': {'ανώτατη'}, 'acc': {'ανώτατη'}}}}}
        )
