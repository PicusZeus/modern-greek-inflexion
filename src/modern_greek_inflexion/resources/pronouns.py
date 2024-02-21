from .variables import *

EAUTO = {
    SG: {GEN: {'εαυτού'},
         ACC: {'εαυτόν'}},
    PL: {
        GEN: {'εαυτών'},
        ACC: {'εαυτούς'}
    }
}

OSPER = {
    SG: {
        MASC: {
            NOM: {'όσπερ'},
            GEN: {'ούπερ'},
            ACC: {'όνπερ'},
        },
        FEM: {
            NOM: {'ήπερ'},
            GEN: {'ήσπερ'},
            ACC: {'ήνπερ'},
        },
        NEUT: {
            NOM: {'όπερ'},
            GEN: {'ούπερ'},
            ACC: {'όπερ'},
        }},
    PL: {
        MASC: {
            NOM: {'οίπερ'},
            GEN: {'ώνπερ'},
            ACC: {'ούσπερ'},
        },
        FEM: {
            NOM: {'αίπερ'},
            GEN: {'ώνπερ'},
            ACC: {'άσπερ'}
        },
        NEUT: {
            NOM: {'άπερ'},
            GEN: {'ώνπερ'},
            ACC: {'άπερ'}
        }
    }
}

OSTIS = {

    SG: {
        MASC: {
            NOM: {'όστις'},
            GEN: {'ούτινος', 'ότου'},
            ACC: {'όντινα'},
        },
        FEM: {
            NOM: {'ήτις'},
            GEN: {'ήστινος'},
            ACC: {'ήντίνα'},
        },
        NEUT: {
            NOM: {'ότι'},
            GEN: {'ούτινος', 'ότου'},
            ACC: {'ότι'},
        }},
    PL: {
        MASC: {
            NOM: {'οίτινες'},
            GEN: {'ώντινων'},
            ACC: {'ούστινας'},
        },
        FEM: {
            NOM: {'αίτινες'},
            GEN: {'ώντινων'},
            ACC: {'άστινας'}
        },
        NEUT: {
            NOM: {'άτινα', 'άττα'},
            GEN: {'ώντινων'},
            ACC: {'άτινα', 'άττα'}
        }
    }
}

TIS = {

    SG: {
        MASC: {
            NOM: {'τις'},
            GEN: {'τίνος'},
            ACC: {'τίνα'},
        },
        FEM: {
            NOM: {'τις'},
            GEN: {'τίνος'},
            ACC: {'τίνα'},
        },
        NEUT: {
            NOM: {'τι'},
            GEN: {'τίνος'},
            ACC: {'τι'},
        }},
    PL: {
        MASC: {
            NOM: {'τίνες'},
            GEN: {'τίνων'},
            ACC: {'τίνας'},
        },
        FEM: {
            NOM: {'τίνες'},
            GEN: {'τίνων'},
            ACC: {'τίνας'}
        },
        NEUT: {
            NOM: {'τίνα'},
            GEN: {'τίνων'},
            ACC: {'τίνα'}
        }
    }
}

AUTOS_WEAK = {
    SG: {
        MASC: {
            NOM: {'τος'},
            GEN: {'του'},
            ACC: {'τον'},
        },
        FEM: {
            NOM: {'τη'},
            GEN: {'της'},
            ACC: {'την', 'τη'},
        },
        NEUT: {
            NOM: {'το'},
            GEN: {'του'},
            ACC: {'το'},
        }},
    PL: {MASC: {
        NOM: {'τοι'},
        GEN: {'τους'},
        ACC: {'τους'},
    },
        FEM: {
            NOM: {'τες'},
            GEN: {'τους'},
            ACC: {'τες', 'τις'},
        },
        NEUT: {
            NOM: {'τα'},
            GEN: {'τους'},
            ACC: {'τα'},
        }
    }
}

