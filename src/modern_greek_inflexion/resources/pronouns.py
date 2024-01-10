from .variables import *


EAUTO = {
    SG: {GEN: 'εαυτού',
         ACC: 'εαυτόν'},
    PL: {
        GEN: 'εαυτών',
        ACC: 'εαυτούς'
    }
}

OSPER = {
    SG: {
        MASC: {
            NOM: 'όσπερ',
            GEN: 'ούπερ',
            ACC: 'όνπερ',
        },
        FEM: {
            NOM: 'ήπερ',
            GEN: 'ήσπερ',
            ACC: 'ήνπερ',
        },
        NEUT: {
            NOM: 'όπερ',
            GEN: 'ούπερ',
            ACC: 'όπερ',
        }},
    PL: {
        MASC: {
            NOM: 'οίπερ',
            GEN: 'ώνπερ',
            ACC: 'ούσπερ',
        },
        FEM: {
            NOM: 'αίπερ',
            GEN: 'ώνπερ',
            ACC: 'άσπερ'
        },
        NEUT: {
            NOM: 'άπερ',
            GEN: 'ώνπερ',
            ACC: 'άπερ'
        }
    }
}


OSTIS = {

    SG: {
        MASC: {
            NOM: 'όστις',
            GEN: 'ούτινος,ότου',
            ACC: 'όντινα',
        },
        FEM: {
            NOM: 'ήτις',
            GEN: 'ήστινος',
            ACC: 'ήντίνα',
        },
        NEUT: {
            NOM: 'ότι',
            GEN: 'ούτινος,ότου',
            ACC: 'ότι',
        }},
    PL: {
        MASC: {
            NOM: 'οίτινες',
            GEN: 'ώντινων',
            ACC: 'ούστινας',
        },
        FEM: {
            NOM: 'αίτινες',
            GEN: 'ώντινων',
            ACC: 'άστινας'
        },
        NEUT: {
            NOM: 'άτινα,άττα',
            GEN: 'ώντινων',
            ACC: 'άτινα,άττα'
        }
    }
}


TIS = {

    SG: {
        MASC: {
            NOM: 'τις',
            GEN: 'τίνος',
            ACC: 'τίνα',
        },
        FEM: {
            NOM: 'τις',
            GEN: 'τίνος',
            ACC: 'τίνα',
        },
        NEUT: {
            NOM: 'τι',
            GEN: 'τίνος',
            ACC: 'τι',
        }},
    PL: {
        MASC: {
            NOM: 'τίνες',
            GEN: 'τίνων',
            ACC: 'τίνας',
        },
        FEM: {
            NOM: 'τίνες',
            GEN: 'τίνων',
            ACC: 'τίνας'
        },
        NEUT: {
            NOM: 'τίνα',
            GEN: 'τίνων',
            ACC: 'τίνα'
        }
    }
}

AUTOS_WEAK = {
    SG: {
        MASC: {
            NOM: 'τος',
            GEN: 'του',
            ACC: 'τον',
        },
        FEM: {
            NOM: 'τη',
            GEN: 'της',
            ACC: 'την,τη',
        },
        NEUT: {
            NOM: 'το',
            GEN: 'του',
            ACC: 'το',
        }},
    PL: {MASC: {
        NOM: 'τοι',
        GEN: 'τους',
        ACC: 'τους',
    },
        FEM: {
            NOM: 'τες',
            GEN: 'τους',
            ACC: 'τες,τις',
        },
        NEUT: {
            NOM: 'τα',
            GEN: 'τους',
            ACC: 'τα',
        }
    }
}

AUTOS_STRONG = {

    SG: {
        MASC: {
            NOM: 'αυτός',
            GEN: 'αυτού',
            ACC: 'αυτόν,αυτό',
        },
        FEM: {
            NOM: 'αυτή',
            GEN: 'αυτής',
            ACC: 'αυτήν,αυτή',
        },
        NEUT: {
            NOM: 'αυτό',
            GEN: 'αυτού',
            ACC: 'αυτό',
        }},
    PL: {MASC: {
        NOM: 'αυτοί',
        GEN: 'αυτών',
        ACC: 'αυτούς',
    },
        FEM: {
            NOM: 'αυτές',
            GEN: 'αυτών',
            ACC: 'αυτές,αυτάς',
        },
        NEUT: {
            NOM: 'αυτά',
            GEN: 'αυτών',
            ACC: 'αυτά',
        }
    }
}

ESU_WEAK = {

    SG: {ND: {
        NOM: '',
        GEN: 'σου',
        ACC: 'σε',
    }},
    PL: {ND: {
        NOM: '',
        GEN: 'σας',
        ACC: 'σας',
    }
    }
}

ESU_STRONG = {

    SG: {
        ND: {
            NOM: 'εσύ',
            GEN: 'εσένα',
            ACC: 'εσένα,σένα',
        }},
    PL:
        {ND: {
            NOM: 'εσείς',
            GEN: 'εσάς,υμών',
            ACC: 'εσάς',
        }
        }
}

EGO_STRONG = {
    SG:
        {ND: {
            NOM: 'εγώ',
            GEN: 'εμένα',
            ACC: 'εμένα,μένα',
        }
        },
    PL:
        {ND: {
            NOM: 'εμείς',
            GEN: 'εμάς,ημών',
            ACC: 'εμάς,μας',
        }
        }
}

EGO_WEAK = {

    SG: {
        ND: {
            NOM: '',
            GEN: 'μου',
            ACC: 'με',
        }},
    PL: {
        ND: {
            NOM: '',
            GEN: 'μας',
            ACC: 'μας',
        }
    }

}