import pickle
import os

this_dir, this_filename = os.path.split(__file__)
data_path = os.path.join(this_dir, 'el_GR.pickle')

greek_corpus = pickle.load(open(data_path, 'rb'))

# numb
SG = 'sg'
PL = 'pl'

# cases
NOM = 'nom'
GEN = 'gen'
ACC = 'acc'
VOC = 'voc'
MASC = 'masc'
FEM = 'fem'
NEUT = 'neut'

# genders
MASC_FEM = 'masc,fem'
ND = 'nd'
PRI = 'pri'
SEC = 'sec'
TER = 'ter'

# voice

ACTIVE = 'active'
PASSIVE = 'passive'
DEPONENS = 'deponens'
# tenses

AORIST = 'aorist'
PRESENT = 'present'
PARATATIKOS = 'paratatikos'
FIN = 'fin'
PAST = 'past'
# mood

IMP = 'imp'
CONJUNCTIVE = 'conjunctive'
IND = 'ind'
MODAL = 'modal'

# accents
ULTIMATE = 'ultimate'
PENULTIMATE = 'penultimate'
ANTEPENULTIMATE = 'antepenultimate'

# var
GENDER = 'gender'
CONJUGATION_IND = 'conjugation_ind'
CONJUGATION_IMP = 'conjugation_imp'
ROOT = 'root'
IMPER = 'imper'

# POS
ADJ = 'adj'
COMP = 'comp'
COMP_ADV = 'comp_adv'
ADVERB = 'adverb'
ADV = 'adv'
SUPERL = 'superl'
SUPERL_ADV = 'superl_adv'
COMPARATIVE = 'comparative'
ADVERB_COMPARATIVE = 'adverb_comparative'
# aspect

PERF = 'perf'
IMPERF = 'imperf'

# genders
NOM_PL = 'nom_pl'
GEN_SG = 'gen_sg'
NOM_SG = 'nom_sg'
FEM_PL = 'fem_pl'
MASC_PL = 'masc_pl'
NEUT_PL = 'neut_pl'
FEM_SG = 'fem_sg'
MASC_SG = 'masc_sg'
NEUT_SG = 'neut_sg'
ONLY_SG = 'only_sg'

forms_with_alternatives = ('ακόμη', 'ακόμα', 'και', 'κι', 'τίποτα', 'τίποτε')
dictionary_with_alt = {'ακόμη': 'ακόμα', 'και': 'κι', 'τίποτα': 'τίποτε'}

irregular_comparatives = {'καλό': 'καλύτερος/άριστος',
                          'κακό': 'χειρότερος,ήσσων/χείριστος,ήκιστος',
                          'απλό': 'απλούστερος/απλούστατος',
                          'μεγάλο': 'μεγαλύτερος/μέγιστος',
                          'πολύ': 'περισσότερος/-',
                          'λίγο': 'λιγότερος/ελάχιστος',
                          'μέγα': 'μεγαλύτερος/μέγιστος',
                          'πρώτο': 'πρωτύτερος/πρώτιστος',
                          'ταχύ': 'ταχύτερος/ταχύτατος,τάχιστος'}

irregular_comparative_adverbs = {'κακό': 'χειρότερα,ήσσον,ήττον/κάκιστα,ήκιστα',
                                 'καλό': 'καλύτερα,κάλλιον,κάλλιο/άριστα',
                                 'λίγο': 'λιγότερο/ελάχιστα', 'πολύ': 'περισσότερο/-'}

irregular_adv = {
    'νωρίς': {COMP_ADV: 'νωρίτερα/'}, 'άνω': {COMP_ADV: 'ανώτερα/ανώτατα', COMP: 'ανώτερος/ανώτατος'},
    'κάτω': {COMP_ADV: 'κατώτερα/κατώτατα', COMP: 'κατώτερος/κατώτατος'}}

adj_basic_template = {SG: {
    MASC: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''
    },
    FEM: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''},
    NEUT: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''}
},
    PL: {
        MASC: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''},
        FEM: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        },
        NEUT: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        }
    }}
"""
these lists are not needed, if you have a correct list of words with such metadata as gender, that can be obtained 
by scraping wikileksiko. Still, even though the lists ara also incomplete, I'll live them here, maybe there will come a need.
"""

feminine_h_eis = ('γύρη', 'κύστη', 'παλισάνδρη', 'πίστη', 'τίγρη', 'πόλη')

feminine_os = ('άμμος', 'οδός', 'διάλεκτος', 'είσοδος', 'έξοδος', 'κάθοδος', 'λεωφόρος',
               'νήσος', 'παράγραφος', 'πρόοδος', 'περίοδος', 'χερσόνησος', 'ψήφος',
               'αεροσυνοδός', 'ακταιωρός', 'ατραπός', 'δοκός', 'επωδός', 'βάλανος', 'θαλαμηγός', 'σποδός', 'λίθος',
               'άβυσσος', 'Aειπάρθενος', 'άκανθος', 'άκατος', 'άλυσος', 'άμπελος', 'άνοδος', 'κιβωτός', 'στενωπός',
               'κόπρος', 'ασβεστοκάμινος', 'άσβεστος', 'άσφαλτος', 'ατμάκατος', 'άτρακτος', 'σιδηροδοκός', 'τροφός',
               'φηγός', 'άμμος', 'άρκτος', 'βάτος', 'Bίβλος', 'βίβλος', 'κανηφόρος', 'κανονιοφόρος', 'νηπιαγωγός',
               'βρεφοδόχος', 'γνάθος', 'δέλτος', 'δρόσος', 'ζωοφόρος', 'ζωφόρος', 'Θεοτόκος', 'πλίνθος', 'Ρόδος',
               'σορός', 'λέμβος', 'λαιμητόμος', 'λέμφος', 'λουτροφόρος', 'νηπιοκόμος', 'νήσος', 'νόσος', 'παρθένος',
               'ράβδος', 'σαρκοφάγος', 'σκευοφόρος', 'τεφροδόχος', 'τριτοτόκος', 'χοηφόρος', 'ψάμμος', 'ψηφοδόχος',
               'ψήφος', 'βάρβιτος', 'βάσανος', 'βενζινάκατος', 'Διακαινήσιμος', 'διάκεντρος', 'διάλεκτος', 'διάμεσος',
               'διάμετρος', 'διέξοδος', 'δικάσιμος', 'δίοδος', 'δωδεκάδελτος', 'εγκύκλιος', 'είσοδος', 'έλαφος',
               'έξοδος',
               'επάνοδος', 'επέτειος', 'έρημος', 'έφοδος', 'ημισέληνος', 'ιερόδουλος', 'κάθετος', 'κάθοδος', 'κάμηλος',
               'κυπάρισσος', 'ημιδιάμετρος', 'ημιπερίοδος', 'ήπειρος', 'ίνδικτος', 'κάμινος', 'κέραμος', 'κλιμακτήριος',
               'λέκιθος', 'λήκυθος', 'μεγαλόνησος', 'μέθοδος', 'μεθόριος', 'μεσόφωνος', 'οκτώηχος', 'οπτόπλινθος',
               'Παμμακάριστος', 'Πανάχραντος', 'πανσέληνος', 'παράγραφος', 'παράγωγος', 'παρακαμπτήριος', 'παράμετρος',
               'πάροδος', 'Πεντάτευχος', 'πεντηκόντορος', 'περίμετρος', 'περίοδος', 'περίπολος', 'πισσάσφαλτος',
               'προβατοκάμηλος', 'πρόοδος', 'πρόσοδος', 'πύελος', 'πυραυλάκατος', 'σεληνάκατος', 'σταφιδάμπελος',
               'στρουθοκάμηλος', 'σύγκλητος', 'σύνοδος', 'τήβεννος', 'τορπιλάκατος', 'ύαλος', 'ύπαιθρος',
               'υπερλεωφόρος', 'υφήλιος', 'υψικάμινος', 'χερσόνησος', 'ωμόπλινθος')

