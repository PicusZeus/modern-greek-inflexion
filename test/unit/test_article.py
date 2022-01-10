from unittest import TestCase, main

from modern_greek_inflexion.articles import articles


#
# res = articles.create_all('ένας')
# print(res)


class ArticleTests(TestCase):

    def test_o(self):
        self.assertEqual(
            articles.create_all('ο'),
            {'sg': {'masc': {'nom': {'ο'}, 'acc': {'τον', 'το'}, 'gen': {'του'}},
                    'fem': {'nom': {'η'}, 'acc': {'την', 'τη'}, 'gen': {'της'}},
                    'neut': {'nom': {'το'}, 'acc': {'του'}, 'gen': {'το'}}},
             'pl': {'masc': {'nom': {'οι'}, 'acc': {'τους'}, 'gen': {'των'}},
                    'fem': {'nom': {'οι', 'αι'}, 'acc': {'τις', 'τας'}, 'gen': {'των'}},
                    'neut': {'nom': {'τα'}, 'acc': {'τα'}, 'gen': {'των'}}}}
        )

    def test_enas(self):
        self.assertEqual(
            articles.create_all('ένας'),
            {'sg': {'masc': {'nom': {'ένας'}, 'acc': {'ένα', 'έναν'}, 'gen': {'ενός'}},
                    'fem': {'nom': {'μια', 'μία'}, 'acc': {'μίαν', 'μιαν', 'μια', 'μία'}, 'gen': {'μίας', 'μιας'}},
                    'neut': {'nom': {'ένα'}, 'acc': {'ένα'}, 'gen': {'ενός'}}}}
        )

if __name__ == '__main__':
    main()