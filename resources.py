poses = {'def_article': 'definite article', 'indef_article': 'indefinite article', 'conj': 'conjunction', 'no_tag': 'not classified',
         'part': 'particle',
         'excl': 'exclamation', 'noun': 'noun', 'prep': 'preposition', 'adv': 'adverb', 'pron': 'pronoun', 'verb': 'verb',
         'quant': 'quantifier', 'properN': 'proper noun', 'adj': 'adjective', 'adv,adj*': "adverb adjective",
         'quant,noun': "quantifier-noun", 'pers_pron': 'personal pronoun',
         'quant,adj': 'quiantifier adjective', 'pron,noun': 'pronoun noun', 'adv,conj': 'adverb conjunctive',
         'adv,adj': 'adverb adjective', 'ind': 'indicative', 'imper': 'imperative', 'nd': 'not defined'


         }

secondary_poses = {

    'inf': 'infinitive', 'imps': 'impersonal',
    'pant': 'adverbial past active participle',
    'pcon': 'adverbial present active participle',
    'prpas': 'present passive participle',
    'praet': 'praeteritum',
    'impt': 'imperative',
    'fin': 'present',
    'pact': 'present active participle',
    'ppas': 'past passive participle',
    'perfpart': 'perfect passive participle',
    'papart': 'past active participle',
    'prespred': 'modal pres',
    'pastpred': 'modal past',
    'comp': 'comparative',
    'superl': 'superlative',
    'adv': 'adverb',
    'comp_adv': 'comparative adverb',
    'superl_adv': 'superlative adverb',
    'ind': 'indicative',
    'imp': 'imperative',
    'part': 'participle',
    'card': 'cardinal quantifiers',
    'nakc': 'weak personal pronoun',
    'akc': 'strong personal pronoun',
    'nd': 'not defined'

}

length_of_endings = {
    "1": [
        "ω",
        "ώ",
        "ά",
        "ς",
        "ν",
        "α",
        "ε"
    ],
    "2": [
        "ει",
        "άω",
        "ας",
        "άν",
        "εί",
        "με",
        "τε",
        "νε",
        "ες",
        "αν",
        "ου"
    ],
    "3": [
        "εις",
        "ετε",
        "ουν",
        "άει",
        "άμε",
        "άτε",
        "άνε",
        "ούν",
        "είς",
        "αμε",
        "ατε",
        "ανε"
    ],
    "4": [
        "ουμε",
        "ουνε",
        "ούμε",
        "ούνε",
        "είτε",
        "ομαι",
        "εσαι",
        "εται",
        "εστε",
        "άμαι",
        "άσαι",
        "άται",
        "άστε",
        "όταν",
        "είτο",
        "είσο"
    ],
    "5": [
        "ονται",
        "ιέμαι",
        "ιέσαι",
        "ιέται",
        "ιέστε",
        "ούμαι",
        "είσαι",
        "είται",
        "είστε",
        "όμουν",
        "όσουν",
        "ότανε",
        "ονταν",
        "ούντο",
        "ούμην",
        "είσθε"
    ],
    "6": [
        "όμαστε",
        "όσαστε",
        "ούμεθα",
        "ούνται",
        "όμουνα",
        "όσουνα",
        "ιόμουν",
        "ιόσουν",
        "ούμουν",
        "ούσουν",
        "ούνταν"
    ],
    "7": [
        "ιόμαστε",
        "ιόσαστε",
        "ιούνται",
        "ούμαστε",
        "όμασταν",
        "όσασταν",
        "ιόμουνα",
        "ιόσουνα",
        "ιούνταν",
        "ούσαστε"
    ],
    "8": [
        "όντουσαν",
        "ιόμασταν",
        "ιόσασταν",
        "ούμασταν",
        "ούσασταν"
    ]
}

pronouns= ['εγώ', 'εσύ', 'αυτός, αυτή, αυτό', 'εμείς', 'εσείς', 'αυτοί, αυτές, αυτά']


common_tenses = {'fin': 'present', 'past': 'past', 'fut': 'future', 'nd': 'not defined'}

# maps tenses with other data
greek_tenses = {
    'present': ['fin', 'imperf'],
    'continuous subjunctive': ['fin', 'imperf', 'να '],
    'continuous hortative': ['fin', 'imperf', 'ας '],
    'future continuous': ['fin', 'imperf', 'θα '],
    'continuous imperative': ['impt', 'imperf'],
    'simple subjunctive': ['fin', 'perf', 'να '],
    'simple future': ['fin', 'perf', 'θα '],
    'simple imperative': ['impt', 'perf'],
    'aorist': ['praet', 'perf'],
    'paratatikos': ['praet', 'imperf'],
    'perfect': ['aux_fin', 'perf'],
    'future perfect': ['aux_fin', 'perf', 'θα '],
    'past perfect': ['aux_praet', 'perf'],
    'dinitiki': ['praet', 'imperf', 'θα '],
    'optative_2': ['praet', 'imperf', 'να '],
    'first conditional': ['fin', 'perf', 'αν '],
    'second conditional': ['praet', 'imperf', 'αν '],
    'third conditional': ['aux_praet', 'perf', 'αν ']

}

cases = {'voc': 'vocative', 'gen': 'genitive', 'acc': 'accusative', 'nom': 'nominative', 'dat': 'dative', 'nd': 'not defined'}