feminine_or_masc = ('καπνοδόχος', 'άργιλος', 'τάφρος', 'κρύσταλλος', 'περιβαλλοντολόγος', 'απόστροφος', 'γιατρός',
                    'μηχανικός', 'ηθοποιός', 'νηπιαγογός', 'δικιγόρος',)


plur_tant_neut = ('Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια', 'Ιωάννινα', 'Γιάννενα', 'Γιάννινα')

aklita_gender = {'μαδιάμ': FEM, 'μωάμεθ': MASC, 'μάνατζερ': MASC, 'σερ': MASC, 'σεφ': MASC,
                 'ντετέκτιβ': MASC, 'ντεντέκτιβ': MASC, 'ρεπόρτερ': MASC, 'πλαζ': FEM,
                 'σεζόν': FEM, 'σπεσιαλιτέ': FEM, 'ρεσεψιόν': FEM}

irregular_nouns = {'σέβας': {NOM_SG: 'σέβας', NOM_PL: 'σέβη', GEN_SG: '', GENDER: NEUT},
                   'σέλας': {NOM_SG: 'σέλας', NOM_PL: 'σέλατα,σέλαα', GEN_SG: 'σέλατος,σέλαος', GENDER: NEUT},
                   'δείλι': {NOM_SG: 'δείλι', NOM_PL: '', GEN_SG: '', GENDER: NEUT},
                   'Πάσχα': {NOM_SG: 'Πάσχα', NOM_PL: '', GEN_SG: '', GENDER: NEUT},
                   'δόρυ': {NOM_SG: 'δόρυ', NOM_PL: 'δόρατα', GEN_SG: 'δόρατος', GENDER: NEUT},
                   'ήμισυ': {NOM_SG: 'ήμισυ', NOM_PL: '', GEN_SG: 'ημίσεος', GENDER: NEUT},
                   'γης': {NOM_SG: 'γης', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDER: FEM},
                   'γη': {NOM_SG: 'γη', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDER: FEM}
                   }

diploklita = {'βράχος': 'βράχοι,βράχια', 'λαιμός': 'λαιμοί,λαιμά',
              'λόγος': 'λόγοι,λόγια', 'πλούτος': ',πλούτη',
              'σανός': ',σανά', 'χρόνος': 'χρόνοι,χρόνια',
              'καπνός': 'καπνοί,καπνά', 'νιότη': ',νιάτα'}

aklita_num_alternatives = {'εφτά': 'επτά', 'οχτώ': 'οκτώ', 'εννιά': 'εννέα', 'δεκαέξι': 'δεκάξι',
                           'δεκαοχτώ': 'δεκαοκτώ', 'δεκαεννιά': 'δεκαεννέα', 'δεκαεφτά': 'δεκαεπτά'}

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

EAUTO = {
    SG: {GEN: 'εαυτού',
         ACC: 'εαυτόν'},
    PL: {
        GEN: 'εαυτών',
        ACC: 'εαυτούς'
    }
}
# these are not all the irregular verbs, but if you take into account compounds, most.

