from unittest import TestCase

from modern_greek_inflexion.exceptions import NotInGreekException
from modern_greek_inflexion import Verb


def basic_verb(v):
    return Verb(v).basic_forms


class VerbTestBasic(TestCase):

    def test_verb_ksanarxomai(self):
        self.assertDictEqual(
            basic_verb('ξανάρχομαι'),
            {'aorist': {'active': {'ξανήρθα'}},
             'conjunctive': {'active': {'ξαναρθώ'}},
             'modal': False,
             'paratatikos': {'passive': {'ξαναρχόμουν'}},
             'pres_conjugation': 'con1_pass',
             'present': {'passive': {'ξανάρχομαι'}}}

        )

    def test_verb_synepairnw(self):
        self.assertDictEqual(
            basic_verb('συνεπαίρνω'),
            {'act_pres_participle': {'συνεπαίρνοντας'},
             'aorist': {'active': {'συνεπήρα'}, 'passive': {'συνεπάρθηκα'}},
             'conjunctive': {'active': {'συνεπάρω'}, 'passive': {'συνεπαρθώ'}},
             'modal': False,
             'paratatikos': {'active': {'συνέπαιρνα'}, 'passive': {'συνεπαιρνόμουν'}},
             'passive_perfect_participle': {'συνεπαρμένος/συνεπαρμένη/συνεπαρμένο'},
             'pres_conjugation': 'con1_act',
             'present': {'active': {'συνεπαίρνω'}, 'passive': {'συνεπαίρνομαι'}}}

        )

    def test_verb_arxw(self):
        self.assertDictEqual(
            basic_verb('άρχω'),
            {'act_pres_participle': {'άρχοντας'},
             'aorist': {'active': {'ήρξα'}},
             'arch_act_pres_participle': {'άρχων/άρχουσα/άρχον'},
             'conjunctive': {'active': {'άρξω'}},
             'modal': False,
             'paratatikos': {'active': {'ήρχα'}, 'passive': {'αρχόμουν'}},
             'pass_pres_participle': {'αρχόμενος/αρχόμενη/αρχόμενο'},
             'pres_conjugation': 'con1_act',
             'present': {'active': {'άρχω'}, 'passive': {'άρχομαι'}}}

        )

    def test_verb_anamenw(self):
        self.assertDictEqual(
            basic_verb('αναμένω'),
            {'act_pres_participle': {'αναμένοντας'},
             'active_aorist_participle': {'αναμείνας/αναμείνασα/αναμείναν'},
             'aorist': {'active': {'ανέμεινα'}},
             'arch_act_pres_participle': {'αναμένων/αναμένουσα/αναμένον'},
             'conjunctive': {'active': {'αναμείνω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'ανάμενα', 'ανέμενα'}, 'passive': {'αναμενόμουν'}},
             'pass_pres_participle': {'αναμενόμενος/αναμενόμενη/αναμενόμενο'},
             'present': {'active': {'αναμένω'}, 'passive': {'αναμένομαι'}}},

        )

    def test_verb_forw(self):
        self.assertDictEqual(
            basic_verb('μαυροφορώ'),
            {'act_pres_participle': {'μαυροφορώντας'},
             'aorist': {'active': {'μαυροφόρεσα'}, 'passive': {'μαυροφορέθηκα'}},
             'conjunctive': {'active': {'μαυροφορέσω'}, 'passive': {'μαυροφορεθώ'}},
             'modal': False,
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'μαυροφορούσα'}, 'passive': {'μαυροφοριόμουν'}},
             'passive_perfect_participle': {'μαυροφορεμένος/μαυροφορεμένη/μαυροφορεμένο'},
             'present': {'active': {'μαυροφορώ'}, 'passive': {'μαυροφοριέμαι'}}}

        )

    def test_verb_ξεροκαταπίνω(self):
        self.assertDictEqual(
            basic_verb('ξεπροβαίνω'),
            {'act_pres_participle': {'ξεπροβαίνοντας'},
             'aorist': {'active': {'ξεπροέβηκα'}},
             'arch_act_pres_participle': {'ξεπροβαίνων/ξεπροβαίνουσα/ξεπροβαίνον'},
             'conjunctive': {'active': {'ξεπροβώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'ξεπρόβαινα'}},
             'present': {'active': {'ξεπροβαίνω'}}}
        )

    def test_verb_orw(self):
        self.assertDictEqual(
            basic_verb('ορώ'),
            {'act_pres_participle': {'ορώντας'},
             'aorist': {'active': {'είδα'}},
             'conjunctive': {'active': {'ιδώ'}},
             'modal': False,
             'pres_conjugation': 'con2ak_act',

             'paratatikos': {},
             'present': {'active': {'ορώ'}}}

        )

    def test_verb_elkw(self):
        self.assertDictEqual(
            basic_verb('έλκω'),
            {'act_pres_participle': {'έλκοντας'},
             'aorist': {'active': {'έλξα'}, 'passive': {'ελκύσθηκα', 'ελκύστηκα'}},
             'conjunctive': {'active': {'έλξω'}, 'passive': {'ελκυσθώ', 'ελκυστώ'}},
             'modal': False,
             'arch_act_pres_participle': {'έλκων/έλκουσα/έλκον'},
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'είλκα'}, 'passive': {'ελκόμουν'}},
             'pass_pres_participle': {'ελκόμενος/ελκόμενη/ελκόμενο'},
             'present': {'active': {'έλκω'}, 'passive': {'έλκομαι'}}},
            # print_verbs(verbs)
        )

    def test_verb_sbarnw(self):
        self.assertDictEqual(
            basic_verb('σβαρνώ'),
            {'act_pres_participle': {'σβαρνώντας'},
             'aorist': {'active': {'σβάρνισα'}},
             'conjunctive': {'active': {'σβαρνίσω'}},
             'modal': False,
             'pres_conjugation': 'con2b_act',
             'paratatikos': {'active': {'σβαρνούσα'}},
             'passive_perfect_participle': {'σβαρνισμένος/σβαρνισμένη/σβαρνισμένο'},
             'present': {'active': {'σβαρνώ'}}}

        )

    def test_verb_sbarnizw(self):
        self.assertDictEqual(
            basic_verb('σβαρνίζω'),
            {'act_pres_participle': {'σβαρνίζοντας'},
             'aorist': {'active': {'σβάρνισα'}, 'passive': {'σβαρνίσθηκα', 'σβαρνίστηκα'}},
             'conjunctive': {'active': {'σβαρνίσω'}, 'passive': {'σβαρνισθώ', 'σβαρνιστώ'}},
             'modal': False,
             'paratatikos': {'active': {'σβάρνιζα'}, 'passive': {'σβαρνιζόμουν'}},
             'passive_aorist_participle': {'σβαρνισθείς/σβαρνισθείσα/σβαρνισθέν'},
             'passive_perfect_participle': {'σβαρνισμένος/σβαρνισμένη/σβαρνισμένο'},
             'pres_conjugation': 'con1_act',
             'present': {'active': {'σβαρνίζω'}, 'passive': {'σβαρνίζομαι'}}}

        )

    def test_verb_ennoeitai(self):
        self.assertDictEqual(
            basic_verb('εννοείται'),
            {'aorist': {'passive': {'εννοήθηκε'}},
             'conjunctive': {'passive': {'εννοηθεί'}},
             'modal': True,
             'pres_conjugation': 'con2_pass_modal',

             'paratatikos': {'passive': {'εννοούνταν', 'εννοείτο'}},
             'present': {'passive': {'εννοείται'}}}

        )

    def test_verb_strimognomai(self):
        self.assertDictEqual(
            basic_verb('στριμώχνομαι'),
            {'present': {'passive': {'στριμώχνομαι'}}, 'conjunctive': {'passive': {'στριμωχθώ'}},
             'aorist': {'passive': {'στριμώχθηκα'}},
             'pres_conjugation': 'con1_pass',
             'paratatikos': {'passive': {'στριμωχνόμουν'}},
             'passive_perfect_participle': {'στριμωγμένος/στριμωγμένη/στριμωγμένο'},
             'modal': False}

        )

    def test_verb_anathetw(self):
        self.assertDictEqual(
            basic_verb('αναθέτω'),
            {'act_pres_participle': {'αναθέτοντας'},
             'active_aorist_participle': {'αναθέσας/αναθέσασα/αναθέσαν'},
             'aorist': {'active': {'ανάθεσα', 'ανέθεσα'},
                        'passive': {'ανατέθηκα', 'ανετέθη'}},
             'arch_act_pres_participle': {'αναθέτων/αναθέτουσα/αναθέτον'},
             'conjunctive': {'active': {'αναθέσω'}, 'passive': {'ανατεθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'ανάθετα', 'ανέθετα'},
                             'passive': {'ανατιθέμην', 'αναθετόμουν'}},
             'passive_aorist_participle': {'ανατεθείς/ανατεθείσα/ανατεθέν'},
             'passive_perfect_participle': {'αναθεμένος/αναθεμένη/αναθεμένο',
                                            'ανατεθειμένος/ανατεθειμένη/ανατεθειμένο'},
             'present': {'active': {'αναθέτω'}, 'passive': {'ανατίθεμαι', 'αναθέτομαι'}}},
            # printVerbs(verbs)

        )

    def test_verb_fysaw(self):
        self.assertDictEqual(
            basic_verb('φυσάω'),
            {'present': {'active': {'φυσάω'}, 'passive': {'φυσιέμαι'}},
             'conjunctive': {'active': {'φυσήσω', 'φυσήξω'}, 'passive': {'φυσηθώ', 'φυσηχτώ'}},
             'aorist': {'active': {'φύσησα', 'φύσηξα'}, 'passive': {'φυσήθηκα', 'φυσήχτηκα'}},
             'paratatikos': {'active': {'φυσούσα', 'φύσαγα'}, 'passive': {'φυσιόμουν'}},
             'act_pres_participle': {'φυσώντας'},
             'pres_conjugation': 'con2a_act',

             'passive_perfect_participle': {'φυσημένος/φυσημένη/φυσημένο'}, 'modal': False},

        )

    def test_verb_swpainw(self):
        self.assertDictEqual(
            basic_verb('σωπαίνω'),
            {'act_pres_participle': {'σωπαίνοντας'},
             'aorist': {'active': {'σώπασα'}},
             'conjunctive': {'active': {'σωπάσω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'σώπαινα'}},
             'passive_perfect_participle': {'σωπασμένος/σωπασμένη/σωπασμένο'},
             'present': {'active': {'σωπαίνω'}}}

        )

    def test_verb_eksanistamai(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('εξανίσταμαι'),
            {'aorist': {'passive': {'εξαναστάθηκα', 'εξανέστη'}},
             'conjunctive': {'passive': {'εξανασταθώ', 'εξαναστώ'}},
             'modal': False,
             'pres_conjugation': 'con2e_pass',

             'paratatikos': {'passive': {'εξανιστάμην'}},
             'passive_perfect_participle': {'εξαναστημένος/εξαναστημένη/εξαναστημένο'},
             'present': {'passive': {'εξανίσταμαι'}}}

        )

    def test_verb_skarifw(self):
        self.assertDictEqual(
            basic_verb('σκαριφώ'),
            {'act_pres_participle': {'σκαριφώντας'},
             'aorist': {'active': {'σκαρίφισα'}},
             'conjunctive': {'active': {'σκαριφίσω'}},
             'modal': False,
             'pres_conjugation': 'con2ak_act',

             'paratatikos': {'active': {'σκαριφούσα'}},
             'present': {'active': {'σκαριφώ'}}}

        )

    def test_verb_istamai(self):
        self.assertDictEqual(
            basic_verb('ίσταμαι'),
            {'aorist': {'passive': {'έστη', 'στάθηκα'}},
             'conjunctive': {'passive': {'σταθώ', 'στώ'}},
             'modal': False,
             'pres_conjugation': 'con2e_pass',
             'paratatikos': {'passive': {'ιστάμην'}},
             'pass_pres_participle': {'ιστάμενος/ιστάμενη/ιστάμενο'},
             'passive_aorist_participle': {'στάς/στάσα/στάν'},
             'present': {'passive': {'ίσταμαι'}}}

        )

    def test_bastaw(self):
        self.assertDictEqual(
            basic_verb('βαστάω'),
            {'act_pres_participle': {'βαστώντας'},
             'aorist': {'active': {'βάσταξα', 'βάστηξα'},
                        'passive': {'βαστάχτηκα', 'βαστήχτηκα'}},
             'conjunctive': {'active': {'βαστάξω', 'βαστήξω'},
                             'passive': {'βασταχτώ', 'βαστηχτώ'}},
             'modal': False,
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'βαστούσα', 'βάσταγα'}, 'passive': {'βαστιόμουν'}},
             'passive_perfect_participle': {'βαστηγμένος/βαστηγμένη/βαστηγμένο',
                                            'βασταγμένος/βασταγμένη/βασταγμένο'},
             'present': {'active': {'βαστάω'}, 'passive': {'βαστιέμαι'}}},
        )

    def test_verb_thewmai(self):
        self.assertDictEqual(
            basic_verb('θεώμαι'),
            {'aorist': {'passive': {'θεάθηκα', 'εθεάθη'}},
             'conjunctive': {'passive': {'θεαθώ'}},
             'pres_conjugation': 'con2ak_pass',
             'modal': False,
             'paratatikos': {'passive': {'θεόμουν'}},
             'pass_pres_participle': {'θεώμενος/θεώμενη/θεώμενο'},
             'present': {'passive': {'θεώμαι'}}}

        )

    def test_verb_diegeirw(self):
        self.assertDictEqual(
            basic_verb('διεγείρω'),
            {'act_pres_participle': {'διεγείροντας'},
             'aorist': {'active': {'διήγειρα', 'διέγειρα'}, 'passive': {'διεγέρθηκα'}},
             'arch_act_pres_participle': {'διεγείρων/διεγείρουσα/διεγείρον'},
             'conjunctive': {'active': {'διεγείρω'}, 'passive': {'διεγερθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'διήγειρα', 'διέγειρα'},
                             'passive': {'διεγειρόμουν'}},
             'pass_pres_participle': {'διεγειρόμενος/διεγειρόμενη/διεγειρόμενο'},
             'passive_aorist_participle': {'διεγερθείς/διεγερθείσα/διεγερθέν'},
             'passive_perfect_participle': {'διεγερμένος/διεγερμένη/διεγερμένο'},
             'present': {'active': {'διεγείρω'}, 'passive': {'διεγείρομαι'}}}

        )

    def test_verb_kauxomai(self):
        self.assertDictEqual(
            basic_verb('καυχώμαι'),
            {'aorist': {'passive': {'καυχήθηκα'}},
             'conjunctive': {'passive': {'καυχηθώ'}},
             'modal': False,
             'pres_conjugation': 'con2ak_pass',
             'paratatikos': {'passive': {'καυχιόμουν'}},
             'passive_perfect_participle': {'καυχημένος/καυχημένη/καυχημένο'},
             'present': {'passive': {'καυχώμαι', 'καυχιέμαι'}}}

        )

    def test_verb_aposurnw(self):
        self.assertDictEqual(
            basic_verb('αποσύρω'),
            {'act_pres_participle': {'αποσύροντας'},
             'aorist': {'active': {'απέσυρα'}, 'passive': {'αποσύρθηκα'}},
             'conjunctive': {'active': {'αποσύρω'}, 'passive': {'αποσυρθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'απέσυρα'}, 'passive': {'αποσυρόμουν'}},
             'pass_pres_participle': {'αποσυρόμενος/αποσυρόμενη/αποσυρόμενο'},
             'passive_aorist_participle': {'αποσυρθείς/αποσυρθείσα/αποσυρθέν'},
             'passive_perfect_participle': {'αποσυρμένος/αποσυρμένη/αποσυρμένο'},
             'present': {'active': {'αποσύρω'}, 'passive': {'αποσύρομαι'}}}

        )

    def test_verb_wolodernw(self):
        self.assertDictEqual(
            basic_verb('βωλοδέρνω'),
            {'act_pres_participle': {'βωλοδέρνοντας'},
             'aorist': {},
             'conjunctive': {},
             'pres_conjugation': 'con1_act',

             'modal': False,
             'paratatikos': {'active': {'βωλόδερνα'}},
             'present': {'active': {'βωλοδέρνω'}}})

    def test_verb_ksanalegw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('ξαναλέω'),
            {'act_pres_participle': {'ξαναλέγοντας'},
             'pres_conjugation': 'con2c_act',
             'aorist': {'active': {'ξαναείπα'},
                        'passive': {'ξαναειπώθηκα', 'ξαναελέχθη', 'ξαναλέχθηκα'}},
             'conjunctive': {'active': {'ξαναπώ'}, 'passive': {'ξαναειπωθώ', 'ξαναλεχθώ'}},
             'arch_act_pres_participle': {'ξαναλέγων/ξαναλέγουσα/ξαναλέγον'},
             'modal': False,
             'paratatikos': {'active': {'ξαναέλεγα', 'ξανάλεγα'},
                             'passive': {'ξαναλεγόμουν'}},
             'pass_pres_participle': {'ξαναλεγόμενος/ξαναλεγόμενη/ξαναλεγόμενο'},
             'passive_aorist_participle': {'ξαναλεχθείς/ξαναλεχθείσα/ξαναλεχθέν'},
             'passive_perfect_participle': {'ξαναειπωμένος/ξαναειπωμένη/ξαναειπωμένο'},
             'present': {'active': {'ξαναλέω'}, 'passive': {'ξαναλέγομαι'}}},

        )

    def test_verb_diabazw(self):
        self.assertDictEqual(
            basic_verb('διαβάζω'),
            {'act_pres_participle': {'διαβάζοντας'},
             'aorist': {'active': {'διάβασα'}, 'passive': {'διαβάστηκα', 'διαβάσθηκα'}},
             'conjunctive': {'active': {'διαβάσω'}, 'passive': {'διαβαστώ', 'διαβασθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'διάβαζα'}, 'passive': {'διαβαζόμουν'}},
             'passive_perfect_participle': {'διαβασμένος/διαβασμένη/διαβασμένο'},
             'present': {'active': {'διαβάζω'}, 'passive': {'διαβάζομαι'}}}

        )

    def test_verb_ekpempomai(self):
        self.assertDictEqual(
            basic_verb('εκπέμπομαι'),
            {'aorist': {'passive': {'εκπέμφθηκα'}},
             'conjunctive': {'passive': {'εκπεμφθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'εκπεμπόμουν'}},
             'pass_pres_participle': {'εκπεμπόμενος/εκπεμπόμενη/εκπεμπόμενο'},
             'present': {'passive': {'εκπέμπομαι'}}}

        )

    def test_verb_apokathairw(self):
        self.assertDictEqual(
            basic_verb('αποκαθαίρω'),
            {'act_pres_participle': {'αποκαθαίροντας'},
             'aorist': {'active': {'αποκάθαρα'}},
             'conjunctive': {'active': {'αποκαθάρω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'αποκάθαιρα'}, 'passive': {'αποκαθαιρόμουν'}},
             'present': {'active': {'αποκαθαίρω'}, 'passive': {'αποκαθαίρομαι'}}}

        )

    def test_verb_aposperno(self):
        self.assertDictEqual(
            basic_verb('αποσπέρνω'),
            {'act_pres_participle': {'αποσπέρνοντας'},
             'aorist': {'active': {'απέσπειρα'}, 'passive': {'αποσπάρθηκα', 'αποσπάρηκα'}},
             'conjunctive': {'active': {'αποσπείρω'}, 'passive': {'αποσπαρθώ', 'αποσπαρώ'}},
             'modal': False,
             'arch_act_pres_participle': {'αποσπέρνων/αποσπέρνουσα/αποσπέρνον'},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'απόσπερνα'}, 'passive': {'αποσπερνόμουν'}},
             'pass_pres_participle': {'αποσπερνόμενος/αποσπερνόμενη/αποσπερνόμενο'},
             'passive_aorist_participle': {'αποσπαρείς/αποσπαρείσα/αποσπαρέν',
                                           'αποσπαρθείς/αποσπαρθείσα/αποσπαρθέν'},
             'passive_perfect_participle': {'αποσπαρμένος/αποσπαρμένη/αποσπαρμένο',
                                            'απεσπαρμένος/απεσπαρμένη/απεσπαρμένο'},
             'present': {'active': {'αποσπέρνω'}, 'passive': {'αποσπέρνομαι'}}},
            # ic(basic_verb('αποσπέρνω'))

        )

    def test_verb_ferno(self):
        self.assertDictEqual(
            basic_verb('φέρνω'),
            {'act_pres_participle': {'φέρνοντας'},
             'aorist': {'active': {'έφερα'}, 'passive': {'φέρθηκα'}},
             'conjunctive': {'active': {'φέρω'}, 'passive': {'φερθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'έφερνα'}, 'passive': {'φερνόμουν'}},
             'passive_perfect_participle': {'φερμένος/φερμένη/φερμένο'},
             'present': {'active': {'φέρνω'}, 'passive': {'φέρνομαι'}}}

        )

    def test_verb_diepo(self):
        self.assertDictEqual(
            basic_verb('διέπω'),
            {'act_pres_participle': {'διέποντας'},
             'aorist': {},
             'pres_conjugation': 'con1_act',

             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'διείπα'}, 'passive': {'διεπόμουν'}},
             'present': {'active': {'διέπω'}, 'passive': {'διέπομαι'}}}

        )

    def test_verb_anaggellw(self):
        self.assertDictEqual(
            basic_verb('αναγγέλλω'),
            {'act_pres_participle': {'αναγγέλλοντας'},
             'active_aorist_participle': {'αναγγείλας/αναγγείλασα/αναγγείλαν'},
             'aorist': {'active': {'ανήγγειλα', 'ανάγγειλα'},
                        'passive': {'ανηγγέλθη', 'αναγγέλθηκα'}},
             'arch_act_pres_participle': {'αναγγέλλων/αναγγέλλουσα/αναγγέλλον'},
             'conjunctive': {'active': {'αναγγείλω'}, 'passive': {'αναγγελθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'ανήγγελλα', 'ανάγγελλα'},
                             'passive': {'αναγγελλόμουν'}},
             'pass_pres_participle': {'αναγγελλόμενος/αναγγελλόμενη/αναγγελλόμενο'},
             'passive_aorist_participle': {'αναγγελθείς/αναγγελθείσα/αναγγελθέν'},
             'passive_perfect_participle': {'αναγγελμένος/αναγγελμένη/αναγγελμένο'},
             'present': {'active': {'αναγγέλλω'}, 'passive': {'αναγγέλλομαι'}}}

        )

    def test_verb_prwtoblepw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('πρωτοβλέπω'),
            {'act_pres_participle': {'πρωτοβλέποντας'},
             'pres_conjugation': 'con1_act',
             'aorist': {'active': {'πρωτοείδα'},
                        'passive': {'πρωτοϊδώθηκα', 'πρωτοειδώθηκα'}},
             'arch_act_pres_participle': {'πρωτοβλέπων/πρωτοβλέπουσα/πρωτοβλέπον'},
             'conjunctive': {'active': {'πρωτοδώ'}, 'passive': {'πρωτοϊδωθώ'}},
             'modal': False,
             'paratatikos': {'active': {'πρωτόβλεπα', 'πρωτοέβλεπα'},
                             'passive': {'πρωτοβλεπόμουν'}},
             'passive_perfect_participle': {'πρωτοϊδωμένος/πρωτοϊδωμένη/πρωτοϊδωμένο'},
             'present': {'active': {'πρωτοβλέπω'}, 'passive': {'πρωτοβλέπομαι'}}}

        )

    def test_verb_protrepw(self):
        self.assertDictEqual(
            basic_verb('προτρέπω'),
            {'act_pres_participle': {'προτρέποντας'},
             'aorist': {'active': {'προέτρεψα'}, 'passive': {'προτράπηκα', 'προετράπη'}},
             'conjunctive': {'active': {'προτρέψω'}, 'passive': {'προτραπώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'passive_perfect_participle': {'προτετραμμένος/προτετραμμένη/προτετραμμένο'},
             'paratatikos': {'active': {'προέτρεπα'}, 'passive': {'προτρεπόμουν'}},
             'present': {'active': {'προτρέπω'}, 'passive': {'προτρέπομαι'}}}
        )

    def test_verb_periblepw(self):
        self.assertDictEqual(
            basic_verb('περιβλέπω'),
            {'act_pres_participle': {'περιβλέποντας'},
             'aorist': {'active': {'περιέβλεψα'}},
             'arch_act_pres_participle': {'περιβλέπων/περιβλέπουσα/περιβλέπον'},
             'conjunctive': {'active': {'περιβλέψω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'περιέβλεπα'}},
             'present': {'active': {'περιβλέπω'}}}

        )

    def test_verb_parablepw_dimotiko(self):
        self.assertDictEqual(
            basic_verb('παραβλέπω'),
            {'act_pres_participle': {'παραβλέποντας'},
             'aorist': {'active': {'παρέβλεψα', 'παράβλεψα'}, 'passive': {'παραβλέφθηκα'}},
             'conjunctive': {'active': {'παραβλέψω'}, 'passive': {'παραβλεφθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'παρέβλεπα', 'παράβλεπα'},
                             'passive': {'παραβλεπόμουν'}},
             'present': {'active': {'παραβλέπω'}, 'passive': {'παραβλέπομαι'}}}

        )

    def test_verb_parablepw_logio(self):
        self.maxDiff = False
        self.assertDictEqual(
            Verb('παραβλέπω', para=True).basic_forms,
            {'act_pres_participle': {'παραβλέποντας'},
             'aorist': {'active': {'παραείδα'}, 'passive': {'παραειδώθηκα', 'παραϊδώθηκα'}},
             'arch_act_pres_participle': {'παραβλέπων/παραβλέπουσα/παραβλέπον'},
             'conjunctive': {'active': {'παραδώ'}, 'passive': {'παραϊδωθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'παραέβλεπα', 'παράβλεπα'}, 'passive': {'παραβλεπόμουν'}},
             'passive_perfect_participle': {'παραϊδωμένος/παραϊδωμένη/παραϊδωμένο'},
             'present': {'active': {'παραβλέπω'}, 'passive': {'παραβλέπομαι'}}},

        )

    def test_verb_parexw(self):
        self.assertDictEqual(
            basic_verb('παρέχω'),
            {'act_pres_participle': {'παρέχοντας'},
             'aorist': {'active': {'παρέσχον', 'παρείχα'}},
             'arch_act_pres_participle': {'παρέχων/παρέχουσα/παρέχον'},
             'conjunctive': {'active': {'παρέχω', 'παράσχω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'παρείχα'}, 'passive': {'παρεχόμουν'}},
             'pass_pres_participle': {'παρεχόμενος/παρεχόμενη/παρεχόμενο'},
             'present': {'active': {'παρέχω'}, 'passive': {'παρέχομαι'}}}

        )

    def test_verb_apokaiw(self):
        self.assertDictEqual(
            basic_verb('αποκαίω'),
            {'act_pres_participle': {'αποκαίγοντας'},
             'aorist': {'active': {'απέκαψα'}, 'passive': {'αποκάηκα'}},
             'conjunctive': {'active': {'αποκάψω'}, 'passive': {'αποκαώ'}},
             'modal': False,
             'pres_conjugation': 'con2c_act',

             'paratatikos': {'active': {'απέκαιγα'}, 'passive': {'αποκαιγόμουν'}},
             'pass_pres_participle': {'αποκαιγόμενος/αποκαιγόμενη/αποκαιγόμενο'},
             'passive_perfect_participle': {'αποκεκαυμένος/αποκεκαυμένη/αποκεκαυμένο',
                                            'αποκεκαμμένος/αποκεκαμμένη/αποκεκαμμένο',
                                            'αποκαμένος/αποκαμένη/αποκαμένο'},
             'present': {'active': {'αποκαίω'}, 'passive': {'αποκαίγομαι'}}}

        )

    def test_verb_katalabainw(self):
        self.assertDictEqual(
            basic_verb('καταλαβαίνω'),
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
            basic_verb('συνυπάρχω'),
            {'act_pres_participle': {'συνυπάρχοντας'},
             'aorist': {'active': {'συνύπαρξα'}},
             'arch_act_pres_participle': {'συνυπάρχων/συνυπάρχουσα/συνυπάρχον'},
             'conjunctive': {'active': {'συνυπάρξω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'συνυπήρχα'}},
             'present': {'active': {'συνυπάρχω'}}}

        )

    def test_verb_synchairw(self):
        self.assertDictEqual(
            basic_verb('συγχαίρω'),
            {'act_pres_participle': {'συγχαίροντας'},
             'aorist': {'passive': {'συνεχάρη', 'συγχάρηκα'}},
             'arch_act_pres_participle': {'συγχαίρων/συγχαίρουσα/συγχαίρον'},
             'conjunctive': {'passive': {'συγχαρώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'συνέχαιρα'}, 'passive': {'συγχαιρόμουν'}},
             'pass_pres_participle': {'συγχαιρόμενος/συγχαιρόμενη/συγχαιρόμενο'},
             'present': {'active': {'συγχαίρω'}, 'passive': {'συγχαίρομαι'}}}

        )

    def test_verb_serbirw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('σερβίρω'),
            {'act_pres_participle': {'σερβίροντας'},
             'aorist': {'active': {'σερβίρισα', 'σέρβιρα'}, 'passive': {'σερβιρίστηκα'}},
             'conjunctive': {'active': {'σερβιρίσω', 'σερβίρω'}, 'passive': {'σερβιριστώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'σέρβιρα', 'σερβίριζα'},
                             'passive': {'σερβιρόμουν', 'σερβιριζόμουν'}},
             'passive_perfect_participle': {'σερβιρισμένος/σερβιρισμένη/σερβιρισμένο'},
             'present': {'active': {'σερβίρω'}, 'passive': {'σερβίρομαι'}}}

        )

    def test_verb_eksairw(self):
        self.assertDictEqual(
            basic_verb('εξαίρω'),
            {'act_pres_participle': {'εξαίροντας'},
             'aorist': {'active': {'εξήρα'}, 'passive': {'εξήρθη', 'εξάρθηκα'}},
             'conjunctive': {'active': {'εξάρω'}, 'passive': {'εξαρθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'εξήρα'}, 'passive': {'εξαιρόμουν'}},
             'present': {'active': {'εξαίρω'}, 'passive': {'εξαίρομαι'}}}

        )

    def test_verb_prosmeignuw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('προσμειγνύω'),
            {'act_pres_participle': {'προσμειγνύοντας'},
             'active_aorist_participle': {'προσμείξας/προσμείξασα/προσμείξαν'},
             'aorist': {'active': {'προσέμειξα'}, 'passive': {'προσμείχθηκα'}},
             'conjunctive': {'active': {'προσμείξω'}, 'passive': {'προσμειχθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'προσμείγνυα'}, 'passive': {'προσμειγνυόμουν'}},
             'pass_pres_participle': {'προσμειγνυόμενος/προσμειγνυόμενη/προσμειγνυόμενο'},
             'passive_aorist_participle': {'προσμειχθείς/προσμειχθείσα/προσμειχθέν'},
             'passive_perfect_participle': {'προσμειγμένος/προσμειγμένη/προσμειγμένο',
                                            'προσμεμειγμένος/προσμεμειγμένη/προσμεμειγμένο'},

             'present': {'active': {'προσμειγνύω'}, 'passive': {'προσμειγνύομαι'}}}

        )

    def test_verb_epanakrinw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('επανακρίνω'),
            {'act_pres_participle': {'επανακρίνοντας'},
             'aorist': {'active': {'επανέκρινα'},
                        'passive': {'επανεκρίθη', 'επανακρίθηκα'}},
             'arch_act_pres_participle': {'επανακρίνων/επανακρίνουσα/επανακρίνον'},
             'conjunctive': {'active': {'επανακρίνω'}, 'passive': {'επανακριθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'επανέκρινα'}, 'passive': {'επανακρινόμουν'}},
             'pass_pres_participle': {'επανακρινόμενος/επανακρινόμενη/επανακρινόμενο'},
             'passive_aorist_participle': {'επανακριθείς/επανακριθείσα/επανακριθέν'},
             'passive_perfect_participle': {'επανακριμένος/επανακριμένη/επανακριμένο',
                                            'επανακεκριμένος/επανακεκριμένη/επανακεκριμένο'},

             'present': {'active': {'επανακρίνω'}, 'passive': {'επανακρίνομαι'}}}

        )

    def test_verb_synizanw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('συνιζάνω'),
            {'act_pres_participle': {'συνιζάνοντας'},
             'aorist': {'active': {'συνίζανα'}, 'passive': {'συνιζήθηκα'}},
             'conjunctive': {'active': {'συνιζάνω'}, 'passive': {'συνιζηθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'συνίζανα'}, 'passive': {'συνιζανόμουν'}},
             'passive_perfect_participle': {'συνιζημένος/συνιζημένη/συνιζημένο'},
             'present': {'active': {'συνιζάνω'}, 'passive': {'συνιζάνομαι'}}}

        )

    def test_dankanw(self):
        self.assertDictEqual(
            basic_verb('δαγκάνω'),
            {'act_pres_participle': {'δαγκάνοντας'},
             'aorist': {'active': {'δάγκασα'}, 'passive': {'δαγκάθηκα'}},
             'conjunctive': {'active': {'δαγκάσω'}, 'passive': {'δαγκαθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'δάγκανα'}, 'passive': {'δαγκανόμουν'}},
             'passive_perfect_participle': {'δαγκαμένος/δαγκαμένη/δαγκαμένο'},
             'present': {'active': {'δαγκάνω'}, 'passive': {'δαγκάνομαι'}}}

        )

    def test_anufainw(self):
        self.assertDictEqual(
            basic_verb('ανυφαίνω'),
            {'act_pres_participle': {'ανυφαίνοντας'},
             'aorist': {'active': {'ανύφανα'}, 'passive': {'ανυφάνθηκα'}},
             'conjunctive': {'active': {'ανυφάνω'}, 'passive': {'ανυφανθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'ανύφαινα'}, 'passive': {'ανυφαινόμουν'}},
             'passive_perfect_participle': {'ανυφασμένος/ανυφασμένη/ανυφασμένο'},
             'present': {'active': {'ανυφαίνω'}, 'passive': {'ανυφαίνομαι'}}}

        )

    def test_verb_elaunw(self):
        self.assertDictEqual(
            basic_verb('ελαύνω'),
            {'act_pres_participle': {'ελαύνοντας'},
             'aorist': {'active': {'έλασα'}},
             'pres_conjugation': 'con1_act',

             'arch_act_pres_participle': {'ελαύνων/ελαύνουσα/ελαύνον'},
             'conjunctive': {'active': {'ελάσω'}},
             'modal': False,
             'paratatikos': {'active': {'ήλαυνα', 'έλαυνα'}},
             'present': {'active': {'ελαύνω'}}}

        )

    def test_verb_protopianw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('πρωτοπιάνω'),
            {'act_pres_participle': {'πρωτοπιάνοντας'},
             'aorist': {'active': {'πρωτοέπιασα'}, 'passive': {'πρωτοπιάστηκα'}},
             'conjunctive': {'active': {'πρωτοπιάσω'}, 'passive': {'πρωτοπιαστώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'pass_pres_participle': {'πρωτοπιανούμενος/πρωτοπιανούμενη/πρωτοπιανούμενο'},
             'paratatikos': {'active': {'πρωτοέπιανα'}, 'passive': {'πρωτοπιανόμουν'}},
             'passive_perfect_participle': {'πρωτοπιασμένος/πρωτοπιασμένη/πρωτοπιασμένο'},
             'present': {'active': {'πρωτοπιάνω'}, 'passive': {'πρωτοπιάνομαι'}}}

        )

    def test_verb_buzanw(self):
        self.assertDictEqual(
            basic_verb('βυζάνω'),
            {'act_pres_participle': {'βυζάνοντας'},
             'aorist': {'active': {'βύζαξα'}},
             'conjunctive': {'active': {'βυζάξω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'βύζανα'}},
             'passive_perfect_participle': {'βυζαγμένος/βυζαγμένη/βυζαγμένο'},
             'present': {'active': {'βυζάνω'}}}

        )

    def test_verb_eksolisthanw(self):
        self.assertDictEqual(
            basic_verb('εξολισθάνω'),
            {'act_pres_participle': {'εξολισθάνοντας'},
             'aorist': {'active': {'εξολίσθησα'}},
             'conjunctive': {'active': {'εξολισθήσω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'εξολίσθανα'}},
             'present': {'active': {'εξολισθάνω'}}}

        )

    def test_paratw(self):
        self.assertDictEqual(
            basic_verb('παρατώ'),
            {'act_pres_participle': {'παρατώντας'},
             'aorist': {'active': {'παράτησα'}, 'passive': {'παρατήθηκα'}},
             'conjunctive': {'active': {'παρατήσω'}, 'passive': {'παρατηθώ'}},
             'modal': False,
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'παρατούσα', 'παράταγα'},
                             'passive': {'παρατιόμουν'}},
             'passive_perfect_participle': {'παρατημένος/παρατημένη/παρατημένο'},
             'present': {'active': {'παρατώ'}, 'passive': {'παρατιέμαι'}}}
        )

    def test_verb_parabainw(self):
        self.assertDictEqual(
            basic_verb('παραβαίνω'),
            {'act_pres_participle': {'παραβαίνοντας'},
             'aorist': {'active': {'παραβήκα', 'παρέβη'}},
             'active_aorist_participle': {'παραβάς/παραβάσα/παραβάν'},
             'arch_act_pres_participle': {'παραβαίνων/παραβαίνουσα/παραβαίνον'},
             'conjunctive': {'active': {'παραβώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'παράβαινα'}, 'passive': {'παραβαινόμουν'}},
             'present': {'active': {'παραβαίνω'}, 'passive': {'παραβαίνομαι'}}}

        )

    def test_verb_uperbainw(self):
        self.assertDictEqual(
            basic_verb('υπερβαίνω'),
            {'act_pres_participle': {'υπερβαίνοντας'},
             'aorist': {'active': {'υπερέβη'}},
             'pres_conjugation': 'con1_act',

             'active_aorist_participle': {'υπερβάς/υπερβάσα/υπερβάν'},
             'arch_act_pres_participle': {'υπερβαίνων/υπερβαίνουσα/υπερβαίνον'},
             'conjunctive': {'active': {'υπερβώ'}},
             'modal': False,
             'paratatikos': {'active': {'υπερέβαινα', 'υπέρβαινα'}, 'passive': {'υπερβαινόμουν'}},
             'present': {'active': {'υπερβαίνω'}, 'passive': {'υπερβαίνομαι'}}},

        )

    def test_verb_katalabainw(self):
        self.assertDictEqual(
            basic_verb('καταλαβαίνω'),
            {'act_pres_participle': {'καταλαβαίνοντας'},
             'aorist': {'active': {'κατάλαβα'}},
             'conjunctive': {'active': {'καταλάβω'}},
             'modal': False,
             'paratatikos': {'active': {'καταλάβαινα'}, 'passive': {'καταλαβαινόμουν'}},
             'present': {'active': {'καταλαβαίνω'}, 'passive': {'καταλαβαίνομαι'}}}

        )

    def test_embainw(self):
        self.assertDictEqual(
            basic_verb('εμβαίνω'),
            {'act_pres_participle': {'εμβαίνοντας'},
             'active_aorist_participle': {'εμβάς/εμβάσα/εμβάν'},
             'aorist': {'active': {'εμβήκα', 'ενέβη'}},
             'arch_act_pres_participle': {'εμβαίνων/εμβαίνουσα/εμβαίνον'},
             'conjunctive': {'active': {'εμβώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'ενέβαινα'}, 'passive': {'εμβαινόμουν'}},
             'present': {'active': {'εμβαίνω'}, 'passive': {'εμβαίνομαι'}}}

        )

    def test_nostimainw(self):
        self.assertDictEqual(
            basic_verb('νοστιμαίνω'),
            {'act_pres_participle': {'νοστιμαίνοντας'},
             'aorist': {},
             'conjunctive': {},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'νοστίμαινα'}},
             'present': {'active': {'νοστιμαίνω'}}}

        )

    def test_verb_prosexw(self):
        self.assertDictEqual(
            basic_verb('προσέχω'),
            {'act_pres_participle': {'προσέχοντας'},
             'aorist': {'active': {'πρόσεξα'}, 'passive': {'προσέχθηκα', 'προσέχτηκα'}},
             'conjunctive': {'active': {'προσέξω'}, 'passive': {'προσεχθώ', 'προσεχτώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'πρόσεχα'}, 'passive': {'προσεχόμουν'}},
             'passive_perfect_participle': {'προσεγμένος/προσεγμένη/προσεγμένο'},
             'present': {'active': {'προσέχω'}, 'passive': {'προσέχομαι'}}},
        )

    def test_syntheto_toy_agw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('παραεισάγω'),
            {'act_pres_participle': {'παραεισάγοντας'},
             'pres_conjugation': 'con1_act',

             'aorist': {'active': {'παραεισήγαγα'},
                        'passive': {'παραεισήχθη', 'παραεισάχθηκα'}},
             'arch_act_pres_participle': {'παραεισάγων/παραεισάγουσα/παραεισάγον'},
             'conjunctive': {'active': {'παραεισαγάγω'}, 'passive': {'παραεισαχθώ'}},
             'modal': False,
             'paratatikos': {'active': {'παραεισήγα'}, 'passive': {'παραεισαγόμουν'}},
             'pass_pres_participle': {'παραεισαγόμενος/παραεισαγόμενη/παραεισαγόμενο'},
             'passive_perfect_participle': {'παραεισηγμένος/παραεισηγμένη/παραεισηγμένο'},

             'present': {'active': {'παραεισάγω'}, 'passive': {'παραεισάγομαι'}}}

        )

    def test_verb_eisexw(self):
        self.assertDictEqual(
            basic_verb('εισέχω'),
            {'act_pres_participle': {'εισέχοντας'},
             'aorist': {'active': {'εισείχα'}},
             'pres_conjugation': 'con1_act',

             'conjunctive': {'active': {'εισέχω'}},
             'modal': False,
             'paratatikos': {'active': {'εισείχα'}},
             'present': {'active': {'εισέχω'}}}

        )

    def test_verb_uperexw(self):
        self.assertDictEqual(
            basic_verb('υπερέχω'),
            {'act_pres_participle': {'υπερέχοντας'},
             'aorist': {'active': {'υπερείχα'}},
             'arch_act_pres_participle': {'υπερέχων/υπερέχουσα/υπερέχον'},
             'conjunctive': {'active': {'υπερέχω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'υπερείχα'}},
             'present': {'active': {'υπερέχω'}}}

        )

    def test_verb_tragoudo(self):
        self.assertDictEqual(
            basic_verb('τραγουδώ'),
            {'present': {'active': {'τραγουδώ'}, 'passive': {'τραγουδιέμαι'}},
             'conjunctive': {'active': {'τραγουδήσω'}, 'passive': {'τραγουδηθώ'}},
             'aorist': {'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}},
             'paratatikos': {'active': {'τραγουδούσα', 'τραγούδαγα'},
                             'passive': {'τραγουδιόμουν'}},
             'act_pres_participle': {'τραγουδώντας'},
             'pres_conjugation': 'con2a_act',
             'passive_perfect_participle': {'τραγουδισμένος/τραγουδισμένη/τραγουδισμένο',
                                            'τραγουδημένος/τραγουδημένη/τραγουδημένο'},
             'modal': False},

        )

    def test_verb_synkatexw(self):
        self.assertDictEqual(
            basic_verb('συγκατέχω'),
            {'act_pres_participle': {'συγκατέχοντας'},
             'aorist': {'active': {'συγκατείχα'}},
             'arch_act_pres_participle': {'συγκατέχων/συγκατέχουσα/συγκατέχον'},
             'conjunctive': {'active': {'συγκατέχω'}},
             'pres_conjugation': 'con1_act',
             'modal': False,
             'paratatikos': {'active': {'συγκατείχα', 'συγκάτεχα'},
                             'passive': {'συγκατεχόμουν'}},
             'pass_pres_participle': {'συγκατεχόμενος/συγκατεχόμενη/συγκατεχόμενο'},
             'present': {'active': {'συγκατέχω'}, 'passive': {'συγκατέχομαι'}}},

        )

    def test_verb_anhkw(self):
        self.assertDictEqual(
            basic_verb('ανήκω'),
            {'act_pres_participle': {'ανήκοντας'},
             'aorist': {},
             'arch_act_pres_participle': {'ανήκων/ανήκουσα/ανήκον'},
             'conjunctive': {},
             'pres_conjugation': 'con1_act',

             'modal': False,
             'paratatikos': {'active': {'άνηκα', 'ανήκα'}},
             'present': {'active': {'ανήκω'}}},

        )

    def test_verb_drw(self):
        self.assertDictEqual(
            basic_verb('δρω'),
            {'present': {'active': {'δρω'}},
             'conjunctive': {'active': {'δράσω'}},
             'pres_conjugation': 'con2a_act',

             'aorist': {'active': {'έδρασα'}},
             'paratatikos': {'active': {'δρούσα'}},
             'act_pres_participle': {'δρώντας'},
             'arch_act_pres_participle': {'δρών/δρούσα/δρών'},
             'pass_pres_participle': {'δρώμενος/δρώμενη/δρώμενο'}, 'modal': False},

        )

    def test_verb_titrwskw(self):
        self.assertDictEqual(
            basic_verb('τιτρώσκω'),
            {'present': {'active': {'τιτρώσκω'}},
             'conjunctive': {'passive': {'τρωθώ'}},
             'aorist': {'passive': {'ετρώθη', 'τρώθηκα'}},
             'paratatikos': {'active': {'ετίτρωσκα'}},
             'pres_conjugation': 'con1_act',

             'act_pres_participle': {'τιτρώσκοντας'}, 'modal': False},

        )

    def test_verb_bexw(self):
        self.assertDictEqual(
            basic_verb('βέχω'),
            {'act_pres_participle': {'βέχοντας'},
             'aorist': {},
             'conjunctive': {},
             'pres_conjugation': 'con1_act',

             'modal': False,
             'paratatikos': {'active': {'έβεχα'}},
             'present': {'active': {'βέχω'}}},

        )

    def test_verb_diaspeirw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('διασπείρω'),
            {'act_pres_participle': {'διασπείροντας'},
             'pres_conjugation': 'con1_act',

             'aorist': {'active': {'διέσπειρα'}, 'passive': {'διασπάρθηκα', 'διασπάρηκα'}},
             'conjunctive': {'active': {'διασπείρω'}, 'passive': {'διασπαρώ', 'διασπαρθώ'}},
             'modal': False,
             'paratatikos': {'active': {'διέσπειρα'}, 'passive': {'διασπειρόμουν'}},
             'passive_aorist_participle': {'διασπαρείς/διασπαρείσα/διασπαρέν',
                                           'διασπαρθείς/διασπαρθείσα/διασπαρθέν'},
             'passive_perfect_participle': {'διασπαρμένος/διασπαρμένη/διασπαρμένο'},
             'present': {'active': {'διασπείρω'}, 'passive': {'διασπείρομαι'}}}

        )

    def test_verb_thwrakizw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('θωρακίζω'),
            {'act_pres_participle': {'θωρακίζοντας'},
             'aorist': {'active': {'θωράκισα'}, 'passive': {'θωρακίστηκα', 'θωρακίσθηκα'}},
             'conjunctive': {'active': {'θωρακίσω'}, 'passive': {'θωρακισθώ', 'θωρακιστώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'θωράκιζα'}, 'passive': {'θωρακιζόμουν'}},
             'passive_aorist_participle': {'θωρακισθείς/θωρακισθείσα/θωρακισθέν'},
             'passive_perfect_participle': {'θωρακισμένος/θωρακισμένη/θωρακισμένο',
                                            'τεθωρακισμένος/τεθωρακισμένη/τεθωρακισμένο'},
             'present': {'active': {'θωρακίζω'}, 'passive': {'θωρακίζομαι'}}}

        )

    def test_verb_upomimnhskw(self):
        self.assertDictEqual(
            basic_verb('υπομιμνήσκω'),
            {'act_pres_participle': {'υπομιμνήσκοντας'},
             'aorist': {'active': {'υπέμνησα', 'υπόμνησα'},
                        'passive': {'υπεμνήσθη', 'υπομνήσθηκα'}},
             'conjunctive': {'active': {'υπομνήσω'},
                             'passive': {'υπομνησθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'υπομίμνησκα', 'υπεμίμνησκα'},
                             'passive': {'υπομιμνησκόμουν'}},
             'present': {'active': {'υπομιμνήσκω'}, 'passive': {'υπομιμνήσκομαι'}}}

        )

    def test_verb_methuskw(self):
        self.assertDictEqual(
            basic_verb('μεθύσκω'),
            {'act_pres_participle': {'μεθύσκοντας'},
             'aorist': {'active': {'μέθυσα'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {'active': {'μεθύσω'}},
             'modal': False,
             'paratatikos': {'active': {'μέθυσκα'}, 'passive': {'μεθυσκόμουν'}},
             'passive_perfect_participle': {'μεθυσμένος/μεθυσμένη/μεθυσμένο'},
             'present': {'active': {'μεθύσκω'}, 'passive': {'μεθύσκομαι'}}}

        )

    def test_verb_boskw(self):
        self.assertDictEqual(
            basic_verb('βόσκω'),
            {'act_pres_participle': {'βόσκοντας'},
             'aorist': {'active': {'βόσκησα'}},
             'conjunctive': {'active': {'βοσκήσω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'έβοσκα'}},
             'passive_perfect_participle': {'βοσκημένος/βοσκημένη/βοσκημένο'},
             'present': {'active': {'βόσκω'}}}

        )

    def test_verb_bibrwskw(self):
        self.assertDictEqual(
            basic_verb('καταβιβρώσκω'),
            {'act_pres_participle': {'καταβιβρώσκοντας'},
             'aorist': {},
             'pres_conjugation': 'con1_act',

             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'καταβίβρωσκα'}},
             'present': {'active': {'καταβιβρώσκω'}}},

        )

    def test_verb_kathisto(self):
        self.assertDictEqual(
            basic_verb('καθιστώ'),
            {'act_pres_participle': {'καθιστώντας'},
             'aorist': {'active': {'κατάστησα', 'κατέστησα'},
                        'passive': {'κατέστη', 'κατάστηκα'}},
             'conjunctive': {'active': {'καταστήσω'}, 'passive': {'καταστώ'}},
             'modal': False,
             'paratatikos': {'active': {'καθιστούσα'}, 'passive': {'καθιστάμην'}},
             'pass_pres_participle': {'καθιστάμενος/καθιστάμενη/καθιστάμενο'},
             'passive_aorist_participle': {'καταστάς/καταστάσα/καταστάν'},
             'passive_perfect_participle': {'κατεστημένος/κατεστημένη/κατεστημένο',
                                            'καταστισμένος/καταστισμένη/καταστισμένο'},
             'pres_conjugation': 'con2ak_act',
             'present': {'active': {'καθιστώ'}, 'passive': {'καθίσταμαι'}}}

        )

    def test_verb_gernw(self):
        self.assertDictEqual(
            basic_verb('γέρνω'),
            {'present': {'active': {'γέρνω'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {'active': {'γείρω'}}, 'aorist': {'active': {'έγειρα'}},
             'paratatikos': {'active': {'έγερνα'}}, 'act_pres_participle': {'γέρνοντας'}, 'modal': False}

        )

    def test_verb_dew(self):
        self.assertDictEqual(
            basic_verb('δέω'),
            {'present': {'active': {'δέω'}, 'passive': {'δέομαι'}},
             'conjunctive': {'active': {'δεήσω'}, 'passive': {'δεηθώ'}},
             'aorist': {'active': {'δέησα', 'εδέησα'}, 'passive': {'δεήθηκα'}}, 'paratatikos': {'passive': {'δεόμουν'}},
             'act_pres_participle': {'δέοντας'}, 'arch_act_pres_participle': {'δέων/δέουσα/δέον'},
             'pass_pres_participle': {'δεόμενος'}, 'active_aorist_participle': {'δεήσας/δεήσασα/δεήσαν'},
             'passive_aorist_participle': {'δεηθείς/δεηθείσα/δεηθέν'}, 'modal': False},

        )

    def test_verb_dew(self):
        self.assertDictEqual(
            basic_verb('δει'),
            {'present': {'active': {'δει'}}, 'conjunctive': {'active': {'δεήσει'}},
             'paratatikos': {'active': {'έδει'}}, 'pres_conjugation': 'con1_act_modal',

             'aorist': {'active': {'δέησε', 'εδέησε'}}, 'modal': True}

        )

    def test_verb_theto(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('θέτω'),
            {'present':
                 {'active': {'θέτω'},
                  'passive': {'θέτομαι', 'τίθεμαι'}},
             'pres_conjugation': 'con1_act',
             'conjunctive':
                 {'active': {'θέσω'},
                  'passive': {'τεθώ'}},
             'aorist': {'active': {'έθεσα'},
                        'passive': {'τέθηκα', 'ετέθη'}},
             'paratatikos':
                 {'active': {'έθετα'},
                  'passive': {'θετόμουν', 'τιθέμην'}},
             'act_pres_participle': {'θέτοντας'},
             'arch_act_pres_participle': {'θέτων/θέτουσα/θέτον'},

             'passive_aorist_participle': {'τεθείς/τεθείσα/τεθέν'},
             'passive_perfect_participle': {'τεθειμένος/τεθειμένη/τεθειμένο'},
             'modal': False}

        )

    def test_verb_kyberno(self):
        self.assertDictEqual(
            basic_verb('κυβερνώ'),
            {'present': {'active': {'κυβερνώ'},
                         'passive': {'κυβερνούμαι', 'κυβερνιέμαι', 'κυβερνώμαι'}},
             'conjunctive': {'active': {'κυβερνήσω'}, 'passive': {'κυβερνηθώ'}},
             'aorist': {'active': {'κυβέρνησα'}, 'passive': {'κυβερνήθηκα'}},
             'pres_conjugation': 'con2a_act',
             'paratatikos': {'active': {'κυβέρναγα', 'κυβερνούσα'},
                             'passive': {'κυβερνιόμουν', 'κυβερνούμουν'}},
             'act_pres_participle': {'κυβερνώντας'},
             'arch_act_pres_participle': {'κυβερνών/κυβερνούσα/κυβερνών'},
             'pass_pres_participle': {'κυβερνούμενος/κυβερνούμενη/κυβερνούμενο',
                                      'κυβερνώμενος/κυβερνώμενη/κυβερνώμενο'},
             'passive_perfect_participle': {'κυβερνημένος/κυβερνημένη/κυβερνημένο'},
             'modal': False},
        )

    def test_verb_douleuo(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('δουλεύω'),
            {'act_pres_participle': {'δουλεύοντας'},
             'active_aorist_participle': {'δουλεύσας/δουλεύσασα/δουλεύσαν'},
             'aorist': {'active': {'δούλευσα', 'δούλεψα'},
                        'passive': {'δουλεύτηκα', 'δουλεύθηκα'}},
             'conjunctive': {'active': {'δουλέψω', 'δουλεύσω'},
                             'passive': {'δουλευτώ', 'δουλευθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'δούλευα'}, 'passive': {'δουλευόμουν'}},
             'passive_aorist_participle': {'δουλευθείς/δουλευθείσα/δουλευθέν'},
             'passive_perfect_participle': {'δεδουλευμένος/δεδουλευμένη/δεδουλευμένο',
                                            'δουλεμένος/δουλεμένη/δουλεμένο',
                                            'δουλευμένος/δουλευμένη/δουλευμένο'},
             'present': {'active': {'δουλεύω'}, 'passive': {'δουλεύομαι'}}}

        )

    def test_verb_spatalo(self):
        self.assertDictEqual(
            basic_verb('σπαταλώ'),
            {'present': {'active': {'σπαταλώ'}, 'passive': {'σπαταλώμαι', 'σπαταλιέμαι'}},
             'conjunctive': {'active': {'σπαταλήσω'}, 'passive': {'σπαταληθώ'}},
             'aorist': {'active': {'σπατάλησα'}, 'passive': {'σπαταλήθηκα'}},
             'pres_conjugation': 'con2a_act',
             'paratatikos': {'active': {'σπαταλούσα', 'σπατάλαγα'}, 'passive': {'σπαταλιόμουν'}},
             'act_pres_participle': {'σπαταλώντας'},
             'passive_perfect_participle': {'σπαταλημένος/σπαταλημένη/σπαταλημένο'},
             'modal': False}

        )

    def test_verb_ximaw(self):
        self.assertDictEqual(
            basic_verb('χιμάω'),
            {'present': {'active': {'χιμάω'}},
             'conjunctive': {'active': {'χιμήξω'}},
             'aorist': {'active': {'χίμηξα'}},
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'χιμούσα'}}, 'act_pres_participle': {'χιμώντας'}, 'modal': False}

        )

    def test_verb_xumaw(self):
        self.assertDictEqual(
            basic_verb('χυμάω'),
            {'present': {'active': {'χυμάω'}},
             'conjunctive': {'active': {'χυμήξω'}},
             'aorist': {'active': {'χύμηξα'}},
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'χυμούσα'}},
             'act_pres_participle': {'χυμώντας'}, 'modal': False},

        )

    def test_verb_ikanopoiw(self):
        self.assertDictEqual(
            basic_verb('ικανοποιώ'),
            {'present': {'active': {'ικανοποιώ'}, 'passive': {'ικανοποιούμαι'}},
             'conjunctive': {'active': {'ικανοποιήσω'}, 'passive': {'ικανοποιηθώ'}},
             'aorist': {'active': {'ικανοποίησα'}, 'passive': {'ικανοποιήθηκα'}},
             'paratatikos': {'active': {'ικανοποιούσα'}, 'passive': {'ικανοποιούμουν', 'ικανοποιόμουν'}},
             'act_pres_participle': {'ικανοποιώντας'},
             'pres_conjugation': 'con2b_act',

             'pass_pres_participle': {'ικανοποιούμενος/ικανοποιούμενη/ικανοποιούμενο'},
             'passive_perfect_participle': {'ικανοποιημένος/ικανοποιημένη/ικανοποιημένο'},
             'passive_aorist_participle': {'ικανοποιηθείς/ικανοποιηθείσα/ικανοποιηθέν'}, 'modal': False},

        )

    def test_verb_apokleiw(self):
        self.assertDictEqual(
            basic_verb('αποκλείω'),
            {'act_pres_participle': {'αποκλείοντας'},
             'aorist': {'active': {'απέκλεισα', 'απόκλεισα'},
                        'passive': {'αποκλείστηκα', 'αποκλείσθηκα'}},
             'conjunctive': {'active': {'αποκλείσω'},
                             'passive': {'αποκλειστώ', 'αποκλεισθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'απέκλεια', 'απόκλεια'}, 'passive': {'αποκλειόμουν'}},
             'pass_pres_participle': {'αποκλειόμενος/αποκλειόμενη/αποκλειόμενο'},
             'passive_aorist_participle': {'αποκλεισθείς/αποκλεισθείσα/αποκλεισθέν'},
             'passive_perfect_participle': {'αποκλεισμένος/αποκλεισμένη/αποκλεισμένο'},
             'present': {'active': {'αποκλείω'}, 'passive': {'αποκλείομαι'}}},

        )

    def test_verb_xew(self):
        self.assertDictEqual(
            basic_verb('χέω'),
            {'act_pres_participle': {'χέοντας'},
             'aorist': {'active': {'έχυσα'}, 'passive': {'χύθηκα'}},
             'conjunctive': {'active': {'χύσω'}, 'passive': {'χυθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'έχεα'}},
             'passive_perfect_participle': {'χυμένος/χυμένη/χυμένο'},
             'present': {'active': {'χέω'}}}

        )

    def test_verb_βαρυγκομάω(self):
        self.assertDictEqual(
            basic_verb('βαρυγκομάω'),
            {'present': {'active': {'βαρυγκομάω'}},
             'conjunctive': {'active': {'βαρυγκομήσω'}},
             'pres_conjugation': 'con2a_act',
             'aorist': {'active': {'βαρυγκόμησα'}},
             'paratatikos': {'active': {'βαρυγκομούσα'}},
             'act_pres_participle': {'βαρυγκομώντας'},
             'passive_perfect_participle': {'βαρυγκομισμένος/βαρυγκομισμένη/βαρυγκομισμένο'},
             'modal': False},
        )

    def test_verb_ζω(self):
        self.assertDictEqual(
            basic_verb('ζω'),
            {'present': {'active': {'ζω'}}, 'conjunctive': {'active': {'ζήσω'}},
             'aorist': {'active': {'έζησα'}}, 'paratatikos': {'active': {'ζούσα'}},
             'act_pres_participle': {'ζώντας'},
             'pres_conjugation': 'con2b_act',
             'arch_act_pres_participle': {'ζών/ζώσα/ζών'},
             'modal': False},

        )

    def test_verb_paxaino(self):
        self.assertDictEqual(
            basic_verb('παχαίνω'),
            {'present': {'active': {'παχαίνω'}}, 'conjunctive': {'active': {'παχύνω'}},
             'aorist': {'active': {'πάχυνα'}},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'πάχαινα'}},
             'act_pres_participle': {'παχαίνοντας'},
             'passive_perfect_participle': {'παχυμένος/παχυμένη/παχυμένο'},
             'modal': False}

        )

    def test_verb_blepo(self):
        self.assertDictEqual(
            basic_verb('βλέπω'),
            {'present': {'active': {'βλέπω'}, 'passive': {'βλέπομαι'}},
             'conjunctive': {'active': {'δω'}, 'passive': {'ιδωθώ'}},
             'aorist': {'active': {'είδα'}, 'passive': {'ειδώθηκα', 'ιδώθηκα'}},
             'paratatikos': {'active': {'έβλεπα'}, 'passive': {'βλεπόμουν'}},
             'pres_conjugation': 'con1_act',
             'act_pres_participle': {'βλέποντας'},
             'arch_act_pres_participle': {'βλέπων/βλέπουσα/βλέπον'},
             'passive_perfect_participle': {'ιδωμένος/ιδωμένη/ιδωμένο'},
             'modal': False}
        )

    def test_verb_syllambano(self):
        self.assertDictEqual(
            basic_verb('συλλαμβάνω'),
            {'present': {'active': {'συλλαμβάνω'}, 'passive': {'συλλαμβάνομαι'}},
             'conjunctive': {'active': {'συλλάβω'}, 'passive': {'συλληφθώ'}},
             'aorist': {'active': {'συνέλαβα'}, 'passive': {'συνελήφθη', 'συλλήφθηκα'}},
             'paratatikos': {'active': {'συλλάμβανα', 'συνελάμβανα'},
                             'passive': {'συλλαμβανόμουν'}},
             'act_pres_participle': {'συλλαμβάνοντας'},
             'pres_conjugation': 'con1_act',
             'pass_pres_participle': {'συλλαμβανόμενος/συλλαμβανόμενη/συλλαμβανόμενο'},
             'passive_aorist_participle': {'συλληφθείς/συλληφθείσα/συλληφθέν'},
             'modal': False},

        )

    def test_verb_phgainvo(self):
        self.assertDictEqual(
            basic_verb('πηγαίνω'),
            {'present': {'active': {'πηγαίνω'}}, 'conjunctive': {'active': {'πάω'}},
             'aorist': {'active': {'πήγα'}}, 'paratatikos': {'active': {'πήγαινα'}},
             'act_pres_participle': {'πηγαίνοντας'},
             'pres_conjugation': 'con1_act',

             'modal': False},

        )

    def test_verb_nothing(self):
        self.assertRaises(NotInGreekException, basic_verb, '')

    def test_verb_gibberish(self):
        self.assertRaises(NotInGreekException, basic_verb, 'gamao')

    def test_verb_prokeitai(self):
        self.assertDictEqual(
            basic_verb('πρόκειται'),
            {'present': {'passive': {'πρόκειται'}},
             'paratatikos': {'passive': {'επρόκειτο'}},
             'pres_conjugation': 'con2_pass_modal',

             'aorist': {},
             'modal': True},
        )

    def test_verb_erxomai(self):
        self.assertDictEqual(
            basic_verb('έρχομαι'),
            {'present': {'passive': {'έρχομαι'}},
             'conjunctive': {'active': {'έλθω', 'έρθω'}},
             'aorist': {'active': {'ήλθα', 'ήρθα'}},
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'ερχόμουν'}},
             'pass_pres_participle': {'ερχόμενος/ερχόμενη/ερχόμενο'},
             'modal': False},

        )

    def test_verb_synerxomai(self):
        self.maxDiff = None
        self.assertDictEqual(

            basic_verb('συνέρχομαι'),
            {'present': {'passive': {'συνέρχομαι'}}, 'conjunctive': {'active': {'συνέλθω', 'συνέρθω'}},
             'aorist': {'active': {'συνήρθα', 'συνήλθα'}}, 'paratatikos': {'passive': {'συνερχόμουν'}},
             'pass_pres_participle': {'συνερχόμενος/συνερχόμενη/συνερχόμενο'},
             'pres_conjugation': 'con1_pass',
             'active_aorist_participle': {'συνελθών/συνελθούσα/συνελθόν'},
             'modal': False},

        )

    def test_verb_katebainw(self):
        self.assertDictEqual(
            basic_verb('κατεβαίνω'),
            {'present': {'active': {'κατεβαίνω'}},
             'conjunctive': {'active': {'κατέβω', 'κατεβώ'}},
             'aorist': {'active': {'κατέβηκα', 'κατέβη'}},
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'κατέβαινα'}},
             'act_pres_participle': {'κατεβαίνοντας'},
             'modal': False},

        )

    def test_verb_arnoumai(self):
        self.assertDictEqual(
            basic_verb('αρνιέμαι'),
            {'present': {'passive': {'αρνιέμαι', 'αρνούμαι'}},
             'conjunctive': {'passive': {'αρνηθώ'}},
             'aorist': {'passive': {'αρνήθηκα'}},
             'paratatikos': {'passive': {'αρνούμουν', 'αρνιόμουν'}},
             'pass_pres_participle': {'αρνούμενος/αρνούμενη/αρνούμενο'},
             'pres_conjugation': 'con2a_pass',

             'modal': False},

        )

    def test_verb_eisago(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('εισάγω'),
            {'present': {'active': {'εισάγω'}, 'passive': {'εισάγομαι'}},
             'conjunctive': {'active': {'εισαγάγω'}, 'passive': {'εισαχθώ'}},
             'aorist': {'active': {'εισήγαγα'}, 'passive': {'εισήχθη', 'εισάχθηκα'}},
             'paratatikos': {'active': {'εισήγα'}, 'passive': {'εισαγόμουν'}},
             'act_pres_participle': {'εισάγοντας'},
             'pres_conjugation': 'con1_act',

             'arch_act_pres_participle': {'εισάγων/εισάγουσα/εισάγον'},
             'pass_pres_participle': {'εισαγόμενος/εισαγόμενη/εισαγόμενο'},
             'passive_perfect_participle': {'εισηγμένος/εισηγμένη/εισηγμένο',
                                            'εισαγμένος/εισαγμένη/εισαγμένο'},
             'passive_aorist_participle': {'εισαχθείς/εισαχθείσα/εισαχθέν'}, 'modal': False},

        )

    def test_verb_dialego(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('διαλέγω'),
            {'present': {'active': {'διαλέγω'}, 'passive': {'διαλέγομαι'}},
             'conjunctive': {'active': {'διαλέξω'}, 'passive': {'διαλεχθώ', 'διαλεχτώ'}},
             'aorist': {'active': {'διάλεξα'}, 'passive': {'διαλέχτηκα', 'διαλέχθηκα'}},
             'paratatikos': {'active': {'διάλεγα'}, 'passive': {'διαλεγόμουν'}},
             'pres_conjugation': 'con1_act',

             'act_pres_participle': {'διαλέγοντας'},
             'pass_pres_participle': {'διαλεγόμενος/διαλεγόμενη/διαλεγόμενο'},
             'passive_perfect_participle': {'διαλεγμένος/διαλεγμένη/διαλεγμένο'},
             'modal': False},

        )

    def test_verb_deiknuw(self):
        self.assertDictEqual(
            basic_verb('δεικνύω'),
            {'present': {'active': {'δεικνύω'}, 'passive': {'δεικνύομαι'}},
             'conjunctive': {'active': {'δείξω'}, 'passive': {'δειχθώ'}},
             'aorist': {'active': {'έδειξα'}, 'passive': {'δείχθηκα'}},
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'δείκνυα'}, 'passive': {'δεικνυόμουν'}},
             'act_pres_participle': {'δεικνύοντας'},
             'arch_act_pres_participle': {'δεικνύων/δεικνύουσα/δεικνύον'},
             'pass_pres_participle': {'δεικνυόμενος/δεικνυόμενη/δεικνυόμενο'},
             'passive_perfect_participle': {'δειγμένος/δειγμένη/δειγμένο'},
             'active_aorist_participle': {'δείξας/δείξασα/δείξαν'},
             'passive_aorist_participle': {'δειχθείς/δειχθείσα/δειχθέν'}, 'modal': False},

        )

    def test_verb_nemw(self):
        self.assertDictEqual(
            basic_verb('νέμω'),
            {'present': {'active': {'νέμω'}, 'passive': {'νέμομαι'}},
             'conjunctive': {'active': {'νείμω'}, 'passive': {'νεμηθώ'}},
             'aorist': {'active': {'ένειμα'}, 'passive': {'νεμήθηκα'}},
             'paratatikos': {'active': {'ένεμα'}, 'passive': {'νεμόμουν'}},
             'act_pres_participle': {'νέμοντας'},
             'passive_perfect_participle': {'νεμημένος/νεμημένη/νεμημένο'},
             'pres_conjugation': 'con1_act',
             'passive_aorist_participle': {'νεμηθείς/νεμηθείσα/νεμηθέν'},
             'modal': False},

        )

    def test_verb_kleptw(self):
        self.assertDictEqual(
            basic_verb('κλέπτω'),
            {'act_pres_participle': {'κλέπτοντας'},
             'aorist': {'active': {'έκλεψα'}, 'passive': {'κλέφτηκα', 'εκλάπη', 'κλάπηκα'}},
             'conjunctive': {'active': {'κλέψω'}, 'passive': {'κλαπώ', 'κλεφτώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'έκλεπτα'}, 'passive': {'κλεπτόμουν'}},
             'passive_aorist_participle': {'κλαπείς/κλαπείσα/κλαπέν'},
             'passive_perfect_participle': {'κλεμμένος/κλεμμένη/κλεμμένο'},
             'present': {'active': {'κλέπτω'}, 'passive': {'κλέπτομαι'}}}

        )

    def test_verb_antiparaballw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('αντιπαραβάλλω'),
            {'act_pres_participle': {'αντιπαραβάλλοντας'},
             'active_aorist_participle': {'αντιπαραβαλών/αντιπαραβαλούσα/αντιπαραβαλόν'},
             'aorist': {'active': {'αντιπαρέβαλα'},
                        'passive': {'αντιπαρεβλήθη', 'αντιπαραβλήθηκα'}},
             'arch_act_pres_participle': {'αντιπαραβάλλων/αντιπαραβάλλουσα/αντιπαραβάλλον'},
             'conjunctive': {'active': {'αντιπαραβάλω'}, 'passive': {'αντιπαραβληθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'αντιπαρέβαλλα'}, 'passive': {'αντιπαραβαλλόμουν'}},
             'pass_pres_participle': {'αντιπαραβαλλόμενος/αντιπαραβαλλόμενη/αντιπαραβαλλόμενο'},
             'passive_aorist_participle': {'αντιπαραβληθείς/αντιπαραβληθείσα/αντιπαραβληθέν'},
             'passive_perfect_participle': {'αντιπαραβεβλημένος/αντιπαραβεβλημένη/αντιπαραβεβλημένο'},

             'present': {'active': {'αντιπαραβάλλω'}, 'passive': {'αντιπαραβάλλομαι'}}}

        )

    def test_verb_pethainw(self):
        self.assertDictEqual(
            basic_verb('πεθαίνω'),
            {'present': {'active': {'πεθαίνω'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {'active': {'πεθάνω'}},
             'aorist': {'active': {'πέθανα'}}, 'paratatikos': {'active': {'πέθαινα'}},
             'act_pres_participle': {'πεθαίνοντας'},
             'passive_perfect_participle': {'πεθαμένος/πεθαμένη/πεθαμένο'},
             'modal': False},

        )

    def test_verb_perimenw(self):
        self.assertDictEqual(
            basic_verb('περιμένω'),
            {'present': {'active': {'περιμένω'}}, 'conjunctive': {'active': {'περιμένω'}},
             'aorist': {'active': {'περίμενα'}},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'περίμενα'}},
             'act_pres_participle': {'περιμένοντας'}, 'arch_act_pres_participle': {'περιμένων/περιμένουσα/περιμένον'},
             'modal': False},

        )

    def test_verb_pathainw(self):
        self.assertDictEqual(
            basic_verb('παθαίνω'),
            {'present': {'active': {'παθαίνω'}, 'passive': {'παθαίνομαι'}},
             'conjunctive': {'active': {'πάθω'}},
             'aorist': {'active': {'έπαθα'}},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'πάθαινα'}, 'passive': {'παθαινόμουν'}},
             'act_pres_participle': {'παθαίνοντας'},
             'passive_perfect_participle': {'παθημένος/παθημένη/παθημένο'},
             'active_aorist_participle': {'παθών/παθούσα/παθόν'}, 'modal': False},

        )

    def test_verb_proferw(self):
        self.assertDictEqual(
            basic_verb('προφέρω'),
            {'present': {'active': {'προφέρω'},
                         'passive': {'προφέρομαι'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {'active': {'προφέρω'}, 'passive': {'προφερθώ'}},
             'aorist': {'active': {'πρόφερα'}, 'passive': {'προφέρθηκα'}},
             'paratatikos': {'active': {'πρόφερα'}, 'passive': {'προφερόμουν'}},
             'act_pres_participle': {'προφέροντας'},
             'passive_perfect_participle': {'προφερμένος/προφερμένη/προφερμένο'},
             'modal': False},

        )

    def test_verb_brithw(self):
        # an example of an elliptive verb
        self.assertDictEqual(
            basic_verb('βρίθω'),
            {'present': {'active': {'βρίθω'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {}, 'aorist': {}, 'paratatikos': {'active': {'έβριθα'}},
             'act_pres_participle': {'βρίθοντας'}, 'arch_act_pres_participle': {'βρίθων/βρίθουσα/βρίθον'},
             'modal': False},

        )

    def test_verb_kserw(self):
        self.assertDictEqual(
            basic_verb('ξέρω'),
            {'present': {'active': {'ξέρω'}},
             'pres_conjugation': 'con1_act',
             'conjunctive': {}, 'aorist': {}, 'paratatikos': {'active': {'ήξερα'}},
             'act_pres_participle': {'ξέροντας'}, 'modal': False},

        )

    def test_verb_euthunomai(self):
        self.assertDictEqual(
            basic_verb('ευθύνομαι'),
            {'present': {'passive': {'ευθύνομαι'}},
             'paratatikos': {'passive': {'ευθυνόμουν'}},
             'pres_conjugation': 'con1_pass',

             'modal': False},

        )

    def test_verb_thabw(self):
        self.assertDictEqual(
            basic_verb('θάβω'),
            {'present': {'active': {'θάβω'},
                         'passive': {'θάβομαι'}},
             'conjunctive': {'active': {'θάψω'},
                             'passive': {'θαφθώ', 'θαφτώ', 'ταφώ'}},
             'aorist': {'active': {'έθαψα'},
                        'passive': {'θάφτηκα', 'θάφθηκα', 'τάφηκα', 'ετάφη'}},
             'passive_aorist_participle': {'ταφείς/ταφείσα/ταφέν'},
             'paratatikos': {'active': {'έθαβα'}, 'passive': {'θαβόμουν'}},
             'act_pres_participle': {'θάβοντας'},
             'pres_conjugation': 'con1_act',
             'passive_perfect_participle': {'θαμμένος/θαμμένη/θαμμένο'},
             'active_aorist_participle': {'θάψας/θάψασα/θάψαν'},
             'modal': False},

        )

    def test_verb_epitaxunw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('επιταχύνω'),
            {'present': {'active': {'επιταχύνω'}, 'passive': {'επιταχύνομαι'}},
             'conjunctive': {'active': {'επιταχύνω'}, 'passive': {'επιταχυνθώ'}},
             'aorist': {'active': {'επιτάχυνα'}, 'passive': {'επιταχύνθηκα'}},
             'paratatikos': {'active': {'επιτάχυνα'}, 'passive': {'επιταχυνόμουν'}},
             'act_pres_participle': {'επιταχύνοντας'},
             'pass_pres_participle': {'επιταχυνόμενος/επιταχυνόμενη/επιταχυνόμενο'},
             'passive_perfect_participle': {'επιταχυμένος/επιταχυμένη/επιταχυμένο'},
             'pres_conjugation': 'con1_act',

             'passive_aorist_participle': {'επιταχυνθείς/επιταχυνθείσα/επιταχυνθέν'}, 'modal': False},

        )

    def test_verb_apallassw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('απαλλάσσω'),
            {'act_pres_participle': {'απαλλάσσοντας'},
             'aorist': {'active': {'απήλλαξα', 'απάλλαξα'},
                        'passive': {'απαλλάχτηκα', 'απαλλάχθηκα', 'απαλλάγηκα', 'απηλλάγη'}},
             'conjunctive': {'active': {'απαλλάξω'},
                             'passive': {'απαλλαχθώ', 'απαλλαχτώ', 'απαλλαγώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'απάλλασσα'}, 'passive': {'απαλλασσόμουν'}},
             'pass_pres_participle': {'απαλλασσόμενος/απαλλασσόμενη/απαλλασσόμενο'},
             'passive_aorist_participle': {'απαλλαγείς/απαλλαγείσα/απαλλαγέν'},
             'passive_perfect_participle': {'απαλλαγμένος/απαλλαγμένη/απαλλαγμένο'},
             'present': {'active': {'απαλλάσσω'}, 'passive': {'απαλλάσσομαι'}}},

        )

    def test_verb_kataxrvmai(self):
        self.assertDictEqual(
            basic_verb('καταχρώμαι'),
            {'aorist': {'passive': {'καταχράστηκα'}},
             'conjunctive': {'passive': {'καταχραστώ'}},
             'pres_conjugation': 'con2ak_pass',

             'modal': False,
             'paratatikos': {'passive': {'καταχρόμουν'}},
             'pass_pres_participle': {'καταχρώμενος/καταχρώμενη/καταχρώμενο'},
             'passive_perfect_participle': {'καταχρασμένος/καταχρασμένη/καταχρασμένο'},
             'present': {'passive': {'καταχρώμαι'}}})

    def test_verb_kleinw(self):
        self.assertDictEqual(
            basic_verb('κλείνω'),
            {'act_pres_participle': {'κλείνοντας'},
             'pres_conjugation': 'con1_act',

             'aorist': {'active': {'έκλεισα'}, 'passive': {'κλείστηκα', 'κλείσθηκα'}},
             'conjunctive': {'active': {'κλείσω'}, 'passive': {'κλεισθώ', 'κλειστώ'}},
             'modal': False,
             'paratatikos': {'active': {'έκλεινα'}, 'passive': {'κλεινόμουν'}},
             'passive_perfect_participle': {'κλεισμένος/κλεισμένη/κλεισμένο',
                                            'κεκλεισμένος/κεκλεισμένη/κεκλεισμένο'},
             'present': {'active': {'κλείνω'}, 'passive': {'κλείνομαι'}}},
            # ic(basic_verb('παραέχω'))
        )

    def test_verb_paralabainw(self):
        self.assertDictEqual(
            basic_verb('παραλαβαίνω'),
            {'act_pres_participle': {'παραλαβαίνοντας'},
             'aorist': {'active': {'παρέλαβα'}, 'passive': {'παρελήφθη', 'παραλήφθηκα'}},
             'conjunctive': {'active': {'παραλάβω'}, 'passive': {'παραληφθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'παραλάβαινα'}, 'passive': {'παραλαβαινόμουν'}},
             'present': {'active': {'παραλαβαίνω'}, 'passive': {'παραλαβαίνομαι'}}},

        )

    def test_verb_parakathomai(self):
        self.assertDictEqual(
            Verb('παρακάθομαι', para=True).basic_forms,
            {'aorist': {'active': {'παραέκατσα', 'παρακάθισα'}},
             'conjunctive': {'active': {'παρακάτσω', 'παρακαθίσω'}},
             'modal': False,
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'παρακαθόμουν'}},
             'pass_pres_participle': {'παρακαθούμενος/παρακαθούμενη/παρακαθούμενο'},
             'passive_perfect_participle': {'παρακαθισμένος/παρακαθισμένη/παρακαθισμένο'},
             'present': {'passive': {'παρακάθομαι'}}}
        )

    def test_verb_filaw(self):
        self.assertDictEqual(
            basic_verb('φιλάω'),
            {'act_pres_participle': {'φιλώντας'},
             'aorist': {'active': {'φίλησα'}, 'passive': {'φιλήθηκα'}},
             'conjunctive': {'active': {'φιλήσω'}, 'passive': {'φιληθώ'}},
             'modal': False,
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'φιλούσα', 'φίλαγα'}, 'passive': {'φιλιόμουν'}},
             'passive_perfect_participle': {'φιλημένος/φιλημένη/φιλημένο'},
             'present': {'active': {'φιλάω'}, 'passive': {'φιλιέμαι'}}}

        )

    def test_verb_trww(self):
        self.assertDictEqual(
            basic_verb('τρώω'),
            {'act_pres_participle': {'τρώγοντας'},
             'aorist': {'active': {'έφαγα'}, 'passive': {'φαγώθηκα'}},
             'conjunctive': {'active': {'φάγω', 'φάω'}, 'passive': {'φαγωθώ'}},
             'arch_act_pres_participle': {'τρώγων/τρώγουσα/τρώγον'},
             'pres_conjugation': 'con2c_act',

             'modal': False,
             'paratatikos': {'active': {'έτρωγα'}, 'passive': {'τρωγόμουν'}},
             'passive_aorist_participle': {'φαγωθείς/φαγωθείσα/φαγωθέν'},
             'passive_perfect_participle': {'φαγωμένος/φαγωμένη/φαγωμένο'},
             'present': {'active': {'τρώω'}, 'passive': {'τρώγομαι'}}}

        )

    def test_verb_sebomai(self):
        self.assertDictEqual(
            basic_verb('σέβομαι'),
            {'aorist': {'passive': {'σεβάστηκα', 'σεβάσθηκα'}},
             'conjunctive': {'passive': {'σεβασθώ', 'σεβαστώ'}},
             'modal': False,
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'σεβόμουν'}},
             'pass_pres_participle': {'σεβόμενος/σεβόμενη/σεβόμενο'},
             'passive_perfect_participle': {'σεβασμένος/σεβασμένη/σεβασμένο'},
             'present': {'passive': {'σέβομαι'}}}

        )

    def test_verb_ofeilw(self):
        self.assertDictEqual(
            basic_verb('οφείλω'),
            {'act_pres_participle': {'οφείλοντας'},
             'aorist': {},
             'pres_conjugation': 'con1_act',

             'conjunctive': {},
             'modal': False,
             'paratatikos': {'active': {'όφειλα'}, 'passive': {'οφειλόμουν'}},
             'pass_pres_participle': {'οφειλόμενος/οφειλόμενη/οφειλόμενο'},
             'present': {'active': {'οφείλω'}, 'passive': {'οφείλομαι'}}}

        )

    def test_verb_diamarturomai(self):
        self.assertDictEqual(
            basic_verb('διαμαρτύρομαι'),
            {'aorist': {'passive': {'διαμαρτυρήθηκα'}},
             'conjunctive': {'passive': {'διαμαρτυρηθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'διαμαρτυρόμουν'}},
             'pass_pres_participle': {'διαμαρτυρόμενος/διαμαρτυρόμενη/διαμαρτυρόμενο'},
             'passive_aorist_participle': {'διαμαρτυρηθείς/διαμαρτυρηθείσα/διαμαρτυρηθέν'},
             'passive_perfect_participle': {'διαμαρτυρημένος/διαμαρτυρημένη/διαμαρτυρημένο'},
             'present': {'passive': {'διαμαρτύρομαι'}}}

        )

    def test_verb_zhlw(self):
        self.assertDictEqual(
            basic_verb('ζηλώ'),
            {'act_pres_participle': {'ζηλώντας'},
             'aorist': {'active': {'εζήλωσα', 'ζήλωσα'}},
             'conjunctive': {'active': {'ζηλώσω'}},
             'modal': False,
             'pres_conjugation': 'con2d_act',

             'paratatikos': {'active': {'ζηλούσα'}},
             'present': {'active': {'ζηλώ'}}},

        )

    def test_verb_ksanakukloforw(self):
        self.assertDictEqual(
            basic_verb('ξανακυκλοφορώ'),
            {'act_pres_participle': {'ξανακυκλοφορώντας'},
             'pres_conjugation': 'con2b_act',
             'active_aorist_participle': {'ξανακυκλοφορήσας/ξανακυκλοφορήσασα/ξανακυκλοφορήσαν'},
             'aorist': {'active': {'ξανακυκλοφόρησα'}, 'passive': {'ξανακυκλοφορήθηκα'}},
             'arch_act_pres_participle': {'ξανακυκλοφορών/ξανακυκλοφορούσα/ξανακυκλοφορούν'},
             'conjunctive': {'active': {'ξανακυκλοφορήσω'}, 'passive': {'ξανακυκλοφορηθώ'}},
             'modal': False,

             'paratatikos': {'active': {'ξανακυκλοφορούσα'},
                             'passive': {'ξανακυκλοφοριόμουν', 'ξανακυκλοφορούμουν'}},
             'pass_pres_participle': {'ξανακυκλοφορούμενος/ξανακυκλοφορούμενη/ξανακυκλοφορούμενο'},
             'passive_perfect_participle': {'ξανακυκλοφορημένος/ξανακυκλοφορημένη/ξανακυκλοφορημένο'},
             'present': {'active': {'ξανακυκλοφορώ'},
                         'passive': {'ξανακυκλοφοριέμαι', 'ξανακυκλοφορούμαι'}}}

        )

    def test_verb_isoumai(self):
        self.assertDictEqual(
            basic_verb('ισούμαι'),
            {'aorist': {'passive': {'ισώθηκα'}},
             'conjunctive': {'passive': {'ισωθώ'}},
             'pres_conjugation': 'con2f_pass',

             'modal': False,
             'paratatikos': {'passive': {'ισούμουν'}},
             'passive_perfect_participle': {'ισωμένος/ισωμένη/ισωμένο'},
             'present': {'passive': {'ισούμαι'}}}

        )

    def test_verb_antikoimai(self):
        self.assertDictEqual(
            basic_verb('αντίκειμαι'),
            {'modal': False,
             'pres_conjugation': 'con2d_pass',

             'paratatikos': {'passive': {'αντίκειτο'}},
             'pass_pres_participle': {'αντικείμενος/αντικείμενη/αντικείμενο'},
             'present': {'passive': {'αντίκειμαι'}}}

        )

    def test_verb_katapsixv(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('καταψύχω'),
            {'present': {'active': {'καταψύχω'}, 'passive': {'καταψύχομαι'}},
             'conjunctive': {'active': {'καταψύξω'}, 'passive': {'καταψυχθώ', 'καταψυχτώ'}},
             'aorist': {'active': {'κατέψυξα'}, 'passive': {'καταψύχτηκα', 'καταψύχθηκα'}},
             'paratatikos': {'active': {'κατέψυχα'}, 'passive': {'καταψυχόμουν'}},
             'act_pres_participle': {'καταψύχοντας'},
             'pres_conjugation': 'con1_act',
             'passive_perfect_participle': {'κατεψυγμένος/κατεψυγμένη/κατεψυγμένο',
                                            'καταψυγμένος/καταψυγμένη/καταψυγμένο'},
             'modal': False},

        )

    def test_verb_sthnw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('στήνω'),
            {'present': {'active': {'στήνω'}, 'passive': {'στήνομαι'}},
             'conjunctive': {'active': {'στήσω'}, 'passive': {'στηθώ'}},
             'aorist': {'active': {'έστησα'}, 'passive': {'στήθηκα'}},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'έστηνα'}, 'passive': {'στηνόμουν'}},
             'act_pres_participle': {'στήνοντας'},
             'passive_perfect_participle': {'στημένος/στημένη/στημένο'}, 'modal': False},

        )

    def test_verb_systhnw(self):
        self.assertDictEqual(
            basic_verb('συστήνω'),
            {'present': {'active': {'συστήνω'}, 'passive': {'συστήνομαι'}},
             'conjunctive': {'active': {'συστήσω'}, 'passive': {'συστηθώ', 'συσταθώ'}},
             'aorist': {'active': {'σύστησα', 'συνέστησα'},
                        'passive': {'συνεστήθη', 'συστάθηκα', 'συνεστάθη', 'συστήθηκα'}},
             'paratatikos': {'active': {'σύστηνα'},
                             'passive': {'συστηνόμουν'}},
             'act_pres_participle': {'συστήνοντας'},
             'pres_conjugation': 'con1_act',

             'passive_perfect_participle': {'συστημένος/συστημένη/συστημένο'},
             'passive_aorist_participle': {'συσταθείς/συσταθείσα/συσταθέν'}, 'modal': False},

        )

    def test_verb_katasxw(self):
        self.assertDictEqual(
            basic_verb('κατάσχω'),
            {'act_pres_participle': {'κατάσχοντας'},
             'active_aorist_participle': {'κατασχέσας/κατασχέσασα/κατασχέσαν'},
             'aorist': {'active': {'κατάσχεσα'}, 'passive': {'κατασχέθηκα'}},
             'conjunctive': {'active': {'κατασχέσω'}, 'passive': {'κατασχεθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'κάτασχα'}, 'passive': {'κατασχόμουν'}},
             'pass_pres_participle': {'κατασχόμενος/κατασχόμενη/κατασχόμενο'},
             'passive_aorist_participle': {'κατασχεθείς/κατασχεθείσα/κατασχεθέν'},
             'passive_perfect_participle': {'κατασχεμένος/κατασχεμένη/κατασχεμένο'},
             'present': {'active': {'κατάσχω'}, 'passive': {'κατάσχομαι'}}},

        )

    def test_verb_antikathistw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('αντικαθιστώ'),
            {'present': {'active': {'αντικαθιστώ'}, 'passive': {'αντικαθίσταμαι'}},
             'conjunctive': {'active': {'αντικαταστήσω'}, 'passive': {'αντικαταστώ'}},

             'passive_aorist_participle': {'αντικαταστάς/αντικαταστάσα/αντικαταστάν'},
             'pres_conjugation': 'con2ak_act',

             'aorist': {'active': {'αντικατέστησα'}, 'passive': {'αντικατέστη', 'αντικατάστηκα'}},
             'paratatikos': {'active': {'αντικαθιστούσα'}, 'passive': {'αντικαθιστάμην'}},
             'act_pres_participle': {'αντικαθιστώντας'},
             'pass_pres_participle': {'αντικαθιστάμενος/αντικαθιστάμενη/αντικαθιστάμενο'},
             'passive_perfect_participle': {'αντικαταστισμένος/αντικαταστισμένη/αντικαταστισμένο',
                                            'αντικατεστημένος/αντικατεστημένη/αντικατεστημένο'},
             'modal': False},

        )

    def test_verb_anastainw(self):
        self.assertDictEqual(
            basic_verb('ανασταίνω'),
            {'present': {'active': {'ανασταίνω'}, 'passive': {'ανασταίνομαι'}},
             'conjunctive': {'active': {'αναστήσω'}},
             'aorist': {'active': {'ανάστησα', 'ανέστησα'}},
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'ανέσταινα', 'ανάσταινα'},
                             'passive': {'ανασταινόμουν'}},
             'act_pres_participle': {'ανασταίνοντας'},
             'passive_perfect_participle': {'αναστημένος/αναστημένη/αναστημένο'},
             'active_aorist_participle': {'αναστήσας/αναστήσασα/αναστήσαν'}, 'modal': False},

        )

    def test_verb_ago(self):
        self.assertDictEqual(
            basic_verb('άγω'),
            {'present': {'active': {'άγω'}, 'passive': {'άγομαι'}},
             'conjunctive': {'active': {'αγάγω'}, 'passive': {'αχθώ'}},
             'aorist': {'active': {'ήγαγα'}, 'passive': {'ήχθη', 'άχθηκα'}},
             'paratatikos': {'active': {'ήγα'}, 'passive': {'αγόμουν'}},
             'passive_perfect_participle': {'ηγμένος/ηγμένη/ηγμένο'},
             'pres_conjugation': 'con1_act',

             'act_pres_participle': {'άγοντας'},
             'arch_act_pres_participle': {'άγων/άγουσα/άγον'},
             'pass_pres_participle': {'αγόμενος/αγόμενη/αγόμενο'}, 'modal': False},

        )

    def test_verb_elegxw(self):
        self.assertDictEqual(
            basic_verb('ελέγχω'),
            {'act_pres_participle': {'ελέγχοντας'},
             'aorist': {'active': {'έλεγξα'}, 'passive': {'ελέγχτηκα', 'ελέγχθηκα'}},
             'arch_act_pres_participle': {'ελέγχων/ελέγχουσα/ελέγχον'},
             'conjunctive': {'active': {'ελέγξω'}, 'passive': {'ελεγχθώ', 'ελεγχτώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'έλεγχα'}, 'passive': {'ελεγχόμουν'}},
             'pass_pres_participle': {'ελεγχόμενος/ελεγχόμενη/ελεγχόμενο'},
             'passive_aorist_participle': {'ελεγχθείς/ελεγχθείσα/ελεγχθέν'},
             'passive_perfect_participle': {'ελεγμένος/ελεγμένη/ελεγμένο'},
             'present': {'active': {'ελέγχω'}, 'passive': {'ελέγχομαι'}}}

        )

    def test_verb_apolambano(self):
        self.assertDictEqual(
            basic_verb('απολαμβάνω'),
            {'present': {'active': {'απολαμβάνω'}},
             'pres_conjugation': 'con1_act',

             'conjunctive': {'active': {'απολαύσω'}},
             'aorist': {'active': {'απόλαυσα'}}, 'paratatikos': {'active': {'απολάμβανα'}},
             'act_pres_participle': {'απολαμβάνοντας'}, 'modal': False},

        )

    def test_verb_memfomai(self):
        self.assertDictEqual(
            basic_verb('μέμφομαι'),
            {'present': {'passive': {'μέμφομαι'}},
             'pres_conjugation': 'con1_pass',
             'conjunctive': {'passive': {'μεμφτώ', 'μεμφθώ'}},
             'aorist': {'passive': {'μέμφθηκα', 'μέμφτηκα'}},
             'paratatikos': {'passive': {'μεμφόμουν'}},
             'pass_pres_participle': {'μεμφόμενος/μεμφόμενη/μεμφόμενο'},
             'modal': False},

        )

    def test_verb_katalabainw(self):
        self.assertDictEqual(
            basic_verb('καταλαβαίνω'),
            {'present': {'active': {'καταλαβαίνω'}, 'passive': {'καταλαβαίνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}},
             'pres_conjugation': 'con1_act',
             'aorist': {'active': {'κατάλαβα'}},
             'paratatikos': {'active': {'καταλάβαινα'}, 'passive': {'καταλαβαινόμουν'}},
             'act_pres_participle': {'καταλαβαίνοντας'}, 'modal': False},

        )

    def test_verb_katalambanw(self):
        self.assertDictEqual(
            basic_verb('καταλαμβάνω'),
            {'present': {'active': {'καταλαμβάνω'}, 'passive': {'καταλαμβάνομαι'}},
             'conjunctive': {'active': {'καταλάβω'}, 'passive': {'καταληφθώ'}},
             'pres_conjugation': 'con1_act',

             'aorist': {'active': {'κατέλαβα'}, 'passive': {'καταλήφθηκα', 'κατελήφθη'}},
             'paratatikos': {'active': {'καταλάμβανα', 'κατελάμβανα'},
                             'passive': {'καταλαμβανόμουν'}},
             'act_pres_participle': {'καταλαμβάνοντας'},
             'pass_pres_participle': {'καταλαμβανόμενος/καταλαμβανόμενη/καταλαμβανόμενο'},
             'passive_aorist_participle': {'καταληφθείς/καταληφθείσα/καταληφθέν'},
             'passive_perfect_participle': {'κατειλημμένος/κατειλημμένη/κατειλημμένο'},
             'modal': False},

        )

    def test_verb_auksanw(self):
        self.assertDictEqual(
            basic_verb('αυξάνω'),
            {'act_pres_participle': {'αυξάνοντας'},
             'aorist': {'active': {'αύξησα'}, 'passive': {'αυξήθηκα'}},
             'arch_act_pres_participle': {'αυξάνων/αυξάνουσα/αυξάνον'},
             'conjunctive': {'active': {'αυξήσω'}, 'passive': {'αυξηθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'αύξανα'}, 'passive': {'αυξανόμουν'}},
             'pass_pres_participle': {'αυξανόμενος/αυξανόμενη/αυξανόμενο'},
             'passive_perfect_participle': {'αυξημένος/αυξημένη/αυξημένο',
                                            'ηυξημένος/ηυξημένη/ηυξημένο'},
             'present': {'active': {'αυξάνω'}, 'passive': {'αυξάνομαι'}}}

        )

    def test_verb_antilambanomai(self):
        self.assertDictEqual(
            basic_verb('αντιλαμβάνομαι'),
            {'present': {'passive': {'αντιλαμβάνομαι'}}, 'conjunctive': {'passive': {'αντιληφθώ'}},
             'aorist': {'passive': {'αντιλήφθηκα', 'αντελήφθη'}},
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'αντιλαμβανόμουν'}},
             'pass_pres_participle': {'αντιλαμβανόμενος/αντιλαμβανόμενη/αντιλαμβανόμενο'},
             'passive_aorist_participle': {'αντιληφθείς/αντιληφθείσα/αντιληφθέν'},
             'modal': False},

        )

    def test_verb_symponw(self):
        self.assertDictEqual(
            basic_verb('συμπονώ'),
            {'present': {'active': {'συμπονώ'}, 'passive': {'συμπονούμαι', 'συμπονιέμαι'}},
             'conjunctive': {'active': {'συμπονέσω'}, 'passive': {'συμπονηθώ'}},
             'aorist': {'active': {'συμπόνεσα'}, 'passive': {'συμπονήθηκα'}},
             'paratatikos': {'active': {'συμπόναγα', 'συμπονούσα'}, 'passive': {'συμπονιόμουν'}},
             'act_pres_participle': {'συμπονώντας'},
             'pres_conjugation': 'con2a_act',

             'passive_aorist_participle': {'συμπονηθείς/συμπονηθείσα/συμπονηθέν'}, 'modal': False},

        )

    def test_verb_synkrinw(self):
        self.assertDictEqual(
            basic_verb('συγκρίνω'),
            {'present': {'active': {'συγκρίνω'}, 'passive': {'συγκρίνομαι'}},
             'conjunctive': {'active': {'συγκρίνω'}, 'passive': {'συγκριθώ'}},
             'pres_conjugation': 'con1_act',
             'aorist': {'active': {'συνέκρινα', 'σύγκρινα'}, 'passive': {'συγκρίθηκα'}},
             'paratatikos': {'active': {'σύγκρινα', 'συνέκρινα'}, 'passive': {'συγκρινόμουν'}},
             'act_pres_participle': {'συγκρίνοντας'},
             'pass_pres_participle': {'συγκρινόμενος/συγκρινόμενη/συγκρινόμενο'},
             'passive_perfect_participle': {'συγκριμένος/συγκριμένη/συγκριμένο',
                                            'συγκεκριμένος/συγκεκριμένη/συγκεκριμένο'},
             'modal': False},

        )

    def test_verb_syntribw(self):
        self.assertDictEqual(
            basic_verb('συντρίβω'),
            {'present': {'active': {'συντρίβω'}, 'passive': {'συντρίβομαι'}},
             'conjunctive': {'active': {'συντρίψω'}, 'passive': {'συντριφτώ', 'συντριβώ'}},
             'aorist': {'active': {'συνέτριψα', 'σύντριψα'}, 'passive': {'συνετρίβη', 'συντρίβηκα', 'συντρίφτηκα'}},
             'paratatikos': {'active': {'συνέτριβα'}, 'passive': {'συντριβόμουν'}},
             'act_pres_participle': {'συντρίβοντας'},
             'passive_perfect_participle': {'συντετριμμένος/συντετριμμένη/συντετριμμένο',
                                            'συντριμμένος/συντριμμένη/συντριμμένο'},
             'pres_conjugation': 'con1_act',
             'modal': False},

        )

    def test_verb_xairw(self):
        self.assertDictEqual(
            basic_verb('χαίρω'),
            {'act_pres_participle': {'χαίροντας'},
             'aorist': {'passive': {'χάρηκα'}},
             'arch_act_pres_participle': {'χαίρων/χαίρουσα/χαίρον'},
             'conjunctive': {'passive': {'χαρώ'}},
             'pres_conjugation': 'con1_act',

             'modal': False,
             'paratatikos': {'active': {'έχαιρα'}, 'passive': {'χαιρόμουν'}},
             'pass_pres_participle': {'χαρούμενος/χαρούμενη/χαρούμενο'},
             'present': {'active': {'χαίρω'}, 'passive': {'χαίρομαι'}}}

        )

    def test_verb_parkaro(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('παρκάρω'),
            {'present': {'active': {'παρκάρω'}, 'passive': {'παρκάρομαι'}},
             'conjunctive': {'active': {'παρκαρίσω', 'παρκάρω'}, 'passive': {'παρκαριστώ'}},
             'aorist': {'active': {'πάρκαρα', 'παρκάρισα'}, 'passive': {'παρκαρίστηκα'}},
             'paratatikos': {'active': {'πάρκαρα', 'παρκάριζα'}, 'passive': {'παρκαρόμουν'}},
             'act_pres_participle': {'παρκάροντας'},
             'pres_conjugation': 'con1_act',
             'passive_perfect_participle': {'παρκαρισμένος/παρκαρισμένη/παρκαρισμένο'},
             'modal': False},

        )

    def test_verb_sokarw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('σοκάρω'),
            {'act_pres_participle': {'σοκάροντας'},
             'aorist': {'active': {'σόκαρα', 'σοκάρισα'},
                        'passive': {'σοκαρίστηκα', 'σοκαρίσθηκα'}},
             'conjunctive': {'active': {'σοκάρω', 'σοκαρίσω'},
                             'passive': {'σοκαριστώ', 'σοκαρισθώ'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'σόκαρα', 'σοκάριζα'},
                             'passive': {'σοκαρόμουν', 'σοκαριζόμουν'}},
             'passive_aorist_participle': {'σοκαρισθείς/σοκαρισθείσα/σοκαρισθέν'},
             'passive_perfect_participle': {'σοκαρισμένος/σοκαρισμένη/σοκαρισμένο'},
             'present': {'active': {'σοκάρω', 'σοκαρίζω'},
                         'passive': {'σοκαρίζομαι', 'σοκάρομαι'}}}

        )

    def test_verb_epanalambanw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('αναλαμβάνω'),
            {'present': {'active': {'αναλαμβάνω'}, 'passive': {'αναλαμβάνομαι'}},
             'conjunctive': {'active': {'αναλάβω'}, 'passive': {'αναληφθώ'}},
             'aorist': {'active': {'ανάλαβα', 'ανέλαβα'}, 'passive': {'ανελήφθη', 'αναλήφθηκα'}},
             'paratatikos': {'active': {'αναλάμβανα', 'ανελάμβανα'}, 'passive': {'αναλαμβανόμουν'}},
             'act_pres_participle': {'αναλαμβάνοντας'},
             'pass_pres_participle': {'αναλαμβανόμενος/αναλαμβανόμενη/αναλαμβανόμενο'},
             'passive_aorist_participle': {'αναληφθείς/αναληφθείσα/αναληφθέν'},
             'arch_act_pres_participle': {'αναλαμβάνων/αναλαμβάνουσα/αναλαμβάνον'},
             'pres_conjugation': 'con1_act',
             'passive_perfect_participle': {'ανειλημμένος/ανειλημμένη/ανειλημμένο'},
             'modal': False},

        )

    def test_verb_proteinw(self):
        self.assertDictEqual(
            basic_verb('επιτίθεμαι'),
            {'present': {'passive': {'επιτίθεμαι'}}, 'conjunctive': {'passive': {'επιτεθώ'}},
             'aorist': {'passive': {'επιτέθηκα', 'επετέθη'}},
             'pres_conjugation': 'con2d_pass',
             'paratatikos': {'passive': {'επιτιθέμην'}},
             'pass_pres_participle': {'επιτιθέμενος/επιτιθέμενη/επιτιθέμενο'},
             'passive_perfect_participle': {'επιτεθειμένος/επιτεθειμένη/επιτεθειμένο'},
             'passive_aorist_participle': {'επιτεθείς/επιτεθείσα/επιτεθέν'}, 'modal': False},

        )

    def test_verb_diaftheirw(self):
        self.maxDiff = None
        self.assertDictEqual(

            basic_verb('διαφθείρω'),
            {'present': {'active': {'διαφθείρω'}, 'passive': {'διαφθείρομαι'}},
             'conjunctive': {'active': {'διαφθείρω'}, 'passive': {'διαφθαρώ'}},
             'aorist': {'active': {'διέφθειρα'}, 'passive': {'διαφθάρηκα', 'διεφθάρη'}},
             'paratatikos': {'active': {'διέφθειρα'}, 'passive': {'διαφθειρόμουν'}},
             'act_pres_participle': {'διαφθείροντας'},
             'pres_conjugation': 'con1_act',

             'pass_pres_participle': {'διαφθειρόμενος/διαφθειρόμενη/διαφθειρόμενο'},
             'passive_perfect_participle': {'διεφθαρμένος/διεφθαρμένη/διεφθαρμένο',
                                            'διαφθαρμένος/διαφθαρμένη/διαφθαρμένο'},
             'passive_aorist_participle': {'διαφθαρείς/διαφθαρείσα/διαφθαρέν'}, 'modal': False},

        )

    def test_verb_vazo(self):
        self.assertDictEqual(
            basic_verb('βάζω'),
            {'present': {'active': {'βάζω'}},
             'conjunctive': {'active': {'βάλω'}, 'passive': {'βαλθώ'}},
             'pres_conjugation': 'con1_act',
             'aorist': {'active': {'έβαλα'}, 'passive': {'βάλθηκα'}},
             'paratatikos': {'active': {'έβαζα'}},
             'act_pres_participle': {'βάζοντας'},
             'passive_perfect_participle': {'βαλμένος/βαλμένη/βαλμένο'},
             'active_aorist_participle': {'βαλών/βαλούσα/βαλόν'}, 'modal': False},

        )

    def test_verb_ανebazw(self):
        self.assertDictEqual(
            basic_verb('ανεβάζω'),
            {'present': {'active': {'ανεβάζω'},
                         'passive': {'ανεβάζομαι'}},
             'pres_conjugation': 'con1_act',

             'conjunctive': {'active': {'ανεβάσω'}, 'passive': {'ανεβαστώ'}},
             'aorist': {'active': {'ανέβασα'}, 'passive': {'ανεβάστηκα'}},
             'paratatikos': {'active': {'ανέβαζα'}, 'passive': {'ανεβαζόμουν'}},
             'act_pres_participle': {'ανεβάζοντας'},
             'passive_perfect_participle': {'ανεβασμένος/ανεβασμένη/ανεβασμένο'},
             'modal': False},

        )

    def test_verb_katexo(self):
        self.assertDictEqual(
            basic_verb('κατέχω'),
            {'act_pres_participle': {'κατέχοντας'},
             'aorist': {'active': {'κατείχα'}},
             'arch_act_pres_participle': {'κατέχων/κατέχουσα/κατέχον'},
             'conjunctive': {'active': {'κατάσχω', 'κατέχω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'κάτεχα', 'κατείχα'}, 'passive': {'κατεχόμουν'}},
             'pass_pres_participle': {'κατεχόμενος/κατεχόμενη/κατεχόμενο'},
             'present': {'active': {'κατέχω'}, 'passive': {'κατέχομαι'}}},

        )

    def test_verb_krossaro(self):
        self.assertDictEqual(
            basic_verb('κροσσάρω'),
            {'present': {'active': {'κροσσάρω'}},
             'pres_conjugation': 'con1_act',

             'conjunctive': {'active': {'κροσσαρίσω', 'κροσσάρω'}},
             'aorist': {'active': {'κροσσάρισα', 'κρόσσαρα'}}, 'paratatikos': {'active': {'κρόσσαρα'}},
             'act_pres_participle': {'κροσσάροντας'}, 'modal': False},

        )

    def test_verb_apantexw(self):
        self.assertDictEqual(
            basic_verb('απαντέχω'),
            {'act_pres_participle': {'απαντέχοντας'},
             'aorist': {},
             'conjunctive': {},
             'pres_conjugation': 'con1_act',

             'modal': False,
             'paratatikos': {'active': {'απάντεχα'}},
             'present': {'active': {'απαντέχω'}}},

        )

    def test_verb_spaw(self):
        self.assertDictEqual(
            basic_verb('σπάω'),
            {'present': {'active': {'σπάω'}},
             'conjunctive': {'active': {'σπάσω'}, 'passive': {'σπαστώ', 'σπασθώ'}},
             'aorist': {'active': {'έσπασα'}, 'passive': {'σπάσθηκα', 'σπάστηκα'}},
             'paratatikos': {'active': {'έσπαγα'}}, 'pres_conjugation': 'con2c_act',
             'act_pres_participle': {'σπάγοντας'},
             'passive_perfect_participle': {'σπασμένος/σπασμένη/σπασμένο'}, 'modal': False},

        )

    def test_verb_pempw(self):
        self.assertDictEqual(
            basic_verb('πέμπω'),
            {'present': {'active': {'πέμπω'}, 'passive': {'πέμπομαι'}},
             'conjunctive': {'active': {'πέμψω'}, 'passive': {'πεμφθώ'}},
             'aorist': {'active': {'έπεμψα'}, 'passive': {'πέμφθηκα'}},
             'paratatikos': {'active': {'έπεμπα'}, 'passive': {'πεμπόμουν'}},
             'pres_conjugation': 'con1_act',
             'act_pres_participle': {'πέμποντας'},
             'modal': False},

        )

    def test_verb_sfinggw(self):
        self.assertDictEqual(
            basic_verb('σφίγγω'),

            {'present': {'active': {'σφίγγω'}, 'passive': {'σφίγγομαι'}},
             'conjunctive': {'active': {'σφίξω'}, 'passive': {'σφιχτώ'}},
             'aorist': {'active': {'έσφιξα'}, 'passive': {'σφίχτηκα'}},
             'pres_conjugation': 'con1_act',
             'paratatikos': {'active': {'έσφιγγα'}, 'passive': {'σφιγγόμουν'}},
             'act_pres_participle': {'σφίγγοντας'},
             'passive_perfect_participle': {'σφιγμένος/σφιγμένη/σφιγμένο'},
             'modal': False},

        )

    def test_verb_eggrafw(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('εγγράφω'),
            {'act_pres_participle': {'εγγράφοντας'},
             'active_aorist_participle': {'εγγράψας/εγγράψασα/εγγράψαν'},
             'aorist': {'active': {'ενέγραψα'},
                        'passive': {'ενεγράφη', 'εγγράφηκα', 'εγγράφτηκα'}},
             'arch_act_pres_participle': {'εγγράφων/εγγράφουσα/εγγράφον'},
             'conjunctive': {'active': {'εγγράψω'}, 'passive': {'εγγραφτώ', 'εγγραφώ'}},
             'modal': False,
             'paratatikos': {'active': {'ενέγραφα', 'έγγραφα'}, 'passive': {'εγγραφόμουν'}},
             'pass_pres_participle': {'εγγραφόμενος/εγγραφόμενη/εγγραφόμενο'},
             'pres_conjugation': 'con1_act',
             'passive_aorist_participle': {'εγγραφείς/εγγραφείσα/εγγραφέν'},
             'passive_perfect_participle': {'εγγραμμένος/εγγραμμένη/εγγραμμένο',
                                            'εγγεγραμμένος/εγγεγραμμένη/εγγεγραμμένο'},
             'present': {'active': {'εγγράφω'}, 'passive': {'εγγράφομαι'}}}

        )

    def test_verb_syggrafo(self):
        self.maxDiff = None
        self.assertDictEqual(
            basic_verb('συγγράφω'),
            {'present': {'active': {'συγγράφω'}, 'passive': {'συγγράφομαι'}},
             'conjunctive': {'active': {'συγγράψω'}, 'passive': {'συγγραφτώ', 'συγγραφώ'}},
             'aorist': {'active': {'συνέγραψα'}, 'passive': {'συνεγράφη', 'συγγράφηκα', 'συγγράφτηκα'}},
             'paratatikos': {'active': {'συνέγραφα'}, 'passive': {'συγγραφόμουν'}},
             'arch_act_pres_participle': {'συγγράφων/συγγράφουσα/συγγράφον'},
             'pres_conjugation': 'con1_act',

             'act_pres_participle': {'συγγράφοντας'},
             'pass_pres_participle': {'συγγραφόμενος/συγγραφόμενη/συγγραφόμενο'},
             'passive_perfect_participle': {'συγγεγραμμένος/συγγεγραμμένη/συγγεγραμμένο'},
             'active_aorist_participle': {'συγγράψας/συγγράψασα/συγγράψαν'}, 'modal': False},

        )

    def test_verb_fylaw(self):
        self.assertDictEqual(
            basic_verb('φυλάω'),
            {'present': {'active': {'φυλάω'}},
             'pres_conjugation': 'con2a_act',
             'conjunctive': {'active': {'φυλάξω'}},
             'aorist': {'active': {'εφύλαξα', 'φύλαξα'}},
             'paratatikos': {'active': {'φυλούσα', 'φύλαγα'}},
             'act_pres_participle': {'φυλώντας'},
             'passive_perfect_participle': {'φυλαγμένος/φυλαγμένη/φυλαγμένο'}, 'modal': False},

        )

    def test_verb_paw(self):
        self.assertDictEqual(
            basic_verb('πάω'),
            {'present': {'active': {'πάω'}},
             'pres_conjugation': 'con2c_act',
             'conjunctive': {'active': {'πάω'}},
             'aorist': {'active': {'πήγα'}},
             'paratatikos': {'active': {'πήγαινα'}}, 'modal': False},

        )

    def test_verb_kanw(self):
        self.assertDictEqual(
            basic_verb('κάνω'),
            {'present': {'active': {'κάνω'}},
             'pres_conjugation': 'con1_act',

             'conjunctive': {'active': {'κάνω'}},
             'aorist': {'active': {'έκανα'}},
             'paratatikos': {'active': {'έκανα'}}, 'act_pres_participle': {'κάνοντας'},
             'passive_perfect_participle': {'καμωμένος/καμωμένη/καμωμένο'},
             'modal': False},

        )

    def test_verb_kaiw(self):
        self.assertDictEqual(
            basic_verb('καίω'),
            {'present': {'active': {'καίω'}, 'passive': {'καίγομαι'}},
             'conjunctive': {'active': {'κάψω'}, 'passive': {'καώ'}},
             'aorist': {'active': {'έκαψα'}, 'passive': {'κάηκα'}},
             'paratatikos': {'active': {'έκαιγα'}, 'passive': {'καιγόμουν'}},
             'act_pres_participle': {'καίγοντας'},
             'pass_pres_participle': {'καιγόμενος/καιγόμενη/καιγόμενο'},
             'pres_conjugation': 'con2c_act',

             'passive_perfect_participle': {'καμένος/καμένη/καμένο',
                                            'κεκαυμένος/κεκαυμένη/κεκαυμένο',
                                            'κεκαμμένος/κεκαμμένη/κεκαμμένο'}, 'modal': False},

        )

    def test_verb_agapao(self):
        self.assertDictEqual(
            basic_verb('αγαπάω'),
            {'present': {'active': {'αγαπάω'}, 'passive': {'αγαπώμαι', 'αγαπιέμαι'}},
             'conjunctive': {'active': {'αγαπήσω'}, 'passive': {'αγαπηθώ'}},
             'aorist': {'active': {'αγάπησα'}, 'passive': {'αγαπήθηκα'}},
             'paratatikos': {'active': {'αγαπούσα', 'αγάπαγα'}, 'passive': {'αγαπιόμουν'}},
             'act_pres_participle': {'αγαπώντας'},
             'arch_act_pres_participle': {'αγαπών/αγαπούσα/αγαπών'},
             'passive_perfect_participle': {'αγαπημένος/αγαπημένη/αγαπημένο'},
             'pres_conjugation': 'con2a_act',

             'passive_aorist_participle': {'αγαπηθείς/αγαπηθείσα/αγαπηθέν'}, 'modal': False},

        )

    def test_verb_epembenw(self):
        self.assertDictEqual(
            basic_verb('επεμβαίνω'),
            {'act_pres_participle': {'επεμβαίνοντας'},
             'aorist': {'active': {'επέμβηκα', 'επεμβήκα', 'επενέβη'}},
             'active_aorist_participle': {'επεμβάς/επεμβάσα/επεμβάν'},
             'arch_act_pres_participle': {'επεμβαίνων/επεμβαίνουσα/επεμβαίνον'},
             'conjunctive': {'active': {'επέμβω'}},
             'modal': False,
             'pres_conjugation': 'con1_act',

             'paratatikos': {'active': {'επενέβαινα'}, 'passive': {'επεμβαινόμουν'}},
             'present': {'active': {'επεμβαίνω'}, 'passive': {'επεμβαίνομαι'}}}

        )

    def test_verb_kylaw(self):
        self.assertDictEqual(
            basic_verb('κυλάω'),
            {'present': {'active': {'κυλάω'}, 'passive': {'κυλιέμαι'}},
             'conjunctive': {'active': {'κυλήσω'}, 'passive': {'κυλιστώ'}},
             'aorist': {'active': {'κύλησα'}, 'passive': {'κυλίστηκα'}},
             'pres_conjugation': 'con2a_act',

             'paratatikos': {'active': {'κύλαγα', 'κυλούσα'}, 'passive': {'κυλιόμουν'}},
             'act_pres_participle': {'κυλώντας'},
             'passive_perfect_participle': {'κυλισμένος/κυλισμένη/κυλισμένο'}, 'modal': False},

        )

    def test_verb_anexomai(self):
        self.assertDictEqual(
            basic_verb('ανέχομαι'),
            {'present': {'passive': {'ανέχομαι'}},
             'pres_conjugation': 'con1_pass',

             'conjunctive': {'passive': {'ανεχτώ', 'ανεχθώ'}},
             'aorist': {'passive': {'ανέχθηκα', 'ανέχτηκα'}},
             'paratatikos': {'passive': {'ανεχόμουν'}},
             'pass_pres_participle': {'ανεχόμενος/ανεχόμενη/ανεχόμενο'}, 'modal': False},

        )

    def test_verb_anago(self):
        self.assertDictEqual(
            basic_verb('ανάγω'),
            {'present': {'active': {'ανάγω'}, 'passive': {'ανάγομαι'}},
             'conjunctive': {'active': {'αναγάγω'}, 'passive': {'αναχθώ'}},
             'aorist': {'active': {'ανήγαγα'}, 'passive': {'ανήχθη', 'ανάχθηκα'}},
             'paratatikos': {'active': {'ανήγα'}, 'passive': {'αναγόμουν'}},
             'pres_conjugation': 'con1_act',

             'act_pres_participle': {'ανάγοντας'},
             'arch_act_pres_participle': {'ανάγων/ανάγουσα/ανάγον'},
             'pass_pres_participle': {'αναγόμενος/αναγόμενη/αναγόμενο'},
             'passive_perfect_participle': {'ανηγμένος/ανηγμένη/ανηγμένο'},
             'passive_aorist_participle': {'αναχθείς/αναχθείσα/αναχθέν'},
             'modal': False},

        )

    def test_verb_apago(self):
        self.assertDictEqual(
            basic_verb('απάγω'),
            {'present': {'active': {'απάγω'}, 'passive': {'απάγομαι'}},
             'conjunctive': {'active': {'απαγάγω'}, 'passive': {'απαχθώ'}},
             'aorist': {'active': {'απήγαγα'}, 'passive': {'απήχθη', 'απάχθηκα'}},
             'paratatikos': {'active': {'απήγα'}, 'passive': {'απαγόμουν'}},
             'act_pres_participle': {'απάγοντας'},
             'pass_pres_participle': {'απαγόμενος/απαγόμενη/απαγόμενο'},
             'passive_aorist_participle': {'απαχθείς/απαχθείσα/απαχθέν'},
             'passive_perfect_participle': {'απαγμένος/απαγμένη/απαγμένο'},
             'pres_conjugation': 'con1_act',

             'modal': False},

        )

    def test_verb_diagrafomai(self):
        self.assertDictEqual(
            basic_verb('διαγράφομαι'),
            {'aorist': {'passive': {'διαγράφτηκα', 'διεγράφη', 'διαγράφηκα'}},
             'conjunctive': {'passive': {'διαγραφώ', 'διαγραφτώ'}},
             'modal': False,
             'pres_conjugation': 'con1_pass',

             'paratatikos': {'passive': {'διαγραφόμουν'}},
             'pass_pres_participle': {'διαγραφόμενος/διαγραφόμενη/διαγραφόμενο'},
             'passive_aorist_participle': {'διαγραφείς/διαγραφείσα/διαγραφέν'},
             'passive_perfect_participle': {'διαγεγραμμένος/διαγεγραμμένη/διαγεγραμμένο',
                                            'διαγραμμένος/διαγραμμένη/διαγραμμένο'},
             'present': {'passive': {'διαγράφομαι'}}}

        )

    def test_verb_thelw(self):
        self.assertDictEqual(
            basic_verb('θέλω'),
            {'present': {'active': {'θέλω'}},
             'conjunctive': {'active': {'θελήσω'}},
             'aorist': {'active': {'θέλησα'}},
             'paratatikos': {'active': {'ήθελα'}},
             'act_pres_participle': {'θέλοντας'},
             'pres_conjugation': 'con1_act',
             'arch_act_pres_participle': {'θέλων/θέλουσα/θέλον'},
             'passive_perfect_participle': {'θελημένος/θελημένη/θελημένο'},
             'modal': False},

        )

    def test_verb_dinw(self):
        self.assertDictEqual(
            basic_verb('δίνω'),
            {'present': {'active': {'δίνω'}, 'passive': {'δίνομαι'}},
             'conjunctive': {'active': {'δώσω'}, 'passive': {'δοθώ'}},
             'aorist': {'active': {'έδωσα'}, 'passive': {'εδόθη', 'δόθηκα'}},
             'paratatikos': {'active': {'έδινα'}, 'passive': {'δινόμουν'}},
             'pres_conjugation': 'con1_act',
             'act_pres_participle': {'δίνοντας'},
             'passive_perfect_participle': {'δοσμένος/δοσμένη/δοσμένο',
                                            'δεδομένος/δεδομένη/δεδομένο'},
             'passive_aorist_participle': {'δοθείς/δοθείσα/δοθέν'}, 'modal': False},

        )
