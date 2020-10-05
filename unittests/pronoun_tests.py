from unittest import TestCase, main

from modern_greek_inflexion.pronoun import pronoun

res = pronoun.create_all('ποιος')
print(res)


class PronounTestAll(TestCase):
    def test_pron_opoios(self):
        self.assertEqual(
            pronoun.create_all('οποίος'),
            {'sg': {'masc': {'nom': 'οποίος', 'gen': 'οποίου', 'acc': 'οποίο,οποίον', 'voc': ''},
                    'fem': {'nom': 'οποία', 'gen': 'οποίας', 'acc': 'οποία,οποίαν', 'voc': ''},
                    'neut': {'nom': 'οποίο', 'gen': 'οποίου', 'acc': 'οποίο', 'voc': ''}},
             'pl': {'masc': {'nom': 'οποίοι', 'gen': 'οποίων', 'acc': 'οποίους', 'voc': ''},
                    'fem': {'nom': 'οποίες', 'gen': 'οποίων', 'acc': 'οποίες', 'voc': ''},
                    'neut': {'nom': 'οποία', 'gen': 'οποίων', 'acc': 'οποία', 'voc': ''}}}

        )

    def test_pron_ego(self):
        self.assertEqual(
            pronoun.create_all('εγώ'),
            {'nd': {'sg': {'nom': 'εγώ', 'gen': 'εμένα', 'acc': 'εμένα,μένα'},
                    'pl': {'nom': 'εμείς', 'gen': 'εμάς,ημών', 'acc': 'εμάς,μας'}}}

        )

    def test_pron_ego_weak(self):
        self.assertEqual(
            pronoun.create_all('εγώ', strong=False),
            {'nd': {'sg': {'nom': '', 'gen': 'μου', 'acc': 'με'}, 'pl': {'nom': '', 'gen': 'μας', 'acc': 'μας'}}}
            )

    def test_pron_opoiosdhpote(self):
        self.assertEqual(
            pronoun.create_all('οποιοσδήποτε'),
            {'sg': {
                'masc': {'nom': 'οποιοσδήποτε', 'gen': 'οποιουδήποτε', 'acc': 'οποιοδήποτε,οποιονδήποτε', 'voc': ''},
                'fem': {'nom': 'οποιαδήποτε', 'gen': 'οποιασδήποτε', 'acc': 'οποιαδήποτε,οποιανδήποτε', 'voc': ''},
                'neut': {'nom': 'οποιοδήποτε', 'gen': 'οποιουδήποτε', 'acc': 'οποιοδήποτε', 'voc': ''}},
             'pl': {'masc': {'nom': 'οποιοιδήποτε', 'gen': 'οποιωνδήποτε', 'acc': 'οποιουσδήποτε', 'voc': ''},
                    'fem': {'nom': 'οποιεσδήποτε', 'gen': 'οποιωνδήποτε', 'acc': 'οποιεσδήποτε', 'voc': ''},
                    'neut': {'nom': 'οποιαδήποτε', 'gen': 'οποιωνδήποτε', 'acc': 'οποιαδήποτε', 'voc': ''}}}

        )

    def test_pron_kaneis(self):
        self.assertEqual(
            pronoun.create_all('κανένας'),
            {'sg': {'masc': {'nom': 'κανείς,κανένας,κάνας', 'acc': 'κανένα,κανέναν', 'gen': 'κανενός'},
                    'fem': {'nom': 'καμία,καμιά', 'acc': 'καμία,καμίαν,καμιά,καμιάν', 'gen': 'καμίας,καμιάς'},
                    'neut': {'nom': 'κανένα', 'acc': 'κανένα', 'gen': 'κανενός'}}}

        )

    def test_pron_katheti(self):
        self.assertEqual(
            pronoun.create_all('καθετί'),
            {'sg': {'masc': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                    'fem': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                    'neut': {'nom': 'καθετί', 'gen': '', 'acc': 'καθετί', 'voc': ''}},
             'pl': {'masc': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                    'fem': {'nom': '', 'gen': '', 'acc': '', 'voc': ''},
                    'neut': {'nom': 'καθετί', 'gen': '', 'acc': 'καθετί', 'voc': ''}}}

        )



if __name__ == '__main__':
    main()