irregular_active_roots = \
    [['βρίθω', None], ['ξέρω', None],
     ['έχω', None],
     ['απέχω', None],
     ['οφείλω', None],
     ['εξέχω', None],
     ['ξέρω', None],
     ['στέκω', None],
     ['χρωστάω', None],
     ['χρωστώ', None],
     ['πρέπει', None],
     ['αξίζω', None],
     ['φρονώ', None],
     ['οπλομαχώ', None],
     ['εποφθαλμιώ', None],
     ['κραδαίνω', None],
     ['αναλογώ', None],
     ['λάμνω', None],
     ['μέλει', None],
     ['θαμπίζω', None],
     ['χάσκω', None],
     ['τυρβάζω', None],
     ['αδημονώ', None],
     ['αμερικανίζω', None],
     ['αδυνατώ', None],
     ['ελλείπω', None],
     ['νεοσσεύω', None],
     ['ρηγνύω', None],
     ['κωλύω', None],
     ['παιδιακίζω', None],
     ['σιαλίζω', None],
     ['προσήκω', None],
     ['χατίζω', None],
     ['ταλασιουργώ', None],
     ['ταυτογνωμώ', None],
     ['αγαθοφέρνω', None],
     ['μέλλει', None],
     ['θεόω', None],
     ['απάδω', None],
     ['ανεβαίν', 'ανέβ,ανεβ'], ['περιμέν', 'περιμέν'], ['πον', 'πονέσ'], ['κατεβαίν', 'κατέβ,κατεβ'], ['αίρ', 'άρ'],
     ['βάλλ', 'βάλ'], ['απολαμβάν', 'απολαύσ'], ['λαμβάν', 'λάβ'], ['γέρν', 'γείρ'],
     ['βάζ', 'βάλ'], ['βγάζ', 'βγάλ'], ['λαβαίν', 'λάβ'], ['αγγέλν', 'αγγείλ'], ['αγγέλλ', 'αγγείλ'],
     ['στάν', 'στήσ'], ['σταίν', 'στήσ'], ['πίπτ', 'πέσ'], ['φέρν', 'φέρ'], ['φεύγ', 'φύγ'], ['άγ', 'αγάγ'],
     ['γέρν', 'γεράσ'], ['πάσχ', 'πάθ'], ['σέρν', 'σύρ'], ['τέμν', 'τμήσ'], ['εφιστ', 'επιστήσ'],
     ['καθιστ', 'καταστήσ'], ['λανθάν', 'λάθ'], ['λαγχάνω', 'λάχ'], ['λαχαίν', 'λάχ'], ['αίρν', 'άρ'], ['αίρ', 'άρ'],
     ['δίν', 'δώσ'], ['δίδ', 'δώσ'], ['μέν', 'μείν'], ['στέλν', 'στείλ'], ['στέλλ', 'στείλ'], ['πλέν', 'πλύν'],
     ['βαίν', 'β'], ['βγαίν', 'βγ'], ['αυξάν', 'αυξήσ'], ['μεθ', 'μεθύσ'], ['σπέρν', 'σπείρ'], ['αλίσκ', 'αλώσ'],
     ['μπαίν', 'μπ'], ['μην', 'μηνύσ'], ['πλέ', 'πλεύσ'], ['πνέ', 'πνεύσ'], ['ρέ', 'ρεύσ'], ['βρίσκ', 'βρ'],
     ['πίν', 'πι'], ['τρώ', 'φά'], ['λέ', 'π'], ['λέγ', 'π,λέξ'], ['τρώγ', 'φάγ'], ['δέρν', 'δείρ'], ['κλίν', 'κλίν'],
     ['κάν', 'κάν'], ['μαθαίν', 'μάθ'], ['παθαίν', 'πάθ'], ['πεθαίν', 'πεθάν'], ['βλέπ', 'δ,ιδ'], ['θνήσκ', 'θάν'],
     ['τείν', 'τείν'], ['πέφτ', 'πέσ'], ['πέπτ', 'πέσ'], ['πηγαίν', 'πά'], ['τυχαίν', 'τύχ'], ['πετυχαίν', 'πετύχ'],
     ['τυγχάν', 'τύχ'], ['άσχ', 'ασχέσ'], ['τρέφ', 'θρέψ'], ['ελαύν', 'ελάσ'], ['κρέμ', 'κρεμάσ'], ['ευρίσκ', 'εύρ'],
     ['έχ', 'άσχ'], ['έλκ', 'έλκυσ'], ['θαρρ', 'θαρρέψ'], ['χέ', 'χύσ'], ['νιστ', 'στήσ'], ['ιστάν', 'αστήσ'],
     ['σπά', 'σπάσ'], ['θέλ', 'θελήσ'], ['κρίν', 'κρίν'], ['νέμ', 'νείμ'],
     ['δεικνύ', 'δείξ'], ['μειγνύ', 'μείξ'], ['ρηγνύ', 'ρήξ'], ['γιγνώσκ', 'γνώσ'], ['πηγνύ', 'πήξ'], ['τρώ', 'φά,φάγ'],
     ['τρώγ', 'φά,φάγ'], ['πά', 'πά'], ['φυλ', 'φυλάξ']
     ]

irregular_passive_roots = \
    [['υπέρκειμαι', None],
     ['πηγαινόρχομαι', None],
     ['πέρδομαι', None],
     ['επείγομαι', None],
     ['φύομαι', None],
     ['αγάλλομαι', None],
     ['ίπταμαι', None],
     ['φθέγγομαι', None],
     ['απόκειμαι', None],
     ['απόκειμαι', None],
     ['εναπόκειμαι', None],
     ['εναπόκειμαι', None],
     ['ανίπταμαι', None],
     ['κωλύομαι', None],
     ['πηγαινοέρχομαι', None],
     ['τεκμαίρομαι', None],
     ['ακκίζομαι', None],
     ['ευθύνομαι', None],
     ['οφείλομαι', None],
     ['απεχθάνομαι', None],
     ['μάχομαι', None], ['βάλλ', 'βληθ'], ['βάζ', 'βαλθ'], ['αίρ', 'αρθ'], ['βγάζ', 'βγαλθ'], ['λαμβάν', 'ληφθ'],
     ['πον', 'πονεθ'],
     ['ρήγνυ', 'ραγ,ρηχθ,ρηχτ'], ['ρηγνύ', 'ραγ,ρηχθ,ρηχτ'], ['αίρν', 'αρθ'], ['γράφ', 'γραφ,γραφτ'], ['αίρ', 'αρθ'],
     ['δέρν', 'δαρθ'], ['άσχ', 'ασχεθ'], ['καλ', 'κληθ'], ['εύχ', 'ευχηθ'], ['δίν', 'δοθ'], ['δίδ', 'δοθ'],
     ['δεικνύ', 'δειχθ'], ['τρίβ', 'τριβ,τριφτ,τριφθ'], ['κλέπτ', 'κλαπ,κλεφτ,κλεφθ'], ['φέρ', 'φερθ'],
     ['υπόσχ', 'υποσχεθ'], ['κόπτ', 'κοπ'], ['κόβ', 'κοπ'], ['ακού', 'ακουστ'], ['στέλν', 'σταλθ,σταλ'],
     ['στέλλ', 'σταλθ,σταλ'], ['πλέν', 'πλυθ'], ['έρχ', 'έλθ,έρθ,`ρθ,`λθ'], ['κάθ', 'καθίσ,κάτσ'], ['γίν', 'γίν'],
     ['καί', 'κα'], ['στέκ', 'σταθ'], ['στήν', 'σταθ'], ['οφείλ', 'οφεληθ'], ['πνίγ', 'πνιγ,πνιχτ,πνιχθ'],
     ['θέτ', 'τεθ'], ['θάβ', 'θαφτ,θαφθ,ταφ'], ['αλλάσσ', 'αλλαγ,αλλαχθ,αλλαχτ'],
     ['βλέπ', 'ιδωθ'], ['λέγ', 'ειπωθ,ιπωθ,λεγ'], ['τείν', 'ταθ'], ['φαίν', 'φαν'], ['σέρν', 'συρθ'],
     ['αυξάν', 'αυξηθ'], ['σπέρν', 'σπαρθ'], ['αλίσκ', 'αλωθ'], ['τρέφ', 'τραφ'], ['τέμν', 'τμηθ'], ['κρέμ', 'κρεμαστ'],
     ['βρίσκ', 'βρεθ'], ['τρώ', 'φαγωθ'], ['λέ', 'ειπωθ'], ['τρώγ', 'φαγωθ'], ['αφήν', 'αφεθ'], ['τρέπ', 'τραπ'],
     ['στρέφ', 'στραφ'], ['τίθε', 'τεθ'], ['σέβ', 'σεβαστ'], ['χαίρ', 'χαρ'], ['λέγ', 'λεγ'], ['θιστ', 'ταστ'],
     ['επαφίε', 'επαφεθ'], ['ρήγνυ', 'ραγ'], ['ίστ', 'αστ'], ['ιστ', 'αστ'], ['θίστ', 'ταστ'], ['έλκ', 'ελκυστ'],
     ['χέ', 'χυσθ'],
     ['νιστ', 'σταθ'], ['ελαύν', 'ελαθ'], ['ιστάν', 'ασταθ'], ['δεικνύ', 'δειχθ'], ['δείκνυ', 'δειχθ'],
     ['μειγνύ', 'μειχθ'], ['γιγνώσκ', 'γνωσθ'], ['πηγνύ', 'παγ'], ['ενδείκνυ', 'ενδειχθ'], ['ευρίσκ', 'ευρεθ'],
     ['τρώ', 'φαγωθ'], ['τρώγ', 'φαγωθ'], ['σπά', 'σπαστ'], ['φυλ', 'φυλαχτ'], ['άγ', 'αχθ'], ['φθείρ', 'φθαρ'],
     ['φθείρ', 'φθαρθ'], ['πλήττ', 'πλαγ,πληγ'], ['πλήσσ', 'πλαγ,πληγ'], ['σταίν', 'στ']
     ]

