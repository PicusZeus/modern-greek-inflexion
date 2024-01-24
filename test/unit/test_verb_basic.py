from unittest import TestCase, main

from icecream import ic

# from icecream import ic

from modern_greek_inflexion.exceptions import NotInGreekException
from modern_greek_inflexion import verb

verbs = ['εγκαταλείπω', 'βλέπω', 'λάμπω', 'λείπω', 'παραλείπω', 'προβλέπω', 'μετατρέπω', 'εκτρέπω', 'ρέπω', 'ελλείπω', 'ξαναβλέπω', 'ανατρέπω', 'παρατρέπω', 'μέλπω', 'θάλπω', 'προπέμπω', 'παραπέμπω', 'σπω', 'υποθάλπω', 'υποβλέπω', 'διέπω', 'διαβλέπω', 'επαναβλέπω', 'εκπέμπω', 'καταλάμπω', 'καταλείπω', 'εκλείπω', 'διαλείπω', 'καλοβλέπω', 'πρέπω', 'διαλάμπω', 'διαπρέπω', 'καταπέμπω', 'επιβλέπω', 'επιτρέπω', 'δρέπω', 'παραβλέπω', 'τέρπω', 'έρπω', 'αμφιρρέπω', 'αναβλέπω', 'αναλάμπω', 'τρέπω', 'προτρέπω', 'αναπέμπω', 'πέμπω', 'περιθάλπω', 'περιλάμπω', 'περιβλέπω', 'αντιλάμπω', 'αποτρέπω', 'αποπέμπω', 'αποβλέπω', 'απολείπω', 'προσβλέπω', 'πρωτοβλέπω', 'αγγελοβλέπω', 'επαναπέμπω', 'υφέρπω', 'σκέπω', 'συχνοβλέπω', 'αναμέλπω', 'ματαβλέπω', 'εκλάμπω', 'επανεκπέμπω']
def print_verbs():
    for v in verbs:
        ic(v)
        ic(verb.create_basic_forms(v))


