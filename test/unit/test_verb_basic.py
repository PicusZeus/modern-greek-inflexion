from unittest import TestCase, main

from modern_greek_inflexion.exceptions import NotInGreekException
from modern_greek_inflexion import verb


class VerbTestBasic(TestCase):
    def test_verb_tragoudo(self):
        self.assertDictEqual(
            verb.create_basic_forms('τραγουδώ'),
            {'present': {'active': {'τραγουδώ'}, 'passive': {'τραγουδιέμαι'}},
             'conjunctive': {'active': {'τραγουδήσω'}, 'passive': {'τραγουδηθώ'}},
             'aorist': {'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}},
             'paratatikos': {'active': {'τραγουδούσα', 'τραγούδαγα'}, 'passive': {'τραγουδιόμουν'}},
             'act_pres_participle': {'τραγουδώντας'}, 'passive_perfect_participle': {'τραγουδημένος'},
             'modal': False},
        )

    def test_verb_kathisto(self):
        self.assertDictEqual(
            verb.create_basic_forms('καθιστώ'),
            {'present': {'active': {'καθιστώ'}}, 'conjunctive': {'active': {'καταστήσω'}},
             'aorist': {'active': {'κατέστησα', 'κατάστησα'}},
             'paratatikos': {'active': {'καθιστούσα'}, 'passive': {'καθιστάμην'}},
             'act_pres_participle': {'καθιστώντας'}, 'modal': False}

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
             'modal': False}
        )

    def test_verb_phgainvo(self):
        self.assertDictEqual(
            verb.create_basic_forms('πηγαίνω'),
            {'present': {'active': {'πηγαίνω'}}, 'conjunctive': {'active': {'πάω'}},
             'aorist': {'active': {'πήγα'}}, 'paratatikos': {'active': {'πήγαινα'}},
             'act_pres_participle': {'πηγαίνοντας'},
             'modal': False}
        )

    def test_verb_nothing(self):
        self.assertRaises(NotInGreekException, verb.create_basic_forms, '')

    def test_verb_gibberish(self):
        self.assertRaises(NotInGreekException, verb.create_basic_forms, 'gamao')

    def test_verb_prokeitai(self):
        self.assertDictEqual(
            verb.create_basic_forms('πρόκειται'),
            {'present': {'passive': {'πρόκειται'}}, 'paratatikos': {'passive': {'επρόκειτο'}},
             'modal': True}
        )

    def test_verb_erxomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('έρχομαι'),
            {'present': {'passive': {'έρχομαι'}},
             'conjunctive': {'active': {'έλθω', 'έρθω'}},
             'aorist': {'active': {'ήλθα', 'ήρθα'}},
             'paratatikos': {'passive': {'ερχόμουν'}},
             'pass_pres_participle': {'ερχόμενος'},
             'modal': False}
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
             'modal': False}
        )

    def test_verb_arnoumai(self):
        self.assertDictEqual(
            verb.create_basic_forms('αρνιέμαι'),
            {'present': {'passive': {'αρνιέμαι', 'αρνούμαι'}}, 'conjunctive': {'passive': {'αρνηθώ'}},
             'aorist': {'passive': {'αρνήθηκα'}}, 'paratatikos': {'passive': {'αρνούμουν', 'αρνιόμουν'}},
             'pass_pres_participle': {'αρνούμενος'},
             'modal': False}
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
             'passive_aorist_participle': {'εισαχθείς/εισαχθείσα/εισαχθέν'}, 'modal': False}

        )

    def test_verb_dialego(self):
        self.maxDiff = None
        self.assertDictEqual(
            verb.create_basic_forms('διαλέγω'),
            {'present': {'active': {'διαλέγω'}, 'passive': {'διαλέγομαι'}},
             'conjunctive': {'active': {'διαλέξω'}, 'passive': {'διαλεχθώ', 'διαλεχτώ'}},
             'aorist': {'active': {'διάλεξα'}, 'passive': {'διαλέχτηκα', 'διαλέχθηκα'}},
             'paratatikos': {'active': {'διάλεγα'}, 'passive': {'διαλεγόμουν'}}, 'act_pres_participle': {'διαλέγοντας'},
             'pass_pres_participle': {'διαλεγόμενος'}, 'passive_perfect_participle': {'διαλεγμένος'}, 'modal': False}

        )

    def test_verb_deiknuw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δεικνύω'),
            {'present': {'active': {'δεικνύω'}, 'passive': {'δεικνύομαι'}},
             'conjunctive': {'active': {'δείξω'}, 'passive': {'δειχθώ'}},
             'aorist': {'active': {'έδειξα'}, 'passive': {'δείχθηκα'}},
             'paratatikos': {'passive': {'δεικνυόμουν'}}, 'act_pres_participle': {'δεικνύοντας'},
             'arch_act_pres_participle': {'δεικνύων/δεικνύουσα/δεικνύον'}, 'pass_pres_participle': {'δεικνυόμενος'},
             'active_aorist_participle': {'δείξας/δείξασα/δείξαν'},
             'passive_perfect_participle': {'δειγμένος'},

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
             'modal': False}

        )

    def test_verb_kleptw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κλέπτω'),
            {'present': {'active': {'κλέπτω'}, 'passive': {'κλέπτομαι'}},
             'conjunctive': {'active': {'κλέψω'}, 'passive': {'κλαπώ', 'κλεφτώ'}},
             'aorist': {'active': {'έκλεψα'}, 'passive': {'κλέφτηκα', 'κλάπηκα', 'εκλάπη'}},
             'paratatikos': {'passive': {'κλεπτόμουν'}}, 'act_pres_participle': {'κλέπτοντας'},
             'passive_perfect_participle': {'κλεμμένος'}, 'modal': False}

        )

    def test_verb_proferw(self):
        self.assertDictEqual(
            verb.create_basic_forms('προφέρω'),
            {'present': {'active': {'προφέρω'}, 'passive': {'προφέρομαι'}},
             'conjunctive': {'active': {'προφέρω'}, 'passive': {'προφερθώ'}},
             'aorist': {'active': {'πρόφερα'}, 'passive': {'προφέρθηκα'}},
             'paratatikos': {'active': {'πρόφερα'}, 'passive': {'προφερόμουν'}}, 'act_pres_participle': {'προφέροντας'},
             'passive_perfect_participle': {'προφερμένος'}, 'modal': False}

        )

    def test_verb_sthnw(self):
        self.assertDictEqual(
            verb.create_basic_forms('στήνω'),
            {'present': {'active': {'στήνω'}, 'passive': {'στήνομαι'}},
             'conjunctive': {'active': {'στήσω'}, 'passive': {'σταθώ'}},
             'aorist': {'active': {'έστησα'}, 'passive': {'στάθηκα'}},
             'paratatikos': {'active': {'έστηνα'}, 'passive': {'στηνόμουν'}}, 'act_pres_participle': {'στήνοντας'},
             'passive_perfect_participle': {'στημένος'}, 'modal': False}

        )

    def test_verb_ago(self):
        self.assertDictEqual(
            verb.create_basic_forms('άγω'),
            {'present': {'active': {'άγω'}, 'passive': {'άγομαι'}},
             'conjunctive': {'active': {'αγάγω'}, 'passive': {'αχθώ'}},
             'aorist': {'active': {'ήγαγα'}, 'passive': {'ήχθη'}},
             'paratatikos': {'active': {'ήγα'}, 'passive': {'αγόμουν'}},
             'act_pres_participle': {'άγοντας'}, 'arch_act_pres_participle': {'άγων/άγουσα/άγον'},
             'pass_pres_participle': {'αγόμενος'}, 'modal': False}

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
             'modal': False}

        )

    def test_verb_apolambano(self):
        self.assertDictEqual(
            verb.create_basic_forms('απολαμβάνω'),
            {'present': {'active': {'απολαμβάνω'}}, 'conjunctive': {'active': {'απολαύσω'}},
             'aorist': {'active': {'απόλαυσα'}}, 'paratatikos': {'active': {'απολάμβανα'}},
             'act_pres_participle': {'απολαμβάνοντας'}, 'modal': False}

        )

    def test_verb_memfomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('μέμφομαι'),
            {'present': {'passive': {'μέμφομαι'}}, 'conjunctive': {'passive': {'μεμφτώ', 'μεμφθώ'}},
             'aorist': {'passive': {'μέμφθηκα', 'μέμφτηκα'}}, 'paratatikos': {'passive': {'μεμφόμουν'}},
             'pass_pres_participle': {'μεμφόμενος'}, 'modal': False}

        )

    def test_verb_katalabainw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταλαβαίνω'),
            {'present': {'active': {'καταλαβαίνω'}, 'passive': {'καταλαβαίνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}}, 'aorist': {'active': {'κατάλαβα'}},
             'paratatikos': {'active': {'καταλάβαινα'}, 'passive': {'καταλαβαινόμουν'}},
             'act_pres_participle': {'καταλαβαίνοντας'}, 'modal': False}

        )

    def test_verb_katalambanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καταλαμβάνω'),
            {'present': {'active': {'καταλαμβάνω'}, 'passive': {'καταλαμβάνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}, 'passive': {'καταληφθώ'}},
             'aorist': {'active': {'κατέλαβα'}, 'passive': {'καταλήφθηκα', 'κατελήφθη'}},
             'paratatikos': {'active': {'καταλάμβανα', 'κατελάμβανα'}, 'passive': {'καταλαμβανόμουν'}},
             'act_pres_participle': {'καταλαμβάνοντας'}, 'pass_pres_participle': {'καταλαμβανόμενος'},
             'passive_aorist_participle': {'καταληφθείς/καταληφθείσα/καταληφθέν'}, 'modal': False}

        )

    def test_verb_antilambanomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('αντιλαμβάνομαι'),
            {'present': {'passive': {'αντιλαμβάνομαι'}}, 'conjunctive': {'passive': {'αντιληφθώ'}},
             'aorist': {'passive': {'αντιλήφθηκα', 'αντελήφθη'}}, 'paratatikos': {'passive': {'αντιλαμβανόμουν'}},
             'pass_pres_participle': {'αντιλαμβανόμενος'},
             'passive_aorist_participle': {'αντιληφθείς/αντιληφθείσα/αντιληφθέν'}, 'modal': False}

        )

    def test_verb_symponw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συμπονώ'),
            {'present': {'active': {'συμπονώ'}, 'passive': {'συμπονούμαι', 'συμπονιέμαι'}},
             'conjunctive': {'active': {'συμπονέσω'}, 'passive': {'συμπονηθώ'}},
             'aorist': {'active': {'συμπόνεσα'}, 'passive': {'συμπονήθηκα'}},
             'paratatikos': {'active': {'συμπόναγα', 'συμπονούσα'}}, 'act_pres_participle': {'συμπονώντας'},
             'passive_aorist_participle': {'συμπονηθείς/συμπονηθείσα/συμπονηθέν'}, 'modal': False})

    def test_verb_synkrinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('συγκρίνω'),
            {'present': {'active': {'συγκρίνω'}, 'passive': {'συγκρίνομαι'}},
             'conjunctive': {'active': {'συγκρίνω'}, 'passive': {'συγκριθώ'}},
             'aorist': {'active': {'συνέκρινα'}, 'passive': {'συγκρίθηκα'}},
             'paratatikos': {'active': {'συνέκρινα'}, 'passive': {'συγκρινόμουν'}},
             'act_pres_participle': {'συγκρίνοντας'}, 'pass_pres_participle': {'συγκρινόμενος'},
             'passive_perfect_participle': {'συγκριμένος', 'συγκεκριμένος'}, 'modal': False}

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
             'modal': False}

        )

    def test_verb_parkaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('παρκάρω'),
            {'present': {'active': {'παρκάρω'}, 'passive': {'παρκάρομαι'}},
             'conjunctive': {'active': {'παρκαρίσω', 'παρκάρω'}, 'passive': {'παρκαριστώ'}},
             'aorist': {'active': {'πάρκαρα', 'παρκάρισα'}, 'passive': {'παρκαρίστηκα'}},
             'paratatikos': {'active': {'πάρκαρα'}, 'passive': {'παρκαρόμουν'}}, 'act_pres_participle': {'παρκάροντας'},
             'passive_perfect_participle': {'παρκαρισμένος'}, 'modal': False}

        )

    def test_verb_sokaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('σοκάρω'),
            {'present': {'active': {'σοκάρω'}, 'passive': {'σοκάρομαι'}},
             'conjunctive': {'active': {'σοκάρω', 'σοκαρίσω'}, 'passive': {'σοκαρισθώ', 'σοκαριστώ'}},
             'aorist': {'active': {'σοκάρισα', 'σόκαρα'}, 'passive': {'σοκαρίσθηκα', 'σοκαρίστηκα'}},
             'paratatikos': {'active': {'σόκαρα'}, 'passive': {'σοκαρόμουν'}}, 'act_pres_participle': {'σοκάροντας'},
             'passive_perfect_participle': {'σοκαρισμένος'}, 'modal': False}

        )

    def test_verb_epanalambanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('αναλαμβάνω'),
            {'present': {'active': {'αναλαμβάνω'}, 'passive': {'αναλαμβάνομαι'}},
             'conjunctive': {'active': {'αναλάβω'}, 'passive': {'αναληφθώ'}},
             'aorist': {'active': {'ανάλαβα', 'ανέλαβα'}, 'passive': {'ανελήφθη', 'αναλήφθηκα'}},
             'paratatikos': {'active': {'αναλάμβανα', 'ανελάμβανα'}, 'passive': {'αναλαμβανόμουν'}},
             'act_pres_participle': {'αναλαμβάνοντας'}, 'pass_pres_participle': {'αναλαμβανόμενος'},
             'passive_aorist_participle': {'αναληφθείς/αναληφθείσα/αναληφθέν'}, 'modal': False}

        )

    def test_verb_proteinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('επιτίθεμαι'),
            {'present': {'passive': {'επιτίθεμαι'}}, 'conjunctive': {'passive': {'επιτεθώ'}},
             'aorist': {'passive': {'επιτέθηκα', 'επετέθη'}}, 'paratatikos': {'passive': {'επιτιθέμην'}},
             'pass_pres_participle': {'επιτιθέμενος'}, 'passive_perfect_participle': {'επιτεθειμένος'},
             'passive_aorist_participle': {'επιτεθείς/επιτεθείσα/επιτεθέν'}, 'modal': False}

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
             'passive_aorist_participle': {'διαφθαρείς/διαφθαρείσα/διαφθαρέν'}, 'modal': False}

        )

    def test_verb_vazo(self):
        self.assertDictEqual(
            verb.create_basic_forms('βάζω'),
            {'present': {'active': {'βάζω'}}, 'conjunctive': {'active': {'βάλω'}, 'passive': {'βαλθώ'}},
             'aorist': {'active': {'έβαλα'}, 'passive': {'βάλθηκα'}}, 'paratatikos': {'active': {'έβαζα'}},
             'act_pres_participle': {'βάζοντας'}, 'passive_perfect_participle': {'βαλμένος'},
             'active_aorist_participle': {'βαλών/βαλούσα/βαλόν'}, 'modal': False}

        )

    def test_verb_ανebazw(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανεβάζω'),
            {'present': {'active': {'ανεβάζω'}, 'passive': {'ανεβάζομαι'}},
             'conjunctive': {'active': {'ανεβάσω'}, 'passive': {'ανεβαστώ'}},
             'aorist': {'active': {'ανέβασα'}, 'passive': {'ανεβάστηκα'}},
             'paratatikos': {'active': {'ανέβαζα'}, 'passive': {'ανεβαζόμουν'}}, 'act_pres_participle': {'ανεβάζοντας'},
             'passive_perfect_participle': {'ανεβασμένος'}, 'modal': False}

        )

    def test_verb_katexo(self):
        self.assertDictEqual(
            verb.create_basic_forms('κατέχω'),
            {'present': {'active': {'κατέχω'}, 'passive': {'κατέχομαι'}}, 'conjunctive': {'active': {'κατάσχω'}},
             'aorist': {'active': {'κατείχα'}},
             'paratatikos': {'active': {'κάτεχα', 'κατείχα'}, 'passive': {'κατεχόμουν'}},
             'act_pres_participle': {'κατέχοντας'}, 'arch_act_pres_participle': {'κατέχων/κατέχουσα/κατέχον'},
             'pass_pres_participle': {'κατεχόμενος'}, 'modal': False}

        )

    def test_verb_krossaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('κροσσάρω'),
            {'present': {'active': {'κροσσάρω'}}, 'conjunctive': {'active': {'κροσσαρίσω', 'κροσσάρω'}},
             'aorist': {'active': {'κρόσσαρα', 'κροσσάρισα'}}, 'paratatikos': {'active': {'κρόσσαρα'}}, 'modal': False}

        )

    def test_verb_spaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('σπάω'),
            {'present': {'active': {'σπάω'}}, 'conjunctive': {'active': {'σπάσω'}, 'passive': {'σπαστώ', 'σπασθώ'}},
             'aorist': {'active': {'έσπασα'}, 'passive': {'σπάσθηκα', 'σπάστηκα'}},
             'paratatikos': {'active': {'έσπαγα'}}, 'passive_perfect_participle': {'σπασμένος'}, 'modal': False}

        )

    def test_verb_pempw(self):
        self.assertDictEqual(
            verb.create_basic_forms('πέμπω'),
            {'present': {'active': {'πέμπω'}, 'passive': {'πέμπομαι'}},
             'conjunctive': {'active': {'πέμψω'}, 'passive': {'πεμφθώ'}},
             'aorist': {'active': {'έπεμψα'}, 'passive': {'πέμφθηκα'}},
             'paratatikos': {'active': {'έπεμπα'}, 'passive': {'πεμπόμουν'}}, 'act_pres_participle': {'πέμποντας'},
             'modal': False}

        )

    def test_verb_sfinggw(self):
        self.assertDictEqual(
            verb.create_basic_forms('σφίγγω'),
            {'present': {'active': {'σφίγγω'}, 'passive': {'σφίγγομαι'}},
             'conjunctive': {'active': {'σφίξω'}, 'passive': {'σφιχτώ'}},
             'aorist': {'active': {'έσφιξα'}, 'passive': {'σφίχτηκα'}},
             'paratatikos': {'active': {'έσφιγγα'}, 'passive': {'σφιγγόμουν'}}, 'act_pres_participle': {'σφίγγοντας'},
             'passive_perfect_participle': {'σφιγμένος'}, 'modal': False}

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
             'active_aorist_participle': {'εγγράψας/εγγράψασα/εγγράψαν'}, 'modal': False}

        )

    def test_verb_syggrafo(self):
        self.assertDictEqual(
            verb.create_basic_forms('συγγράφω'),
            {'present': {'active': {'συγγράφω'}, 'passive': {'συγγράφομαι'}},
             'conjunctive': {'active': {'συγγράψω'}, 'passive': {'συγγραφτώ', 'συγγραφώ'}},
             'aorist': {'active': {'συνέγραψα'}, 'passive': {'συνεγράφη', 'συγγράφηκα', 'συγγράφτηκα'}},
             'paratatikos': {'active': {'συνέγραφα'}, 'passive': {'συγγραφόμουν'}},
             'act_pres_participle': {'συγγράφοντας'}, 'pass_pres_participle': {'συγγραφόμενος'},
             'passive_perfect_participle': {'συγγεγραμμένος'},
             'active_aorist_participle': {'συγγράψας/συγγράψασα/συγγράψαν'}, 'modal': False}

        )

    def test_verb_fylaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('φυλάω'),
            {'present': {'active': {'φυλάω'}}, 'conjunctive': {'active': {'φυλάξω'}},
             'aorist': {'active': {'εφύλαξα', 'φύλαξα'}}, 'paratatikos': {'active': {'φυλούσα', 'φύλαγα'}},
             'act_pres_participle': {'φυλώντας'}, 'passive_perfect_participle': {'φυλαγμένος'}, 'modal': False}

        )

    def test_verb_paw(self):
        self.assertDictEqual(
            verb.create_basic_forms('πάω'),
            {'present': {'active': {'πάω'}}, 'conjunctive': {'active': {'πάω'}}, 'aorist': {'active': {'πήγα'}},
             'paratatikos': {'active': {'πήγαινα'}}, 'modal': False}

        )

    def test_verb_kanw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κάνω'),
            {'present': {'active': {'κάνω'}}, 'conjunctive': {'active': {'κάνω'}}, 'aorist': {'active': {'έκανα'}},
             'paratatikos': {'active': {'έκανα'}}, 'act_pres_participle': {'κάνοντας'},
             'passive_perfect_participle': {'καμωμένος'}, 'modal': False}

        )

    def test_verb_kaiw(self):
        self.assertDictEqual(
            verb.create_basic_forms('καίω'),
            {'present': {'active': {'καίω'}, 'passive': {'καίγομαι'}},
             'conjunctive': {'active': {'κάψω'}, 'passive': {'καώ'}},
             'aorist': {'active': {'έκαψα'}, 'passive': {'κάηκα'}},
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
             'passive_aorist_participle': {'αγαπηθείς/αγαπηθείσα/αγαπηθέν'}, 'modal': False}

        )

    def test_verb_epembenw(self):
        self.assertDictEqual(
            verb.create_basic_forms('επεμβαίνω'),
            {'present': {'active': {'επεμβαίνω'}}, 'conjunctive': {'active': {'επεμβώ'}},
             'aorist': {'active': {'επενέβη', 'επέμβηκα'}}, 'paratatikos': {'active': {'επενέβαινα'}},
             'act_pres_participle': {'επεμβαίνοντας'},
             'arch_act_pres_participle': {'επεμβαίνων/επεμβαίνουσα/επεμβαίνον'}, 'modal': False}

        )

    def test_verb_kylaw(self):
        self.assertDictEqual(
            verb.create_basic_forms('κυλάω'),
            {'present': {'active': {'κυλάω'}, 'passive': {'κυλιέμαι'}},
             'conjunctive': {'active': {'κυλήσω'}, 'passive': {'κυλιστώ'}},
             'aorist': {'active': {'κύλησα'}, 'passive': {'κυλίστηκα'}},
             'paratatikos': {'active': {'κύλαγα', 'κυλούσα'}, 'passive': {'κυλιόμουν'}},
             'act_pres_participle': {'κυλώντας'}, 'passive_perfect_participle': {'κυλισμένος'}, 'modal': False}

        )

    def test_verb_anexomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανέχομαι'),
            {'present': {'passive': {'ανέχομαι'}}, 'conjunctive': {'passive': {'ανεχτώ', 'ανεχθώ'}},
             'aorist': {'passive': {'ανέχθηκα', 'ανέχτηκα'}}, 'paratatikos': {'passive': {'ανεχόμουν'}},
             'pass_pres_participle': {'ανεχόμενος'}, 'modal': False}

        )

    def test_verb_anago(self):
        self.assertDictEqual(
            verb.create_basic_forms('ανάγω'),
            {'present': {'active': {'ανάγω'}, 'passive': {'ανάγομαι'}},
             'conjunctive': {'active': {'αναγάγω'}, 'passive': {'αναχθώ'}},
             'aorist': {'active': {'ανήγαγα'}, 'passive': {'ανάχθηκα'}},
             'paratatikos': {'active': {'ανήγα'}, 'passive': {'αναγόμουν'}}, 'act_pres_participle': {'ανάγοντας'},
             'arch_act_pres_participle': {'ανάγων/ανάγουσα/ανάγον'}, 'pass_pres_participle': {'αναγόμενος'},
             'passive_perfect_participle': {'ανηγμένος'}, 'passive_aorist_participle': {'αναχθείς/αναχθείσα/αναχθέν'},
             'modal': False}

        )

    def test_verb_apago(self):
        self.assertDictEqual(
            verb.create_basic_forms('απάγω'),
            {'present': {'active': {'απάγω'}, 'passive': {'απάγομαι'}},
             'conjunctive': {'active': {'απαγάγω'}, 'passive': {'απαχθώ'}},
             'aorist': {'active': {'απήγαγα'}, 'passive': {'απήχθη'}},
             'paratatikos': {'active': {'απήγα'}, 'passive': {'απαγόμουν'}}, 'act_pres_participle': {'απάγοντας'},
             'pass_pres_participle': {'απαγόμενος'}, 'passive_aorist_participle': {'απαχθείς/απαχθείσα/απαχθέν'},
             'modal': False}

        )

    def test_verb_diagrafomai(self):
        self.assertDictEqual(
            verb.create_basic_forms('διαγράφομαι'),
            {'present': {'passive': {'διαγράφομαι'}}, 'conjunctive': {'passive': {'διαγραφώ', 'διαγραφτώ'}},
             'aorist': {'passive': {'διαγράφηκα', 'διεγράφη', 'διαγράφτηκα'}},
             'paratatikos': {'passive': {'διαγραφόμουν'}}, 'pass_pres_participle': {'διαγραφόμενος'},
             'passive_perfect_participle': {'διαγραμμένος', 'διαγεγραμμένος'}, 'modal': False}

        )

    def test_verb_thelw(self):
        self.assertDictEqual(
            verb.create_basic_forms('θέλω'),
            {'present': {'active': {'θέλω'}}, 'conjunctive': {'active': {'θελήσω'}}, 'aorist': {'active': {'θέλησα'}},
             'paratatikos': {'active': {'ήθελα'}}, 'act_pres_participle': {'θέλοντας'},
             'passive_perfect_participle': {'θελημένος'}, 'modal': False}

        )

    def test_verb_dinw(self):
        self.assertDictEqual(
            verb.create_basic_forms('δίνω'),
            {'present': {'active': {'δίνω'}, 'passive': {'δίνομαι'}},
             'conjunctive': {'active': {'δώσω'}, 'passive': {'δοθώ'}},
             'aorist': {'active': {'έδωσα'}, 'passive': {'εδόθη', 'δόθηκα'}},
             'paratatikos': {'active': {'έδινα'}, 'passive': {'δινόμουν'}}, 'act_pres_participle': {'δίνοντας'},
             'passive_perfect_participle': {'δοσμένος', 'δεδομένος'},
             'passive_aorist_participle': {'δοθείς/δοθείσα/δοθέν'}, 'modal': False}

        )

    # def test_verb(self):
    #     self.assertDictEqual(
    #         verb.create_basic_forms('προβάλλω'),
    #         {},
    #         print(verb.create_basic_forms('εκτίθεμαι'))
    #     )