irregular_passive_perfect_participles = {'άγω': 'ηγμένος', 'έχομαι': None, 'αγανακτώ': 'αγανακτισμένος',
                                         'αποτυχαίνω': 'αποτυχημένος', 'κάνω': 'καμωμένος', 'λανθάνω': 'λανθασμένος',
                                         'αγαπάω': 'αγαπημένος', 'αγωνίζομαι': 'αγωνισμένος', 'κάμνω': 'καμωμένος',
                                         'δυστυχώ': 'δυστυχισμένος', 'ευτυχώ': 'ευτυχισμένος', 'θυμώνω': 'θυμωμένος',
                                         'αγοράζω': 'αγορασμένος', 'αφαιρώ': 'αφηρημένος', 'αισθάνομαι': 'αισθαμένος',
                                         'ακολουθώ': 'ακολουθημένος', 'ακούω': 'ακουσμένος', 'αλλάζω': 'αλλαγμένος',
                                         'ανάβω': 'αναμμένος', 'αναγκάζω': 'αναγκασμένος', 'ανήκω': None,
                                         'δίνω': 'δοσμένος', 'κάθομαι': 'καθισμένος', 'καίω': 'κεκαυμένος',
                                         'κλαίω': 'κλαμένος', 'βάλλω': 'βεβλημένος', 'θυμάμαι': 'θυμισμένος',
                                         'τρώω': 'φαγωμένος', 'στρέφω': 'στραμμένος', 'ανοίγω': 'ανοιγμένος',
                                         'αξίζω': None, 'απαγορεύω': 'απαγορευμένος', 'απαντάω': 'απαντημένος',
                                         'αποκτώ': 'αποκτημένος', 'απορώ': None, 'αποτελούμαι': 'αποτελεσμένος',
                                         'αποφασίζω': 'αποφασισμένος', 'αργώ': None, 'αρέσω': None,
                                         'βρέχω': 'βρεγμένος', 'αρχίζω': None, 'αστειεύομαι': None, 'αφήνω': 'αφημένος',
                                         'βάζω': 'βαλμένος', 'βάφω': 'βαμμένος', 'βαριέμαι': 'βαρεμένος',
                                         'βγάζω': 'βγαλμένος', 'βγαίνω': None, 'βιάζομαι': 'βιασμένος',
                                         'βλέπω': 'ιδωμένος', 'βοηθάω': 'βοηθημένος', 'βρίσκω': None,
                                         'βράζω': 'βρασμένος', 'γδύνω': 'γδυμένος', 'γελάω': 'γελασμένος',
                                         'γεμίζω': 'γεμισμένος', 'γεννάω': 'γεννημένος', 'γίνομαι': 'γινωμένος',
                                         'γκρινιάζω': None, 'γυρίζω': 'γυρισμένος',
                                         'δανείζω': 'δανεισμένος', 'δείχνω': 'δειγμένος', 'δένω': 'δεμένος',
                                         'δέχομαι': 'δεχτός, δεκτός', 'διαβάζω': 'διαβασμένος',
                                         'διαλέγω': 'διαλεγμένος', 'διαμαρτύρομαι': 'διαμαρτυρημένος', 'διαφωνώ': None,
                                         'διηγούμαι': 'διηγημένος', 'διορθώνω': 'διορθωμένος', 'διψάω': 'διψασμένος',
                                         'διώχνω': 'διωγμένος', 'δοκιμάζω': 'δοκιμασμένος', 'δουλεύω': None,
                                         'είμαι': None, 'εκφράζω': 'εκφρασμένος', 'ελπίζω': None,
                                         'εμφανίζομαι': 'εμφανισμένος', 'ενδιαφέρομαι': None, 'εξηγώ': 'εξηγημένος',
                                         'εξαφανίζομαι': 'εξαφανισμένος', 'επηρεάζω': 'επηρεασμένος',
                                         'επιτρέπω': 'επιτετραμμένος', 'έρχομαι': None, 'ετοιμάζω': 'ετοιμασμένος',
                                         'εύχομαι': None, 'έχω': None, 'ζεσταίνω': 'ζεσταμένος', 'ζηλεύω': 'ζηλεμένος',
                                         'ζητάω': 'ζητημένος', 'ζω': 'βιωμένος', 'θέλω': None,
                                         'καθαρίζω': 'καθαρισμένος', 'καλώ': 'καλεσμένος', 'καπνίζω': None,
                                         'καταλαβαίνω': None, 'καταστρέφω': 'κατεστραμμένος',
                                         'κατεβάζω': 'κατεβασμένος', 'κατεβαίνω': None, 'κερνάω': 'κερασμένος',
                                         'κλείνω': 'κλεισμένος', 'κόβω': 'κομμένος', 'κοιμάμαι': 'κοιμισμένος',
                                         'κοιτάζω': 'κοιταγμένος', 'κουράζω': 'κουρασμένος', 'κρατάω': 'κρατημένος',
                                         'κρύβω': 'κρυμμένος', 'λέω': 'ειπωμένος', 'λείπω': None, 'λύνω': 'λυμένος',
                                         'λυπάμαι': 'λυπημένος', 'μαγειρεύω': 'μαγειρεμένος', 'μαζεύω': 'μαζεμένος',
                                         'μαθαίνω': 'μαθημένος', 'μιμούμαι': None, 'μένω': None, 'μοιάζω': None,
                                         'μοιράζω': 'μοιρασμένος', 'μπαίνω': None, 'μπορώ': None, 'νικάω': 'νικημένος',
                                         'νοιάζομαι': 'νοιασμένος', 'νομίζω': None, 'ντρέπομαι': None,
                                         'ντύνω': 'ντυμένος', 'ξαπλώνω': 'ξαπλωμένος', 'ξεκινάω': 'ξεκινημένος',
                                         'ξέρω': None, 'ξεχνάω': 'ξεχασμένος', 'ξυπνάω': 'ξυπνημένος',
                                         'ξυρίζω': 'ξυρισμένος', 'οδηγώ': 'οδηγημένος', 'ονειρεύομαι': 'ονειρεμένος',
                                         'ονομάζω': 'ονομασμένος', 'οφείλω': None, 'πεθαίνω': 'πεθαμένος',
                                         'παίζω': None, 'παντρεύομαι': 'παντρεμένος',
                                         'παραγγέλνω': None, 'παραπονιέμαι': 'παραπονεμένος', 'παριστάνω': None,
                                         'παθαίνω': 'παθημένος', 'πάσχω': 'παθημένος', 'πείθω': 'πεπεισμένος',
                                         'πεινάω': 'πεινασμένος',
                                         'περιμένω': None, 'περνάω': 'περασμένος', 'περπατάω': 'περπατημένος',
                                         'πετυχαίνω': 'πετυχημένος', 'πετάω': 'πεταγμένος', 'πέφτω': 'πεσμένος',
                                         'πηγαίνω': None, 'πιάνω': 'πιασμένος', 'πιέζω': 'πιεσμένος',
                                         'πίνω': 'πιωμένος', 'πιστεύω': None, 'πλένω': 'πλυμένος',
                                         'πληρώνω': 'πληρωμένος', 'πονάω': 'πονεμένος', 'πουλάω': 'πουλημένος',
                                         'πρέπει': None, 'πρόκειται': None, 'προκύπτω': None,
                                         'προσθέτω': 'προστεθειμένος', 'προσέχω': None, 'προσποιούμαι': 'προσποιημένος',
                                         'προτείνω': 'προτεταμένος', 'προτιμάω': 'προτιμημένος', 'ράβω': 'ραμμένος',
                                         'ρίχνω': 'ριγμένος', 'ρωτάω': 'ρωτημένος', 'σβήνω': 'σβησμένος',
                                         'σέβομαι': 'σεβασμένος', 'σηκώνω': 'σηκωμένος', 'σημαίνω': None,
                                         'σκεπάζω': 'σκεπασμένος', 'σκέφτομαι': None, 'σκοτώνω': 'σκοτωμένος',
                                         'σκουπίζω': 'σκουπισμένος', 'σπουδάζω': 'σπουδασμένος', 'στέλνω': 'σταλμένος',
                                         'στενοχωριέμαι': 'στενοχωρημένος', 'συμμετέχω': None, 'συμπεριφέρομαι': None,
                                         'συμφωνώ': 'συμφωνημένος', 'στηρίζω': 'στηριγμένος',
                                         'συνηθίζω': 'συνηθισμένος', 'συστήνω': 'συστημένος', 'σώζω': 'σωσμένος',
                                         'ταξιδεύω': None, 'τρελαίνομαι': 'τρελαμένος', 'τρέχω': None, 'υπάρχω': None,
                                         'υποπτεύομαι': None, 'υπόσχομαι': 'υποσχεμένος', 'υποφέρω': 'υποσχεμένος',
                                         'υποψιάζομαι': 'υποψιασμένος', 'φαίνομαι': None, 'φαντάζομαι': 'φαντασμένος',
                                         'φέρνω': 'φερμένος', 'φεύγω': None, 'φοβάμαι': 'φοβισμένος',
                                         'φοράω': 'φορεμένος', 'στήν': 'στημένος',
                                         'φταίω': 'φοβημένος', 'φτάνω': None, 'φτιάχνω': 'φτιαγμένος', 'φωνάζω': None,
                                         'χαίρομαι': 'χαρούμενος', 'χαλάω': None, 'χάνω': 'χαμένος', 'χρειάζομαι': None,
                                         'χρησιμοποιώ': 'χρησιμοποιημένος', 'χρωστάω': None, 'χτυπάω': 'χτυπημένος',
                                         'χωράω': None, 'ψάχνω': 'ψαγμένος', 'ωφελώ': 'ωφελημένος',
                                         'θέτω': 'τεθειμένος', 'τίθεμαι': 'τεθειμένος'}