class VerbTestBasic(TestCase):

    def test_verb_elkw(self):
        self.assertDictEqual(
            verb.create_basic_forms('έλκω'),
        {'act_pres_participle': {'έλκοντας'},
             'aorist': {'active': {'έλξα'}, 'passive': {'ελκύσθηκα', 'ελκύστηκα'}},
             'conjunctive': {'active': {'έλξω'}, 'passive': {'ελκυσθώ', 'ελκυστώ'}},
             'modal': False,
             'paratatikos': {'active': {'είλκα'}, 'passive': {'ελκόμουν'}},
             'pass_pres_participle': {'ελκόμενος'},
             'passive_perfect_participle': {'ελεγμένος'},
             'present': {'active': {'έλκω'}, 'passive': {'έλκομαι'}}}

        )

    def test_verb_wolodernw(self):
        self.assertDictEqual(
            verb.create_basic_forms('βωλοδέρνω'),
            {'act_pres_participle': {'βωλοδέρνοντας'},
             'aorist': {},
             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'βωλόδερνα'}},
             'present': {'active': {'βωλοδέρνω'}}})

    def test_verb_ksanalegw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ξαναλέγω'),
            {'act_pres_participle': {'ξαναλέγοντας'},
             'aorist': {'active': {'ξαναείπα'}, 'passive': {'ξαναειπώθηκα'}},
             'arch_act_pres_participle': {'ξαναλέγων/ξαναλέγουσα/ξαναλέγον'},
             'conjunctive': {'active': {'ξαναπώ'}, 'passive': {'ξαναειπωθώ'}},
             'modal': False,
             'paratatikos': {'active': {'ξαναέλεγα'}, 'passive': {'ξαναλεγόμουν'}},
             'pass_pres_participle': {'ξαναλεγόμενος'},
             'passive_perfect_participle': {'ξαναειπωμένος'},
             'present': {'active': {'ξαναλέγω'}, 'passive': {'ξαναλέγομαι'}}},

        # print_verbs()
        # ic(verb.create_basic_forms('μέλπω'))
        )

    def test_verb_apokaiw(self):
        self.assertDictEqual(
            verb.create_basic_forms('αποκαίω'),
            {'act_pres_participle': {'αποκαίγοντας'},
             'aorist': {'active': {'απέκαψα'}, 'passive': {'αποκαήκα', 'αποκάηκα'}},
             'conjunctive': {'active': {'αποκάψω'}, 'passive': {'αποκαώ'}},
             'modal': False,
             'paratatikos': {'active': {'απέκαιγα'}, 'passive': {'αποκαιγόμουν'}},
             'pass_pres_participle': {'αποκαιγόμενος'},
             'passive_perfect_participle': {'αποκαμένος'},
             'present': {'active': {'αποκαίω'}, 'passive': {'αποκαίγομαι'}}}

        )
    def test_verb_katalabainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταλαβαίνω'),
            {'act_pres_participle': {'καταλαβαίνοντας'},
             'aorist': {'active': {'κατάλαβα'}},
             'conjunctive': {'active': {'καταλάβω'}},
             'modal': False,
             'paratatikos': {'active': {'καταλάβαινα'}, 'passive': {'καταλαβαινόμουν'}},
             'present': {'active': {'καταλαβαίνω'}, 'passive': {'καταλαβαίνομαι'}}}

        )
    def test_verb_synyparxw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('συνυπάρχω'),
            {'act_pres_participle': {'συνυπάρχοντας'},
             'aorist': {'active': {'συνύπαρξα'}},
             'arch_act_pres_participle': {'συνυπάρχων/συνυπάρχουσα/συνυπάρχον'},
             'conjunctive': {'active': {'συνυπάρξω'}},
             'modal': False,
             'paratatikos': {'active': {'συνυπήρχα'}},
             'present': {'active': {'συνυπάρχω'}}}

        )


    def test_verb_prosmeignuw(self):
        self.assertDictEqual(
            verb.create_basic_forms('προσμειγνύω'),
            {'act_pres_participle': {'προσμειγνύοντας'},
             'active_aorist_participle': {'προσμείξας/προσμείξασα/προσμείξαν'},
             'aorist': {'active': {'προσέμειξα'}, 'passive': {'προσμείχθηκα'}},
             'conjunctive': {'active': {'προσμείξω'}, 'passive': {'προσμειχθώ'}},
             'modal': False,
             'paratatikos': {'active': {'προσμείγνυα'}, 'passive': {'προσμειγνυόμουν'}},
             'pass_pres_participle': {'προσμειγνυόμενος'},
             'passive_aorist_participle': {'προσμειχθείς/προσμειχθείσα/προσμειχθέν'},
             'passive_perfect_participle': {'προσμεμειγμένος', 'προσμειγμένος'},
             'present': {'active': {'προσμειγνύω'}, 'passive': {'προσμειγνύομαι'}}}

        )
    def test_verb_epanakrinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('επανακρίνω'),
            {'act_pres_participle': {'επανακρίνοντας'},
             'aorist': {'active': {'επανέκρινα'},
                        'passive': {'επανεκρίθη', 'επανακρίθηκα'}},
             'arch_act_pres_participle': {'επανακρίνων/επανακρίνουσα/επανακρίνον'},
             'conjunctive': {'active': {'επανακρίνω'}, 'passive': {'επανακριθώ'}},
             'modal': False,
             'paratatikos': {'active': {'επανέκρινα'}, 'passive': {'επανακρινόμουν'}},
             'pass_pres_participle': {'επανακρινόμενος'},
             'passive_aorist_participle': {'επανακριθείς/επανακριθείσα/επανακριθέν'},
             'passive_perfect_participle': {'επανακριμένος'},
             'present': {'active': {'επανακρίνω'}, 'passive': {'επανακρίνομαι'}}}

        )

    def test_verb_synizanw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('συνιζάνω'),
            {'act_pres_participle': {'συνιζάνοντας'},
             'aorist': {'active': {'συνίζανα'}, 'passive': {'συνιζήθηκα'}},
             'conjunctive': {'active': {'συνιζάνω'}, 'passive': {'συνιζηθώ'}},
             'modal': False,
             'paratatikos': {'active': {'συνίζανα'}, 'passive': {'συνιζανόμουν'}},
             'passive_perfect_participle': {'συνιζημένος'},
             'present': {'active': {'συνιζάνω'}, 'passive': {'συνιζάνομαι'}}}

        )

    def test_dankanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δαγκάνω'),
            {'act_pres_participle': {'δαγκάνοντας'},
             'aorist': {'active': {'δάγκασα'}, 'passive': {'δαγκάθηκα'}},
             'conjunctive': {'active': {'δαγκάσω'}, 'passive': {'δαγκαθώ'}},
             'modal': False,
             'paratatikos': {'active': {'δάγκανα'}, 'passive': {'δαγκανόμουν'}},
             'passive_perfect_participle': {'δαγκαμένος'},
             'present': {'active': {'δαγκάνω'}, 'passive': {'δαγκάνομαι'}}}

        )

    def test_anufainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανυφαίνω'),
            {'act_pres_participle': {'ανυφαίνοντας'},
             'aorist': {'active': {'ανύφανα'}},
             'conjunctive': {'active': {'ανυφάνω'}},
             'modal': False,
             'paratatikos': {'active': {'ανύφαινα'}},
             'present': {'active': {'ανυφαίνω'}}}

        )

    def test_syntheta_tou_kathistw(self):
        self.assertDictEqual(
            verb.create_basic_forms('μετεγκαθιστώ'),
            {'act_pres_participle': {'μετεγκαθιστώντας'},
             'aorist': {'active': {'μετεγκατάστησα'}},
             'conjunctive': {'active': {'μετεγκαταστήσω'}},
             'modal': False,
             'paratatikos': {'active': {'μετεγκαθιστούσα'}},
             'present': {'active': {'μετεγκαθιστώ'}}},

        )

    def test_verb_elaunw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ελαύνω'),
            {'act_pres_participle': {'ελαύνοντας'},
             'aorist': {'active': {'έλασα'}},
             'arch_act_pres_participle': {'ελαύνων/ελαύνουσα/ελαύνον'},
             'conjunctive': {'active': {'ελάσω'}},
             'modal': False,
             'paratatikos': {'active': {'ήλαυνα', 'έλαυνα'}},
             'present': {'active': {'ελαύνω'}}}

        )

    def test_verb_protopianw(self):
        self.assertDictEqual(
            verb.create_all_basic_forms('πρωτοπιάνω'),
            {'act_pres_participle': {'πρωτοπιάνοντας'},
             'aorist': {'active': {'πρωτοέπιασα'}, 'passive': {'πρωτοπιάστηκα'}},
             'conjunctive': {'active': {'πρωτοπιάσω'}, 'passive': {'πρωτοπιαστώ'}},
             'modal': False,
             'paratatikos': {'active': {'πρωτοέπιανα'}, 'passive': {'πρωτοπιανόμουν'}},
             'passive_perfect_participle': {'πρωτοπιασμένος'},
             'present': {'active': {'πρωτοπιάνω'}, 'passive': {'πρωτοπιάνομαι'}}}

        )

    def test_verb_buzanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('βυζάνω'),
            {'act_pres_participle': {'βυζάνοντας'},
             'aorist': {'active': {'βύζαξα'}},
             'conjunctive': {'active': {'βυζάξω'}},
             'modal': False,
             'paratatikos': {'active': {'βύζανα'}},
             'passive_perfect_participle': {'βυζαγμένος'},
             'present': {'active': {'βυζάνω'}}}

        )

    def test_verb_eksolisthanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('εξολισθάνω'),
            {'act_pres_participle': {'εξολισθάνοντας'},
             'aorist': {'active': {'εξολίσθησα'}},
             'conjunctive': {'active': {'εξολισθήσω'}},
             'modal': False,
             'paratatikos': {'active': {'εξολίσθανα'}},
             'present': {'active': {'εξολισθάνω'}}}

        )

    def test_paratw(self):
        self.assertDictEqual(
            verb.create_basic_forms('παρατώ'),
            {'act_pres_participle': {'παρατώντας'},
             'aorist': {'active': {'παράτησα'}, 'passive': {'παρατήθηκα'}},
             'conjunctive': {'active': {'παρατήσω'}, 'passive': {'παρατηθώ'}},
             'modal': False,
             'paratatikos': {'active': {'παρατούσα', 'παράταγα'},
                             'passive': {'παρατιόμουν'}},
             'passive_perfect_participle': {'παρατημένος'},
             'present': {'active': {'παρατώ'}, 'passive': {'παρατιέμαι'}}}
        )

    def test_verb_parabainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('παραβαίνω'),
            {'act_pres_participle': {'παραβαίνοντας'},
             'aorist': {'active': {'παραβήκα'}},
             'conjunctive': {'active': {'παραβώ'}},
             'modal': False,
             'paratatikos': {'active': {'παράβαινα'}},
             'present': {'active': {'παραβαίνω'}}}

        )

    def test_verb_uperbainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('υπερβαίνω'),
            {'act_pres_participle': {'υπερβαίνοντας'},
             'aorist': {'active': {'υπερέβη'}},
             'arch_act_pres_participle': {'υπερβαίνων/υπερβαίνουσα/υπερβαίνον'},
             'conjunctive': {'active': {'υπερβώ'}},
             'modal': False,
             'paratatikos': {'active': {'υπερέβαινα', 'υπέρβαινα'},
                             'passive': {'υπερβαινόμουν'}},
             'present': {'active': {'υπερβαίνω'}, 'passive': {'υπερβαίνομαι'}}}

        )

    def test_embainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('εμβαίνω'),
            {'act_pres_participle': {'εμβαίνοντας'},
             'aorist': {'active': {'ενέβη'}},
             'conjunctive': {'active': {'εμβώ'}},
             'modal': False,
             'paratatikos': {'active': {'ενέβαινα'}},
             'present': {'active': {'εμβαίνω'}}}

        )

    def test_nostimainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('νοστιμαίνω'),
            {'act_pres_participle': {'νοστιμαίνοντας'},
             'aorist': {'active': {'νοστίμανα'}},
             'conjunctive': {'active': {'νοστιμάνω'}},
             'modal': False,
             'paratatikos': {'active': {'νοστίμαινα'}},
             'present': {'active': {'νοστιμαίνω'}}}

        )

    def test_verb_prosexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('προσέχω'),
            {'act_pres_participle': {'προσέχοντας'},
             'aorist': {'active': {'πρόσεξα'}, 'passive': {'προσέχθηκα', 'προσέχτηκα'}},
             'conjunctive': {'active': {'προσέξω'}, 'passive': {'προσεχθώ', 'προσεχτώ'}},
             'modal': False,
             'paratatikos': {'active': {'πρόσεχα'}, 'passive': {'προσεχόμουν'}},
             'passive_perfect_participle': {'προσεγμένος'},
             'present': {'active': {'προσέχω'}, 'passive': {'προσέχομαι'}}},
        )

    def test_syntheto_toy_agw(self):
        self.assertDictEqual(
            verb.create_basic_forms('παραεισάγω'),
            {'act_pres_participle': {'παραεισάγοντας'},
             'aorist': {'active': {'παραεισήγαγα'}, 'passive': {'παραεισήχθη'}},
             'arch_act_pres_participle': {'παραεισάγων/παραεισάγουσα/παραεισάγον'},
             'conjunctive': {'active': {'παραεισαγάγω'}, 'passive': {'παραεισαχθώ'}},
             'modal': False,
             'paratatikos': {'active': {'παραεισήγα'}, 'passive': {'παραεισαγόμουν'}},
             'pass_pres_participle': {'παραεισαγόμενος'},
             'present': {'active': {'παραεισάγω'}, 'passive': {'παραεισάγομαι'}}}

        )

    def test_verb_eisexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('εισέχω'),
            {'act_pres_participle': {'εισέχοντας'},
             'aorist': {'active': {'εισείχα'}},
             'conjunctive': {'active': {'εισέχω'}},
             'modal': False,
             'paratatikos': {'active': {'εισείχα'}},
             'present': {'active': {'εισέχω'}}}

        )

    def test_verb_uperexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('υπερέχω'),
            {'act_pres_participle': {'υπερέχοντας'},
             'aorist': {'active': {'υπερείχα'}},
             'arch_act_pres_participle': {'υπερέχων/υπερέχουσα/υπερέχον'},
             'conjunctive': {'active': {'υπερέχω'}},
             'modal': False,
             'paratatikos': {'active': {'υπερείχα'}},
             'present': {'active': {'υπερέχω'}}}

        )

    def test_verb_tragoudo(self):
        self.assertDictEqual(
            verb.create_basic_forms('τραγουδώ'),
            {'present': {'active': {'τραγουδώ'}, 'passive': {'τραγουδιέμαι'}},
             'conjunctive': {'active': {'τραγουδήσω'}, 'passive': {'τραγουδηθώ'}},
             'aorist': {'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}},
             'paratatikos': {'active': {'τραγουδούσα', 'τραγούδαγα'}, 'passive': {'τραγουδιόμουν'}},
             'act_pres_participle': {'τραγουδώντας'}, 'passive_perfect_participle': {'τραγουδημένος'},
             'modal': False},
            # print_exw()
            # ic()

        )

    def test_verb_synkatexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συγκατέχω'),
            {'act_pres_participle': {'συγκατέχοντας'},
             'aorist': {'active': {'συγκατείχα'}},
             'arch_act_pres_participle': {'συγκατέχων/συγκατέχουσα/συγκατέχον'},
             'conjunctive': {'active': {'συγκατέχω'}},
             'modal': False,
             'paratatikos': {'active': {'συγκατείχα', 'συγκάτεχα'},
                             'passive': {'συγκατεχόμουν'}},
             'pass_pres_participle': {'συγκατεχόμενος'},
             'present': {'active': {'συγκατέχω'}, 'passive': {'συγκατέχομαι'}}},

        )

    def test_verb_anhkw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανήκω'),
            {'act_pres_participle': {'ανήκοντας'},
             'aorist': {},
             'arch_act_pres_participle': {'ανήκων/ανήκουσα/ανήκον'},
             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'άνηκα', 'ανήκα'}},
             'present': {'active': {'ανήκω'}}},

        )

    def test_verb_drw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δρω'),
            {'present': {'active': {'δρω'}},
             'conjunctive': {'active': {'δράσω'}},
             'aorist': {'active': {'έδρασα'}},
             'paratatikos': {'active': {'δρούσα'}},
             'act_pres_participle': {'δρώντας'},
             'arch_act_pres_participle': {'δρών/δρώσα/δρών'},
             'pass_pres_participle': {'δρώμενος'}, 'modal': False},

        )

    def test_verb_titrwskw(self):
        self.assertDictEqual(
            verb.create_basic_forms('τιτρώσκω'),
            {'present': {'active': {'τιτρώσκω'}}, 'conjunctive': {'passive': {'τρωθώ'}},
             'aorist': {'passive': {'ετρώθη'}}, 'paratatikos': {'active': {'ετίτρωσκα'}},
             'act_pres_participle': {'τιτρώσκοντας'}, 'modal': False},

        )

    def test_verb_bexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('βέχω'),
            {'act_pres_participle': {'βέχοντας'},
             'aorist': {},
             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'έβεχα'}},
             'present': {'active': {'βέχω'}}},

        )

    def test_verb_thwrakizw(self):
        self.assertDictEqual(
            verb.create_basic_forms('θωρακίζω'),
            {'act_pres_participle': {'θωρακίζοντας'},
             'aorist': {'active': {'θωράκισα'}, 'passive': {'θωρακίστηκα'}},
             'conjunctive': {'active': {'θωρακίσω'}, 'passive': {'θωρακισθώ', 'θωρακιστώ'}},
             'modal': False,
             'paratatikos': {'active': {'θωράκιζα'}, 'passive': {'θωρακιζόμουν'}},
             'passive_perfect_participle': {'τεθωρακισμένος', 'θωρακισμένος'},
             'present': {'active': {'θωρακίζω'}, 'passive': {'θωρακίζομαι'}}},

        )

    def test_verb_upomimnhskw(self):
        self.assertDictEqual(
            verb.create_basic_forms('υπομιμνήσκω'),
            {'act_pres_participle': {'υπομιμνήσκοντας'},
             'aorist': {'active': {'υπέμνησα', 'υπόμνησα'}, 'passive': {'υπεμνήσθη'}},
             'conjunctive': {'active': {'υπομνήσω'}, 'passive': {'υπομνησθώ'}},
             'modal': False,
             'paratatikos': {'active': {'υπομίμνησκα', 'υπεμίμνησκα'},
                             'passive': {'υπομιμνησκόμουν'}},
             'present': {'active': {'υπομιμνήσκω'}, 'passive': {'υπομιμνήσκομαι'}}}

        )

    def test_verb_methuskw(self):
        self.assertDictEqual(
            verb.create_basic_forms('μεθύσκω'),
            {'act_pres_participle': {'μεθύσκοντας'},
             'aorist': {'active': {'μέθυσα'}},
             'conjunctive': {'active': {'μεθύσω'}},
             'modal': False,
             'paratatikos': {'active': {'μέθυσκα'}},
             'passive_perfect_participle': {'μεθυσμένος'},
             'present': {'active': {'μεθύσκω'}, 'passive': {'μεθύσκομαι'}}}

        )

    def test_verb_boskw(self):
        self.assertDictEqual(
            verb.create_basic_forms('βόσκω'),
            {'act_pres_participle': {'βόσκοντας'},
             'aorist': {'active': {'βόσκησα'}},
             'conjunctive': {'active': {'βοσκήσω'}},
             'modal': False,
             'paratatikos': {'active': {'έβοσκα'}},
             'passive_perfect_participle': {'βοσκημένος'},
             'present': {'active': {'βόσκω'}}}

        )

    def test_verb_bibrwskw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταβιβρώσκω'),
            {'act_pres_participle': {'καταβιβρώσκοντας'},
             'aorist': {},
             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'καταβίβρωσκα'}},
             'present': {'active': {'καταβιβρώσκω'}}},

        )

    def test_verb_kathisto(self):
        self.assertDictEqual(
            verb.create_basic_forms('καθιστώ'),
            {'present': {'active': {'καθιστώ'}}, 'conjunctive': {'active': {'καταστήσω'}},
             'aorist': {'active': {'κατέστησα', 'κατάστησα'}},
             'paratatikos': {'active': {'καθιστούσα'}, 'passive': {'καθιστάμην'}},
             'act_pres_participle': {'καθδιστώντας'}, 'modal': False},

        )

    def test_verb_gernw(self):
        self.assertDictEqual(
            verb.create_basic_forms('γέρνω'),
            {'present': {'active': {'γέρνω'}}, 'conjunctive': {'active': {'γείρω'}}, 'aorist': {'active': {'έγειρα'}},
             'paratatikos': {'active': {'έγερνα'}}, 'act_pres_participle': {'γέρνοντας'}, 'modal': False}

        )

    def test_verb_dew(self):
        self.assertDictEqual(
            verb.create_basic_forms('δέω'),
            {'present': {'active': {'δέω'}, 'passive': {'δέομαι'}},
             'conjunctive': {'active': {'δεήσω'}, 'passive': {'δεηθώ'}},
             'aorist': {'active': {'δέησα', 'εδέησα'}, 'passive': {'δεήθηκα'}}, 'paratatikos': {'passive': {'δεόμουν'}},
             'act_pres_participle': {'δέοντας'}, 'arch_act_pres_participle': {'δέων/δέουσα/δέον'},
             'pass_pres_participle': {'δεόμενος'}, 'active_aorist_participle': {'δεήσας/δεήσασα/δεήσαν'},
             'passive_aorist_participle': {'δεηθείς/δεηθείσα/δεηθέν'}, 'modal': False},

        )

    def test_verb_dew(self):
        self.assertDictEqual(
            verb.create_basic_forms('δέει'),
            {'present': {'active': {'δέει'}}, 'conjunctive': {'active': {'δεήσει'}},
             'aorist': {'active': {'δέησε', 'εδέησε'}}, 'paratatikos': {}, 'modal': True}

        )

    def test_verb_theto(self):
        self.assertDictEqual(
            verb.create_basic_forms('θέτω'),
            {'present':
                 {'active': {'θέτω'},
                  'passive': {'θέτομαι'}},
             'conjunctive':
                 {'active': {'θέσω'},
                  'passive': {'τεθώ'}},
             'aorist': {'active': {'έθεσα'},
                        'passive': {'τέθηκα', 'ετέθη'}},
             'paratatikos':
                 {'active': {'έθετα'},
                  'passive': {'θετόμουν'}},
             'act_pres_participle': {'θέτοντας'},
             'passive_aorist_participle': {'τεθείς/τεθείσα/τεθέν'},
             'passive_perfect_participle': {'τεθειμένος'},
             'modal': False}

        )

    def test_verb_kyberno(self):
        self.assertDictEqual(
            verb.create_basic_forms('κυβερνώ'),
            {'present': {'active': {'κυβερνώ'}, 'passive': {'κυβερνούμαι', 'κυβερνιέμαι', 'κυβερνώμαι'}},
             'conjunctive': {'active': {'κυβερνήσω'}, 'passive': {'κυβερνηθώ'}},
             'aorist': {'active': {'κυβέρνησα'}, 'passive': {'κυβερνήθηκα'}},
             'paratatikos': {'active': {'κυβέρναγα', 'κυβερνούσα'}, 'passive': {'κυβερνιόμουν'}},
             'act_pres_participle': {'κυβερνώντας'}, 'arch_act_pres_participle': {'κυβερνών/κυβερνώσα/κυβερνών'},
             'pass_pres_participle': {'κυβερνούμενος', 'κυβερνώμενος'}, 'passive_perfect_participle': {'κυβερνημένος'},
             'modal': False}
        )

    def test_verb_douleuo(self):
        self.assertDictEqual(
            verb.create_basic_forms('δουλεύω'),
            {'present': {'active': {'δουλεύω'}, 'passive': {'δουλεύομαι'}},
             'conjunctive': {'active': {'δουλέψω', 'δουλεύσω'}, 'passive': {'δουλευθώ', 'δουλευτώ'}},
             'aorist': {'active': {'δούλευσα', 'δούλεψα'}, 'passive': {'δουλεύθηκα', 'δουλεύτηκα'}},
             'paratatikos': {'active': {'δούλευα'}, 'passive': {'δουλευόμουν'}}, 'act_pres_participle': {'δουλεύοντας'},
             'passive_perfect_participle': {'δουλευμένος', 'δεδουλευμένος'},
             'active_aorist_participle': {'δουλεύσας/δουλεύσασα/δουλεύσαν'}, 'modal': False}

        )

    def test_verb_spatalo(self):
        self.assertDictEqual(
            verb.create_basic_forms('σπαταλώ'),
            {'present': {'active': {'σπαταλώ'}, 'passive': {'σπαταλώμαι', 'σπαταλιέμαι'}},
             'conjunctive': {'active': {'σπαταλήσω'}, 'passive': {'σπαταληθώ'}},
             'aorist': {'active': {'σπατάλησα'}, 'passive': {'σπαταλήθηκα'}},
             'paratatikos': {'active': {'σπαταλούσα', 'σπατάλαγα'}, 'passive': {'σπαταλιόμουν'}},
             'act_pres_participle': {'σπαταλώντας'}, 'passive_perfect_participle': {'σπαταλημένος', 'σπαταλεμένος'},
             'modal': False}

        )

    def test_verb_ximaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('χιμάω'),
            {'present': {'active': {'χιμάω'}}, 'conjunctive': {'active': {'χιμήξω'}}, 'aorist': {'active': {'χίμηξα'}},
             'paratatikos': {'active': {'χιμούσα'}}, 'act_pres_participle': {'χιμώντας'}, 'modal': False}

        )

    def test_verb_xumaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('χυμάω'),
            {'present': {'active': {'χυμάω'}}, 'conjunctive': {'active': {'χυμήξω'}}, 'aorist': {'active': {'χύμηξα'}},
             'paratatikos': {'active': {'χυμούσα'}}, 'act_pres_participle': {'χυμώντας'}, 'modal': False},

        )

    def test_verb_ikanopoiw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ικανοποιώ'),
            {'present': {'active': {'ικανοποιώ'}, 'passive': {'ικανοποιούμαι'}},
             'conjunctive': {'active': {'ικανοποιήσω'}, 'passive': {'ικανοποιηθώ'}},
             'aorist': {'active': {'ικανοποίησα'}, 'passive': {'ικανοποιήθηκα'}},
             'paratatikos': {'active': {'ικανοποιούσα'}, 'passive': {'ικανοποιούμουν', 'ικανοποιόμουν'}},
             'act_pres_participle': {'ικανοποιώντας'}, 'pass_pres_participle': {'ικανοποιούμενος'},
             'passive_perfect_participle': {'ικανοποιημένος'},
             'passive_aorist_participle': {'ικανοποιηθείς/ικανοποιηθείσα/ικανοποιηθέν'}, 'modal': False}

        )

    def test_verb_apokleiw(self):
        self.assertDictEqual(
            verb.create_basic_forms('αποκλείω'),
            {'act_pres_participle': {'αποκλείοντας'},
             'aorist': {'active': {'απέκλεισα', 'απόκλεισα'},
                        'passive': {'αποκλείστηκα', 'αποκλείσθηκα'}},
             'conjunctive': {'active': {'αποκλείσω'},
                             'passive': {'αποκλεισθώ', 'αποκλειστώ'}},
             'modal': False,
             'paratatikos': {'active': {'απέκλεια'}, 'passive': {'αποκλειόμουν'}},
             'pass_pres_participle': {'αποκλειόμενος'},
             'passive_perfect_participle': {'αποκλεισμένος'},
             'present': {'active': {'αποκλείω'}, 'passive': {'αποκλείομαι'}}},
            # ic(verb.create_basic_forms('αποκλείω'))

        )

    def test_verb_xew(self):
        self.assertDictEqual(
            verb.create_basic_forms('χέω'),
            {'act_pres_participle': {'χέοντας'},
             'aorist': {'active': {'έχυσα'}, 'passive': {'χύθηκα'}},
             'conjunctive': {'active': {'χύσω'}, 'passive': {'χυθώ'}},
             'modal': False,
             'paratatikos': {'active': {'έχεα'}},
             'passive_perfect_participle': {'χυμένος'},
             'present': {'active': {'χέω'}}}

        )

    def test_verb_βαρυγκομάω(self):
        self.assertDictEqual(
            verb.create_basic_forms('βαρυγκομάω'),
            {'present': {'active': {'βαρυγκομάω'}}, 'conjunctive': {'active': {'βαρυγκομήσω'}},
             'aorist': {'active': {'βαρυγκόμησα'}}, 'paratatikos': {'active': {'βαρυγκομούσα'}},
             'act_pres_participle': {'βαρυγκομώντας'}, 'passive_perfect_participle': {'βαρυγκομισμένος'},
             'modal': False},
        )

    def test_verb_ζω(self):
        self.assertDictEqual(
            verb.create_basic_forms('ζω'),
            {'present': {'active': {'ζω'}}, 'conjunctive': {'active': {'ζήσω'}},
             'aorist': {'active': {'έζησα'}}, 'paratatikos': {'active': {'ζούσα'}},
             'act_pres_participle': {'ζώντας'},
             'arch_act_pres_participle': {'ζων/ζώσα/ζων'},
             'passive_perfect_participle': {'βιωμένος'}, 'modal': False},

        )

    def test_verb_paxaino(self):
        self.assertDictEqual(
            verb.create_basic_forms('παχαίνω'),
            {'present': {'active': {'παχαίνω'}}, 'conjunctive': {'active': {'παχύνω'}},
             'aorist': {'active': {'πάχυνα'}}, 'paratatikos': {'active': {'πάχαινα'}},
             'act_pres_participle': {'παχαίνοντας'}, 'passive_perfect_participle': {'παχυμένος'}, 'modal': False}

        )

    def test_verb_blepo(self):
        self.assertDictEqual(
            verb.create_basic_forms('βλέπω'),
            {'present': {'active': {'βλέπω'}, 'passive': {'βλέπομαι'}},
             'conjunctive': {'active': {'δω'}, 'passive': {'ιδωθώ'}},
             'aorist': {'active': {'είδα'}, 'passive': {'ειδώθηκα'}},
             'paratatikos': {'active': {'έβλεπα'}, 'passive': {'βλεπόμουν'}}, 'act_pres_participle': {'βλέποντας'},
             'arch_act_pres_participle': {'βλέπων/βλέπουσα/βλέπον'}, 'passive_perfect_participle': {'ιδωμένος'},
             'modal': False}
        )

    def test_verb_syllambano(self):
        self.assertDictEqual(
            verb.create_basic_forms('συλλαμβάνω'),
            {'present': {'active': {'συλλαμβάνω'}, 'passive': {'συλλαμβάνομαι'}},
             'conjunctive': {'active': {'συλλάβω'}, 'passive': {'συλληφθώ'}},
             'aorist': {'active': {'συνέλαβα'}, 'passive': {'συνελήφθη'}},
             'paratatikos': {'active': {'συλλάμβανα', 'συνελάμβανα'}, 'passive': {'συλλαμβανόμουν'}},
             'act_pres_participle': {'συλλαμβάνοντας'}, 'pass_pres_participle': {'συλλαμβανόμενος'},
             'passive_aorist_participle': {'συλληφθείς/συλληφθείσα/συλληφθέν'},
             'modal': False},

        )

    def test_verb_phgainvo(self):
        self.assertDictEqual(
            verb.create_basic_forms('πηγαίνω'),
            {'present': {'active': {'πηγαίνω'}}, 'conjunctive': {'active': {'πάω'}},
             'aorist': {'active': {'πήγα'}}, 'paratatikos': {'active': {'πήγαινα'}},
             'act_pres_participle': {'πηγαίνοντας'},
             'modal': False},

        )

    def test_verb_nothing(self):
        self.assertRaises(NotInGreekException, verb.create_basic_forms, '')

    def test_verb_gibberish(self):
        self.assertRaises(NotInGreekException, verb.create_basic_forms, 'gamao')

    def test_verb_prokeitai(self):
        self.assertDictEqual(
            verb.create_basic_forms('πρόκειται'),
            {'present': {'passive': {'πρόκειται'}}, 'paratatikos': {'passive': {'επρόκειτο'}},
             'modal': True},

        )

    def test_verb_erxomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('έρχομαι'),
            {'present': {'passive': {'έρχομαι'}},
             'conjunctive': {'active': {'έλθω', 'έρθω'}},
             'aorist': {'active': {'ήλθα', 'ήρθα'}},
             'paratatikos': {'passive': {'ερχόμουν'}},
             'pass_pres_participle': {'ερχόμενος'},
             'modal': False},

        )

    def test_verb_synerxomai(self):
        self.maxDiff = None
        self.assertDictEqual(

            verb.create_basic_forms('συνέρχομαι'),
            {'present': {'passive': {'συνέρχομαι'}}, 'conjunctive': {'active': {'συνέλθω', 'συνέρθω'}},
             'aorist': {'active': {'συνήρθα', 'συνήλθα'}}, 'paratatikos': {'passive': {'συνερχόμουν'}},
             'pass_pres_participle': {'συνερχόμενος'}, 'active_aorist_participle': {'συνελθών/συνελθούσα/συνελθόν'},
             'modal': False},

        )

    def test_verb_katebainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κατεβαίνω'),
            {'present': {'active': {'κατεβαίνω'}}, 'conjunctive': {'active': {'κατέβω', 'κατεβώ'}},
             'aorist': {'active': {'κατέβηκα', 'κατέβη'}}, 'paratatikos': {'active': {'κατέβαινα'}},
             'act_pres_participle': {'κατεβαίνοντας'},
             'modal': False},

        )

    def test_verb_arnoumai(self):
        self.assertDictEqual(
            verb.create_basic_forms('αρνιέμαι'),
            {'present': {'passive': {'αρνιέμαι', 'αρνούμαι'}}, 'conjunctive': {'passive': {'αρνηθώ'}},
             'aorist': {'passive': {'αρνήθηκα'}}, 'paratatikos': {'passive': {'αρνούμουν', 'αρνιόμουν'}},
             'pass_pres_participle': {'αρνούμενος'},
             'modal': False},

        )

    def test_verb_eisago(self):
        self.assertDictEqual(
            verb.create_basic_forms('εισάγω'),
            {'present': {'active': {'εισάγω'}, 'passive': {'εισάγομαι'}},
             'conjunctive': {'active': {'εισαγάγω'}, 'passive': {'εισαχθώ'}},
             'aorist': {'active': {'εισήγαγα'}, 'passive': {'εισήχθη', 'εισάχθηκα'}},
             'paratatikos': {'active': {'εισήγα'}, 'passive': {'εισαγόμουν'}}, 'act_pres_participle': {'εισάγοντας'},
             'arch_act_pres_participle': {'εισάγων/εισάγουσα/εισάγον'}, 'pass_pres_participle': {'εισαγόμενος'},
             'passive_perfect_participle': {'εισηγμένος'},
             'passive_aorist_participle': {'εισαχθείς/εισαχθείσα/εισαχθέν'}, 'modal': False},

        )

    def test_verb_dialego(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('διαλέγω'),
            {'present': {'active': {'διαλέγω'}, 'passive': {'διαλέγομαι'}},
             'conjunctive': {'active': {'διαλέξω'}, 'passive': {'διαλεχθώ', 'διαλεχτώ'}},
             'aorist': {'active': {'διάλεξα'}, 'passive': {'διαλέχτηκα', 'διαλέχθηκα'}},
             'paratatikos': {'active': {'διάλεγα'}, 'passive': {'διαλεγόμουν'}}, 'act_pres_participle': {'διαλέγοντας'},
             'pass_pres_participle': {'διαλεγόμενος'}, 'passive_perfect_participle': {'διαλεγμένος'}, 'modal': False},

        )

    def test_verb_deiknuw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δεικνύω'),
            {'present': {'active': {'δεικνύω'}, 'passive': {'δεικνύομαι'}},
             'conjunctive': {'active': {'δείξω'}, 'passive': {'δειχθώ'}},
             'aorist': {'active': {'έδειξα'}, 'passive': {'δείχθηκα'}},
             'paratatikos': {'active': {'δείκνυα'}, 'passive': {'δεικνυόμουν'}}, 'act_pres_participle': {'δεικνύοντας'},
             'arch_act_pres_participle': {'δεικνύων/δεικνύουσα/δεικνύον'}, 'pass_pres_participle': {'δεικνυόμενος'},
             'passive_perfect_participle': {'δειγμένος'}, 'active_aorist_participle': {'δείξας/δείξασα/δείξαν'},
             'passive_aorist_participle': {'δειχθείς/δειχθείσα/δειχθέν'}, 'modal': False},

        )

    def test_verb_nemw(self):
        self.assertDictEqual(
            verb.create_basic_forms('νέμω'),
            {'present': {'active': {'νέμω'}, 'passive': {'νέμομαι'}},
             'conjunctive': {'active': {'νείμω'}, 'passive': {'νεμηθώ'}},
             'aorist': {'active': {'ένειμα'}, 'passive': {'νεμήθηκα'}},
             'paratatikos': {'active': {'ένεμα'}, 'passive': {'νεμόμουν'}}, 'act_pres_participle': {'νέμοντας'},
             'passive_perfect_participle': {'νεμημένος'}, 'passive_aorist_participle': {'νεμηθείς/νεμηθείσα/νεμηθέν'},
             'modal': False},

        )

    def test_verb_kleptw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κλέπτω'),
            {'present': {'active': {'κλέπτω'}, 'passive': {'κλέπτομαι'}},
             'conjunctive': {'active': {'κλέψω'}, 'passive': {'κλαπώ', 'κλεφτώ'}},
             'aorist': {'active': {'έκλεψα'}, 'passive': {'κλέφτηκα', 'κλάπηκα', 'εκλάπη'}},
             'paratatikos': {'active': {'έκλεπτα'}, 'passive': {'κλεπτόμουν'}}, 'act_pres_participle': {'κλέπτοντας'},
             'passive_perfect_participle': {'κλεμμένος'}, 'modal': False},

        )

    def test_verb_antiparaballw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('αντιπαραβάλλω'),
            {'act_pres_participle': {'αντιπαραβάλλοντας'},
             'active_aorist_participle': {'αντιπαραβαλών/αντιπαραβαλούσα/αντιπαραβαλόν'},
             'aorist': {'active': {'αντιπαρέβαλα'},
                        'passive': {'αντιπαρεβλήθη', 'αντιπαραβλήθηκα'}},
             'arch_act_pres_participle': {'αντιπαραβάλλων/αντιπαραβάλλουσα/αντιπαραβάλλον'},
             'conjunctive': {'active': {'αντιπαραβάλω'}, 'passive': {'αντιπαραβληθώ'}},
             'modal': False,
             'paratatikos': {'active': {'αντιπαρέβαλλα'}, 'passive': {'αντιπαραβαλλόμουν'}},
             'pass_pres_participle': {'αντιπαραβαλλόμενος'},
             'passive_aorist_participle': {'αντιπαραβληθείς/αντιπαραβληθείσα/αντιπαραβληθέν'},
             'passive_perfect_participle': {'αντιπαραβεβλημένος'},
             'present': {'active': {'αντιπαραβάλλω'}, 'passive': {'αντιπαραβάλλομαι'}}}

        )

    def test_verb_pethainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('πεθαίνω'),
            {'present': {'active': {'πεθαίνω'}}, 'conjunctive': {'active': {'πεθάνω'}},
             'aorist': {'active': {'πέθανα'}}, 'paratatikos': {'active': {'πέθαινα'}},
             'act_pres_participle': {'πεθαίνοντας'}, 'passive_perfect_participle': {'πεθαμένος'}, 'modal': False},

        )

    def test_verb_perimenw(self):
        self.assertDictEqual(
            verb.create_basic_forms('περιμένω'),
            {'present': {'active': {'περιμένω'}}, 'conjunctive': {'active': {'περιμένω'}},
             'aorist': {'active': {'περίμενα'}}, 'paratatikos': {'active': {'περίμενα'}},
             'act_pres_participle': {'περιμένοντας'}, 'arch_act_pres_participle': {'περιμένων/περιμένουσα/περιμένον'},
             'modal': False},

        )

    def test_verb_pathainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('παθαίνω'),
            {'present': {'active': {'παθαίνω'}, 'passive': {'παθαίνομαι'}}, 'conjunctive': {'active': {'πάθω'}},
             'aorist': {'active': {'έπαθα'}}, 'paratatikos': {'active': {'πάθαινα'}, 'passive': {'παθαινόμουν'}},
             'act_pres_participle': {'παθαίνοντας'}, 'passive_perfect_participle': {'παθημένος'},
             'active_aorist_participle': {'παθών/παθούσα/παθόν'}, 'modal': False},

        )

    def test_verb_proferw(self):
        self.assertDictEqual(
            verb.create_basic_forms('προφέρω'),
            {'present': {'active': {'προφέρω'}, 'passive': {'προφέρομαι'}},
             'conjunctive': {'active': {'προφέρω'}, 'passive': {'προφερθώ'}},
             'aorist': {'active': {'πρόφερα'}, 'passive': {'προφέρθηκα'}},
             'paratatikos': {'active': {'πρόφερα'}, 'passive': {'προφερόμουν'}}, 'act_pres_participle': {'προφέροντας'},
             'passive_perfect_participle': {'προφερμένος'}, 'modal': False},

        )

    def test_verb_brithw(self):
        # an example of an elliptive verb
        self.assertDictEqual(
            verb.create_basic_forms('βρίθω'),
            {'present': {'active': {'βρίθω'}}, 'conjunctive': {}, 'aorist': {}, 'paratatikos': {'active': {'έβριθα'}},
             'act_pres_participle': {'βρίθοντας'}, 'arch_act_pres_participle': {'βρίθων/βρίθουσα/βρίθον'},
             'modal': False},

        )

    def test_verb_kserw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ξέρω'),
            {'present': {'active': {'ξέρω'}}, 'conjunctive': {}, 'aorist': {}, 'paratatikos': {'active': {'ήξερα'}},
             'act_pres_participle': {'ξέροντας'}, 'modal': False},

        )

    def test_verb_euthunomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('ευθύνομαι'),
            {'present': {'passive': {'ευθύνομαι'}}, 'paratatikos': {'passive': {'ευθυνόμουν'}}, 'modal': False},

        )

    def test_verb_thabw(self):
        self.assertDictEqual(
            verb.create_basic_forms('θάβω'),
            {'present': {'active': {'θάβω'}, 'passive': {'θάβομαι'}},
             'conjunctive': {'active': {'θάψω'}, 'passive': {'θαφθώ', 'θαφτώ', 'ταφώ'}},
             'aorist': {'active': {'έθαψα'}, 'passive': {'θάφτηκα', 'θάφθηκα', 'τάφηκα', 'ετάφη'}},
             'paratatikos': {'active': {'έθαβα'}, 'passive': {'θαβόμουν'}}, 'act_pres_participle': {'θάβοντας'},
             'passive_perfect_participle': {'θαμμένος'}, 'active_aorist_participle': {'θάψας/θάψασα/θάψαν'},
             'modal': False},

        )

    def test_verb_epitaxunw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('επιταχύνω'),
            {'present': {'active': {'επιταχύνω'}, 'passive': {'επιταχύνομαι'}},
             'conjunctive': {'active': {'επιταχύνω'}, 'passive': {'επιταχυνθώ'}},
             'aorist': {'active': {'επιτάχυνα'}, 'passive': {'επιταχύνθηκα'}},
             'paratatikos': {'active': {'επιτάχυνα'}, 'passive': {'επιταχυνόμουν'}},
             'act_pres_participle': {'επιταχύνοντας'}, 'pass_pres_participle': {'επιταχυνόμενος'},
             'passive_perfect_participle': {'επιταχυμένος'},
             'passive_aorist_participle': {'επιταχυνθείς/επιταχυνθείσα/επιταχυνθέν'}, 'modal': False},

        )

    def test_verb_apallassw(self):
        self.assertDictEqual(
            verb.create_basic_forms('απαλλάσσω'),
            {'present': {'active': {'απαλλάσσω'}, 'passive': {'απαλλάσσομαι'}},
             'conjunctive': {'active': {'απαλλάξω'}, 'passive': {'απαλλαγώ', 'απαλλαχθώ', 'απαλλαχτώ'}},
             'aorist': {'active': {'απάλλαξα'}, 'passive': {'απαλλάχθηκα', 'απηλλάγη', 'απαλλάχτηκα'}},
             'paratatikos': {'active': {'απάλλασσα'}, 'passive': {'απαλλασσόμουν'}},
             'act_pres_participle': {'απαλλάσσοντας'}, 'pass_pres_participle': {'απαλλασσόμενος'},
             'passive_perfect_participle': {'απαλλαγμένος'}, 'modal': False},

        )

    def test_verb_katapsixv(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταψύχω'),
            {'present': {'active': {'καταψύχω'}, 'passive': {'καταψύχομαι'}},
             'conjunctive': {'active': {'καταψύξω'}, 'passive': {'καταψυχθώ', 'καταψυχτώ'}},
             'aorist': {'active': {'κατέψυξα'}, 'passive': {'καταψύχτηκα'}},
             'paratatikos': {'active': {'κατέψυχα'}, 'passive': {'καταψυχόμουν'}},
             'act_pres_participle': {'καταψύχοντας'}, 'passive_perfect_participle': {'κατεψυγμένος', 'καταψυγμένος'},
             'modal': False},

        )

    def test_verb_sthnw(self):
        self.assertDictEqual(
            verb.create_basic_forms('στήνω'),
            {'present': {'active': {'στήνω'}, 'passive': {'στήνομαι'}},
             'conjunctive': {'active': {'στήσω'}, 'passive': {'σταθώ'}},
             'aorist': {'active': {'έστησα'}, 'passive': {'στάθηκα'}},
             'paratatikos': {'active': {'έστηνα'}, 'passive': {'στηνόμουν'}}, 'act_pres_participle': {'στήνοντας'},
             'passive_perfect_participle': {'στημένος'}, 'modal': False},

        )

    def test_verb_kathisto(self):
        self.assertDictEqual(
            verb.create_basic_forms('καθιστώ'),
            {'present': {'active': {'καθιστώ'}, 'passive': {'καθίσταμαι'}},
             'conjunctive': {'active': {'καταστήσω'}, 'passive': {'καταστώ'}},
             'aorist': {'active': {'κατάστησα', 'κατέστησα'}, 'passive': {'κατέστη'}},
             'paratatikos': {'active': {'καθιστούσα'}, 'passive': {'καθιστάμην'}},
             'act_pres_participle': {'καθιστώντας'}, 'arch_act_pres_participle': {'καθιστών/καθιστώσα/καθιστών'},
             'passive_perfect_participle': {'κατεστημένος'}, 'pass_pres_participle': {'καθιστάμενος'},
             'modal': False},

        )

    def test_verb_antikathistw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('αντικαθιστώ'),
            {'present': {'active': {'αντικαθιστώ'}, 'passive': {'αντικαθίσταμαι'}},
             'conjunctive': {'active': {'αντικαταστήσω'}, 'passive': {'αντικαταστώ'}},
             'aorist': {'active': {'αντικατάστησα', 'αντικατέστησα'}, 'passive': {'αντικατέστη'}},
             'paratatikos': {'active': {'αντικαθιστούσα'}}, 'act_pres_participle': {'αντικαθιστώντας'},
             'pass_pres_participle': {'αντικαθιστώμενος', 'αντικαθιστάμενος'},
             'passive_perfect_participle': {'αντικαταστημένος', 'αντικατεστημένος'}, 'modal': False},

        )

    def test_verb_anastainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανασταίνω'),
            {'present': {'active': {'ανασταίνω'}, 'passive': {'ανασταίνομαι'}}, 'conjunctive': {'active': {'αναστήσω'}},
             'aorist': {'active': {'ανάστησα', 'ανέστησα'}},
             'paratatikos': {'active': {'ανέσταινα', 'ανάσταινα'}, 'passive': {'ανασταινόμουν'}},
             'act_pres_participle': {'ανασταίνοντας'}, 'passive_perfect_participle': {'αναστημένος'},
             'active_aorist_participle': {'αναστήσας/αναστήσασα/αναστήσαν'}, 'modal': False},

        )

    def test_verb_ago(self):
        self.assertDictEqual(
            verb.create_basic_forms('άγω'),
            {'present': {'active': {'άγω'}, 'passive': {'άγομαι'}},
             'conjunctive': {'active': {'αγάγω'}, 'passive': {'αχθώ'}},
             'aorist': {'active': {'ήγαγα'}, 'passive': {'ήχθη'}},
             'paratatikos': {'active': {'ήγα'}, 'passive': {'αγόμουν'}},
             'act_pres_participle': {'άγοντας'}, 'arch_act_pres_participle': {'άγων/άγουσα/άγον'},
             'pass_pres_participle': {'αγόμενος'}, 'modal': False},

        )

    def test_verb_elegxw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ελέγχω'),
            {'present': {'active': {'ελέγχω'}, 'passive': {'ελέγχομαι'}},
             'conjunctive': {'active': {'ελέγξω'}, 'passive': {'ελεγχτώ', 'ελεγχθώ'}},
             'aorist': {'active': {'έλεγξα'}, 'passive': {'ελέγχτηκα', 'ελέγχθηκα'}},
             'paratatikos': {'active': {'έλεγχα'}, 'passive': {'ελεγχόμουν'}}, 'act_pres_participle': {'ελέγχοντας'},
             'arch_act_pres_participle': {'ελέγχων/ελέγχουσα/ελέγχον'}, 'pass_pres_participle': {'ελεγχόμενος'},
             'passive_perfect_participle': {'ελεγμένος'},
             'modal': False},

        )

    def test_verb_apolambano(self):
        self.assertDictEqual(
            verb.create_basic_forms('απολαμβάνω'),
            {'present': {'active': {'απολαμβάνω'}}, 'conjunctive': {'active': {'απολαύσω'}},
             'aorist': {'active': {'απόλαυσα'}}, 'paratatikos': {'active': {'απολάμβανα'}},
             'act_pres_participle': {'απολαμβάνοντας'}, 'modal': False},

        )

    def test_verb_memfomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('μέμφομαι'),
            {'present': {'passive': {'μέμφομαι'}}, 'conjunctive': {'passive': {'μεμφτώ', 'μεμφθώ'}},
             'aorist': {'passive': {'μέμφθηκα', 'μέμφτηκα'}}, 'paratatikos': {'passive': {'μεμφόμουν'}},
             'pass_pres_participle': {'μεμφόμενος'}, 'modal': False},

        )

    def test_verb_katalabainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταλαβαίνω'),
            {'present': {'active': {'καταλαβαίνω'}, 'passive': {'καταλαβαίνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}}, 'aorist': {'active': {'κατάλαβα'}},
             'paratatikos': {'active': {'καταλάβαινα'}, 'passive': {'καταλαβαινόμουν'}},
             'act_pres_participle': {'καταλαβαίνοντας'}, 'modal': False},

        )

    def test_verb_katalambanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταλαμβάνω'),
            {'present': {'active': {'καταλαμβάνω'}, 'passive': {'καταλαμβάνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}, 'passive': {'καταληφθώ'}},
             'aorist': {'active': {'κατέλαβα'}, 'passive': {'καταλήφθηκα', 'κατελήφθη'}},
             'paratatikos': {'active': {'καταλάμβανα', 'κατελάμβανα'}, 'passive': {'καταλαμβανόμουν'}},
             'act_pres_participle': {'καταλαμβάνοντας'}, 'pass_pres_participle': {'καταλαμβανόμενος'},
             'passive_aorist_participle': {'καταληφθείς/καταληφθείσα/καταληφθέν'},
             'passive_perfect_participle': {'κατειλημμένος'},'modal': False},

        )

    def test_verb_antilambanomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('αντιλαμβάνομαι'),
            {'present': {'passive': {'αντιλαμβάνομαι'}}, 'conjunctive': {'passive': {'αντιληφθώ'}},
             'aorist': {'passive': {'αντιλήφθηκα', 'αντελήφθη'}}, 'paratatikos': {'passive': {'αντιλαμβανόμουν'}},
             'pass_pres_participle': {'αντιλαμβανόμενος'},
             'passive_aorist_participle': {'αντιληφθείς/αντιληφθείσα/αντιληφθέν'}, 'modal': False},

        )

    def test_verb_symponw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συμπονώ'),
            {'present': {'active': {'συμπονώ'}, 'passive': {'συμπονούμαι', 'συμπονιέμαι'}},
             'conjunctive': {'active': {'συμπονέσω'}, 'passive': {'συμπονηθώ'}},
             'aorist': {'active': {'συμπόνεσα'}, 'passive': {'συμπονήθηκα'}},
             'paratatikos': {'active': {'συμπόναγα', 'συμπονούσα'}}, 'act_pres_participle': {'συμπονώντας'},
             'passive_aorist_participle': {'συμπονηθείς/συμπονηθείσα/συμπονηθέν'}, 'modal': False},

        )

    def test_verb_synkrinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συγκρίνω'),
            {'present': {'active': {'συγκρίνω'}, 'passive': {'συγκρίνομαι'}},
             'conjunctive': {'active': {'συγκρίνω'}, 'passive': {'συγκριθώ'}},
             'aorist': {'active': {'συνέκρινα'}, 'passive': {'συγκρίθηκα'}},
             'paratatikos': {'active': {'συνέκρινα'}, 'passive': {'συγκρινόμουν'}},
             'act_pres_participle': {'συγκρίνοντας'}, 'pass_pres_participle': {'συγκρινόμενος'},
             'passive_perfect_participle': {'συγκριμένος', 'συγκεκριμένος'}, 'modal': False},

        )

    def test_verb_syntribw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συντρίβω'),
            {'present': {'active': {'συντρίβω'}, 'passive': {'συντρίβομαι'}},
             'conjunctive': {'active': {'συντρίψω'}, 'passive': {'συντριφτώ', 'συντριβώ'}},
             'aorist': {'active': {'συνέτριψα'}, 'passive': {'συνετρίβη', 'συντρίφτηκα'}},
             'paratatikos': {'active': {'συνέτριβα'}, 'passive': {'συντριβόμουν'}},
             'act_pres_participle': {'συντρίβοντας'}, 'passive_perfect_participle': {'συντετριμμένος', 'συντριμμένος'},
             'modal': False},

        )

    def test_verb_xairw(self):
        self.assertDictEqual(
            verb.create_basic_forms('χαίρω'),
            {'present': {'active': {'χαίρω'}, 'passive': {'χαίρομαι'}},
             'conjunctive': {'active': {'χαίρω'}, 'passive': {'χαρώ'}},
             'aorist': {'active': {'έχαιρα'}, 'passive': {'χάρηκα'}},
             'paratatikos': {'active': {'έχαιρα'}, 'passive': {'χαιρόμουν'}}, 'act_pres_participle': {'χαίροντας'},
             'arch_act_pres_participle': {'χαίρων/χαίρουσα/χαίρον'}, 'pass_pres_participle': {'χαρούμενος'},
             'modal': False},

        )

    def test_verb_parkaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('παρκάρω'),
            {'present': {'active': {'παρκάρω'}, 'passive': {'παρκάρομαι'}},
             'conjunctive': {'active': {'παρκαρίσω', 'παρκάρω'}, 'passive': {'παρκαριστώ'}},
             'aorist': {'active': {'πάρκαρα', 'παρκάρισα'}, 'passive': {'παρκαρίστηκα'}},
             'paratatikos': {'active': {'πάρκαρα'}, 'passive': {'παρκαρόμουν'}}, 'act_pres_participle': {'παρκάροντας'},
             'passive_perfect_participle': {'παρκαρισμένος'}, 'modal': False},

        )

    def test_verb_sokaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('σοκάρω'),
            {'present': {'active': {'σοκάρω'}, 'passive': {'σοκάρομαι'}},
             'conjunctive': {'active': {'σοκάρω', 'σοκαρίσω'}, 'passive': {'σοκαρισθώ', 'σοκαριστώ'}},
             'aorist': {'active': {'σοκάρισα', 'σόκαρα'}, 'passive': {'σοκαρίσθηκα', 'σοκαρίστηκα'}},
             'paratatikos': {'active': {'σόκαρα'}, 'passive': {'σοκαρόμουν'}}, 'act_pres_participle': {'σοκάροντας'},
             'passive_perfect_participle': {'σοκαρισμένος'}, 'modal': False},

        )

    def test_verb_epanalambanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('αναλαμβάνω'),
            {'present': {'active': {'αναλαμβάνω'}, 'passive': {'αναλαμβάνομαι'}},
             'conjunctive': {'active': {'αναλάβω'}, 'passive': {'αναληφθώ'}},
             'aorist': {'active': {'ανάλαβα', 'ανέλαβα'}, 'passive': {'ανελήφθη', 'αναλήφθηκα'}},
             'paratatikos': {'active': {'αναλάμβανα', 'ανελάμβανα'}, 'passive': {'αναλαμβανόμουν'}},
             'act_pres_participle': {'αναλαμβάνοντας'}, 'pass_pres_participle': {'αναλαμβανόμενος'},
             'passive_aorist_participle': {'αναληφθείς/αναληφθείσα/αναληφθέν'},
             'passive_perfect_participle': {'ανειλημμένος'},
'modal': False},

        )

    def test_verb_proteinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('επιτίθεμαι'),
            {'present': {'passive': {'επιτίθεμαι'}}, 'conjunctive': {'passive': {'επιτεθώ'}},
             'aorist': {'passive': {'επιτέθηκα', 'επετέθη'}}, 'paratatikos': {'passive': {'επιτιθέμην'}},
             'pass_pres_participle': {'επιτιθέμενος'}, 'passive_perfect_participle': {'επιτεθειμένος'},
             'passive_aorist_participle': {'επιτεθείς/επιτεθείσα/επιτεθέν'}, 'modal': False},

        )

    def test_verb_diaftheirw(self):
        self.assertDictEqual(
            verb.create_basic_forms('διαφθείρω'),
            {'present': {'active': {'διαφθείρω'}, 'passive': {'διαφθείρομαι'}},
             'conjunctive': {'active': {'διαφθείρω'}, 'passive': {'διαφθαρώ'}},
             'aorist': {'active': {'διέφθειρα'}, 'passive': {'διαφθάρηκα', 'διεφθάρη'}},
             'paratatikos': {'active': {'διέφθειρα'}, 'passive': {'διαφθειρόμουν'}},
             'act_pres_participle': {'διαφθείροντας'}, 'pass_pres_participle': {'διαφθειρόμενος'},
             'passive_perfect_participle': {'διεφθαρμένος', 'διαφθαρμένος'},
             'passive_aorist_participle': {'διαφθαρείς/διαφθαρείσα/διαφθαρέν'}, 'modal': False},

        )

    def test_verb_vazo(self):
        self.assertDictEqual(
            verb.create_basic_forms('βάζω'),
            {'present': {'active': {'βάζω'}}, 'conjunctive': {'active': {'βάλω'}, 'passive': {'βαλθώ'}},
             'aorist': {'active': {'έβαλα'}, 'passive': {'βάλθηκα'}}, 'paratatikos': {'active': {'έβαζα'}},
             'act_pres_participle': {'βάζοντας'}, 'passive_perfect_participle': {'βαλμένος'},
             'active_aorist_participle': {'βαλών/βαλούσα/βαλόν'}, 'modal': False},

        )

    def test_verb_ανebazw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανεβάζω'),
            {'present': {'active': {'ανεβάζω'}, 'passive': {'ανεβάζομαι'}},
             'conjunctive': {'active': {'ανεβάσω'}, 'passive': {'ανεβαστώ'}},
             'aorist': {'active': {'ανέβασα'}, 'passive': {'ανεβάστηκα'}},
             'paratatikos': {'active': {'ανέβαζα'}, 'passive': {'ανεβαζόμουν'}}, 'act_pres_participle': {'ανεβάζοντας'},
             'passive_perfect_participle': {'ανεβασμένος'}, 'modal': False},

        )

    def test_verb_katexo(self):
        self.assertDictEqual(
            verb.create_basic_forms('κατέχω'),
            {'act_pres_participle': {'κατέχοντας'},
             'aorist': {'active': {'κατείχα'}},
             'arch_act_pres_participle': {'κατέχων/κατέχουσα/κατέχον'},
             'conjunctive': {'active': {'κατάσχω', 'κατέχω'}},
             'modal': False,
             'paratatikos': {'active': {'κάτεχα', 'κατείχα'}, 'passive': {'κατεχόμουν'}},
             'pass_pres_participle': {'κατεχόμενος'},
             'present': {'active': {'κατέχω'}, 'passive': {'κατέχομαι'}}},

        )

    def test_verb_krossaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('κροσσάρω'),
            {'present': {'active': {'κροσσάρω'}}, 'conjunctive': {'active': {'κροσσαρίσω', 'κροσσάρω'}},
             'aorist': {'active': {'κροσσάρισα', 'κρόσσαρα'}}, 'paratatikos': {'active': {'κρόσσαρα'}},
             'act_pres_participle': {'κροσσάροντας'}, 'modal': False},

        )

    def test_verb_apantexw(self):
        self.assertDictEqual(
            verb.create_basic_forms('απαντέχω'),
            {'act_pres_participle': {'απαντέχοντας'},
             'aorist': {},
             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'απάντεχα'}},
             'present': {'active': {'απαντέχω'}}},

        )

    def test_verb_spaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('σπάω'),
            {'present': {'active': {'σπάω'}}, 'conjunctive': {'active': {'σπάσω'}, 'passive': {'σπαστώ', 'σπασθώ'}},
             'aorist': {'active': {'έσπασα'}, 'passive': {'σπάσθηκα', 'σπάστηκα'}},
             'paratatikos': {'active': {'έσπαγα'}}, 'act_pres_participle': {'σπάγοντας'},
             'passive_perfect_participle': {'σπασμένος'}, 'modal': False},

        )

    def test_verb_pempw(self):
        self.assertDictEqual(
            verb.create_basic_forms('πέμπω'),
            {'present': {'active': {'πέμπω'}, 'passive': {'πέμπομαι'}},
             'conjunctive': {'active': {'πέμψω'}, 'passive': {'πεμφθώ'}},
             'aorist': {'active': {'έπεμψα'}, 'passive': {'πέμφθηκα'}},
             'paratatikos': {'active': {'έπεμπα'}, 'passive': {'πεμπόμουν'}}, 'act_pres_participle': {'πέμποντας'},
             'modal': False},

        )

    def test_verb_sfinggw(self):
        self.assertDictEqual(
            verb.create_basic_forms('σφίγγω'),
            {'present': {'active': {'σφίγγω'}, 'passive': {'σφίγγομαι'}},
             'conjunctive': {'active': {'σφίξω'}, 'passive': {'σφιχτώ'}},
             'aorist': {'active': {'έσφιξα'}, 'passive': {'σφίχτηκα'}},
             'paratatikos': {'active': {'έσφιγγα'}, 'passive': {'σφιγγόμουν'}}, 'act_pres_participle': {'σφίγγοντας'},
             'passive_perfect_participle': {'σφιγμένος'}, 'modal': False},

        )

    def test_verb_eggrafw(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('εγγράφω'),
            {'present': {'active': {'εγγράφω'}, 'passive': {'εγγράφομαι'}},
             'conjunctive': {'active': {'εγγράψω'}, 'passive': {'εγγραφώ', 'εγγραφτώ'}},
             'aorist': {'active': {'ενέγραψα'}, 'passive': {'εγγράφηκα', 'ενεγράφη', 'εγγράφτηκα'}},
             'paratatikos': {'active': {'ενέγραφα', 'έγγραφα'}, 'passive': {'εγγραφόμουν'}},
             'act_pres_participle': {'εγγράφοντας'}, 'arch_act_pres_participle': {'εγγράφων/εγγράφουσα/εγγράφον'},
             'pass_pres_participle': {'εγγραφόμενος'}, 'passive_perfect_participle': {'εγγραμμένος', 'εγγεγραμμένος'},
             'active_aorist_participle': {'εγγράψας/εγγράψασα/εγγράψαν'}, 'modal': False},

        )

    def test_verb_syggrafo(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('συγγράφω'),
            {'present': {'active': {'συγγράφω'}, 'passive': {'συγγράφομαι'}},
             'conjunctive': {'active': {'συγγράψω'}, 'passive': {'συγγραφτώ', 'συγγραφώ'}},
             'aorist': {'active': {'συνέγραψα'}, 'passive': {'συνεγράφη', 'συγγράφηκα', 'συγγράφτηκα'}},
             'paratatikos': {'active': {'συνέγραφα'}, 'passive': {'συγγραφόμουν'}},
             'act_pres_participle': {'συγγράφοντας'}, 'pass_pres_participle': {'συγγραφόμενος'},
             'passive_perfect_participle': {'συγγεγραμμένος'},
             'active_aorist_participle': {'συγγράψας/συγγράψασα/συγγράψαν'}, 'modal': False},

        )

    def test_verb_fylaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('φυλάω'),
            {'present': {'active': {'φυλάω'}}, 'conjunctive': {'active': {'φυλάξω'}},

             'aorist': {'active': {'εφύλαξα', 'φύλαξα'}}, 'paratatikos': {'active': {'φυλούσα', 'φύλαγα'}},
             'act_pres_participle': {'φυλώντας'}, 'passive_perfect_participle': {'φυλαγμένος'}, 'modal': False},

        )

    def test_verb_paw(self):
        self.assertDictEqual(
            verb.create_basic_forms('πάω'),
            {'present': {'active': {'πάω'}}, 'conjunctive': {'active': {'πάω'}}, 'aorist': {'active': {'πήγα'}},
             'paratatikos': {'active': {'πήγαινα'}}, 'modal': False},

        )

    def test_verb_kanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κάνω'),
            {'present': {'active': {'κάνω'}}, 'conjunctive': {'active': {'κάνω'}}, 'aorist': {'active': {'έκανα'}},
             'paratatikos': {'active': {'έκανα'}}, 'act_pres_participle': {'κάνοντας'},
             'passive_perfect_participle': {'καμωμένος'}, 'modal': False},

        )

    def test_verb_kaiw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καίω'),
            {'present': {'active': {'καίω'}, 'passive': {'καίγομαι'}},
             'conjunctive': {'active': {'κάψω'}, 'passive': {'καώ'}},
             'aorist': {'active': {'έκαψα'}, 'passive': {'καήκα', 'κάηκα'}},
             'paratatikos': {'active': {'έκαιγα'}, 'passive': {'καιγόμουν'}}, 'act_pres_participle': {'καίγοντας'},
             'pass_pres_participle': {'καιγόμενος'}, 'passive_perfect_participle': {'καμένος'}, 'modal': False},

        )

    def test_verb_agapao(self):
        self.assertDictEqual(
            verb.create_basic_forms('αγαπάω'),
            {'present': {'active': {'αγαπάω'}, 'passive': {'αγαπώμαι', 'αγαπιέμαι'}},
             'conjunctive': {'active': {'αγαπήσω'}, 'passive': {'αγαπηθώ'}},
             'aorist': {'active': {'αγάπησα'}, 'passive': {'αγαπήθηκα'}},
             'paratatikos': {'active': {'αγαπούσα', 'αγάπαγα'}, 'passive': {'αγαπιόμουν'}},
             'act_pres_participle': {'αγαπώντας'}, 'arch_act_pres_participle': {'αγαπών/αγαπώσα/αγαπών'},
             'passive_perfect_participle': {'αγαπημένος'},
             'passive_aorist_participle': {'αγαπηθείς/αγαπηθείσα/αγαπηθέν'}, 'modal': False},

        )

    def test_verb_epembenw(self):
        self.assertDictEqual(
            verb.create_basic_forms('επεμβαίνω'),
            {'present': {'active': {'επεμβαίνω'}}, 'conjunctive': {'active': {'επεμβώ'}},
             'aorist': {'active': {'επενέβη', 'επεμβήκα', 'επέμβηκα'}}, 'paratatikos': {'active': {'επενέβαινα'}},
             'act_pres_participle': {'επεμβαίνοντας'},
             'arch_act_pres_participle': {'επεμβαίνων/επεμβαίνουσα/επεμβαίνον'}, 'modal': False},

        )

    def test_verb_kylaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κυλάω'),
            {'present': {'active': {'κυλάω'}, 'passive': {'κυλιέμαι'}},
             'conjunctive': {'active': {'κυλήσω'}, 'passive': {'κυλιστώ'}},
             'aorist': {'active': {'κύλησα'}, 'passive': {'κυλίστηκα'}},
             'paratatikos': {'active': {'κύλαγα', 'κυλούσα'}, 'passive': {'κυλιόμουν'}},
             'act_pres_participle': {'κυλώντας'}, 'passive_perfect_participle': {'κυλισμένος'}, 'modal': False},

        )

    def test_verb_anexomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανέχομαι'),
            {'present': {'passive': {'ανέχομαι'}}, 'conjunctive': {'passive': {'ανεχτώ', 'ανεχθώ'}},
             'aorist': {'passive': {'ανέχθηκα', 'ανέχτηκα'}}, 'paratatikos': {'passive': {'ανεχόμουν'}},
             'pass_pres_participle': {'ανεχόμενος'}, 'modal': False},

        )

    def test_verb_anago(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανάγω'),
            {'present': {'active': {'ανάγω'}, 'passive': {'ανάγομαι'}},
             'conjunctive': {'active': {'αναγάγω'}, 'passive': {'αναχθώ'}},
             'aorist': {'active': {'ανήγαγα'}, 'passive': {'ανήχθη', 'ανάχθηκα'}},
             'paratatikos': {'active': {'ανήγα'}, 'passive': {'αναγόμουν'}}, 'act_pres_participle': {'ανάγοντας'},
             'arch_act_pres_participle': {'ανάγων/ανάγουσα/ανάγον'}, 'pass_pres_participle': {'αναγόμενος'},
             'passive_perfect_participle': {'ανηγμένος'}, 'passive_aorist_participle': {'αναχθείς/αναχθείσα/αναχθέν'},
             'modal': False},

        )

    def test_verb_apago(self):
        self.assertDictEqual(
            verb.create_basic_forms('απάγω'),
            {'present': {'active': {'απάγω'}, 'passive': {'απάγομαι'}},
             'conjunctive': {'active': {'απαγάγω'}, 'passive': {'απαχθώ'}},
             'aorist': {'active': {'απήγαγα'}, 'passive': {'απήχθη'}},
             'paratatikos': {'active': {'απήγα'}, 'passive': {'απαγόμουν'}}, 'act_pres_participle': {'απάγοντας'},
             'pass_pres_participle': {'απαγόμενος'}, 'passive_aorist_participle': {'απαχθείς/απαχθείσα/απαχθέν'},
             'modal': False},

        )

    def test_verb_diagrafomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('διαγράφομαι'),
            {'present': {'passive': {'διαγράφομαι'}}, 'conjunctive': {'passive': {'διαγραφώ', 'διαγραφτώ'}},
             'aorist': {'passive': {'διαγράφηκα', 'διεγράφη', 'διαγράφτηκα'}},
             'paratatikos': {'passive': {'διαγραφόμουν'}}, 'pass_pres_participle': {'διαγραφόμενος'},
             'passive_perfect_participle': {'διαγραμμένος', 'διαγεγραμμένος'}, 'modal': False},

        )

    def test_verb_thelw(self):
        self.assertDictEqual(
            verb.create_basic_forms('θέλω'),
            {'present': {'active': {'θέλω'}}, 'conjunctive': {'active': {'θελήσω'}}, 'aorist': {'active': {'θέλησα'}},
             'paratatikos': {'active': {'ήθελα'}}, 'act_pres_participle': {'θέλοντας'},
             'passive_perfect_participle': {'θελημένος'}, 'modal': False},

        )

    def test_verb_dinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δίνω'),
            {'present': {'active': {'δίνω'}, 'passive': {'δίνομαι'}},
             'conjunctive': {'active': {'δώσω'}, 'passive': {'δοθώ'}},
             'aorist': {'active': {'έδωσα'}, 'passive': {'εδόθη', 'δόθηκα'}},
             'paratatikos': {'active': {'έδινα'}, 'passive': {'δινόμουν'}}, 'act_pres_participle': {'δίνοντας'},
             'passive_perfect_participle': {'δοσμένος', 'δεδομένος'},
             'passive_aorist_participle': {'δοθείς/δοθείσα/δοθέν'}, 'modal': False},

        )
