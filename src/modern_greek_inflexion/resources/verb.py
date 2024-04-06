from .variables import *

conjugations = {
    EIMAI: {SG: {PRI: ['είμαι'], SEC: ['είσαι'], TER: ['είναι']},
            PL: {PRI: ['είμαστε'], SEC: ['είστε', 'είσαστε'], TER: ['είναι']}},
    EIMAI_PARATATIKOS: {SG: {PRI: ['ήμουν', 'ήμουνα'], SEC: ['ήσουν', 'ήσουνα'], TER: ['ήταν', 'ήτο', 'ήτανε']},
                        PL: {PRI: ['ήμαστε', 'ήμασταν'], SEC: ['ήσαστε', 'ήσασταν'], TER: ['ήταν', 'ήσαν', 'ήτανε']}},
    CON1_ACT: {SG: {PRI: ['ω'], SEC: ['εις'], TER: ['ει']},
               PL: {PRI: ['ουμε', 'ομε'], SEC: ['ετε'], TER: ['ουν', 'ουνε']}},
    CON2A_ACT: {SG: {PRI: ['ώ', 'άω'], SEC: ['άς'], TER: ['ά', 'άει']},
                PL: {PRI: ['ούμε', 'άμε'], SEC: ['άτε'], TER: ['άνε', 'άν', 'ούν', 'ούνε']}},
    CON2AK_ACT: {SG: {PRI: ['ώ'], SEC: ['άς'], TER: ['ά']},
                 PL: {PRI: ['ούμε', 'άμε'], SEC: ['άτε'], TER: ['ούν']}},
    CON2B_ACT: {SG: {PRI: ['ώ'], SEC: ['είς'], TER: ['εί']}, PL: {PRI: ['ούμε'], SEC: ['είτε'], TER: ['ούνε', 'ούν']}},
    CON2C_ACT: {SG: {PRI: ['ω'], SEC: ['ς'], TER: ['ει']}, PL: {PRI: ['με'], SEC: ['τε'], TER: ['νε', 'ν']}},
    CON2D_ACT: {SG: {PRI: ['ώ'], SEC: ['οίς'], TER: ['οί']},
                PL: {PRI: ['ούμε'], SEC: ['ούτε'], TER: ['ούν']}},
    CON1_ACT_MODAL: {SG: {TER: ['ει']}},
    CON2_ACT_MODAL: {SG: {TER: ['εί']}},

    CON1_PASS: {SG: {PRI: ['ομαι'], SEC: ['εσαι'], TER: ['εται']},
                PL: {PRI: ['όμαστε'], SEC: ['εστε', 'όσαστε'], TER: ['ονται']}},
    CON1_PASS_ARCHAIC: {PL: {PRI: ['όμεθα'], SEC: ['εσθε']}},
    CON2A_PASS: {SG: {PRI: ['ιέμαι'], SEC: ['ιέσαι'], TER: ['ιέται']},
                 PL: {PRI: ['ιόμαστε'], SEC: ['ιέστε', 'ιόσαστε'], TER: ['ιούνται', 'ιόνται']}},
    CON2AK_PASS: {SG: {PRI: ['ώμαι'], SEC: ['άσαι'], TER: ['άται']},
                  PL: {PRI: ['ώμεθα', 'όμαστε'], SEC: ['άσθε', 'άστε'], TER: ['ώνται']}},

    CON2B_PASS: {SG: {PRI: ['ούμαι'], SEC: ['είσαι'], TER: ['είται']},
                 PL: {PRI: ['ούμαστε'], SEC: ['είστε'], TER: ['ούνται']}},
    CON2B_PASS_ARCHAIC: {PL: {PRI: ['ούμεθα'], SEC: ['είσθε']}},

    CON2C_PASS: {SG: {PRI: ['άμαι', 'ούμαι'], SEC: ['άσαι'], TER: ['άται']},
                 PL: {PRI: ['ούμαστε', 'όμαστε'], SEC: ['άστε', 'όσαστε'], TER: ['όνται', 'ούνται']}},

    CON2D_PASS: {SG: {PRI: ['μαι'], SEC: ['σαι'], TER: ['ται']}, PL: {PRI: ['μεθα', 'μαστε'], SEC: ['σθε', 'στε'],
                                                                      TER: ['νται']}},
    CON2E_PASS: {SG: {PRI: ['αμαι'], SEC: ['ασαι'], TER: ['αται']}, PL: {PRI: ['άμεθα', 'όμαστε'],
                                                                         SEC: ['ασθε', 'αστε'],
                                                                         TER: ['ανται']}},
    CON2F_PASS: {SG: {PRI: ['ούμαι'], SEC: ['ούσαι'], TER: ['ούται']},
                 PL: {PRI: ['ούμεθα', 'ούμαστε'], SEC: ['ούσθε', 'ούστε'], TER: ['ούνται']}},

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

    PARAT2AK_PASS: {SG: {PRI: ['όμουν'], SEC: ['όσουν'], TER: ['όταν', 'άτο']},
                    PL: {PRI: ['όμασταν', 'όμαστε'], SEC: ['όσαστε', 'όσασταν'],
                         TER: ['όνταν', 'ώντο']}},
    PARAT2B_PASS: {SG: {PRI: ['ούμουν'], SEC: ['ούσουν'], TER: ['ούνταν']},
                   PL: {PRI: ['ούμασταν', 'ούμαστε'], SEC: ['ούσασταν', 'ούσαστε'],
                        TER: ['ούνταν']}},

    PARAT2C_PASS: {SG: {PRI: ['όμουν', 'όμουνα'], SEC: ['όσουν', 'όσουνα'], TER: ['όταν', 'ότανε']},
                   PL: {PRI: ['όμασταν', 'όμαστε'], SEC: ['όσασταν', 'όσαστε'], TER: ['ούνταν', 'όνταν', 'όντουσαν']}},
    PARAT2F_PASS: {SG: {PRI: ['ούμουν'], SEC: ['ούσουν'], TER: ['ούνταν', 'ούτο']},
                   PL: {PRI: ['ούμασταν', 'ούμαστε'], SEC: ['ούσαστε', 'ούσασταν'], TER: ['ούντο', 'ούνταν']}},

    PARAT2D_PASS: {SG: {PRI: ['έμην'], SEC: ['εσο'], TER: ['ετο']},
                   PL: {PRI: ['έμεθα', 'έμασταν', 'έμαστε'], SEC: ['εσθε', 'εστε'], TER: ['εντο']}},
    PARAT2E_PASS: {SG: {PRI: ['άμην'], SEC: ['ασο'], TER: ['ατο']},
                   PL: {PRI: ['άμεθα', 'όμαστε', 'όμασταν'], SEC: ['ασθε', 'αστε'],
                        TER: ['αντο']}},

    IMPER_ACT_CONT_1: {SG: {SEC: ['ε']}, PL: {SEC: ['ετε']}},
    IMPER_ACT_CONT_1B: {PL: {SEC: ['ετε']}},
    IMPER_ACT_EIMAI: {SG: {TER: ['έστω']}},
    IMPER_ACT_CONT_2A: {SG: {SEC: ['α', 'αγε']}, PL: {SEC: ['άτε']}},
    IMPER_ACT_CONT_2B: {SG: {SEC: ['ει']}, PL: {SEC: ['είτε']}},
    IMPER_ACT_CONT_2D: {PL: {SEC: ['ούτε']}},
    IMPER_ACT_CONT_2C: {SG: {SEC: ['γε']}, PL: {SEC: ['γετε', 'τε']}},
    IMPER_PASS_CONT_2D: {SG: {SEC: ['σο']}, PL: {SEC: ['σθε', 'στε']}},
    IMPER_PASS_CONT_2AB: {PL: {SEC: ['άσθε', 'άστε']}},
    IMPER_PASS_CONT_2E: {PL: {SEC: ['ασθε', 'αστε']}},
    IMPER_PASS_CONT_1: {SG: {SEC: ['ου']}, PL: {SEC: ['εστε']}},
    IMPER_PASS_CONT_2A: {PL: {SEC: ['ιέστε']}},
    IMPER_PASS_CONT_2B: {PL: {SEC: ['είστε']}},
    IMPER_PASS_CONT_2C: {PL: {SEC: ['άστε']}},
    IMPER_PASS_CONT_2SA: {PL: {SEC: ['ούσθε', 'ούστε']}},
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

irregular_active_roots = {
    'βρίθω': None,
    'βλέπω': 'δ',
    'έχω': None,
    'καλένω': None,
    'οφείλω': None,
    'ψέν': 'ψήσ',
    'εξέχω': None,
    'ξεδιαλύνω': 'ξεδιαλύσ',
    'ξέρω': None,
    'προπαραγγέλνω': 'προπαραγγείλ',
    'στέκω': None,
    'χρωστάω': None,
    'φτω': None,
    'χρωστώ': None,
    'πρέπει': None,
    'αξίζω': None,
    'φρονώ': None,
    'οπλομαχώ': None,
    'εποφθαλμιώ': None,
    'κραδαίνω': None,
    'βολώ': None,
    'αναλογώ': None,
    'λάμνω': None,
    'αρέσ': 'αρέσ',
    'ανταίνω': 'αντέσ',
    'μέλει': None,
    'θαμπίζω': None,
    'χάσκω': None,
    'τυρβάζω': None,
    'αδημονώ': None,
    'αμερικανίζω': None,
    'αδυνατώ': None,
    'πέτομαι': None,
    'νεοσσεύω': None,
    'παίω': 'παισ',
    'ζευγνύω': 'ζευγνύσ',
    'καίγ': 'κάψ',
    'κορεννύ': 'κορέσ',
    'προσαρτώ': 'προσαρτήσ',
    'κωλύω': None,
    'περεχύνω': None,
    'ακούγω': 'ακούσ',
    'κλαίγω': 'κλάψ',
    'παιδιακίζω': None,
    'ελαύνω': 'ελάσ',
    'θέω': 'τρέξ',
    'σιαλίζω': None,
    'δαγκάν': 'δαγκάσ',
    'παίρν': 'πάρ',
    'ρηγνύω': 'ρήξ',
    'προσήκω': None,
    'παραέχω': None,
    'βγάνω': 'βγάλ',
    'βάνω': 'βάλ',
    'χατίζω': None,
    'πάγω': None,
    'παριστ': 'παραστήσ',
    'μανθάν': 'μάθ',
    'ταλασιουργώ': None,
    'βόσκ': 'βοσκήσ',
    'ταυτογνωμώ': None,
    'κατέχ': 'κατέχ,κατάσχ',
    'απέχ': 'απέχ,απάσχ',
    'ισαπέχ': 'ισαπέχ,ισαπάσχ',
    'μεθύσκ': 'μεθύσ',
    'αγαθοφέρνω': None,
    'υπερέχ': 'υπερέχ,υπεράσχ',
    'επέχ': 'επέχ,επάσχ',
    'εισέχ': 'εισέχ,εισάσχ',
    'συνέχ': 'συνέχ',
    'μέλλει': None,
    'μιμνήσκ': 'μνήσ',
    'ενέχ': 'ενέχ,ενάσχ',
    'υπέχ': 'υπέχ,υπάσχ',
    'παρέχ': 'παράσχ,παρέχ',
    'θεόω': None,
    'δ': 'δεήσ',
    'γινώσκ': 'γνώσ',
    'περιέχ': 'περιέχ',
    'γηράσκ': 'γεράσ',
    'διδράσκ': 'δράσ',
    'απάδω': None,
    'ανήκω': None,
    'βιβρώσκ': 'βρώσ',
    'αντέχ': 'αντέξ',
    'θρώσκ': 'θορ',
    'αρέσκ': 'αρέσκ',
    'ανεβαίν': 'ανέβ,ανεβ',
    'δέ': 'δεήσ',
    'περιμέν': 'περιμέν',
    'πον': 'πονέσ',
    'κατεβαίν': 'κατέβ,κατεβ',
    'αίρ': 'άρ',
    'τιτρώσκ': 'τρώσ',
    'μετέχ': 'μετάσχ,μετέχ',
    'εξέχ': 'εξέχ,εξάσχ',
    'βάλλ': 'βάλ',
    'απολαμβάν': 'απολαύσ',
    'λαμβάν': 'λάβ',
    'γέρν': 'γείρ',
    'χυμ': 'χυμήξ',
    'βάζω': 'βάλ',
    'βγάζω': 'βγάλ',
    'λαβαίν': 'λάβ',
    'αγγέλν': 'αγγείλ',
    'αγγέλλ': 'αγγείλ',
    'στάν': 'στήσ',
    'σταίν': 'στήσ',
    'πίπτ': 'πέσ',
    'φέρν': 'φέρ',
    'φεύγ': 'φύγ',
    'άγ': 'αγάγ',
    'πάσχ': 'πάθ',
    'σέρν': 'σύρ',
    'τέμν': 'τμήσ',
    'εφιστ': 'επιστήσ',
    'καθιστ': 'καταστήσ',
    'λανθάν': 'λάθ',
    'λαγχάνω': 'λάχ',
    'λαχαίν': 'λάχ',
    'αίρν': 'άρ',
    'δίν': 'δώσ',
    'δίδ': 'δώσ',
    'μέν': 'μείν',
    'στέλν': 'στείλ',
    'στέλλ': 'στείλ',
    'πλέν': 'πλύν',
    'βαίνω': 'β',
    'βγαίνω': 'βγ',
    'αυξάν': 'αυξήσ',
    'μεθ': 'μεθύσ',
    'σπέρν': 'σπείρ',
    'αλίσκ': 'αλώσ',
    'μπαίν': 'μπ',
    'μην': 'μηνύσ',
    'πλέ': 'πλεύσ',
    'πνέ': 'πνεύσ',
    'ρέ': 'ρεύσ',
    'βρίσκ': 'βρ',
    'πίν': 'πι',
    'λέ': 'π',
    'λέγ': 'π,λέξ',
    'δέρν': 'δείρ',
    'κλίν': 'κλίν',
    'κάν': 'κάν',
    'μαθαίν': 'μάθ',
    'παθαίν': 'πάθ',
    'πεθαίν': 'πεθάν',
    'θνήσκ': 'θάν',
    'τείν': 'τείν',
    'πέφτ': 'πέσ',
    # 'πέπτ': 'πέσ',
    'κραίνω': None,
    'πηγαίν': 'πά',
    'τυχαίν': 'τύχ',
    'πετυχαίν': 'πετύχ',
    'τυγχάν': 'τύχ',
    'άσχ': 'ασχέσ',
    'τρέφ': 'θρέψ',
    'ελαύν': 'ελάσ',
    'κρέμ': 'κρεμάσ',
    'ευρίσκ': 'εύρ',
    'έχ': 'άσχ',
    'έλκ': 'έλκυσ',
    'θαρρ': 'θαρρέψ',
    'χέ': 'χύσ',
    'νιστ': 'στήσ',
    'ιστάν': 'αστήσ',
    'φρέ': 'φρήσ',
    'σπά': 'σπάσ',
    'θέλ': 'θελήσ',
    'κρίν': 'κρίν',
    'νέμ': 'νείμ',
    'σβεννύω': 'σβήσ',
    'συρρέ': 'συρρεύσ',
    'διαρρέ': 'διαρρεύσ',
    'ρρέω': 'ρρεύσ',
    'δεικνύ': 'δείξ',
    'μειγνύ': 'μείξ',
    'μιγνύ': 'μίξ',
    'ρηγνύ': 'ρήξ',
    'γιγνώσκ': 'γνώσ',
    'πηγνύ': 'πήξ',
    'τρώ': 'φά,φάγ',
    'τρώγ': 'φά,φάγ',
    'έρχ': 'έλθ,έρθ,`ρθ,`λθ',
    'ξανάρχομαι': 'ξαναρθ',
    'κάθ': 'καθίσ,κάτσ',
    'γίν': 'γίν',
    'πά': 'πά',
    'φυλ': 'φυλάξ',
    'παγαίν': 'πά',
    'ομνύω': 'ομόσ',
    'ορώ': 'ιδ',
    'συσπώ': None,
    # 'ανιώ': 'ανιάσ',
    'σφριγώ': None,
    'σοβώ': None,
    # 'χρήζω': None,
    'σκολιώ': 'σκολιάσ',
    'βογκάω': 'βογκήσ,βογκήξ',
    'βογγάω': 'βογγήσ,βογγήξ',
    'βογγώ': 'βογγήσ,βογγήξ',
    'διορώ': None,
    "όζω": None,
    'διαιτώ': 'διατήσ',
    'σαλντώ': 'σαλντήσ',
    'βουρώ': 'βουρήσ',
    'παρατυγχάνω': 'παρατύχ',
    'χραίνω': None
}

irregular_passive_roots = \
    {
        'φυσάω': 'φυσηθ,φυσηχτ',
        'υπέρκειμαι': None,
        'πηγαινόρχομαι': None,
        'πέρδομαι': None,
        'πέτομαι': None,
        'επείγομαι': None,
        'φύομαι': None,
        'αγάλλομαι': None,
        'ίπταμαι': None,
        'φθέγγομαι': None,
        'απόκειμαι': None,
        'εναπόκειμαι': None,
        'ανίπταμαι': None,
        'κωλύομαι': None,
        'πηγαινοέρχομαι': None,
        'τεκμαίρομαι': None,
        'ελαύνω': None,
        'ακκίζομαι': None,
        'ευθύνομαι': None,
        'σπέρνω': 'σπαρ,σπαρθ',
        'οφείλομαι': None,
        'καίγ': 'κάηκ',
        'μειγνύ': 'μειχθ',
        'μιγνύ': 'μιχθ',
        'ομνύω': 'ομοσθ',
        'απεχθάνομαι': None,
        'τιτρώσκ': 'τρωθ',
        'βάζω': 'βαλθ',
        'μάχομαι': None,
        'βάλλ': 'βληθ',
        'βάζ': 'βαλθ',
        'αίρ': 'αρθ',
        'βγάζ': 'βγαλθ',
        'λαμβάν': 'ληφθ',
        'λαβαίν': 'ληφθ',
        'πον': 'πονεθ',
        'μιμνήσκ': 'μνησθ',
        'δεικνύ': 'δειχθ',
        'τέμν': 'τμηθ',
        'ρήγνυ': 'ραγ',
        'ρηγνύ': 'ραγ,ρηχθ,ρηχτ',
        'αίρν': 'αρθ',
        'γράφ': 'γραφ,γραφτ',
        'δέρν': 'δαρθ,δαρ',
        'άσχ': 'ασχεθ',
        'καλ': 'κληθ',
        'εύχ': 'ευχηθ',
        'δίν': 'δοθ',
        'δίδ': 'δοθ',
        'τρίβ': 'τριβ,τριφτ,τριφθ',
        'κλέπτ': 'κλαπ,κλεφτ,κλεφθ',
        'φέρ': 'φερθ',
        'υπόσχ': 'υποσχεθ',
        'κόπτ': 'κοπ',
        'κόβ': 'κοπ,κοφτ',
        'ακού': 'ακουστ',
        'στέλν': 'σταλθ,σταλ',
        'στέλλ': 'σταλθ,σταλ',
        'πλέν': 'πλυθ',
        'καί': 'κα',
        'στέκ': 'σταθ',
        'στήνω': 'στηθ',
        'στήν': 'σταθ,στηθ',
        'οφείλ': 'οφεληθ',
        'πνίγ': 'πνιγ,πνιχτ,πνιχθ',
        'θέτ': 'τεθ',
        'θάβ': 'θαφτ,θαφθ,ταφ',
        'αλλάσσ': 'αλλαγ,αλλαχθ,αλλαχτ',
        'χέ': 'χυθ',
        'βλέπω': 'ιδωθ',
        'λέγ': 'λεγ,λεχθ,λεχτ',
        'τείν': 'ταθ',
        'φαίν': 'φαν',
        'σέρν': 'συρθ',
        'αυξάν': 'αυξηθ',
        'αλίσκ': 'αλωθ',
        'τρέφ': 'τραφ',
        'κρέμ': 'κρεμαστ',
        'βρίσκ': 'βρεθ',
        'τρώ': 'φαγωθ',
        'λέω': 'ειπωθ,λεχθ',
        'λέγω': 'ειπωθ,λεχθ',
        'τρώγ': 'φαγωθ',
        'αφήν': 'αφεθ',
        'τρέπ': 'τραπ',
        'στρέφ': 'στραφ',
        'τίθε': 'τεθ',
        'σέβ': 'σεβαστ',
        'χαίρ': 'χαρ',
        'θιστ': 'ταστ',
        'επαφίε': 'επαφεθ',
        'ίστ': 'στ,ιστ',
        'ιστ': 'στ',
        'θίστ': 'ταστ',
        'έλκ': 'ελκυστ',
        'ακούγ': 'ακουστ',
        'δέ': 'δεηθ',
        'ρρέω': 'ρρευτ',
        'κορεννύω': 'κορεσθ',
        'νιστ': 'στ,σταθ',
        'νίστ': 'στ,σταθ',
        'ρίστ': 'ραστ,ρασταθ',
        'ελαύν': 'ελαθ',
        'ιστάν': 'ασταθ',
        'δείκνυ': 'δειχθ',
        'γιγνώσκ': 'γνωσθ',
        'πηγνύω': 'πυχθ,παγ',
        'ενδείκνυ': 'ενδειχθ',
        'ευρίσκ': 'ευρεθ',
        'σπά': 'σπαστ',
        'φυλ': 'φυλαχτ',
        'άγ': 'αχθ',
        'χρήζω': None,

        'φθείρ': 'φθαρ,φθαρθ',
        'πλήττ': 'πλαγ,πληγ',
        'πλήσσ': 'πλαγ,πληγ',
        'σταίν': 'στ,σταθ',
        'σπείρω': 'σπαρ,σπαρθ',
        'ίσταμαι': 'στ,σταθ',
        "υφίσταμαι": 'υποστ',
        'ανίσταμαι': 'αναστ,ανασταθ',
        'ανθίσταμαι': 'αντιστ',
        'εξίσταμαι': 'εξιστ',
        'ενίσταμαι': 'ενιστ',
        'διίσταμαι': 'διιστ',
        'αφίσταμαι': 'αποστ',
        'αφικν': 'αφιχθ',
        'καταλαβαίνω': None,
        'βαίνω': None}

irregular_passive_perfect_participles = {'άγω': 'ηγμένος',
                                         'έχομαι': None,
                                         'αγανακτώ': 'αγανακτισμένος',
                                         'αποτυχαίνω': 'αποτυχημένος',
                                         'κάνω': 'καμωμένος', 'λανθάνω': 'λανθασμένος',
                                         'αγωνίζομαι': 'αγωνισμένος',
                                         'κάμνω': 'καμωμένος',
                                         'δυστυχώ': 'δυστυχισμένος',
                                         'ευτυχώ': 'ευτυχισμένος',
                                         'αφαιρώ': 'αφηρημένος,αφαιρεμένος',
                                         'ανήκω': None,
                                         'πέτομαι': None,
                                         'δίνω': 'δοσμένος,δεδομένος',
                                         'κάθομαι': 'καθισμένος',
                                         'καίω': 'κεκαυμένος,καμένος,κεκαμμένος',
                                         'θυμάμαι': 'θυμισμένος',
                                         'θυμούμαι': 'θυμισμένος',
                                         'τρώω': 'φαγωμένος',
                                         'αξίζω': None,
                                         'λαμβάνω': 'ειλημμένος',
                                         'λαμβάνομαι': 'ειλημμένος',
                                         'αρέσω': None,
                                         'κερδαίνω': 'κερδαιμένος',
                                         'αστειεύομαι': None,
                                         'βγαίνω': None,
                                         'βρίσκομαι': None,
                                         'γίνομαι': 'γινωμένος',
                                         'τρέπω': 'τετραμμένος',
                                         'σπέρνω': 'σπαρμένος,εσπαρμένος',
                                         'είμαι': None,
                                         "τέμνω": "τμημένος,τετμημένος",
                                         'έρχομαι': None,
                                         'έχω': None,
                                         'τρέφω': 'θρεμμένος',
                                         'τρέφομαι': 'θρεμμένος',
                                         'λέγω': 'ειπωμένος',
                                         'καταλαβαίνω': None,
                                         'κατεβαίνω': None,
                                         'κοιμάμαι': 'κοιμισμένος,κεκοιμημένος',
                                         'κοιμούμαι': 'κοιμισμένος,κεκοιμημένος',
                                         'λέω': 'ειπωμένος',
                                         'μαθαίνω': 'μαθημένος',

                                         'μένω': None,
                                         'κρίνω': 'κριμένος,κεκριμένος',
                                         'μπαίνω': None,
                                         'μπορώ': None,
                                         'νοιάζομαι': 'νοιασμένος',
                                         'παίρνω': 'παρμένος',
                                         'ξέρω': None,
                                         'οφείλω': None,
                                         'πεθαίνω': 'πεθαμένος',
                                         'παριστάνω': None,
                                         'παθαίνω': 'παθημένος',
                                         'πάσχω': 'παθημένος',
                                         'βρίσκω': None,
                                         'περιμένω': None,
                                         'περνάω': 'περασμένος',
                                         'πετυχαίνω': 'πετυχημένος',
                                         'πέφτω': 'πεσμένος',
                                         'πηγαίνω': None,
                                         'πίνω': 'πιωμένος',
                                         'πρέπει': None,
                                         'πρόκειται': None,
                                         'σέβομαι': 'σεβασμένος',
                                         'συμμετέχω': None,
                                         'συμπεριφέρομαι': None,
                                         'συστήνω': 'συστημένος',
                                         'σώζω': 'σωσμένος',
                                         'υπάρχω': None,
                                         'υπόσχομαι': 'υποσχεμένος,υποσχημένος',
                                         'φεύγω': None,
                                         'χρήζω': None,

                                         'βαίνω': None,
                                         'φοβάμαι': 'φοβισμένος',
                                         'φοβούμαι': 'φοβισμένος',
                                         'στήνω': 'στημένος',
                                         'πάγω': None,
                                         'φταίω': None,
                                         'χτυπάω': 'χτυπημένος',
                                         'θέτω': 'τεθειμένος',
                                         'τίθεμαι': 'τεθειμένος'}

irregular_active_aorists = {'εισέχω': "εισείχα",
                            'έχω': 'έσχον',
                            'άρχω': 'ήρξα',
                            'μπαίνω': 'μπήκα',
                            'αναθιβάλλω': 'αναθίβαλα,ανεθίβαλα',
                            'ξανάρχομαι': 'ξανήρθα',
                            'αίρω': 'ήρα',
                            'βγαίνω': 'βγήκα',
                            'βρίσκω': 'βρήκα',
                            'ρηγνύω': 'έρρηξα',
                            'κατεβαίνω': 'κατέβη,κατέβηκα',
                            'ανεβαίνω': 'ανέβηκα, ανέβη',
                            'δίδω': 'έδωσα,έδωκα',
                            'πηγαίνω': 'πήγα',
                            'παίρνω': 'πήρα',
                            'λέω': 'είπα',
                            'ομνύω': 'ώμοσα',
                            'βαίνω': 'βήκα,έβη',
                            'λέγω': 'είπα',
                            'πίνω': 'ήπια',
                            'παίω': 'έπαισα',
                            'ρέω': 'έρρευσα',
                            "επιδράμω": "επέδραμα",
                            'τρώω': 'έφαγα',
                            'τρώγω': 'έφαγα',
                            'βλέπω': 'είδα',
                            'πάω': 'πήγα',
                            'ευρίσκω': 'ηύρα',
                            'παγαίνω': 'πήγα',
                            'καταλαβαίνω': 'κατάλαβα',
                            'καταλαμβάνω': 'κατέλαβα',
                            'κατέχω': 'κατείχα',
                            'συγκατέχω': 'συγκατείχα',
                            'γινώσκω': 'έγνωσα',
                            # 'παρέχω': "παρείχα,παρέσχον"
                            }

irregular_active_paratatikos = {'πάω': 'πήγαινα',
                                'έλκω': 'είλκα',
                                'άρχω': 'ήρχα',
                                'έρπω': 'είρπα',
                                'κατέχω': 'κατείχα,κάτεχα',
                                'φινίρω': 'φινίριζα',
                                'άδω': '',
                                'επείγω': 'ήπειγα',
                                'όζω': '',
                                'δει': 'έδει',
                                'επείγει': 'ήπειγε',
                                'πάγω': 'πήγα',
                                'ρέω': 'έρρεα',
                                "επιδράμω": "επέδραμα",
                                "ανήκω": "ανήκα,άνηκα",
                                'σπάω': 'έσπαγα',
                                'έχω': 'είχα',
                                'εξεύρω': 'ήξευρα',
                                'δαγκάνω': 'δάγκανα',
                                'όψομαι': '',
                                'ορώ': ''}

irregular_passive_aorists = {
    'ομνύω': 'ωμόσθη',
    'φυσάω': 'φυσήθηκα,φυσήχτηκα',
    'αίρομαι': 'άρθηκα', 'ρηγνύω': 'ερράγη',
    'ίσταμαι': 'έστη,στάθηκα',
    'υφίσταμαι': 'υπέστη',
    'ανίσταμαι': 'ανέστη,αναστάθηκα',
    'συνίσταμαι': 'συνέστη',
    'παρίσταμαι': 'παρέστη',
    'αφίσταμαι': 'απέστη',
    'διίσταμαι': 'διέστη',
    'ενίσταμαι': 'ενέστη',
    'εξίσταμαι': 'εξέστη',
    'ανθίσταμαι': 'αντέστη',

}

irregular_passive_paratatikos = {'ίσταμαι': 'ιστάμην',
                                 'υφίσταμαι': 'υφιστάμην',
                                 'ανίσταμαι': 'ανιστάμην',
                                 'εξίσταμαι': 'εξιστάμην',
                                 'ενίσταμαι': 'ενιστάμην',
                                 'διίσταμαι': 'διιστάμην',
                                 'αφίσταμαι': 'αφιστάμην',
                                 'ανίπταμαι': 'ανιπτάμην',
                                 }

deponens_with_active_perf_forms = ['έρχομαι', 'κάθομαι', 'γίνομαι', 'άρχομαι']



ancient_oomai = ['δικαιούμαι', 'οικειούμαι', 'ογκούμαι', 'ισούμαι',
                 'ρικνούμαι', 'θρομβούμαι', 'χρεούμαι',
                 'καρπούμαι', 'διογκούμαι', 'ψιλούμαι', 'ξενούμαι',
                 'πληρούμαι', 'κυρούμαι', 'αξιούμαι',
                 'βιούμαι', 'γομούμαι', 'ζηλούμαι', 'γαγγραινούμαι', 'πελιδνούμαι']

para_detachable_never = ['παραφθείρω', 'παρατρέπω', 'παραφράζω', 'παραπέμπω',
                         'παραβλάπτω', 'παραβάλλω', 'παραγγέλλω',
                         'παραβιάζω', 'παραβαίνω', 'παρακάμπτω', 'παρακούω',
                         'παραλλάζω', 'παρακμάζω', 'παραλύω',
                         'παρατείνω', 'παραπείθω',
                         'παραπέφτω', 'παρασταίνω', 'παραρρέω', 'παρασέρνω',
                         'παραστέκω', 'παραπλέω', 'παραπαίω',
                         'παρασύρω', 'παραλλάσσω', 'παρατάσσω']

para_detachable_only = ['παραβγαίνω', 'παρατρώγω', 'παρατρέχω', 'παραδέρνω',
                        'παραέχω', 'παρακάνω', 'παραλέω',
                        'παραμπαίνω', 'παραρίχνω', 'παραψένω', 'παραψήνω',
                        'παραπίνω', 'παραπαίρνω', 'παρατρώω',
                        'παραχέζω', 'παραβράζω', 'παραγίνομαι', ]

para_detachable_opt = ['παρατρίβω', 'παρακάθομαι',
                       'παραφέρνω', 'παραβλέπω', 'παραγράφω',
                       'παραδίνω', 'παραθέτω', 'παραμένω',
                       'παραχώνω', 'παραπείθω',
                       ]

verbs_dif_para = ["παραλείπω", "παρατρίβω", "παραβλέπω", "παραγράφω", "παρακάθομαι", "παραδίνω", "παραθέτω", "παραμένω"]