irregular_active_aorists = {'βαίνω': 'βηκα', 'μπαίνω': 'μπήκα', 'αίρω': 'ήρα', 'βγαίνω': 'βγήκα', 'βρίσκω': 'βρήκα',
                            'πηγαίνω': 'πήγα', 'παίρνω': 'πήρα', 'λέω': 'είπα', 'λέγω': 'είπα', 'πίνω': 'ήπια',
                            'τρώω': 'έφαγα', 'τρώγω': 'έφαγα', 'βλέπω': 'είδα', 'πάω': 'πήγα',
                            'καταλαβαίνω': 'κατάλαβα', 'καταλαμβάνω': 'κατέλαβα'}

irregular_active_paratatikos = {'πάω': 'πήγαινα', 'σπάω': 'σπαγα'}

irregular_passive_aorists = {'λέω': 'ειπώθηκα', 'λέγω': 'ειπώθηκα', 'βλέπω': 'ειδώθηκα', 'αίρομαι': 'άρθηκα'}

deponens_with_active_perf_forms = ['έρχομαι', 'κάθομαι', 'γίνομαι']

irregular_imperative_forms = {
    'σηκωθ': {SG: {SEC: 'σήκω'}},
    'ακού': {SG: {SEC: 'άκου'}},
    'ακούσ': {SG: {SEC: 'άκου'}},
    'ανέβ': {SG: {SEC: 'ανέβα'}, PL: {SEC: 'ανεβείτε'}},
    'κατέβ': {SG: {SEC: 'κατέβα'}, PL: {SEC: 'κατεβείτε'}},
    'ανεβ': {SG: {SEC: 'ανέβα'}, PL: {SEC: 'ανεβείτε'}},
    'κατεβ': {SG: {SEC: 'κατέβα'}, PL: {SEC: 'κατεβείτε'}},
    "φύγ": {SG: {SEC: 'φεύγα'}, PL: {SEC: 'φευγάτε'}},
    "τρέξ": {SG: {SEC: 'τρέχα'}, PL: {SEC: 'τρεχάτε'}},
    "πλύν": {PL: {SEC: 'πλύντε'}},
    "πά": {SG: {SEC: 'πήγαινε'}, PL: {SEC: 'πηγαίνετε'}},
    "έρθ": {SG: {SEC: 'έλα'}, PL: {SEC: 'ελάτε'}},
    "έλθ": {SG: {SEC: 'έλα'}, PL: {SEC: 'ελάτε'}},
}

