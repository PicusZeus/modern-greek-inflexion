
nd = 'nd'
fem = 'fem'
masc = 'masc'
neut = 'neut'

nom = 'nom'
gen = 'gen'
acc = 'acc'
voc = 'voc'



EGO_STRONG = {
    'sg':
        {nd: {
            nom: 'εγώ',
            gen: 'εμένα',
            acc: 'εμένα,μένα',
            }
        },
    'pl':
        {nd: {
            nom: 'εμείς',
            gen: 'εμάς,ημών',
            acc: 'εμάς,μας',
            }
        }
}

EGO_WEAK = {

    'sg': {
        nd: {
            nom: '',
            gen: 'μου',
            acc: 'με',
            }},
    'pl': {
        nd: {
            nom: '',
            gen: 'μας',
            acc: 'μας',
            }
        }


}

ESU_STRONG = {

    'sg': {
        nd: {
        nom: 'εσύ',
        gen: 'εσένα',
        acc: 'εσένα,σένα',
    }},
    'pl':
        {nd: {
        nom: 'εσείς',
        gen: 'εσάς,υμών',
        acc: 'εσάς',
    }
    }
}

ESU_WEAK = {

    'sg': {  nd: {
        nom: '',
        gen: 'σου',
        acc: 'σε',
    }},
    'pl': {nd: {
        nom: '',
        gen: 'σας',
        acc: 'σας',
    }
    }
}

AUTOS_STRONG = {

        'sg': {
            masc: {
                nom: 'αυτός',
                gen: 'αυτού',
                acc: 'αυτόν,αυτό',
                },
            fem: {
                nom: 'αυτή',
                gen: 'αυτής',
                acc: 'αυτήν,αυτή',
                },
            neut: {
                nom: 'αυτό',
                gen: 'αυτού',
                acc: 'αυτό',
                }},
        'pl': {masc: {
                nom: 'αυτοί',
                gen: 'αυτών',
                acc: 'αυτούς',
                    },
                fem: {
                    nom: 'αυτές',
                    gen: 'αυτών',
                    acc: 'αυτές,αυτάς',
                    },
                neut: {
                    nom: 'αυτά',
                    gen: 'αυτών',
                    acc: 'αυτά',
                    }
        }
        }

AUTOS_WEAK = {
    'sg': {
        masc: {
            nom: 'τος',
            gen: 'του',
            acc: 'τον',
        },
        fem: {
            nom: 'τη',
            gen: 'της',
            acc: 'την,τη',
        },
        neut: {
            nom: 'το',
            gen: 'του',
            acc: 'το',
        }},
    'pl': {masc: {
        nom: 'τοι',
        gen: 'τους',
        acc: 'τους',
    },
        fem: {
            nom: 'τες',
            gen: 'τους',
            acc: 'τες,τις',
        },
        neut: {
            nom: 'τα',
            gen: 'τους',
            acc: 'τα',
        }
    }
}


TIS = {

        'sg': {
            masc: {
                nom: 'τις',
                gen: 'τίνος',
                acc: 'τίνα',
            },
            fem: {
                nom: 'τις',
                gen: 'τίνος',
                acc: 'τίνα',
            },
            neut: {
                nom: 'τι',
                gen: 'τίνος',
                acc: 'τι',
            }},
        'pl': {
            masc: {
                nom: 'τίνες',
                gen: 'τίνων',
                acc: 'τίνας',
            },
            fem: {
                nom: 'τίνες',
                gen: 'τίνων',
                acc: 'τίνας'
            },
            neut: {
                nom: 'τίνα',
                gen: 'τίνων',
                acc: 'τίνα'
            }
        }
        }
