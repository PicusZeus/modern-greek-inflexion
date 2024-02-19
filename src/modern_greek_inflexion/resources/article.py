from modern_greek_inflexion.resources import MASC, NOM, ACC, GEN, FEM, NEUT, SG, PL

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