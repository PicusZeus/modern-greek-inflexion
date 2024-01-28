from .variables import *

conjugations = {
    EIMAI: {SG: {PRI: ['είμαι'], SEC: ['είσαι'], TER: ['είναι']},
            PL: {PRI: ['είμαστε'], SEC: ['είστε', 'είσαστε'], TER: ['είναι']}},
    EIMAI_PARATATIKOS: {SG: {PRI: ['ήμουν', 'ήμουνα'], SEC: ['ήσουν', 'ήσουνα'], TER: ['ήταν', 'ήτο', 'ήτανε']},
                        PL: {PRI: ['ήμαστε', 'ήμασταν'], SEC: ['ήσαστε', 'ήσασταν'], TER: ['ήταν', 'ήσαν', 'ήτανε']}},
    CON1_ACT: {SG: {PRI: ['ω'], SEC: ['εις'], TER: ['ει']}, PL: {PRI: ['ουμε'], SEC: ['ετε'], TER: ['ουν', 'ουνε']}},
    CON2A_ACT: {SG: {PRI: ['ώ', 'άω'], SEC: ['άς'], TER: ['ά', 'άει']},
                PL: {PRI: ['ούμε', 'άμε'], SEC: ['άτε'], TER: ['άνε', 'άν', 'ούν', 'ούνε']}},
    CON2A_ACT_LOGIA: {SG: {PRI: ['ώ'], SEC: ['άς'], TER: ['ά']},
                      PL: {PRI: ['ούμε', 'άμε'], SEC: ['άτε'], TER: ['ούν']}},
    CON2B_ACT: {SG: {PRI: ['ώ'], SEC: ['είς'], TER: ['εί']}, PL: {PRI: ['ούμε'], SEC: ['είτε'], TER: ['ούνε', 'ούν']}},
    CON2C_ACT: {SG: {PRI: ['ω'], SEC: ['ς'], TER: ['ει']}, PL: {PRI: ['με'], SEC: ['τε'], TER: ['νε', 'ν']}},
    CON2D_ACT: {SG: {PRI: ['ώ'], SEC: ['οίς'], TER: ['οί']},
                PL: {PRI: ['ούμε', 'ούμεν'], SEC: ['ούτε'], TER: ['ούν']}},
    CON1_ACT_MODAL: {SG: {TER: ['ει']}},
    CON2_ACT_MODAL: {SG: {TER: ['εί']}},

    CON1_PASS: {SG: {PRI: ['ομαι'], SEC: ['εσαι'], TER: ['εται']},
                PL: {PRI: ['όμαστε'], SEC: ['εστε', 'όσαστε'], TER: ['ονται']}},
    CON1_PASS_ARCHAIC: {SG: {PRI: ['ομαι'], SEC: ['εσαι'], TER: ['εται']},
                        PL: {PRI: ['όμεθα'], SEC: ['εσθε'], TER: ['ονται']}},
    CON2A_PASS: {SG: {PRI: ['ιέμαι'], SEC: ['ιέσαι'], TER: ['ιέται']},
                 PL: {PRI: ['ιόμαστε', 'ιούμαστε'], SEC: ['ιέστε', 'ιόσαστε'], TER: ['ιούνται', 'ιόνται']}},
    CON2AB_PASS: {SG: {PRI: ['ώμαι'], SEC: ['άσαι'], TER: ['άται']}, PL: {PRI: ['όμαστε'], SEC: ['άστε'],
                                                                          TER: ['ώνται']}},

    CON2B_PASS: {SG: {PRI: ['ούμαι'], SEC: ['είσαι'], TER: ['είται']},
                 PL: {PRI: ['ούμαστε', 'ούμεθα'], SEC: ['είστε', 'είσθε'], TER: ['ούνται']}},
    CON2C_PASS: {SG: {PRI: ['άμαι'], SEC: ['άσαι'], TER: ['άται']},
                 PL: {PRI: ['όμαστε'], SEC: ['άστε', 'όσαστε'], TER: ['ούνται']}},
    CON2SA_PASS: {SG: {PRI: ['ούμαι'], SEC: ['ούσαι'], TER: ['ούται']},
                  PL: {PRI: ['ούμεθα', 'ούμαστε'], SEC: ['ούσθε', 'ούστε'],TER: ['ούνται']}},
    CON2D_PASS: {SG: {PRI: ['μαι'], SEC: ['σαι'], TER: ['ται']}, PL: {PRI: ['μεθα'], SEC: ['σθε'],
                                                                      TER: ['νται']}},
    CON2E_PASS: {SG: {PRI: ['αμαι'], SEC: ['ασαι'], TER: ['αται']}, PL: {PRI: ['άμεθα', 'όμαστε'],
                                                                         SEC: ['ασθε'],
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
    PARAT2B_PASS: {SG: {PRI: ['ούμουν'], SEC: ['ούσουν'], TER: ['είτο', 'ούνταν']},
                   PL: {PRI: ['ούμασταν', 'ούμαστε'], SEC: ['ούσασταν', 'ούσαστε'],
                        TER: ['ούνταν', 'ούντο']}},
    PARAT2B_PASS_LOGIA: {SG: {PRI: ['ούμην'], SEC: ['είσο'], TER: ['είτο']},
                         PL: {PRI: ['ούμεθα'], SEC: ['είσθε'], TER: ['ούντο']}},
    PARAT2C_PASS: {SG: {PRI: ['όμουν', 'όμουνα'], SEC: ['όσουν', 'όσουνα'], TER: ['όταν', 'ότανε']},
                   PL: {PRI: ['όμασταν', 'όμαστε'], SEC: ['όσασταν', 'όσαστε'], TER: ['ούνταν', 'όντουσαν']}},
    PARAT2SA_PASS: {SG: {PRI: ['ούμουν', 'ούμην'], SEC: ['ούσουν', 'ούσο'], TER: ['ούνταν', 'ούτο']},
                    PL: {PRI: ['ούμασταν', 'ούμαστε'], SEC: ['ούσαστε', 'ούσασταν'], TER: ['ούντο', 'ούνταν']}},

    PARAT2D_PASS: {SG: {PRI: ['όμουν', 'έμην'], SEC: ['όσουν', 'εσο'], TER: ['όταν', 'ετο']},
                   PL: {PRI: ['όμασταν', 'έμεθα'], SEC: ['όσασταν', 'εσθε'], TER: ['ούνταν', 'εντο']}},
    PARAT2E_PASS: {SG: {PRI: ['άμην'], SEC: ['ασο'], TER: ['ατο']},
                   PL: {PRI: ['άμεθα', 'όμαστε', 'όμασταν'], SEC: ['ασθε'],
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
    'έχω': None, 'καλένω': None,
    'οφείλω': None, 'ψέν': 'ψήσ',
    'εξέχω': None, 'ξεδιαλύνω': 'ξεδιαλύσ',
    'ξέρω': None, 'προπαραγγέλνω': 'προπαραγγείλ',
    'στέκω': None,
    'χρωστάω': None, 'φτω': None,
    'χρωστώ': None,
    'πρέπει': None,
    'αξίζω': None,
    'φρονώ': None,
    'οπλομαχώ': None,
    'εποφθαλμιώ': None,
    'κραδαίνω': None,
    'αναλογώ': None, 'φινίρω': 'φινιρίσ',
    'λάμνω': None, 'αρέσ': 'αρέσ', 'ανταίνω': 'αντέσ',
    'μέλει': None,
    'θαμπίζω': None,
    'χάσκω': None,
    'τυρβάζω': None,
    'αδημονώ': None,
    'αμερικανίζω': None,
    'αδυνατώ': None, 'πέτομαι': None,
    'νεοσσεύω': None, 'παίω': 'παισ', 'ζευγνύω': 'ζευγνύσ',
    'καίγ': 'κάψ', 'κορεννύ': 'κορέσ', 'προσαρτώ': 'προσαρτήσ',
    'κωλύω': None, 'περεχύνω': None, 'ακούγω': 'ακούσ', 'κλαίγω': 'κλάψ',
    'παιδιακίζω': None, 'ελαύνω': 'ελάσ', 'θέω': 'τρέξ',
    'σιαλίζω': None, 'δαγκάν': 'δαγκάσ', 'παίρν': 'πάρ', 'ρηγνύω': 'ρήξ',
    'προσήκω': None, 'παραέχω': None, 'βγάνω': 'βγάλ', 'βάνω': 'βάλ',
    'χατίζω': None, 'πάγω': None, 'παριστ': 'παραστήσ', 'μανθάν': 'μάθ',
    'ταλασιουργώ': None, 'βόσκ': 'βοσκήσ',
    'ταυτογνωμώ': None, 'κατέχ': 'κατέχ,κατάσχ', 'απέχ': 'απέχ,απάσχ', 'ισαπέχ': 'ισαπέχ,ισαπάσχ', 'μεθύσκ': 'μεθύσ',
    'αγαθοφέρνω': None, 'υπερέχ': 'υπερέχ,υπεράσχ', 'επέχ': 'επέχ,επάσχ', 'εισέχ': 'εισέχ,εισάσχ', 'συνέχ': 'συνέχ',
    'μέλλει': None, 'μιμνήσκ': 'μνήσ', 'ενέχ': 'ενέχ,ενάσχ', 'υπέχ': 'υπέχ,υπάσχ', 'παρέχ': 'παράσχ,παρέχ',
    'θεόω': None, 'δ': 'δεήσ', 'γινώσκ': 'γνώσ', 'περιέχ': 'περιέχ', 'γηράσκ': 'γεράσ', 'διδράσκ': 'δράσ',
    'απάδω': None, 'ανήκω': None, 'βιβρώσκ': 'βρώσ', 'αντέχ': 'αντέξ', 'θρώσκ': 'θορ', 'αρέσκ': 'αρέσκ',
    'ανεβαίν': 'ανέβ,ανεβ', 'δέ': 'δεήσ', 'περιμέν': 'περιμέν', 'πον': 'πονέσ', 'κατεβαίν': 'κατέβ,κατεβ',
    'αίρ': 'άρ', 'τιτρώσκ': 'τρώσ', 'μετέχ': 'μετάσχ,μετέχ', 'εξέχ': 'εξέχ,εξάσχ',
    'βάλλ': 'βάλ', 'απολαμβάν': 'απολαύσ', 'λαμβάν': 'λάβ', 'γέρν': 'γείρ', 'χυμ': 'χυμήξ',
    'βάζω': 'βάλ', 'βγάζω': 'βγάλ', 'λαβαίν': 'λάβ', 'αγγέλν': 'αγγείλ', 'αγγέλλ': 'αγγείλ',
    'στάν': 'στήσ', 'σταίν': 'στήσ', 'πίπτ': 'πέσ', 'φέρν': 'φέρ', 'φεύγ': 'φύγ', 'άγ': 'αγάγ',
    'πάσχ': 'πάθ', 'σέρν': 'σύρ', 'τέμν': 'τμήσ', 'εφιστ': 'επιστήσ',
    'καθιστ': 'καταστήσ', 'λανθάν': 'λάθ', 'λαγχάνω': 'λάχ', 'λαχαίν': 'λάχ', 'αίρν': 'άρ',
    'δίν': 'δώσ', 'δίδ': 'δώσ', 'μέν': 'μείν', 'στέλν': 'στείλ', 'στέλλ': 'στείλ', 'πλέν': 'πλύν',
    'βαίνω': 'β', 'βγαίνω': 'βγ', 'αυξάν': 'αυξήσ', 'μεθ': 'μεθύσ', 'σπέρν': 'σπείρ', 'αλίσκ': 'αλώσ',
    'μπαίν': 'μπ', 'μην': 'μηνύσ', 'πλέ': 'πλεύσ', 'πνέ': 'πνεύσ', 'ρέ': 'ρεύσ', 'βρίσκ': 'βρ',
    'πίν': 'πι', 'λέ': 'π', 'λέγ': 'π,λέξ', 'δέρν': 'δείρ', 'κλίν': 'κλίν',
    'κάν': 'κάν', 'μαθαίν': 'μάθ', 'παθαίν': 'πάθ', 'πεθαίν': 'πεθάν', 'βλέπ': 'δ,ίδ|βλέψ', 'θνήσκ': 'θάν',
    'τείν': 'τείν', 'πέφτ': 'πέσ', 'πέπτ': 'πέσ', 'πηγαίν': 'πά', 'τυχαίν': 'τύχ', 'πετυχαίν': 'πετύχ',
    'τυγχάν': 'τύχ', 'άσχ': 'ασχέσ', 'τρέφ': 'θρέψ', 'ελαύν': 'ελάσ', 'κρέμ': 'κρεμάσ', 'ευρίσκ': 'εύρ',
    'έχ': 'άσχ', 'έλκ': 'έλκυσ', 'θαρρ': 'θαρρέψ', 'χέ': 'χύσ', 'νιστ': 'στήσ', 'ιστάν': 'αστήσ', 'φρέ': 'φρήσ',
    'σπά': 'σπάσ', 'θέλ': 'θελήσ', 'κρίν': 'κρίν', 'νέμ': 'νείμ', 'σβεννύω': 'σβήσ', 'συρρέ': 'συρρεύσ',
    'διαρρέ': 'διαρρεύσ', 'ρρέω': 'ρρεύσ',
    'δεικνύ': 'δείξ', 'μειγνύ': 'μείξ', 'μιγνύ': 'μίξ', 'ρηγνύ': 'ρήξ', 'γιγνώσκ': 'γνώσ', 'πηγνύ': 'πήξ',
    'τρώ': 'φά,φάγ',
    'τρώγ': 'φά,φάγ', 'πά': 'πά', 'φυλ': 'φυλάξ', 'παγαίν': 'πά', 'ομνύω': 'ομόσ'}

irregular_passive_roots = \
    {'υπέρκειμαι': None,
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
     'έρχ': 'έλθ,έρθ,`ρθ,`λθ',
     'κάθ': 'καθίσ,κάτσ',
     'γίν': 'γίν',
     'καί': 'κα',
     'στέκ': 'σταθ',
     'στήν': 'σταθ',
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
     'αφικν': 'αφιχθ'}

irregular_passive_perfect_participles = {'άγω': 'ηγμένος', 'έχομαι': None, 'αγανακτώ': 'αγανακτισμένος',
                                         'αποτυχαίνω': 'αποτυχημένος', 'κάνω': 'καμωμένος', 'λανθάνω': 'λανθασμένος',
                                         'αγαπάω': 'αγαπημένος', 'αγωνίζομαι': 'αγωνισμένος', 'κάμνω': 'καμωμένος',
                                         'δυστυχώ': 'δυστυχισμένος', 'ευτυχώ': 'ευτυχισμένος', 'θυμώνω': 'θυμωμένος',
                                         'αγοράζω': 'αγορασμένος', 'αφαιρώ': 'αφηρημένος', 'αισθάνομαι': 'αισθαμένος',
                                         'ακολουθώ': 'ακολουθημένος', 'ακούω': 'ακουσμένος', 'αλλάζω': 'αλλαγμένος',
                                         'ανάβω': 'αναμμένος', 'αναγκάζω': 'αναγκασμένος', 'ανήκω': None,
                                         'πέτομαι': None,
                                         'δίνω': 'δοσμένος,δεδομένος', 'κάθομαι': 'καθισμένος',
                                         'καίω': 'κεκαυμένος,καμένος,κεκαμμένος',
                                         'κλαίω': 'κλαμένος', 'βάλλω': 'βεβλημένος', 'θυμάμαι': 'θυμισμένος',
                                         'τρώω': 'φαγωμένος', 'στρέφω': 'στραμμένος', 'ανοίγω': 'ανοιγμένος',
                                         'αξίζω': None, 'απαγορεύω': 'απαγορευμένος', 'απαντάω': 'απαντημένος',
                                         'αποκτώ': 'αποκτημένος', 'αποτελούμαι': 'αποτελεσμένος',
                                         'λαμβάνω': 'ειλημμένος',
                                         'αποφασίζω': 'αποφασισμένος', 'αρέσω': None, 'κερδαίνω': 'κερδαιμένος',
                                         'βρέχω': 'βρεγμένος', 'αστειεύομαι': None, 'αφήνω': 'αφημένος',
                                         'βάζω': 'βαλμένος', 'βάφω': 'βαμμένος', 'βαριέμαι': 'βαρεμένος',
                                         'βγάζω': 'βγαλμένος', 'βγαίνω': None, 'βιάζομαι': 'βιασμένος',
                                         'βλέπω': 'ιδωμένος', 'βοηθάω': 'βοηθημένος', 'βρίσκομαι': None,
                                         'βράζω': 'βρασμένος', 'γδύνω': 'γδυμένος', 'γελάω': 'γελασμένος',
                                         'γεμίζω': 'γεμισμένος', 'γεννάω': 'γεννημένος', 'γίνομαι': 'γινωμένος',
                                         'γυρίζω': 'γυρισμένος', 'τρέπω': 'τετραμμένος',
                                         'σπέρνω': 'σπαρμένος,εσπαρμένος',
                                         'δανείζω': 'δανεισμένος', 'δείχνω': 'δειγμένος', 'δένω': 'δεμένος',
                                         'δέχομαι': 'δεχτός, δεκτός', 'διαβάζω': 'διαβασμένος',
                                         'διαλέγω': 'διαλεγμένος', 'διαμαρτύρομαι': 'διαμαρτυρημένος', 'διαφωνώ': None,
                                         'διηγούμαι': 'διηγημένος', 'διορθώνω': 'διορθωμένος', 'διψάω': 'διψασμένος',
                                         'διώχνω': 'διωγμένος', 'δοκιμάζω': 'δοκιμασμένος',
                                         'είμαι': None, 'εκφράζω': 'εκφρασμένος', "τέμνω": "τμημένος,τετμημένος",
                                         'εμφανίζομαι': 'εμφανισμένος', 'εξηγώ': 'εξηγημένος',
                                         'εξαφανίζομαι': 'εξαφανισμένος', 'επηρεάζω': 'επηρεασμένος',
                                         'επιτρέπω': 'επιτετραμμένος', 'έρχομαι': None, 'ετοιμάζω': 'ετοιμασμένος',
                                         'έχω': None, 'ζεσταίνω': 'ζεσταμένος', 'ζηλεύω': 'ζηλεμένος',
                                         'ζητάω': 'ζητημένος', 'ζω': 'βιωμένος', 'τρέφω': 'θρεμμένος',
                                         'τρέφομαι': 'θρεμμένος',
                                         'καθαρίζω': 'καθαρισμένος', 'καλώ': 'καλεσμένος',
                                         'καταλαβαίνω': None, 'καταστρέφω': 'κατεστραμμένος',
                                         'κατεβάζω': 'κατεβασμένος', 'κατεβαίνω': None, 'κερνάω': 'κερασμένος',
                                         'κλείνω': 'κλεισμένος', 'κόβω': 'κομμένος', 'κοιμάμαι': 'κοιμισμένος',
                                         'κοιτάζω': 'κοιταγμένος', 'κουράζω': 'κουρασμένος', 'κρατάω': 'κρατημένος',
                                         'κρύβω': 'κρυμμένος', 'λέω': 'ειπωμένος', 'λύνω': 'λυμένος',
                                         'λυπάμαι': 'λυπημένος', 'μαγειρεύω': 'μαγειρεμένος', 'μαζεύω': 'μαζεμένος',
                                         'μαθαίνω': 'μαθημένος', 'μένω': None, 'κρίνω': 'κριμένος,κεκριμένος',
                                         'μοιράζω': 'μοιρασμένος', 'μπαίνω': None, 'μπορώ': None, 'νικάω': 'νικημένος',
                                         'νοιάζομαι': 'νοιασμένος', 'παίρνω': 'παρμένος',
                                         'ντύνω': 'ντυμένος', 'ξαπλώνω': 'ξαπλωμένος', 'ξεκινάω': 'ξεκινημένος',
                                         'ξέρω': None, 'ξεχνάω': 'ξεχασμένος', 'ξυπνάω': 'ξυπνημένος',
                                         'ξυρίζω': 'ξυρισμένος', 'οδηγώ': 'οδηγημένος', 'ονειρεύομαι': 'ονειρεμένος',
                                         'ονομάζω': 'ονομασμένος', 'οφείλω': None, 'πεθαίνω': 'πεθαμένος',
                                         'παίζω': None, 'παντρεύομαι': 'παντρεμένος',
                                         'παραπονιέμαι': 'παραπονεμένος', 'παριστάνω': None,
                                         'παθαίνω': 'παθημένος', 'πάσχω': 'παθημένος', 'πείθω': 'πεπεισμένος',
                                         'πεινάω': 'πεινασμένος', 'βρίσκω': None,
                                         'περιμένω': None, 'περνάω': 'περασμένος', 'περπατάω': 'περπατημένος',
                                         'πετυχαίνω': 'πετυχημένος', 'πετάω': 'πεταγμένος', 'πέφτω': 'πεσμένος',
                                         'πηγαίνω': None, 'πιάνω': 'πιασμένος', 'πιέζω': 'πιεσμένος',
                                         'πίνω': 'πιωμένος', 'πλένω': 'πλυμένος',
                                         'πληρώνω': 'πληρωμένος', 'πονάω': 'πονεμένος', 'πουλάω': 'πουλημένος',
                                         'πρέπει': None, 'πρόκειται': None, 'προκύπτω': None,
                                         'προσθέτω': 'προστεθειμένος', 'προσποιούμαι': 'προσποιημένος',
                                         'προτείνω': 'προτεταμένος', 'προτιμάω': 'προτιμημένος', 'ράβω': 'ραμμένος',
                                         'ρίχνω': 'ριγμένος', 'ρωτάω': 'ρωτημένος', 'σβήνω': 'σβησμένος',
                                         'σβεννύω': 'σβησμένος',
                                         'σέβομαι': 'σεβασμένος', 'σηκώνω': 'σηκωμένος', 'σημαίνω': None,
                                         'σκεπάζω': 'σκεπασμένος', 'σκέφτομαι': None, 'σκοτώνω': 'σκοτωμένος',
                                         'σκουπίζω': 'σκουπισμένος', 'σπουδάζω': 'σπουδασμένος', 'στέλνω': 'σταλμένος',
                                         'στενοχωριέμαι': 'στενοχωρημένος', 'συμμετέχω': None, 'συμπεριφέρομαι': None,
                                         'συμφωνώ': 'συμφωνημένος', 'στηρίζω': 'στηριγμένος',
                                         'συνηθίζω': 'συνηθισμένος', 'συστήνω': 'συστημένος', 'σώζω': 'σωσμένος',
                                         'τρελαίνομαι': 'τρελαμένος', 'υπάρχω': None,
                                         'υπόσχομαι': 'υποσχεμένος', 'υποφέρω': 'υποσχεμένος',
                                         'υποψιάζομαι': 'υποψιασμένος', 'φαντάζομαι': 'φαντασμένος',
                                         'φέρνω': 'φερμένος', 'φεύγω': None, 'φοβάμαι': 'φοβισμένος',
                                         'φοράω': 'φορεμένος', 'στήνω': 'στημένος', 'πάγω': None,
                                         'φταίω': 'φοβημένος', 'φτιάχνω': 'φτιαγμένος',
                                         'χαίρομαι': 'χαρούμενος', 'χάνω': 'χαμένος',
                                         'χρησιμοποιώ': 'χρησιμοποιημένος', 'χρωστάω': None, 'χτυπάω': 'χτυπημένος',
                                         'ψάχνω': 'ψαγμένος', 'ωφελώ': 'ωφελημένος',
                                         'θέτω': 'τεθειμένος', 'τίθεμαι': 'τεθειμένος'}

irregular_active_aorists = {'εισέχω': "εισείχα", 'μπαίνω': 'μπήκα',
                            'αναθιβάλλω': 'αναθίβαλα,ανεθίβαλα',
                            'αίρω': 'ήρα', 'βγαίνω': 'βγήκα', 'βρίσκω': 'βρήκα', 'ρηγνύω': 'έρρηξα',
                            'κατεβαίνω': 'κατέβη,κατέβηκα',
                            'ανεβαίνω': 'ανέβηκα, ανέβη',
                            'πηγαίνω': 'πήγα', 'παίρνω': 'πήρα', 'λέω': 'είπα', 'ομνύω': 'ώμοσα', 'βαίνω': 'βήκα,έβη',
                            'λέγω': 'είπα', 'πίνω': 'ήπια', 'παίω': 'έπαισα', 'ρέω': 'έρρευσα', "επιδράμω": "επέδραμα",
                            'τρώω': 'έφαγα', 'τρώγω': 'έφαγα', 'βλέπω': 'είδα', 'πάω': 'πήγα', 'ευρίσκω': 'ηύρα',
                            'παγαίνω': 'πήγα',
                            'καταλαβαίνω': 'κατάλαβα', 'καταλαμβάνω': 'κατέλαβα', 'κατέχω': 'κατείχα',
                            'συγκατέχω': 'συγκατείχα', 'γινώσκω': 'έγνωσα'}

irregular_active_paratatikos = {'πάω': 'πήγαινα', 'έλκω': 'είλκα', 'άρχω': 'ήρχα',
                                'έρπω': 'είρπα',
                                'φινίρω': 'φινίριζα',
                                'άδω': '',
                                'πάγω': 'πήγα', 'ρέω': 'έρρεα', "επιδράμω": "επέδραμα",
                                "ανήκω": "ανήκα,άνηκα",
                                'σπάω': 'έσπαγα', 'έχω': 'είχα', 'εξεύρω': 'ήξευρα',
                                'δαγκάνω': 'δάγκανα', 'όψομαι': ''}

irregular_passive_aorists = {'λέω': 'ειπώθηκα', 'λέγω': 'ειπώθηκα', 'ομνύω': 'ωμόσθη',
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

deponens_with_active_perf_forms = ['έρχομαι', 'κάθομαι', 'γίνομαι']

prefixes_detachable = {'πολυ': 'πολυ', 'καλα': 'καλα', 'κουτσο': 'κουτσο', 'ξανα': 'ξανα',
                       'κρουστο': 'κρουστο', 'λαθρ': 'λαθρ', 'αιματο': 'αιματο',
                       'αγανο': 'αγανο', 'πρωτο': 'πρωτο', 'xolo': 'χολο', 'ανα': 'αν',
                       'προικο': 'προικο', 'λογο': 'λογο', 'λαθρα': 'λαθρα', "αλληλο": "αλληλο",
                       'περνο': 'περνο', 'κακο': 'κακο', 'καταπρο': 'καταπρο', 'επανα': 'επαν',
                       'ξερο': 'ξερο', 'αγγελο': 'αγγελο', 'καλο': 'καλο', 'ηρωο': 'ηρωο', 'ψευτο': 'ψευτο',
                       'μαυρο': 'μαυρο', 'αγγλο': 'αγγλο', 'ψιλο': 'ψιλο', 'φωτοσυν': 'φωτοσυν',
                       'ματα': 'ματα', 'κρυφ': 'κρυφ', 'αυτο': 'αυτο', 'βαριο': 'βαριο', 'παπαδο': 'παπαδο',
                       'ματ': 'ματ', 'κωδωνο': 'κωδωνο', 'διαολο': 'διαολο', 'αιμο': 'αιμο',
                       'υδρο': 'υδρο', 'παραεισ': 'παραεισ', 'ξε': 'ξ', 'αραβο': 'αραβο', 'αιτιο': 'αίτιο', 'ετερο': 'ετερο'}

prefixes_detachable_weak = {'επαναπροσ': 'επαναπροσ', 'διασυμπερι': 'διασυμπερι', 'αναπροσ': 'αναπροσ',
                            'προσ': 'προσ', 'παρα': 'παρα',
                            'υπερ': "υπερ", 'εξ': 'εξ', 'εκ': 'εξ', 'ξε': 'ξ', 'επανα': 'επαν', 'εναπο': 'εναπ',
                            'ψιλ': 'ψιλ'}

# for automatic augmentation of regular stems
prefixes_before_augment = {'ανα': 'αν', 'διακατ': 'διακατ', 'αν': 'αν', 'δια': 'δι', 'δι': 'δι', 'εκ': 'εξ',
                           'παρεισ': 'παρεισ',
                           'συλ': 'συν', 'εμπερι': 'εμπερι', 'επανεξ': 'επανεξ', 'επανεκ': 'επανεξ',
                           'παραεισ': 'παραεισ',
                           'απο': 'απ', 'κακο': 'κακο', 'καλο': 'καλο', 'αντικατα': 'αντικατ', 'συναπο': 'συναπ',
                           'επανεισ': 'επανεισ',
                           'απ': 'απ', 'ισαπ': 'ισαπ', 'προ': 'προ', 'κατα': 'κατ', 'κατ': 'κατ', 'πρωτο': 'πρωτο',
                           'αναπαρα': 'αναπαρ', 'περισυν': 'περισυν', 'διεξ': 'διεξ', 'υπεξ': 'υπεξ', 'μετεγ': 'μετεν',
                           'παρ': 'παρ', 'προσ': 'προσ', 'μετα': 'μετ', 'μετ': 'μετ', 'υποκατα': 'υποκατ',
                           'αποκατα': 'αποκατ',
                           'επανεγκατα': 'επανεγκατ', 'μετεγκατα': 'μετεγκατ', 'απεγκατα': 'απεγκατ',
                           'ανασυν': 'ανασυν',
                           'προεκ': 'προεξ', 'ενδια': 'ενδι', 'ενδι': 'ενδι', 'περι': 'περι', 'υπο': 'υπ',
                           'παρεκ': 'παρεξ',
                           'υπ': 'υπ', 'αμφι': 'αμφ', 'επι': 'επ', 'επ': 'επ', 'εισ': 'εισ', 'συμ': 'συν',
                           'καταπρο': 'καταπρο',
                           'συγ': 'συν', 'συ': 'συν', 'συν': 'συν', 'ελ': 'εξ', 'πολυ': 'πολυ', 'αντιπαρα': 'αντιπαρ',
                           'ματ': 'ματ', 'απεγ': 'απεν',
                           'επεμ': 'επεν', 'υπερ': 'υπερ', 'προεξ': 'προεξ', 'αυτοκατα': 'αυτοκατ', 'συγκατα': 'συγκατ',
                           'υπεκ': 'υπεξ',
                           'επεν': 'επεν', 'επεγ': 'επεν', 'παρεμ': 'παρεν', 'παρεν': 'παρεν', 'παρεγ': 'παρεν',
                           'ξεδια': 'ξεδια',
                           'εν': 'εν', 'εμ': 'εν', 'εγ': 'εν', 'εγκατα': 'εγκατ', 'υφ': 'υφ', 'επισυμ': 'επισυν',
                           "προεν": 'προεν', 'ανακατα': 'ανακατ',
                           'καλα': 'καλα', 'κουτσο': 'κουτσο', 'ξανα': 'ξανα', 'εξ': 'εξ', 'συμμετ': 'συμμετ',
                           'διασυμ': 'διασυν', 'συνυπo': 'συνυπ',
                           'επανα': 'επαν', 'επαν': 'επαν', 'αντι': 'αντ', 'αντ': 'αντ', 'περιδια': 'περιδι',
                           'ξαπο': 'ξαπ', 'προκατα': 'προκατ',
                           'αποδια': 'αποδι', 'ανταπο': 'ανταπ', 'συνεφ': 'συνεφ', 'παρα': 'παρ', 'επαναπο': 'επαναπ',
                           'διεμ': 'διεν', 'αντιδια': 'αντιδι', 'αναδια': 'αναδι'}