persons = {'pri', 'sec', 'ter', 'impersonal', 'nd'}

genders = {'fem': 'feminine', 'masc': 'masculine', 'neut': 'neutral', 'nd': 'not defined'}
# will have to add some other genders specific to Polish language
numbers = {'sg', 'pl', 'dual', 'nd'}

aspects = {'imperf', 'perf', 'nd'}

voices = {'passive', 'active', 'middle', 'deponens', 'nd'}

declinations = {
    'masc_os': {'sg': {'nom': 'ος', 'acc': 'ο', 'gen': 'ου', 'voc': 'ε' }, 'pl': {'nom': 'οι', 'acc': 'ους', 'gen': 'ων', 'voc': 'οι' }},
    'feminine_h':{'sg': {'nom': 'η', 'acc': 'η', 'gen': 'ης', 'voc': 'η' }, 'pl': {'nom': 'ες', 'acc': 'ες', 'gen': 'ων', 'voc': 'ες' }}, 
    'feminine_a':{'sg': {'nom': 'α', 'acc': 'α', 'gen': 'ας', 'voc': 'α' }, 'pl': {'nom': 'ες', 'acc': 'ες', 'gen': 'ων', 'voc': 'ες' }}, 
    'neuter_o':{'sg': {'nom': 'ο', 'acc': 'ο', 'gen': 'ου', 'voc': 'ο' }, 'pl': {'nom': 'α', 'acc': 'α', 'gen': 'ων', 'voc': 'α' }}
}


# these prefixes change themselves or stem by esoteric augmentation
# I probably should change this model into key - augmented prefix, value - anaugmented, because for one augmented there are sometimes more than one unaugmented forms (para: pare, or parh)
dict_of_augmented_prefixes = {'ανα': 'ανε', 'δια': 'διε', 'εκ': 'εξε', 'συλ': 'συνε', 'απο': 'απε', 'προ': 'προε', 'κατευ': 'κατηυ', 'παρα': 'παρε', 'προεξ': 'προεξε', 'ενδια': 'ενδιε', 'περι': 'περιε', 'υπο': 'υπε', 'αμφι': 'αμφε', 'επι': 'επε', 'κατα':'κατε', 'εισ': 'εισε'}



# these prefixes do not merge with verbs at all
prefixes_list_that_allow_augmentaion = ['πολυ', 'παρα', 'καλα', 'κουτσα']

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

a = [

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
    ['το', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc.nakc:npraep']],
    ['αυτό', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc.akc']],
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
    ['αυτά', ['αυτός', 'ppron3:pl:nom.acc:n:ter:akc.akc']],

    # gen
    ['αυτών', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:akc']],
    ['τους', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:nakc:npraep']],

    # acc
    ['τους', ['αυτός', 'ppron3:pl:acc:m:ter:nakc:npraep']],
    ['αυτούς', ['αυτός', 'ppron3:pl:acc:m:ter:akc']],
    ['τις', ['αυτός', 'ppron3:pl:acc:f:ter:akc.nakc:npraep']],
    ['τες', ['αυτός', 'ppron3:pl:acc:f:ter:akc.nakc:npraep']],

]

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
               'διάμετρος', 'διέξοδος', 'δικάσιμος', 'δίοδος', 'δωδεκάδελτος', 'εγκύκλιος', 'είσοδος', 'έλαφος', 'έξοδος',
               'επάνοδος', 'επέτειος', 'έρημος', 'έφοδος', 'ημισέληνος', 'ιερόδουλος', 'κάθετος', 'κάθοδος', 'κάμηλος',
               'κυπάρισσος', 'ημιδιάμετρος', 'ημιπερίοδος', 'ήπειρος', 'ίνδικτος', 'κάμινος', 'κέραμος', 'κλιμακτήριος',
               'λέκιθος', 'λήκυθος', 'μεγαλόνησος', 'μέθοδος', 'μεθόριος', 'μεσόφωνος', 'οκτώηχος', 'οπτόπλινθος',
               'Παμμακάριστος', 'Πανάχραντος', 'πανσέληνος', 'παράγραφος', 'παράγωγος', 'παρακαμπτήριος', 'παράμετρος',
               'πάροδος', 'Πεντάτευχος', 'πεντηκόντορος', 'περίμετρος', 'περίοδος', 'περίπολος', 'πισσάσφαλτος',
               'προβατοκάμηλος', 'πρόοδος', 'πρόσοδος', 'πύελος', 'πυραυλάκατος', 'σεληνάκατος', 'σταφιδάμπελος',
               'στρουθοκάμηλος', 'σύγκλητος', 'σύνοδος', 'τήβεννος', 'τορπιλάκατος', 'ύαλος', 'ύπαιθρος', 'υπερλεωφόρος',
               'υφήλιος', 'υψικάμινος', 'χερσόνησος', 'ωμόπλινθος')


feminine_or_masc = ('καπνοδόχος', 'άργιλος', 'τάφρος', 'κρύσταλλος', 'περιβαλλοντολόγος', 'απόστροφος', 'γιατρός',
                    'μηχανικός', 'ηθοποιός', 'νηπιαγογός', 'δικιγόρος',)

# should there be added language names on ika?
plur_tant_neut = ('Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια', 'Ιωάννινα', 'Γιάννενα', 'Γιάννινα')