EIMAI = 'eimai'
EIMAI_PARATATIKOS = "eimai_paratatikos"
PRESENT_ACTIVE_PART_EIMAI = "present_active_part_eimai"
IMPER_ACT_EIMAI = 'imper_act_eimai'
CON2AB = 'con2ab'
CON1_ACT = "con1_act"
CON2A_ACT = 'con2a_act'
CON2B_ACT = 'con2b_act'
CON2C_ACT = 'con2c_act'
CON2D_ACT = 'con2d_act'
CON1_ACT_MODAL = 'con1_act_modal'
CON2_ACT_MODAL = 'con2_act_modal'
PARAT2_ACT = 'parat2_act'
CON1_PASS = 'con1_pass'
CON2A_PASS = 'con2a_pass'
CON2AB_PASS = 'con2ab_pass'
CON2B_PASS = 'con2b_pass'
CON2C_PASS = 'con2c_pass'
CON2SA_PASS = 'con2sa_pass'
CON2D_PASS = 'con2d_pass'
CON2E_PASS = 'con2e_pass'
AOR_ACT = 'aor_act'
ARCH_PASS_AOR = 'arch_pass_aor'
ARCH_SEC_AOR = 'arch_sec_aor'
PARAT_ACT_MODAL = 'parat_act_modal'
PARAT1_PASS = 'parat1_pass'
IMPER_ACT_CONT_1 = 'imper_act_cont_1'
IMPER_ACT_CONT_2A = 'imper_act_cont_2a'
IMPER_ACT_CONT_2B = 'imper_act_cont_2b'
IMPER_ACT_CONT_2D = 'imper_act_cont_2d'
IMPER_ACT_CONT_2C = 'imper_act_cont_2c'
IMPER_PASS_CONT_2D = 'imper_pass_cont_2d'
IMPER_PASS_CONT_2E = 'imper_pass_cont_2e'
IMPER_PASS_CONT_1 = 'imper_pass_cont_1'
IMPER_PASS_CONT_2A = 'imper_pass_cont_2a'
IMPER_PASS_CONT_2B = 'imper_pass_cont_2b'
IMPER_PASS_CONT_2C = 'imper_pass_cont_2c'
PARAT2A_PASS = 'parat2a_pass'
PARAT2B_PASS = 'parat2b_pass'
PARAT2B_PASS_LOGIA = 'parat2b_pass_logia'
PARAT2C_PASS = 'parat2c_pass'
PARAT2D_PASS = 'parat2d_pass'
PARAT2E_PASS = 'parat2e_pass'
IMPER_ACT_AOR_A = 'imper_act_aor_a'
IMPER_ACT_AOR_B = 'imper_act_aor_b'
IMPER_ACT_AOR_C = 'imper_act_aor_c'
IMPER_ACT_AOR_D = 'imper_act_aor_d'
IMPER_ACT_AOR_CA = 'imper_act_aor_ca'
IMPER_PASS_AOR_A = 'imper_pass_aor_a'
IMPER_PASS_AOR_B = 'imper_pass_aor_b'
IMPER_PASS_CONT_2SA = 'imper_pass_cont_2sa'
PRESENT_ACTIVE_PART_1 = 'present_active_part_1'
PRESENT_ACTIVE_PART_2C = 'present_active_part_2c'
PRESENT_ACTIVE_PART_2 = 'present_active_part_2'
PRESENT_PASSIVE_PART_1 = 'present_passive_part_1'
PRESENT_PASSIVE_PART_2A = 'present_passive_part_2a'
PRESENT_PASSIVE_PART_2AB = 'present_passive_part_2ab'
PRESENT_PASSIVE_PART_2B = 'present_passive_part_2b'
PRESENT_PASSIVE_PART_2D = 'present_passive_part_2d'
PRESENT_PASSIVE_PART_2E = 'present_passive_part_2e'
PAST_PASSIVE_PART = 'past_passive_part'
CON1_PASS_MODAL = 'con1_pass_modal'
CON2_PASS_MODAL = 'con2_pass_modal'
PARAT2B_LOGIA = 'parat2b_logia'

