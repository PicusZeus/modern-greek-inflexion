"""
simply a list
"""
from modern_greek_accentuation.accentuation import convert_to_monotonic

definite_article = {
    'sg': {
        'masc': {
            'nom': {'ο'},
            'acc': {'τον', 'το'},
            'gen': {'του'}
        },
        'fem': {
            'nom': {'η'},
            'acc': {'την', 'τη'},
            'gen': {'της'}
        },
        'neut': {
            'nom': {'το'},
            'acc': {'του'},
            'gen': {'το'}
        }
    },
    'pl': {
        'masc': {
            'nom': {'οι'},
            'acc': {'τους'},
            'gen': {'των'}
        },
        'fem': {
            'nom': {'οι', 'αι'},
            'acc': {'τις', 'τας'},
            'gen': {'των'}
        },
        'neut': {
            'nom': {'τα'},
            'acc': {'τα'},
            'gen': {'των'}
        }
    }
}


indefinite_article = {
    'sg': {
        'masc': {
            'nom': {'ένας'},
            'acc': {'ένα', 'έναν'},
            'gen': {'ενός'}
        },
        'fem': {
            'nom': {'μια', 'μία'},
            'acc': {'μια', 'μία', 'μιαν', 'μίαν'},
            'gen': {'μιας', 'μίας'}
        },
        'neut': {
            'nom': {'ένα'},
            'acc': {'ένα'},
            'gen': {'ενός'}
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