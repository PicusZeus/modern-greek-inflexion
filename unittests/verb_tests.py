from unittest import TestCase, main

from modern_greek_inflexion.verb import verb

res = verb.create_basic_forms('γίνομαι')
print(res)
class VerbTestBasic(TestCase):
    def test_verb_tragoudo(self):
        self.assertEqual(
            verb.create_basic_forms('τραγουδώ'),
            {'present': {'active': {'τραγουδώ'}, 'passive': {'τραγουδιέμαι'}},
             'conjunctive': {'active': {'τραγουδήσω'}, 'passive': {'τραγουδηθώ'}},
             'aorist': {'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}},
             'paratatikos': {'active': {'τραγουδούσα', 'τραγούδαγα'}, 'passive': {'τραγουδιόμουν'}},
             'act_pres_participle': {'τραγουδώντας'}, 'passive_perfect_participle': {'τραγουδημένος'}}

        )

    def test_verb_kyberno(self):
        self.assertEqual(
            verb.create_basic_forms('κυβερνώ'),
            {'present': {'active': {'κυβερνώ'}, 'passive': {'κυβερνώμαι', 'κυβερνιέμαι', 'κυβερνούμαι'}},
             'conjunctive': {'active': {'κυβερνήσω'}, 'passive': {'κυβερνηθώ'}},
             'aorist': {'active': {'κυβέρνησα'}, 'passive': {'κυβερνήθηκα'}},
             'paratatikos': {'active': {'κυβέρναγα', 'κυβερνούσα'}, 'passive': {'κυβερνιόμουν'}},
             'act_pres_participle': {'κυβερνώντας'}, 'arch_act_pres_participle': {'κυβερνών/κυβερνώσα/κυβερνών'},
             'pass_pres_participle': {'κυβερνώμενος'}, 'passive_perfect_participle': {'κυβερνημένος'}}
        )

    def test_verb_douleuo(self):
        self.assertEqual(
            verb.create_basic_forms('δουλεύω'),
            {'present': {'active': {'δουλεύω'}, 'passive': {'δουλεύομαι'}},
             'conjunctive': {'active': {'δουλεύσω', 'δουλέψω'}, 'passive': {'δουλευτώ'}},
             'aorist': {'active': {'δούλεψα', 'δούλευσα'}, 'passive': {'δουλεύτηκα'}},
             'paratatikos': {'active': {'δούλευα'}, 'passive': {'δουλευόμουν'}}, 'act_pres_participle': {'δουλεύοντας'},
             'passive_perfect_participle': {'δεδουλευμένος', 'δουλευμένος'},
             'active_aorist_participle': {'δουλεύσας/δουλεύσασα/δουλεύσαν'}}
        )

    def test_verb_blepo(self):
        self.assertEqual(
            verb.create_basic_forms('βλέπω'),
            {'present': {'active': {'βλέπω'}, 'passive': {'βλέπομαι'}},
             'conjunctive': {'active': {'δω'}, 'passive': {'ιδωθώ'}},
             'aorist': {'active': {'είδα'}, 'passive': {'ειδώθηκα'}},
             'paratatikos': {'active': {'έβλεπα'}, 'passive': {'βλεπόμουν'}}, 'act_pres_participle': {'βλέποντας'},
             'arch_act_pres_participle': {'βλέπων/βλέπουσα/βλέπον'}, 'passive_perfect_participle': {'ιδωμένος'}}
        )

    def test_verb_syllambano(self):
        self.assertEqual(
            verb.create_basic_forms('συλλαμβάνω'),
            {'present': {'active': {'συλλαμβάνω'}, 'passive': {'συλλαμβάνομαι'}},
             'conjunctive': {'active': {'συλλάβω'}, 'passive': {'συλληφθώ'}},
             'aorist': {'active': {'συνέλαβα'}, 'passive': {'συνελήφθη'}},
             'paratatikos': {'active': {'συλλάμβανα', 'συνελάμβανα'}, 'passive': {'συλλαμβανόμουν'}},
             'act_pres_participle': {'συλλαμβάνοντας'}, 'pass_pres_participle': {'συλλαμβανόμενος'},
             'passive_aorist_participle': {'συλληφθείς/συλληφθείσα/συλληφθέν'}}
        )

    def test_verb_phgainvo(self):
        self.assertEqual(
            verb.create_basic_forms('πηγαίνω'),
            {'present': {'active': {'πηγαίνω'}}, 'conjunctive': {'active': {'πάω'}},
             'aorist': {'active': {'πήγα'}}, 'paratatikos': {'active': {'πήγαινα'}},
             'act_pres_participle': {'πηγαίνοντας'}}
        )

    def test_verb_nothing(self):
        self.assertEqual(
            verb.create_basic_forms(''),
            {
                'error': 'It is not a correct verb form. You have to input 1st person sg present in active voice if possible, or modal form in 3rd person sg, and your input is: '}
        )

    def test_verb_gibberish(self):
        self.assertEqual(
            verb.create_basic_forms('laksjdf'),
            {
                'error': 'It is not a correct verb form. You have to input 1st person sg present in active voice if possible, or modal form in 3rd person sg, and your input is: laksjdf'}

        )

    def test_verb_prokeitai(self):
        self.assertEqual(
            verb.create_basic_forms('πρόκειται'),
            {'present': {'passive': {'πρόκειται'}}, 'paratatikos': {'passive': {'επρόκειτο'}}}

        )

    def test_verb_erxomai(self):
        self.assertEqual(
            verb.create_basic_forms('έρχομαι'),
            {'present': {'passive': {'έρχομαι'}},
             'conjunctive': {'active': {'έλθω', 'έρθω'}},
             'aorist': {'active': {'ήλθα', 'ήρθα'}},
             'paratatikos': {'passive': {'ερχόμουν'}},
             'pass_pres_participle': {'ερχόμενος'}}

        )

    def test_verb_synerxomai(self):
        self.assertEqual(
            verb.create_basic_forms('συνέρχομαι'),
            {'present': {'passive': {'συνέρχομαι'}}, 'conjunctive': {'active': {'συνέλθω', 'συνέρθω'}},
             'aorist': {'active': {'συνήρθα', 'συνήλθα'}}, 'paratatikos': {'passive': {'συνερχόμουν'}},
             'pass_pres_participle': {'συνερχόμενος'}, 'active_aorist_participle': {'συνελθών/συνελθούσα/συνέλθον'}}

        )

    def test_verb_katebainw(self):
        self.assertEqual(
            verb.create_basic_forms('κατεβαίνω'),
            {'present': {'active': {'κατεβαίνω'}}, 'conjunctive': {'active': {'κατέβω', 'κατεβώ'}},
             'aorist': {'active': {'κατέβηκα', 'κατέβη'}}, 'paratatikos': {'active': {'κατέβαινα'}},
             'act_pres_participle': {'κατεβαίνοντας'}}

        )

if __name__ == "__main__":
    main()