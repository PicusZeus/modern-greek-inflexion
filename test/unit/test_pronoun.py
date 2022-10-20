from unittest import TestCase

from modern_greek_inflexion import pronoun


class PronounTestAll(TestCase):
    def test_pron_opoios(self):
        self.assertDictEqual(
            pronoun.create_all('οποίος'),
            {'sg': {'fem': {'gen': {'οποίας'}, 'voc': {''}, 'acc': {'οποία', 'οποίαν'}, 'nom': {'οποία'}},
                    'masc': {'gen': {'οποίου'}, 'voc': {''}, 'acc': {'οποίο', 'οποίον'}, 'nom': {'οποίος'}},
                    'neut': {'gen': {'οποίου'}, 'voc': {''}, 'acc': {'οποίο'}, 'nom': {'οποίο'}}},
             'pl': {'fem': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποίες'}, 'nom': {'οποίες'}},
                    'masc': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποίους'}, 'nom': {'οποίοι'}},
                    'neut': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποία'}, 'nom': {'οποία'}}}}
        )

    def test_pron_ostis(self):
        self.assertDictEqual(
            pronoun.create_all('όστις'),
            {'sg': {'masc': {'nom': {'όστις'}, 'gen': {'ούτινος', 'ότου'}, 'acc': {'όντινα'}},
                    'neut': {'nom': {'ότι'}, 'gen': {'ούτινος', 'ότου'}, 'acc': {'ότι'}},
                    'fem': {'nom': {'ήτις'}, 'gen': {'ήστινος'}, 'acc': {'ήντίνα'}}},
             'pl': {'masc': {'nom': {'οίτινες'}, 'gen': {'ώντινων'}, 'acc': {'ούστινας'}},
                    'neut': {'nom': {'άτινα', 'άττα'}, 'gen': {'ώντινων'}, 'acc': {'άτινα', 'άττα'}},
                    'fem': {'nom': {'αίτινες'}, 'gen': {'ώντινων'}, 'acc': {'άστινας'}}}}
        )

    def test_pron_osper(self):
        self.assertDictEqual(
            pronoun.create_all('όσπερ'),
            {'sg': {'neut': {'gen': {'ούπερ'}, 'acc': {'όπερ'}, 'nom': {'όπερ'}},
                    'fem': {'gen': {'ήσπερ'}, 'acc': {'ήνπερ'}, 'nom': {'ήπερ'}},
                    'masc': {'gen': {'ούπερ'}, 'acc': {'όνπερ'}, 'nom': {'όσπερ'}}},
             'pl': {'neut': {'gen': {'ώνπερ'}, 'acc': {'άπερ'}, 'nom': {'άπερ'}},
                    'fem': {'gen': {'ώνπερ'}, 'acc': {'άσπερ'}, 'nom': {'αίπερ'}},
                    'masc': {'gen': {'ώνπερ'}, 'acc': {'ούσπερ'}, 'nom': {'οίπερ'}}}}
        )

    def test_pron_amfoteroi(self):
        self.assertDictEqual(
            pronoun.create_all('αμφότεροι'),
            {'pl': {'neut': {'acc': {'αμφότερα'}, 'nom': {'αμφότερα'}, 'voc': {''}, 'gen': {'αμφότερων'}},
                    'fem': {'acc': {'αμφότερες'}, 'nom': {'αμφότερες'}, 'voc': {''}, 'gen': {'αμφότερων'}},
                    'masc': {'acc': {'αμφότερους'}, 'nom': {'αμφότεροι'}, 'voc': {''}, 'gen': {'αμφότερων'}}}}
        )

    def test_pron_ego(self):
        self.assertDictEqual(
            pronoun.create_all('εγώ'),
            {'sg': {'nd': {'gen': {'εμένα'}, 'acc': {'εμένα', 'μένα'}, 'nom': {'εγώ'}}},
             'pl': {'nd': {'gen': {'εμάς', 'ημών'}, 'acc': {'εμάς', 'μας'}, 'nom': {'εμείς'}}}}
        )

    def test_pron_ego_weak(self):
        self.assertDictEqual(
            pronoun.create_all('εγώ', strong=False),
            {'sg': {'nd': {'acc': {'με'}, 'nom': {''}, 'gen': {'μου'}}},
             'pl': {'nd': {'acc': {'μας'}, 'nom': {''}, 'gen': {'μας'}}}}
        )

    def test_pron_opoiosdhpote(self):
        self.assertDictEqual(
            pronoun.create_all('οποιοσδήποτε'),
            {'pl': {'neut': {'nom': {'οποιαδήποτε'}, 'gen': {'οποιωνδήποτε'}, 'acc': {'οποιαδήποτε'}, 'voc': {''}},
                    'masc': {'nom': {'οποιοιδήποτε'}, 'gen': {'οποιωνδήποτε'}, 'acc': {'οποιουσδήποτε'}, 'voc': {''}},
                    'fem': {'nom': {'οποιεσδήποτε'}, 'gen': {'οποιωνδήποτε'}, 'acc': {'οποιεσδήποτε'}, 'voc': {''}}},
             'sg': {'neut': {'nom': {'οποιοδήποτε'}, 'gen': {'οποιουδήποτε'}, 'acc': {'οποιοδήποτε'}, 'voc': {''}},
                    'masc': {'nom': {'οποιοσδήποτε'}, 'gen': {'οποιουδήποτε'}, 'acc': {'οποιοδήποτε', 'οποιονδήποτε'},
                             'voc': {''}},
                    'fem': {'nom': {'οποιαδήποτε'}, 'gen': {'οποιασδήποτε'}, 'acc': {'οποιαδήποτε', 'οποιανδήποτε'},
                            'voc': {''}}}}
        )

    def test_pron_kaneis(self):
        self.assertDictEqual(
            pronoun.create_all('κανένας'),
            {'sg': {'neut': {'nom': {'κανένα'}, 'gen': {'κανενός'}, 'acc': {'κανένα'}},
                    'masc': {'nom': {'κανένας', 'κανείς', 'κάνας'}, 'gen': {'κανενός'}, 'acc': {'κανένα', 'κανέναν'}},
                    'fem': {'nom': {'καμία', 'καμιά'}, 'gen': {'καμίας', 'καμιάς'},
                            'acc': {'καμιά', 'καμιάν', 'καμίαν', 'καμία'}}}}
        )

    def test_pron_katheti(self):
        self.assertDictEqual(
            pronoun.create_all('καθετί'),
            {'sg': {'masc': {'nom': {''}, 'voc': {''}, 'acc': {''}, 'gen': {''}},
                    'fem': {'nom': {''}, 'voc': {''}, 'acc': {''}, 'gen': {''}},
                    'neut': {'nom': {'καθετί'}, 'voc': {''}, 'acc': {'καθετί'}, 'gen': {''}}},
             'pl': {'masc': {'nom': {''}, 'voc': {''}, 'acc': {''}, 'gen': {''}},
                    'fem': {'nom': {''}, 'voc': {''}, 'acc': {''}, 'gen': {''}},
                    'neut': {'nom': {'καθετί'}, 'voc': {''}, 'acc': {'καθετί'}, 'gen': {''}}}}
        )



