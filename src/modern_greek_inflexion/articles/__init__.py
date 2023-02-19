"""
simply a list
"""
from modern_greek_accentuation.accentuation import convert_to_monotonic
from ..resources import SG, PL, FEM, MASC, NEUT, NOM, ACC, GEN

definite_article = {
    SG: {
        MASC: {
            NOM: {'ο'},
            ACC: {'τον', 'το'},
            GEN: {'του'}
        },
        FEM: {
            NOM: {'η'},
            ACC: {'την', 'τη'},
            GEN: {'της'}
        },
        NEUT: {
            NOM: {'το'},
            ACC: {'του'},
            GEN: {'το'}
        }
    },
    PL: {
        MASC: {
            NOM: {'οι'},
            ACC: {'τους'},
            GEN: {'των'}
        },
        FEM: {
            NOM: {'οι', 'αι'},
            ACC: {'τις', 'τας'},
            GEN: {'των'}
        },
        NEUT: {
            NOM: {'τα'},
            ACC: {'τα'},
            GEN: {'των'}
        }
    }
}


indefinite_article = {
    SG: {
        MASC: {
            NOM: {'ένας'},
            ACC: {'ένα', 'έναν'},
            GEN: {'ενός'}
        },
        FEM: {
            NOM: {'μια', 'μία'},
            ACC: {'μια', 'μία', 'μιαν', 'μίαν'},
            GEN: {'μιας', 'μίας'}
        },
        NEUT: {
            NOM: {'ένα'},
            ACC: {'ένα'},
            GEN: {'ενός'}
        }
    }
}


def create_all(article):
    article = convert_to_monotonic(article)
    if article not in ['ο', 'ένας']:
        raise Exception("it's not a Greek article")
    """
    So that API is consistent
    :param article: o or enas
    :return:
    """
    if article == 'ο':
        return definite_article
    elif article == 'ένας':
        return indefinite_article