AUTOS_STRONG = {

    SG: {
        MASC: {
            NOM: {'αυτός'},
            GEN: {'αυτού'},
            ACC: {'αυτόν', 'αυτό'},
        },
        FEM: {
            NOM: {'αυτή'},
            GEN: {'αυτής'},
            ACC: {'αυτήν', 'αυτή'},
        },
        NEUT: {
            NOM: {'αυτό'},
            GEN: {'αυτού'},
            ACC: {'αυτό'},
        }},
    PL: {MASC: {
        NOM: {'αυτοί'},
        GEN: {'αυτών'},
        ACC: {'αυτούς'},
    },
        FEM: {
            NOM: {'αυτές'},
            GEN: {'αυτών'},
            ACC: {'αυτές', 'αυτάς'},
        },
        NEUT: {
            NOM: {'αυτά'},
            GEN: {'αυτών'},
            ACC: {'αυτά'},
        }
    }
}

ESU_WEAK = {

    SG: {ND: {
        NOM: {''},
        GEN: {'σου'},
        ACC: {'σε'},
    }},
    PL: {ND: {
        NOM: {''},
        GEN: {'σας'},
        ACC: {'σας'},
    }
    }
}

ESU_STRONG = {

    SG: {
        ND: {
            NOM: {'εσύ'},
            GEN: {'εσένα'},
            ACC: {'εσένα', 'σένα'},
        }},
    PL:
        {ND: {
            NOM: {'εσείς', 'υμείς'},
            GEN: {'εσάς', 'υμών'},
            ACC: {'εσάς', 'υμάς'},
        }
        }
}

EGO_STRONG = {
    SG:
        {ND: {
            NOM: {'εγώ'},
            GEN: {'εμένα', 'εμού'},
            ACC: {'εμένα', 'μένα'},
        }
        },
    PL:
        {ND: {
            NOM: {'εμείς', 'ημείς'},
            GEN: {'εμάς', 'ημών'},
            ACC: {'εμάς', 'μας', 'ημάς'},
        }
        }
}

EGO_WEAK = {

    SG: {
        ND: {
            NOM: {''},
            GEN: {'μου'},
            ACC: {'με'},
        }},
    PL: {
        ND: {
            NOM: {''},
            GEN: {'μας'},
            ACC: {'μας'},
        }
    }

}


OUTOS = {
    SG: {
        MASC: {
            NOM: {'ούτος'},
            GEN: {'τούτου'},
            ACC: {'τούτον'},
        },
        FEM: {
            NOM: {'αύτη'},
            GEN: {'ταύτης'},
            ACC: {'ταύτην'},
        },
        NEUT: {
            NOM: {'τούτο'},
            GEN: {'τούτου'},
            ACC: {'τούτο'},
        }
    },
    PL: {
        MASC: {
            NOM: {'ούτοι'},
            GEN: {'τούτων'},
            ACC: {'τούτους'},
        },
        FEM: {
            NOM: {'αύται'},
            GEN: {'τούτων'},
            ACC: {'αύτας'},
        },
        NEUT: {
            NOM: {'ταύτα'},
            GEN: {'τούτων'},
            ACC: {'ταύτα'},
        }
    }
}

OS = {
    SG: {
        MASC: {
            NOM: {'ος'},
            GEN: {'ου'},
            ACC: {'ον'},
        },
        FEM: {
            NOM: {'η'},
            GEN: {'ης'},
            ACC: {'ην'},
        },
        NEUT: {
            NOM: {'ο'},
            GEN: {'ου'},
            ACC: {'ο'},
        }
    },
    PL: {
        MASC: {
            NOM: {'οι'},
            GEN: {'ων'},
            ACC: {'ους'},
        },
        FEM: {
            NOM: {'αι'},
            GEN: {'ων'},
            ACC: {'ας'},
        },
        NEUT: {
            NOM: {'α'},
            GEN: {'ων'},
            ACC: {'α'},
        }
    }
}


"""UNUSED"""

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