conjugations = {
    EIMAI: {SG: {PRI: ['είμαι'], SEC: ['είσαι'], TER: ['είναι']},
            PL: {PRI: ['είμαστε'], SEC: ['είστε', 'είσαστε'], TER: ['είναι']}},
    EIMAI_PARATATIKOS: {SG: {PRI: ['ήμουν', 'ήμουνα'], SEC: ['ήσουν', 'ήσουνα'], TER: ['ήταν', 'ήτανε']},
                        PL: {PRI: ['ήμαστε', 'ήμασταν'], SEC: ['ήσαστε', 'ήσασταν'], TER: ['ήταν', 'ήτανε']}},
    CON1_ACT: {SG: {PRI: ['ω'], SEC: ['εις'], TER: ['ει']}, PL: {PRI: ['ουμε'], SEC: ['ετε'], TER: ['ουν', 'ουνε']}},
    CON2A_ACT: {SG: {PRI: ['ώ', 'άω'], SEC: ['άς'], TER: ['ά', 'άει']},
                PL: {PRI: ['ούμε', 'άμε'], SEC: ['άτε'], TER: ['άνε', 'άν', 'ούν', 'ούνε']}},
    CON2B_ACT: {SG: {PRI: ['ώ'], SEC: ['είς'], TER: ['εί']}, PL: {PRI: ['ούμε'], SEC: ['είτε'], TER: ['ούνε', 'ούν']}},
    CON2C_ACT: {SG: {PRI: ['ω'], SEC: ['ς'], TER: ['ει']}, PL: {PRI: ['με'], SEC: ['τε'], TER: ['νε', 'ν']}},
    CON2D_ACT: {SG: {PRI: ['ώ'], SEC: ['οίς'], TER: ['οί']},
                PL: {PRI: ['ούμε', 'ούμεν'], SEC: ['ούτε'], TER: ['ούνε', 'ούν']}},
    CON1_ACT_MODAL: {SG: {TER: ['ει']}},
    CON2_ACT_MODAL: {SG: {TER: ['εί']}},

    CON1_PASS: {SG: {PRI: ['ομαι'], SEC: ['εσαι'], TER: ['εται']},
                PL: {PRI: ['όμαστε'], SEC: ['εστε', 'όσαστε'], TER: ['ονται']}},
    CON2A_PASS: {SG: {PRI: ['ιέμαι'], SEC: ['ιέσαι'], TER: ['ιέται']},
                 PL: {PRI: ['ιόμαστε', 'ιούμαστε'], SEC: ['ιέστε', 'ιόσαστε'], TER: ['ιούνται', 'ιόνται']}},
    CON2AB_PASS: {SG: {PRI: ['ώμαι'], SEC: ['άσαι'], TER: ['άται']}, PL: {PRI: ['όμαστε'], SEC: ['άστε'],
                                                                          TER: ['ώνται']}},

    CON2B_PASS: {SG: {PRI: ['ούμαι'], SEC: ['είσαι'], TER: ['είται']},
                 PL: {PRI: ['ούμαστε', 'ούμεθα'], SEC: ['είστε', 'είσθε'], TER: ['ούνται']}},
    CON2C_PASS: {SG: {PRI: ['άμαι'], SEC: ['άσαι'], TER: ['άται']},
                 PL: {PRI: ['όμαστε'], SEC: ['άστε', 'όσαστε'], TER: ['ούνται']}},
    CON2SA_PASS: {SG: {PRI: ['ούμαι'], SEC: ['ούσαι'], TER: ['ούται']}, PL: {PRI: ['ούμεθα'], SEC: ['ούσθε'],
                                                                             TER: ['ούνται']}},
    CON2D_PASS: {SG: {PRI: ['μαι'], SEC: ['σαι'], TER: ['ται']}, PL: {PRI: ['μεθα'], SEC: ['σθε'],
                                                                      TER: ['νται']}},
    CON2E_PASS: {SG: {PRI: ['αμαι'], SEC: ['ασαι'], TER: ['αται']}, PL: {PRI: ['άμεθα', 'όμαστε'],
                                                                         SEC: ['ασθε', 'αστε'],
                                                                         TER: ['ανται']}},

    AOR_ACT: {SG: {PRI: ['α'], SEC: ['ες'], TER: ['ε']}, PL: {PRI: ['αμε'], SEC: ['ατε'], TER: ['αν', 'ανε']}},
    ARCH_PASS_AOR: {SG: {PRI: ['ην'], SEC: ['ης'], TER: ['η']}, PL: {PRI: ['ημεν'], SEC: ['ητε'], TER: ['ησαν']}},
    ARCH_SEC_AOR: {SG: {PRI: ['ον'], SEC: ['ες'], TER: ['ε']}, PL: {PRI: ['ομεν'], SEC: ['ετε'], TER: ['ον']}},

    PARAT2_ACT: {SG: {PRI: ['α'], SEC: ['ες'], TER: ['ε']}, PL: {PRI: ['αμε'], SEC: ['ατε'], TER: ['αν', 'ανε']}},
    PARAT_ACT_MODAL: {SG: {TER: ['ε']}},
    PARAT1_PASS: {SG: {PRI: ['όμουν', 'όμουνα'], SEC: ['όσουν', 'όσουνα'], TER: ['όταν', 'ότανε']},
                  PL: {PRI: ['όμασταν', 'όμαστε'], SEC: ['όσασταν', 'όσαστε'], TER: ['ονταν', 'όντουσαν']}},
    PARAT2A_PASS: {SG: {PRI: ['ιόμουν', 'ιόμουνα'], SEC: ['ιόσουν', 'ιόσουνα'], TER: ['ιόταν', 'ιότανε']},
                   PL: {PRI: ['ιόμασταν', 'ιόμαστε'], SEC: ['ιόσασταν', 'ιόσαστε'],
                        TER: ['ιούνταν', 'ιόνταν', 'ιόντουσαν']}},
    PARAT2B_PASS: {SG: {PRI: ['ούμουν'], SEC: ['ούσουν'], TER: ['είτο', 'ούνταν', 'ούντανε']},
                   PL: {PRI: ['ούμασταν', 'ούμαστε'], SEC: ['ούσασταν', 'ούσαστε'],
                        TER: ['ούνταν', 'ούντο', 'ούντανε']}},
    PARAT2B_PASS_LOGIA: {SG: {PRI: ['ούμην'], SEC: ['είσο'], TER: ['είτο']},
                         PL: {PRI: ['ούμεθα'], SEC: ['είσθε'], TER: ['ούντο']}},
    PARAT2C_PASS: {SG: {PRI: ['όμουν', 'όμουνα'], SEC: ['όσουν', 'όσουνα'], TER: ['όταν', 'ότανε']},
                   PL: {PRI: ['όμασταν', 'όμαστε'], SEC: ['όσασταν', 'όσαστε'], TER: ['ούνταν', 'όντουσαν']}},
    PARAT2D_PASS: {SG: {PRI: ['όμουν', 'έμην'], SEC: ['όσουν', 'εσο'], TER: ['όταν', 'ετο']},
                   PL: {PRI: ['όμασταν', 'έμεθα'], SEC: ['όσασταν', 'εσθε'], TER: ['ούνταν', 'εντο']}},
    PARAT2E_PASS: {SG: {PRI: ['άμην'], SEC: ['ασο'], TER: ['ατο']},
                   PL: {PRI: ['άμεθα', 'όμαστε', 'όμασταν'], SEC: ['ασθε', 'άστε', 'όσασταν', 'όσαστε'],
                        TER: ['αντο']}},
    IMPER_ACT_CONT_1: {SG: {SEC: ['ε']}, PL: {SEC: ['ετε']}},
    IMPER_ACT_EIMAI: {SG: {TER: ['έστω']}},
    IMPER_ACT_CONT_2A: {SG: {SEC: ['α', 'αγε']}, PL: {SEC: ['άτε']}},
    IMPER_ACT_CONT_2B: {SG: {SEC: ['ει']}, PL: {SEC: ['είτε']}},
    IMPER_ACT_CONT_2D: {PL: {SEC: ['ούτε']}},
    IMPER_ACT_CONT_2C: {SG: {SEC: ['γε']}, PL: {SEC: ['γετε', 'τε']}},
    IMPER_PASS_CONT_2D: {SG: {SEC: ['σο']}, PL: {SEC: ['σθε']}},
    IMPER_PASS_CONT_2E: {PL: {SEC: ['ασθε']}},
    IMPER_PASS_CONT_1: {PL: {SEC: ['εστε']}},
    IMPER_PASS_CONT_2A: {PL: {SEC: ['ιέστε']}},
    IMPER_PASS_CONT_2B: {PL: {SEC: ['είστε']}},
    IMPER_PASS_CONT_2C: {PL: {SEC: ['άστε']}},
    IMPER_PASS_CONT_2SA: {PL: {SEC: ['ούσθε']}},

    IMPER_ACT_AOR_A: {SG: {SEC: ['ε']}, PL: {SEC: ['τε']}},
    IMPER_ACT_AOR_B: {SG: {SEC: ['ε']}, PL: {SEC: ['ετε']}},
    IMPER_ACT_AOR_C: {SG: {SEC: ['ες']}, PL: {SEC: ['έστε', 'είτε']}},
    IMPER_ACT_AOR_D: {SG: {SEC: []}, PL: {SEC: ['είτε']}},

    IMPER_ACT_AOR_CA: {SG: {SEC: ['α']}, PL: {SEC: ['είτε']}},
    IMPER_PASS_AOR_A: {SG: {SEC: ['ου']}, PL: {SEC: ['είτε']}},
    IMPER_PASS_AOR_B: {PL: {SEC: ['είτε']}},
    PRESENT_ACTIVE_PART_1: {ND: {ND: ['οντας']}},
    PRESENT_ACTIVE_PART_EIMAI: {ND: {ND: ['όντας']}},
    PRESENT_ACTIVE_PART_2C: {ND: {ND: ['γοντας']}},
    PRESENT_ACTIVE_PART_2: {ND: {ND: ['ώντας']}},
    PRESENT_PASSIVE_PART_1: {SG: {ND: ['όμενος']}},
    PRESENT_PASSIVE_PART_2A: {SG: {ND: ['ώμενος']}},
    PRESENT_PASSIVE_PART_2AB: {SG: {ND: ['ώμενος']}},
    PRESENT_PASSIVE_PART_2B: {SG: {ND: ['ούμενος']}},
    PRESENT_PASSIVE_PART_2D: {SG: {ND: ['έμενος']}},
    PRESENT_PASSIVE_PART_2E: {SG: {ND: ['μενος']}},
    PAST_PASSIVE_PART: {SG: {ND: ['μένος']}},
    MODAL: None
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

quant = ['δύο,δυο', 'έξι', 'δέκα', 'ένας/μία/ένα', 'επτά,εφτά', 'οχτώ,οκτώ', 'δεκαεφτά,δεκαεπτά', 'δεκαοχτώ,δεκαοκτώ',
         'εκατόν,εκατό', 'εννέα,εννιά', 'μηδέν', 'πέντε',
         'τρεις/τρία', 'δεκάξι,δεκαέξι', 'δώδεκα', 'είκοσι', 'ένδεκα,έντεκα', 'εξήντα', 'ογδόντα', 'πενήντα',
         'σαράντα', 'τριάντα', 'ενάμισης/μιάμιση/ενάμισι', 'ενενήντα', 'τέσσερις/τέσσερα', 'δεκαεννέα,δεκαεννιά',
         'δεκαπέντε',
         'δεκατρείς/δεκατρία', 'εβδομήντα', 'δεκατέσσερις/δεκατέσσερα']

quant_adj = ['έκτος', 'διπλός', 'ένατος', 'όγδοος', 'πρώτος', 'πέμπτος', 'τρίτος', 'δέκατος', 'έβδομος', 'εξαπλός',
             'τριπλός', 'δεκαπλός', 'δεύτερος', 'εικοστός', 'επταπλός', 'τέταρτος', 'διπλάσιος', 'δωδέκατος',
             'εκατοστός', 'ενδέκατος', 'εξηκοστός', 'πενταπλός', 'τετραπλός', 'χιλιοστός', 'εξαπλάσιος', 'τριακοστός',
             'τριπλάσιος', 'δεκαπλάσιος', 'ενενηκοστός', 'επταπλάσιος', 'ογδοηκοστός', 'διακοσιοστός', 'εβδομηκοστός',
             'εξακοσιοστός', 'πενταπλάσιος', 'τετραπλάσιος', 'εικοσαπλάσιος', 'ενδεκαπλάσιος', 'τεσσαρακοστός',
             'τριακοσιοστός', 'τετρακοσιοστός', 'εκατομμυριοστός', 'εκατονταπλάσιος']

quant_noun = ['δυάδα', 'εξάδα', 'δεκάδα', 'οκτάδα', 'τριάδα', 'μυριάδα', 'πεντάδα', 'τετράδα', 'χιλιάδα',
              'δωδεκάδα', 'εικοσάδα', 'εικοσαριά', 'εκατοντάδα', 'εκατομμύριο', 'δισεκατομμύριο', 'τρισεκατομμύριο',
              'τετρακισεκατομμύριο', 'πεντακισεκατομμύριο', 'δυάδα', 'εξάδα', 'δεκάδα', 'οκτάδα', 'τριάδα', 'μυριάδα',
              'πεντάδα', 'τετράδα', 'χιλιάδα', 'δωδεκάδα', 'εικοσάδα', 'εικοσαριά', 'εκατοντάδα', 'δισεκατομμύριο',
              'εκατομμύριο', 'τρισεκατομμύριο']

hundreds = ['διακόσια', 'τριακόσια', 'τετρακόσια', 'πεντακόσια', 'εξακόσια', 'εφτακόσια,επτακόσια', 'οχτακόσια',
            'εννιακόσια', 'χίλια']

alternative_syllables = {'οκτ': 'οχτ', 'επτ': 'εφτ'}
