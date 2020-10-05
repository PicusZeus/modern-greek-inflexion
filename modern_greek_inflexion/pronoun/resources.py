
nd = 'nd'
fem = 'fem'
masc = 'masc'
neut = 'neut'

nom = 'nom'
gen = 'gen'
acc = 'acc'
voc = 'voc'



EGO_STRONG = {
    nd: {
    'sg': {
        nom: 'εγώ',
        gen: 'εμένα',
        acc: 'εμένα,μένα',
    },
    'pl': {
        nom: 'εμείς',
        gen: 'εμάς,ημών',
        acc: 'εμάς,μας',
    }
    }
}

EGO_WEAK = {
    nd: {
    'sg': {
        nom: '',
        gen: 'μου',
        acc: 'με',
    },
    'pl': {
        nom: '',
        gen: 'μας',
        acc: 'μας',
    }
    }

}

ESU_STRONG = {
    nd: {
    'sg': {
        nom: 'εσύ',
        gen: 'εσένα',
        acc: 'εσένα,σένα',
    },
    'pl': {
        nom: 'εσείς',
        gen: 'εσάς,υμών',
        acc: 'εσάς',
    }
    }
}

ESU_WEAK = {
    nd: {
    'sg': {
        nom: '',
        gen: 'σου',
        acc: 'σε',
    },
    'pl': {
        nom: '',
        gen: 'σας',
        acc: 'σας',
    }
    }
}

AUTOS_STRONG = {
    masc: {
        'sg': {
            nom: 'αυτός',
            gen: 'αυτού',
            acc: 'αυτόν,αυτό',
        },
        'pl': {
            nom: 'αυτοί',
            gen: 'αυτών',
            acc: 'αυτούς',
        }
    },
    fem: {
        'sg': {
            nom: 'αυτή',
            gen: 'αυτής',
            acc: 'αυτήν,αυτή',
        },
        'pl': {
            nom: 'αυτές',
            gen: 'αυτών',
            acc: 'αυτές,αυτάς',
        }
    },
    neut: {
        'sg': {
            nom: 'αυτό',
            gen: 'αυτού',
            acc: 'αυτό',
        },
        'pl': {
            nom: 'αυτά',
            gen: 'αυτών',
            acc: 'αυτά',
        }
    }

}

AUTOS_WEAK = {
    masc: {
        'sg': {
            nom: 'τος',
            gen: 'του',
            acc: 'τον',
        },
        'pl': {
            nom: 'τοι',
            gen: 'τους',
            acc: 'τους',
        }
    },
    fem: {
        'sg': {
            nom: 'τη',
            gen: 'της',
            acc: 'την,τη',
        },
        'pl': {
            nom: 'τες',
            gen: 'τους',
            acc: 'τις,τες',
        }
    },
    neut: {
        'sg': {
            nom: 'το',
            gen: 'του',
            acc: 'το',
        },
        'pl': {
            nom: 'τα',
            gen: 'τους',
            acc: 'τα',
        }
    }
}


TIS = {
    masc: {
        'sg': {
            nom: 'τις',
            gen: 'τίνος',
            acc: 'τίνα',
        },
        'pl': {
            nom: 'τίνες',
            gen: 'τίνων',
            acc: 'τίνας',
        }
    },
    fem: {
        'sg': {
            nom: 'τις',
            gen: 'τίνος',
            acc: 'τίνα',
        },
        'pl': {
            nom: 'τίνες',
            gen: 'τίνων',
            acc: 'τίνας',
        }
    },
    neut: {
        'sg': {
            nom: 'τι',
            gen: 'τίνος',
            acc: 'τι',
        },
        'pl': {
            nom: 'τίνα',
            gen: 'τίνων',
            acc: 'τίνα',
        }
    }
}