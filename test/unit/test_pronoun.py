from unittest import TestCase

# from icecream import ic

from modern_greek_inflexion import pronoun
# from modern_greek_inflexion.resources.resources import greek_corpus


class PronounTestAll(TestCase):
    def test_pron_opoios(self):
        self.maxDiff = None
        self.assertDictEqual(
            pronoun.create_all('οποίος'),
            {'sg': {'fem': {'gen': {'οποίας'}, 'voc': {''}, 'acc': {'οποία', 'οποίαν'}, 'nom': {'οποία'}},
                    'masc': {'gen': {'οποίου'}, 'voc': {''}, 'acc': {'οποίο', 'οποίον'}, 'nom': {'οποίος'}},
                    'neut': {'gen': {'οποίου'}, 'voc': {''}, 'acc': {'οποίο'}, 'nom': {'οποίο'}}},
             'pl': {'fem': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποίες'}, 'nom': {'οποίες'}},
                    'masc': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποίους'}, 'nom': {'οποίοι'}},
                    'neut': {'gen': {'οποίων'}, 'voc': {''}, 'acc': {'οποία'}, 'nom': {'οποία'}}}},
        )

    def test_pron_o(self):
        self.assertDictEqual(
            pronoun.create_all('ό'),
            {'sg': {'neut': {'nom': {'ό'}, 'acc': {'ό'}}}}

        )

    def test_pron_ostis(self):
        self.assertDictEqual(
            pronoun.create_all('όστις'),
            {'sg': {'masc': {'nom': {'όστις'}, 'gen': {'ούτινος', 'ότου'}, 'acc': {'όντινα'}},
                    'neut': {'nom': {'ότι'}, 'gen': {'ούτινος', 'ότου'}, 'acc': {'ότι'}},
                    'fem': {'nom': {'ήτις'}, 'gen': {'ήστινος'}, 'acc': {'ήντίνα'}}},
             'pl': {'masc': {'nom': {'οίτινες'}, 'gen': {'ώντινων'}, 'acc': {'ούστινας'}},
                    'neut': {'nom': {'άτινα', 'άττα'}, 'gen': {'ώντινων'}, 'acc': {'άτινα', 'άττα'}},
                    'fem': {'nom': {'αίτινες'}, 'gen': {'ώντινων'}, 'acc': {'άστινας'}}}},
        )

    def test_pron_pas(self):
        self.assertDictEqual(
            pronoun.create_all('πας'),
            {'pl': {'fem': {'acc': {'πάσες'},
                            'gen': {'πασών'},
                            'nom': {'πάσες'},
                            'voc': {'πάσες'}},
                    'masc': {'acc': {'πάντες'},
                             'gen': {'πάντων'},
                             'nom': {'πάντες'},
                             'voc': {'πάντες'}},
                    'neut': {'acc': {'πάντα'},
                             'gen': {'πάντων'},
                             'nom': {'πάντα'},
                             'voc': {'πάντα'}}},
             'sg': {'fem': {'acc': {'πάσα', 'πάσαν'},
                            'gen': {'πάσας'},
                            'nom': {'πάσα'},
                            'voc': {'πάσα'}},
                    'masc': {'acc': {'πάντα'},
                             'gen': {'παντός'},
                             'nom': {'πας'},
                             'voc': {'πας'}},
                    'neut': {'acc': {'παν'},
                             'gen': {'παντός'},
                             'nom': {'παν'},
                             'voc': {'παν'}}}}

        )
    def test_pron_pouq(self):
        self.assertDictEqual(
            pronoun.create_all('πού'),
            {'nd': {'nd': {'nd': {'πού'}}}}

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
            {'pl': {'fem': {'acc': {'αμφότερες'},
                            'gen': {'αμφοτέρων', 'αμφότερων'},
                            'nom': {'αμφότερες'},
                            'voc': {'αμφότερες'}},
                    'masc': {'acc': {'αμφοτέρους', 'αμφότερους'},
                             'gen': {'αμφοτέρων', 'αμφότερων'},
                             'nom': {'αμφότεροι'},
                             'voc': {'αμφότεροι'}},
                    'neut': {'acc': {'αμφότερα'},
                             'gen': {'αμφοτέρων', 'αμφότερων'},
                             'nom': {'αμφότερα'},
                             'voc': {'αμφότερα'}}}}

        )

    def test_pron_ego(self):
        self.assertDictEqual(
            pronoun.create_all('εγώ'),
            {'sg': {'nd': {'gen': {'εμένα', 'εμού'}, 'acc': {'εμένα', 'μένα'}, 'nom': {'εγώ'}}},
             'pl': {'nd': {'gen': {'εμάς', 'ημών'}, 'acc': {'εμάς', 'μας', 'ημάς'}, 'nom': {'εμείς', 'ημείς'}}}}
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
            {'pl': {'fem': {'acc': {'οποιεσδήποτε'},
                            'gen': {'οποιωνδήποτε'},
                            'nom': {'οποιεσδήποτε'},
                            'voc': {'οποιεσδήποτε'}},
                    'masc': {'acc': {'οποιουσδήποτε'},
                             'gen': {'οποιωνδήποτε'},
                             'nom': {'οποιοιδήποτε'},
                             'voc': {'οποιοιδήποτε'}},
                    'neut': {'acc': {'οποιαδήποτε'},
                             'gen': {'οποιωνδήποτε'},
                             'nom': {'οποιαδήποτε'},
                             'voc': {'οποιαδήποτε'}}},
             'sg': {'fem': {'acc': {'οποιαδήποτε'},
                            'gen': {'οποιασδήποτε'},
                            'nom': {'οποιαδήποτε'},
                            'voc': {'οποιαδήποτε'}},
                    'masc': {'acc': {'οποιοδήποτε'},
                             'gen': {'οποιουδήποτε'},
                             'nom': {'οποιοσδήποτε'},
                             'voc': {'οποιεδήποτε'}},
                    'neut': {'acc': {'οποιοδήποτε'},
                             'gen': {'οποιουδήποτε'},
                             'nom': {'οποιοδήποτε'},
                             'voc': {'οποιοδήποτε'}}}}
        )

    def test_pron_enas(self):
        self.assertDictEqual(
            pronoun.create_all('ένας'),
            {'sg': {'fem': {'acc': {'μίαν', 'μιαν', 'μία', 'μια'},
                            'gen': {'μίας', 'μιας'},
                            'nom': {'μια', 'μία'}},
                    'masc': {'acc': {'έναν', 'ένα'},
                             'gen': {'ενός'},
                             'nom': {'ένας', 'είς'}},
                    'neut': {'acc': {'ένα'}, 'gen': {'ενός'}, 'nom': {'ένα'}}}}

        )

    def test_pron_kaneis(self):
        self.assertDictEqual(
            pronoun.create_all('κανένας'),
            {'sg': {'fem': {'acc': {'καμία', 'καμιάν', 'καμιά'},
                            'gen': {'καμιάς', 'καμίας'},
                            'nom': {'καμία', 'καμιά'}},
                    'masc': {'acc': {'κανένα', 'κανέναν'},
                             'gen': {'κανενός'},
                             'nom': {'κάνας', 'κανένας', 'κανείς'}},
                    'neut': {'acc': {'κανένα'}, 'gen': {'κανενός'}, 'nom': {'κανένα'}}}}

        )

    def test_pron_idios(self):
        self.maxDiff = None
        self.assertDictEqual(
            pronoun.create_all('ίδιος'),
            {'pl': {'fem': {'acc': {'ίδιες'},
                            'gen': {'ίδιων', 'ιδίων'},
                            'nom': {'ίδιες'},
                            'voc': {'ίδιες'}},
                    'masc': {'acc': {'ίδιους', 'ιδίους'},
                             'gen': {'ίδιων', 'ιδίων'},
                             'nom': {'ίδιοι'},
                             'voc': {'ίδιοι'}},
                    'neut': {'acc': {'ίδια'},
                             'gen': {'ίδιων', 'ιδίων'},
                             'nom': {'ίδια'},
                             'voc': {'ίδια'}}},
             'sg': {'fem': {'acc': {'ίδια', 'ιδίαν'},
                            'gen': {'ιδίας', 'ίδιας'},
                            'nom': {'ιδία', 'ίδια'},
                            'voc': {'ίδια', 'ιδία'}},
                    'masc': {'acc': {'ίδιο', 'ίδιον'},
                             'gen': {'ίδιου', 'ιδίου'},
                             'nom': {'ίδιος'},
                             'voc': {'ίδιε'}},
                    'neut': {'acc': {'ίδιο'},
                             'gen': {'ίδιου', 'ιδίου'},
                             'nom': {'ίδιο'},
                             'voc': {'ίδιο'}}}},

        )

    def test_pron_eautos(self):
        self.assertDictEqual(
            pronoun.create_all('εαυτός'),
            {'pl': {'masc': {'acc': {'εαυτούς'},
                             'gen': {'εαυτών'},
                             'nom': {'εαυτοί'},
                             'voc': {'εαυτοί'}}},
             'sg': {'masc': {'acc': {'εαυτό', 'εαυτόν'},
                             'gen': {'εαυτού'},
                             'nom': {'εαυτός'},
                             'voc': {'εαυτέ'}}}}

        )

    def test_pron_tis(self):
        self.assertDictEqual(
            pronoun.create_all('τις'),
            {'sg':
                 {'masc': {'acc': {'τίνα'}, 'gen': {'τίνος'}, 'nom': {'τις'}},
                  'fem': {'acc': {'τίνα'}, 'gen': {'τίνος'}, 'nom': {'τις'}},
                  'neut': {'acc': {'τι'}, 'gen': {'τίνος'}, 'nom': {'τι'}}},
             'pl': {'masc': {'acc': {'τίνας'}, 'gen': {'τίνων'}, 'nom': {'τίνες'}},
                    'fem': {'acc': {'τίνας'}, 'gen': {'τίνων'}, 'nom': {'τίνες'}},
                    'neut': {'acc': {'τίνα'}, 'gen': {'τίνων'}, 'nom': {'τίνα'}}}},

        )

    def test_pron_katheti(self):
        self.assertDictEqual(
            pronoun.create_all('καθετί'),
            {'sg': {'neut': {'acc': {'καθετί'}, 'nom': {'καθετί'}}}}

        )

    def test_pron_pou(self):
        self.assertDictEqual(
            pronoun.create_all('που'),
            {'pl': {'fem': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}},
                    'masc': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}},
                    'neut': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}}},
             'sg': {'fem': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}},
                    'masc': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}},
                    'neut': {'acc': {'που'}, 'gen': {'που'}, 'nom': {'που'}, 'voc': {''}}}}

        )

    def test_pron_pote(self):
        self.assertDictEqual(
            pronoun.create_all('πότε'),
            {
                'nd': {'nd': {'nd': {'πότε'}}}

            }
        )
