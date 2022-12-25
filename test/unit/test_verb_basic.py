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
             'conjunctive': {'active': {'δουλεύσω', 'δουλέψω'}, 'passive': {'δουλευτώ'}},
             'aorist': {'active': {'δούλεψα', 'δούλευσα'}, 'passive': {'δουλεύτηκα'}},
             'paratatikos': {'active': {'δούλευα'}, 'passive': {'δουλευόμουν'}}, 'act_pres_participle': {'δουλεύοντας'},
             'passive_perfect_participle': {'δεδουλευμένος', 'δουλευμένος'},
             'active_aorist_participle': {'δουλεύσας/δουλεύσασα/δουλεύσαν'},
             'modal': False}
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

    def test_verb_krossaro(self):
        self.assertDictEqual(
            verb.create_basic_forms('κροσσάρω'),
            {'aorist': {'active': {'κρόσσαρα'}},
                 'conjunctive': {'active': {'κροσσάρω'}},
                 'modal': False,
                 'paratatikos': {'active': {'κρόσσαρα'}},
                 'present': {'active': {'κροσσάρω'}}}

        )



