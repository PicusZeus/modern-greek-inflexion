from unittest import TestCase


from modern_greek_inflexion import Verb
from modern_greek_inflexion.resources import ACTIVE_AORIST_PARTICIPLE


def active_aorist_participle(v):
    return Verb(v).create_participles()[ACTIVE_AORIST_PARTICIPLE]


class VerbParticiples(TestCase):
    def test_embainw(self):
        self.assertDictEqual(
            active_aorist_participle('εμβαίνω'),
            {'pl': {'fem': {'acc': {'εμβάσες'},
                            'gen': {'εμβασών'},
                            'nom': {'εμβάσες'},
                            'voc': {'εμβάσες'}},
                    'masc': {'acc': {'εμβάντες'},
                             'gen': {'εμβάντων'},
                             'nom': {'εμβάντες'},
                             'voc': {'εμβάντες'}},
                    'neut': {'acc': {'εμβάντα'},
                             'gen': {'εμβάντων'},
                             'nom': {'εμβάντα'},
                             'voc': {'εμβάντα'}}},
             'sg': {'fem': {'acc': {'εμβάσα'},
                            'gen': {'εμβάσας'},
                            'nom': {'εμβάσα'},
                            'voc': {'εμβάσα'}},
                    'masc': {'acc': {'εμβάντα'},
                             'gen': {'εμβάντος'},
                             'nom': {'εμβάς'},
                             'voc': {'εμβάς'}},
                    'neut': {'acc': {'εμβάν'},
                             'gen': {'εμβάντος'},
                             'nom': {'εμβάν'},
                             'voc': {'εμβάν'}}}},

        )