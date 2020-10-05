from unittest import TestCase, main

from modern_greek_inflexion.adverb import adverb

adv = adverb.create_all('ποτέ')
print(adv)

class AdverbTest(TestCase):
    def test_adv_noris(self):
        self.assertEqual(
            adverb.create_all('νωρίς'),
            {'adv': ['νωρίς'], 'comp_adv': ['νωρίτερα'], 'superl_adv': ['']}

        )

    def test_adv_pote(self):
        self.assertEqual(
            adverb.create_all('ποτέ'),
            {'adv': ['ποτέ']}

        )
if __name__ == '__main__':
    main()