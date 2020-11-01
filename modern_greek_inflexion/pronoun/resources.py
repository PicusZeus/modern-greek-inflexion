
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


OSTIS = {

        'sg': {
            masc: {
                nom: 'όστις',
                gen: 'ούτινος,ότου',
                acc: 'όντινα',
            },
            fem: {
                nom: 'ήτις',
                gen: 'ήστινος',
                acc: 'ήντίνα',
            },
            neut: {
                nom: 'ότι',
                gen: 'ούτινος,ότου',
                acc: 'ότι',
            }},
        'pl': {
            masc: {
                nom: 'οίτινες',
                gen: 'ώντινων',
                acc: 'ούστινας',
            },
            fem: {
                nom: 'αίτινες',
                gen: 'ώντινων',
                acc: 'άστινας'
            },
            neut: {
                nom: 'άτινα,άττα',
                gen: 'ώντινων',
                acc: 'άτινα,άττα'
            }
        }
        }

OSPER ={

        'sg': {
            masc: {
                nom: 'όσπερ',
                gen: 'ούπερ',
                acc: 'όνπερ',
            },
            fem: {
                nom: 'ήπερ',
                gen: 'ήσπερ',
                acc: 'ήνπερ',
            },
            neut: {
                nom: 'όπερ',
                gen: 'ούπερ',
                acc: 'όπερ',
            }},
        'pl': {
            masc: {
                nom: 'οίπερ',
                gen: 'ώνπερ',
                acc: 'ούσπερ',
            },
            fem: {
                nom: 'αίπερ',
                gen: 'ώνπερ',
                acc: 'άσπερ'
            },
            neut: {
                nom: 'άπερ',
                gen: 'ώνπερ',
                acc: 'άπερ'
            }
        }
        }


eauto = {
    'sg': {'gen': 'εαυτού',
           'acc': 'εαυτόν'},
    'pl': {
     'gen': 'εαυτών',
     'acc': 'εαυτούς'
    }
}


greek_pers_pronouns = [

    ['εγώ', ['εγώ', 'ppron12:sg:nom:m.f.n:pri:akc']],
    ['μου', ['εγώ', 'ppron12:sg:gen:m.f.n:pri:nakc:npraep']],
    ['εμένα', ['εγώ', 'ppron12:sg:gen.acc:m.f.n:pri:akc:npraep']],
    ['μένα', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:akc:praep']],
    ['με', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:nakc:npraep']],
    ['εμείς', ['εμείς', 'ppron12:pl:nom:m.f.n:pri:akc']],
    ['εμάς', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:npraep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:praep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:nakc:npraep']],

    ['εσύ', ['εσύ', 'ppron12:sg:nom:m.f.n:sec:akc']],
    ['σου', ['εσύ', 'ppron12:sg:gen:m.f.n:sec:nakc:npraep']],
    ['εσένα', ['εσύ', 'ppron12:sg:gen.acc:m.f.n:sec:akc:npraep']],
    ['σένα', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:akc:praep']],
    ['σε', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:nakc:npraep']],

    ['εσείς', ['εσείς', 'ppron12:pl:nom:m.f.n:sec:akc']],
    ['εσάς', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:akc:npraep']],

    ['σας', ['εσείς', 'ppron12:pl:acc:m.f.n:sec:akc:praep']],

    ['σας', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:nakc:npraep']],

    # nom
    ['αυτός', ['αυτός', 'ppron3:sg:nom:m:ter:akc']],
    ['τoς', ['αυτός', 'ppron3:sg:nom:m:ter:nakc']],
    ['το', ['αυτός', 'ppron3:sg:nom.acc:n:ter:nakc:npraep']],
    ['αυτό', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc']],
    ['αυτή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:akc']],
    ['τή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:nakc']],
    # gen
    ['αυτού', ['αυτός', 'ppron3:pl:gen:n.m:ter:akc:praep:npraep']],
    ['του', ['αυτός', 'ppron3:sg:gen:n.m:ter:nakc:npraep']],

    ['αυτής', ['αυτός', 'ppron3:sg:gen:f:ter:akc']],
    ['της', ['αυτός', 'ppron3:sg:gen:f:ter:nakc:npraep']],
    # acc
    ['αυτόν', ['αυτός', 'ppron3:sg:acc:m:ter:akc:npraep:praep']],
    ['αυτήν', ['αυτός', 'ppron3:sg:acc:f:ter:akc']],
    ['τήν', ['αυτός', 'ppron3:sg:acc:f:ter:nakc:npraep']],
    ['τον', ['αυτός', 'ppron3:sg:gen:n:ter:nakc:npraep']],

    # nom
    ['αυτοί', ['αυτός', 'ppron3:pl:nom:m:ter:akc']],
    ['αυτές', ['αυτός', 'ppron3:pl:nom.acc:f:ter:akc']],
    ['τοι', ['αυτός', 'ppron3:pl:nom:m:ter:nakc']],
    ['τες', ['αυτός', 'ppron3:pl:nom:f:ter:nakc']],
    ['τα', ['αυτός', 'ppron3:pl:nom.acc:n:ter:nakc:npraep']],
    ['αυτά', ['αυτός', 'ppron3:pl:nom.acc:n:ter:akc']],

    # gen
    ['αυτών', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:akc']],
    ['τους', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:nakc:npraep']],

    # acc
    ['τους', ['αυτός', 'ppron3:pl:acc:m:ter:nakc:npraep']],
    ['αυτούς', ['αυτός', 'ppron3:pl:acc:m:ter:akc']],
    ['τις', ['αυτός', 'ppron3:pl:acc:f:ter:nakc:npraep']],
    ['τες', ['αυτός', 'ppron3:pl:acc:f:ter:nakc:npraep']],

]
