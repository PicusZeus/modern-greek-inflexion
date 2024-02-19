from unittest import TestCase

from icecream import ic

from modern_greek_inflexion import verb
from modern_greek_inflexion.resources import PARATATIKOS, ACTIVE, IND, PASSIVE, ACTIVE_AORIST_PARTICIPLE


def active_aorist_participle(v):
    return verb.Verb(v).create_participles()[ACTIVE_AORIST_PARTICIPLE]


def parat_pass(v):
    return verb.Verb(v).create_imperfect_forms()[PARATATIKOS][PASSIVE][IND]


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