from unittest import TestCase, main

from modern_greek_inflexion.verb import verb

res = verb.create_all_forms('μουζώνομαι')
print(res)

class VerbTestAll(TestCase):
    def test_verb_erxomai(self):
        self.assertEqual(
            verb.create_all_forms('έρχομαι'),
            {'present': {'passive': {'ind': {'sg': {'pri': {'έρχομαι'}, 'sec': {'έρχεσαι'}, 'ter': {'έρχεται'}},
                                             'pl': {'pri': {'ερχόμαστε'}, 'sec': {'έρχεστε', 'ερχόσαστε'},
                                                    'ter': {'έρχονται'}}}, 'imp': {'pl': {'sec': {'έρχεστε'}}}}},
             'conjunctive': {'active': {
                 'ind': {'sg': {'pri': {'έρθω', 'έλθω'}, 'sec': {'έλα', 'έρθεις', 'έλθεις'}, 'ter': {'έλθει', 'έρθει'}},
                         'pl': {'pri': {'έρθουμε', 'έλθουμε'}, 'sec': {'έρθετε', 'έλθετε', 'ελάτε'},
                                'ter': {'έρθουνε', 'έρθουν', 'έλθουν', 'έλθουνε'}}},
                 'imp': {'sg': {'sec': {'έλα', 'έρθεις', 'έλθεις'}}, 'pl': {'sec': {'έρθετε', 'έλθετε', 'ελάτε'}}}}},
             'aorist': {'active': {
                 'ind': {'sg': {'pri': {'ήρθα', 'ήλθα'}, 'sec': {'ήλθες', 'ήρθες'}, 'ter': {'ήλθε', 'ήρθε'}},
                         'pl': {'pri': {'ήλθαμε', 'ήρθαμε'}, 'sec': {'ήλθατε', 'ήρθατε'},
                                'ter': {'ήρθανε', 'ήρθαν', 'ήλθαν', 'ήλθανε'}}}}}, 'paratatikos': {'passive': {'ind': {
                'sg': {'pri': {'ερχόμουνα', 'ερχόμουν'}, 'sec': {'ερχόσουνα', 'ερχόσουν'},
                       'ter': {'ερχότανε', 'ερχόταν'}},
                'pl': {'pri': {'ερχόμαστε', 'ερχόμασταν'}, 'sec': {'ερχόσαστε', 'ερχόσασταν'},
                       'ter': {'ερχόντουσαν', 'έρχονταν'}}}}}, 'pass_pres_participle': {
                'sg': {'masc': {'gen': {'ερχόμενου'}, 'voc': {'ερχόμενε'}, 'nom': {'ερχόμενος'}, 'acc': {'ερχόμενο'}},
                       'fem': {'gen': {'ερχόμενης'}, 'voc': {'ερχόμενη'}, 'nom': {'ερχόμενη'}, 'acc': {'ερχόμενη'}},
                       'neut': {'gen': {'ερχόμενου'}, 'voc': {'ερχόμενο'}, 'nom': {'ερχόμενο'}, 'acc': {'ερχόμενο'}}},
                'pl': {
                    'masc': {'gen': {'ερχόμενων'}, 'voc': {'ερχόμενοι'}, 'nom': {'ερχόμενοι'}, 'acc': {'ερχόμενους'}},
                    'fem': {'gen': {'ερχόμενων'}, 'voc': {'ερχόμενες'}, 'nom': {'ερχόμενες'}, 'acc': {'ερχόμενες'}},
                    'neut': {'gen': {'ερχόμενων'}, 'voc': {'ερχόμενα'}, 'nom': {'ερχόμενα'}, 'acc': {'ερχόμενα'}}}}}
        )

    def test_verb_tragoudo(self):
        self.assertEqual(
            verb.create_all_forms('τραγουδώ'),
            {'present': {'active': {'ind': {
                'sg': {'pri': {'τραγουδώ', 'τραγουδάω'}, 'sec': {'τραγουδάς'}, 'ter': {'τραγουδά', 'τραγουδάει'}},
                'pl': {'pri': {'τραγουδάμε', 'τραγουδούμε'}, 'sec': {'τραγουδάτε'},
                       'ter': {'τραγουδάν', 'τραγουδούνε', 'τραγουδούν', 'τραγουδάνε'}}},
                                    'imp': {'sg': {'sec': {'τραγούδα', 'τραγούδαγε'}}, 'pl': {'sec': {'τραγουδάτε'}}}},
                         'passive': {
                             'ind': {'sg': {'pri': {'τραγουδιέμαι'}, 'sec': {'τραγουδιέσαι'}, 'ter': {'τραγουδιέται'}},
                                     'pl': {'pri': {'τραγουδιούμαστε', 'τραγουδιόμαστε'},
                                            'sec': {'τραγουδιόσαστε', 'τραγουδιέστε'},
                                            'ter': {'τραγουδιόνται', 'τραγουδιούνται'}}},
                             'imp': {'pl': {'sec': {'τραγουδιέστε'}}}}},
                'conjunctive': {'active': {
                'ind': {'sg': {'pri': {'τραγουδήσω'}, 'sec': {'τραγουδήσεις'}, 'ter': {'τραγουδήσει'}},
                        'pl': {'pri': {'τραγουδήσουμε'}, 'sec': {'τραγουδήσετε'},
                               'ter': {'τραγουδήσουν', 'τραγουδήσουνε'}}},
                'imp': {'sg': {'sec': {'τραγούδησε'}}, 'pl': {'sec': {'τραγουδήστε'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'τραγουδηθώ'}, 'sec': {'τραγουδηθείς'}, 'ter': {'τραγουδηθεί'}},
                        'pl': {'pri': {'τραγουδηθούμε'}, 'sec': {'τραγουδηθείτε'},
                               'ter': {'τραγουδηθούν', 'τραγουδηθούνε'}}},
                'imp': {'sg': {'sec': {'τραγουδήσου'}}, 'pl': {'sec': {'τραγουδηθείτε'}}}}},
                'aorist': {'active': {
                'ind': {'sg': {'pri': {'τραγούδησα'}, 'sec': {'τραγούδησες'}, 'ter': {'τραγούδησε'}},
                        'pl': {'pri': {'τραγουδήσαμε'}, 'sec': {'τραγουδήσατε'},
                               'ter': {'τραγούδησαν', 'τραγουδήσανε'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'τραγουδήθηκα'}, 'sec': {'τραγουδήθηκες'}, 'ter': {'τραγουδήθηκε'}},
                        'pl': {'pri': {'τραγουδηθήκαμε'}, 'sec': {'τραγουδηθήκατε'},
                               'ter': {'τραγουδηθήκανε', 'τραγουδήθηκαν'}}}}},
                'paratatikos': {'active': {'ind': {
                'sg': {'pri': {'τραγουδούσα', 'τραγούδαγα'}, 'sec': {'τραγούδαγες', 'τραγουδούσες'},
                       'ter': {'τραγουδούσε', 'τραγούδαγε'}},
                'pl': {'pri': {'τραγουδούσαμε', 'τραγουδάγαμε'}, 'sec': {'τραγουδάγατε', 'τραγουδούσατε'},
                       'ter': {'τραγουδούσανε', 'τραγούδαγαν', 'τραγουδούσαν', 'τραγουδάγανε'}}}}, 'passive': {'ind': {
                'sg': {'pri': {'τραγουδιόμουν', 'τραγουδιόμουνα'}, 'sec': {'τραγουδιόσουνα', 'τραγουδιόσουν'},
                       'ter': {'τραγουδιότανε', 'τραγουδιόταν'}},
                'pl': {'pri': {'τραγουδιόμασταν', 'τραγουδιόμαστε'}, 'sec': {'τραγουδιόσασταν', 'τραγουδιόσαστε'},
                       'ter': {'τραγουδιούνταν', 'τραγουδιόνταν', 'τραγουδιόντουσαν'}}}}},
             'act_pres_participle': {'τραγουδώντας'}, 'passive_perfect_participle': {'pl': {
                'neut': {'gen': {'τραγουδημένων'}, 'acc': {'τραγουδημένα'}, 'voc': {'τραγουδημένα'},
                         'nom': {'τραγουδημένα'}},
                'fem': {'gen': {'τραγουδημένων'}, 'acc': {'τραγουδημένες'}, 'voc': {'τραγουδημένες'},
                        'nom': {'τραγουδημένες'}},
                'masc': {'gen': {'τραγουδημένων'}, 'acc': {'τραγουδημένους'}, 'voc': {'τραγουδημένοι'},
                         'nom': {'τραγουδημένοι'}}}, 'sg': {
                'neut': {'gen': {'τραγουδημένου'}, 'acc': {'τραγουδημένο'}, 'voc': {'τραγουδημένο'},
                         'nom': {'τραγουδημένο'}},
                'fem': {'gen': {'τραγουδημένης'}, 'acc': {'τραγουδημένη'}, 'voc': {'τραγουδημένη'},
                        'nom': {'τραγουδημένη'}},
                'masc': {'gen': {'τραγουδημένου'}, 'acc': {'τραγουδημένο'}, 'voc': {'τραγουδημένε'},
                         'nom': {'τραγουδημένος'}}}}}
        )

    def test_verb_kybernw(self):
        # self.maxDiff = None
        self.assertEqual(
            verb.create_all_forms('κυβερνώ'),
            {'present': {'active': {
                'ind': {'sg': {'pri': {'κυβερνώ', 'κυβερνάω'}, 'sec': {'κυβερνάς'}, 'ter': {'κυβερνάει', 'κυβερνά'}},
                        'pl': {'pri': {'κυβερνούμε', 'κυβερνάμε'}, 'sec': {'κυβερνάτε'},
                               'ter': {'κυβερνάν', 'κυβερνούν', 'κυβερνάνε', 'κυβερνούνε'}}},
                'imp': {'sg': {'sec': {'κυβέρναγε', 'κυβέρνα'}}, 'pl': {'sec': {'κυβερνάτε'}}}}, 'passive': {'ind': {
                'sg': {'pri': {'κυβερνώμαι', 'κυβερνούμαι', 'κυβερνιέμαι'},
                       'sec': {'κυβερνείσαι', 'κυβερνιέσαι', 'κυβερνάσαι'},
                       'ter': {'κυβερνείται', 'κυβερνάται', 'κυβερνιέται'}},
                'pl': {'pri': {'κυβερνούμεθα', 'κυβερνούμαστε', 'κυβερνόμαστε', 'κυβερνιόμαστε', 'κυβερνιούμαστε'},
                       'sec': {'κυβερνείσθε', 'κυβερνιόσαστε', 'κυβερνάστε', 'κυβερνιέστε', 'κυβερνείστε'},
                       'ter': {'κυβερνώνται', 'κυβερνιούνται', 'κυβερνούνται', 'κυβερνιόνται'}}}, 'imp': {
                'pl': {'sec': {'κυβερνείσθε', 'κυβερνιόσαστε', 'κυβερνάστε', 'κυβερνιέστε', 'κυβερνείστε'}}}}},
             'conjunctive': {'active': {
                 'ind': {'sg': {'pri': {'κυβερνήσω'}, 'sec': {'κυβερνήσεις'}, 'ter': {'κυβερνήσει'}},
                         'pl': {'pri': {'κυβερνήσουμε'}, 'sec': {'κυβερνήσετε'},
                                'ter': {'κυβερνήσουνε', 'κυβερνήσουν'}}},
                 'imp': {'sg': {'sec': {'κυβέρνησε'}}, 'pl': {'sec': {'κυβερνήστε'}}}}, 'passive': {
                 'ind': {'sg': {'pri': {'κυβερνηθώ'}, 'sec': {'κυβερνηθείς'}, 'ter': {'κυβερνηθεί'}},
                         'pl': {'pri': {'κυβερνηθούμε'}, 'sec': {'κυβερνηθείτε'},
                                'ter': {'κυβερνηθούνε', 'κυβερνηθούν'}}},
                 'imp': {'sg': {'sec': {'κυβερνήσου'}}, 'pl': {'sec': {'κυβερνηθείτε'}}}}}, 'aorist': {'active': {
                'ind': {'sg': {'pri': {'κυβέρνησα'}, 'sec': {'κυβέρνησες'}, 'ter': {'κυβέρνησε'}},
                        'pl': {'pri': {'κυβερνήσαμε'}, 'sec': {'κυβερνήσατε'}, 'ter': {'κυβέρνησαν', 'κυβερνήσανε'}}}},
                                                                                                       'passive': {
                                                                                                           'ind': {
                                                                                                               'sg': {
                                                                                                                   'pri': {
                                                                                                                       'κυβερνήθηκα'},
                                                                                                                   'sec': {
                                                                                                                       'κυβερνήθηκες'},
                                                                                                                   'ter': {
                                                                                                                       'κυβερνήθηκε'}},
                                                                                                               'pl': {
                                                                                                                   'pri': {
                                                                                                                       'κυβερνηθήκαμε'},
                                                                                                                   'sec': {
                                                                                                                       'κυβερνηθήκατε'},
                                                                                                                   'ter': {
                                                                                                                       'κυβερνηθήκανε',
                                                                                                                       'κυβερνήθηκαν'}}}}},
             'paratatikos': {'active': {'ind': {
                 'sg': {'pri': {'κυβερνούσα', 'κυβέρναγα'}, 'sec': {'κυβερνούσες', 'κυβέρναγες'},
                        'ter': {'κυβέρναγε', 'κυβερνούσε'}},
                 'pl': {'pri': {'κυβερνούσαμε', 'κυβερνάγαμε'}, 'sec': {'κυβερνούσατε', 'κυβερνάγατε'},
                        'ter': {'κυβερνούσαν', 'κυβερνάγανε', 'κυβερνούσανε', 'κυβέρναγαν'}}}}, 'passive': {'ind': {
                 'sg': {'pri': {'κυβερνιόμουνα', 'κυβερνιόμουν'}, 'sec': {'κυβερνιόσουν', 'κυβερνιόσουνα'},
                        'ter': {'κυβερνιότανε', 'κυβερνιόταν'}},
                 'pl': {'pri': {'κυβερνιόμαστε', 'κυβερνιόμασταν'}, 'sec': {'κυβερνιόσασταν', 'κυβερνιόσαστε'},
                        'ter': {'κυβερνιούνταν', 'κυβερνιόνταν', 'κυβερνιόντουσαν'}}}}},
             'act_pres_participle': {'κυβερνώντας'}, 'arch_act_pres_participle': {
                'sg': {'fem': {'acc': {'κυβερνώσα'}, 'gen': {'κυβερνώσας'}, 'voc': {'κυβερνώσα'}, 'nom': {'κυβερνώσα'}},
                       'neut': {'acc': {'κυβερνών'}, 'gen': {'κυβερνώντος'}, 'voc': {'κυβερνών'}, 'nom': {'κυβερνών'}},
                       'masc': {'acc': {'κυβερνώντα'}, 'gen': {'κυβερνώντος'}, 'voc': {'κυβερνών'},
                                'nom': {'κυβερνών'}}}, 'pl': {
                    'fem': {'acc': {'κυβερνώσες'}, 'gen': {'κυβερνωσών'}, 'voc': {'κυβερνώσες'}, 'nom': {'κυβερνώσες'}},
                    'neut': {'acc': {'κυβερνώντα'}, 'gen': {'κυβερνώντων'}, 'voc': {'κυβερνώντα'},
                             'nom': {'κυβερνώντα'}},
                    'masc': {'acc': {'κυβερνώντες'}, 'gen': {'κυβερνώντων'}, 'voc': {'κυβερνώντες'},
                             'nom': {'κυβερνώντες'}}}}, 'pass_pres_participle': {'sg': {
                'fem': {'acc': {'κυβερνούμενη', 'κυβερνώμενη'}, 'gen': {'κυβερνώμενης', 'κυβερνούμενης'},
                        'voc': {'κυβερνούμενη', 'κυβερνώμενη'}, 'nom': {'κυβερνούμενη', 'κυβερνώμενη'}},
                'neut': {'acc': {'κυβερνούμενο', 'κυβερνώμενο'}, 'gen': {'κυβερνούμενου', 'κυβερνώμενου'},
                         'voc': {'κυβερνούμενο', 'κυβερνώμενο'}, 'nom': {'κυβερνούμενο', 'κυβερνώμενο'}},
                'masc': {'acc': {'κυβερνούμενο', 'κυβερνώμενο'}, 'gen': {'κυβερνούμενου', 'κυβερνώμενου'},
                         'voc': {'κυβερνώμενε', 'κυβερνούμενε'}, 'nom': {'κυβερνούμενος', 'κυβερνώμενος'}}}, 'pl': {
                'fem': {'acc': {'κυβερνώμενες', 'κυβερνούμενες'}, 'gen': {'κυβερνώμενων', 'κυβερνούμενων'},
                        'voc': {'κυβερνώμενες', 'κυβερνούμενες'}, 'nom': {'κυβερνώμενες', 'κυβερνούμενες'}},
                'neut': {'acc': {'κυβερνούμενα', 'κυβερνώμενα'}, 'gen': {'κυβερνώμενων', 'κυβερνούμενων'},
                         'voc': {'κυβερνούμενα', 'κυβερνώμενα'}, 'nom': {'κυβερνούμενα', 'κυβερνώμενα'}},
                'masc': {'acc': {'κυβερνώμενους', 'κυβερνούμενους'}, 'gen': {'κυβερνώμενων', 'κυβερνούμενων'},
                         'voc': {'κυβερνούμενοι', 'κυβερνώμενοι'}, 'nom': {'κυβερνούμενοι', 'κυβερνώμενοι'}}}},
             'passive_perfect_participle': {'sg': {
                 'fem': {'acc': {'κυβερνημένη'}, 'gen': {'κυβερνημένης'}, 'voc': {'κυβερνημένη'},
                         'nom': {'κυβερνημένη'}},
                 'neut': {'acc': {'κυβερνημένο'}, 'gen': {'κυβερνημένου'}, 'voc': {'κυβερνημένο'},
                          'nom': {'κυβερνημένο'}},
                 'masc': {'acc': {'κυβερνημένο'}, 'gen': {'κυβερνημένου'}, 'voc': {'κυβερνημένε'},
                          'nom': {'κυβερνημένος'}}}, 'pl': {
                 'fem': {'acc': {'κυβερνημένες'}, 'gen': {'κυβερνημένων'}, 'voc': {'κυβερνημένες'},
                         'nom': {'κυβερνημένες'}},
                 'neut': {'acc': {'κυβερνημένα'}, 'gen': {'κυβερνημένων'}, 'voc': {'κυβερνημένα'},
                          'nom': {'κυβερνημένα'}},
                 'masc': {'acc': {'κυβερνημένους'}, 'gen': {'κυβερνημένων'}, 'voc': {'κυβερνημένοι'},
                          'nom': {'κυβερνημένοι'}}}}}

        )

    def test_verb_blepo(self):
        self.assertEqual(
            verb.create_all_forms('βλέπω'),
            {'present': {'active': {'ind': {'sg': {'pri': {'βλέπω'}, 'sec': {'βλέπεις'}, 'ter': {'βλέπει'}},
                                            'pl': {'pri': {'βλέπουμε'}, 'sec': {'βλέπετε'},
                                                   'ter': {'βλέπουνε', 'βλέπουν'}}},
                                    'imp': {'sg': {'sec': {'βλέπε'}}, 'pl': {'sec': {'βλέπετε'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'βλέπομαι'}, 'sec': {'βλέπεσαι'}, 'ter': {'βλέπεται'}},
                        'pl': {'pri': {'βλεπόμαστε'}, 'sec': {'βλέπεστε', 'βλεπόσαστε'}, 'ter': {'βλέπονται'}}},
                'imp': {'pl': {'sec': {'βλέπεστε'}}}}}, 'conjunctive': {'active': {
                'ind': {'sg': {'pri': {'δω'}, 'sec': {'δεις'}, 'ter': {'δει'}},
                        'pl': {'pri': {'δούμε'}, 'sec': {'δείτε'}, 'ter': {'δουν', 'δούνε'}}},
                'imp': {'sg': {'sec': {'δες'}}, 'pl': {'sec': {'δέστε', 'δείτε'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'ιδωθώ'}, 'sec': {'ιδωθείς'}, 'ter': {'ιδωθεί'}},
                        'pl': {'pri': {'ιδωθούμε'}, 'sec': {'ιδωθείτε'}, 'ter': {'ιδωθούνε', 'ιδωθούν'}}},
                'imp': {'sg': {'sec': {''}}, 'pl': {'sec': {'ιδωθείτε'}}}}}, 'aorist': {'active': {
                'ind': {'sg': {'pri': {'είδα'}, 'sec': {'είδες'}, 'ter': {'είδε'}},
                        'pl': {'pri': {'είδαμε'}, 'sec': {'είδατε'}, 'ter': {'είδανε', 'είδαν'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'ειδώθηκα'}, 'sec': {'ειδώθηκες'}, 'ter': {'ειδώθηκε'}},
                        'pl': {'pri': {'ειδωθήκαμε'}, 'sec': {'ειδωθήκατε'}, 'ter': {'ειδωθήκανε', 'ειδώθηκαν'}}}}},
             'paratatikos': {'active': {'ind': {'sg': {'pri': {'έβλεπα'}, 'sec': {'έβλεπες'}, 'ter': {'έβλεπε'}},
                                                'pl': {'pri': {'βλέπαμε'}, 'sec': {'βλέπατε'},
                                                       'ter': {'έβλεπαν', 'βλέπανε'}}}}, 'passive': {'ind': {
                 'sg': {'pri': {'βλεπόμουνα', 'βλεπόμουν'}, 'sec': {'βλεπόσουν', 'βλεπόσουνα'},
                        'ter': {'βλεπόταν', 'βλεπότανε'}},
                 'pl': {'pri': {'βλεπόμαστε', 'βλεπόμασταν'}, 'sec': {'βλεπόσασταν', 'βλεπόσαστε'},
                        'ter': {'βλέπονταν', 'βλεπόντουσαν'}}}}}, 'act_pres_participle': {'βλέποντας'},
             'arch_act_pres_participle': {
                 'sg': {'masc': {'gen': {'βλέποντος'}, 'acc': {'βλέποντα'}, 'voc': {'βλέπων'}, 'nom': {'βλέπων'}},
                        'neut': {'gen': {'βλέποντος'}, 'acc': {'βλέπον'}, 'voc': {'βλέπον'}, 'nom': {'βλέπον'}},
                        'fem': {'gen': {'βλέπουσας'}, 'acc': {'βλέπουσα'}, 'voc': {'βλέπουσα'}, 'nom': {'βλέπουσα'}}},
                 'pl': {
                     'masc': {'gen': {'βλεπόντων'}, 'acc': {'βλέποντες'}, 'voc': {'βλέποντες'}, 'nom': {'βλέποντες'}},
                     'neut': {'gen': {'βλεπόντων'}, 'acc': {'βλέποντα'}, 'voc': {'βλέποντα'}, 'nom': {'βλέποντα'}},
                     'fem': {'gen': {'βλεπουσών'}, 'acc': {'βλέπουσες'}, 'voc': {'βλέπουσες'}, 'nom': {'βλέπουσες'}}}},
             'passive_perfect_participle': {
                 'sg': {'masc': {'gen': {'ιδωμένου'}, 'acc': {'ιδωμένο'}, 'voc': {'ιδωμένε'}, 'nom': {'ιδωμένος'}},
                        'neut': {'gen': {'ιδωμένου'}, 'acc': {'ιδωμένο'}, 'voc': {'ιδωμένο'}, 'nom': {'ιδωμένο'}},
                        'fem': {'gen': {'ιδωμένης'}, 'acc': {'ιδωμένη'}, 'voc': {'ιδωμένη'}, 'nom': {'ιδωμένη'}}},
                 'pl': {'masc': {'gen': {'ιδωμένων'}, 'acc': {'ιδωμένους'}, 'voc': {'ιδωμένοι'}, 'nom': {'ιδωμένοι'}},
                        'neut': {'gen': {'ιδωμένων'}, 'acc': {'ιδωμένα'}, 'voc': {'ιδωμένα'}, 'nom': {'ιδωμένα'}},
                        'fem': {'gen': {'ιδωμένων'}, 'acc': {'ιδωμένες'}, 'voc': {'ιδωμένες'}, 'nom': {'ιδωμένες'}}}}}
        )

    def test_verb_syllambanw(self):
        self.assertEqual(
            verb.create_all_forms('συλλαμβάνω'),
            {'present': {'active': {
                'ind': {'sg': {'pri': {'συλλαμβάνω'}, 'sec': {'συλλαμβάνεις'}, 'ter': {'συλλαμβάνει'}},
                        'pl': {'pri': {'συλλαμβάνουμε'}, 'sec': {'συλλαμβάνετε'},
                               'ter': {'συλλαμβάνουν', 'συλλαμβάνουνε'}}},
                'imp': {'sg': {'sec': {'συλλάμβανε'}}, 'pl': {'sec': {'συλλαμβάνετε'}}}}, 'passive': {
                'ind': {'sg': {'pri': {'συλλαμβάνομαι'}, 'sec': {'συλλαμβάνεσαι'}, 'ter': {'συλλαμβάνεται'}},
                        'pl': {'pri': {'συλλαμβανόμαστε'}, 'sec': {'συλλαμβάνεστε', 'συλλαμβανόσαστε'},
                               'ter': {'συλλαμβάνονται'}}}, 'imp': {'pl': {'sec': {'συλλαμβάνεστε'}}}}},
             'conjunctive': {'active': {'ind': {'sg': {'pri': {'συλλάβω'}, 'sec': {'συλλάβεις'}, 'ter': {'συλλάβει'}},
                                                'pl': {'pri': {'συλλάβουμε'}, 'sec': {'συλλάβετε'},
                                                       'ter': {'συλλάβουνε', 'συλλάβουν'}}},
                                        'imp': {'sg': {'sec': {'σύλλαβε'}}, 'pl': {'sec': {'συλλάβετε'}}}}, 'passive': {
                 'ind': {'sg': {'pri': {'συλληφθώ'}, 'sec': {'συλληφθείς'}, 'ter': {'συλληφθεί'}},
                         'pl': {'pri': {'συλληφθούμε'}, 'sec': {'συλληφθείτε'}, 'ter': {'συλληφθούν', 'συλληφθούνε'}}},
                 'imp': {'sg': {'sec': {''}}, 'pl': {'sec': {'συλληφθείτε'}}}}}, 'aorist': {'active': {
                'ind': {'sg': {'pri': {'συνέλαβα'}, 'sec': {'συνέλαβες'}, 'ter': {'συνέλαβε'}},
                        'pl': {'pri': {'συνελάβαμε'}, 'sec': {'συνελάβατε'}, 'ter': {'συνέλαβαν', 'συνελάβανε'}}}},
                                                                                            'passive': {'ind': {'sg': {
                                                                                                'pri': {'συνέληφθην'},
                                                                                                'sec': {'συνέληφθης'},
                                                                                                'ter': {'συνέληφθη'}},
                                                                                                                'pl': {
                                                                                                                    'pri': {
                                                                                                                        'συνελήφθημεν'},
                                                                                                                    'sec': {
                                                                                                                        'συνελήφθητε'},
                                                                                                                    'ter': {
                                                                                                                        'συνελήφθησαν'}}}}},
             'paratatikos': {'active': {'ind': {
                 'sg': {'pri': {'συλλάμβανα', 'συνελάμβανα'}, 'sec': {'συνελάμβανες', 'συλλάμβανες'},
                        'ter': {'συνελάμβανε', 'συλλάμβανε'}},
                 'pl': {'pri': {'συλλαμβάναμε', 'συνελαμβάναμε'}, 'sec': {'συνελαμβάνατε', 'συλλαμβάνατε'},
                        'ter': {'συνελάμβαναν', 'συλλαμβάνανε', 'συλλάμβαναν', 'συνελαμβάνανε'}}}}, 'passive': {'ind': {
                 'sg': {'pri': {'συλλαμβανόμουν', 'συλλαμβανόμουνα'}, 'sec': {'συλλαμβανόσουν', 'συλλαμβανόσουνα'},
                        'ter': {'συλλαμβανότανε', 'συλλαμβανόταν'}},
                 'pl': {'pri': {'συλλαμβανόμαστε', 'συλλαμβανόμασταν'}, 'sec': {'συλλαμβανόσασταν', 'συλλαμβανόσαστε'},
                        'ter': {'συλλαμβάνονταν', 'συλλαμβανόντουσαν'}}}}}, 'act_pres_participle': {'συλλαμβάνοντας'},
             'passive_aorist_participle': {'pl': {
                 'neut': {'voc': {'συλληφθέντα'}, 'acc': {'συλληφθέντα'}, 'gen': {'συλληφθέντων'},
                          'nom': {'συλληφθέντα'}},
                 'masc': {'voc': {'συλληφθέντες'}, 'acc': {'συλληφθέντες'}, 'gen': {'συλληφθέντων'},
                          'nom': {'συλληφθέντες'}},
                 'fem': {'voc': {'συλληφθείσες'}, 'acc': {'συλληφθείσες'}, 'gen': {'συλληφθεισών'},
                         'nom': {'συλληφθείσες'}}}, 'sg': {
                 'neut': {'voc': {'συλληφθέν'}, 'acc': {'συλληφθέν'}, 'gen': {'συλληφθέντος'}, 'nom': {'συλληφθέν'}},
                 'masc': {'voc': {'συλληφθείς'}, 'acc': {'συλληφθέντα'}, 'gen': {'συλληφθέντος'},
                          'nom': {'συλληφθείς'}},
                 'fem': {'voc': {'συλληφθείσα'}, 'acc': {'συλληφθείσα'}, 'gen': {'συλληφθείσας'},
                         'nom': {'συλληφθείσα'}}}}, 'pass_pres_participle': {'pl': {
                'neut': {'voc': {'συλλαμβανόμενα'}, 'acc': {'συλλαμβανόμενα'}, 'gen': {'συλλαμβανόμενων'},
                         'nom': {'συλλαμβανόμενα'}},
                'masc': {'voc': {'συλλαμβανόμενοι'}, 'acc': {'συλλαμβανόμενους'}, 'gen': {'συλλαμβανόμενων'},
                         'nom': {'συλλαμβανόμενοι'}},
                'fem': {'voc': {'συλλαμβανόμενες'}, 'acc': {'συλλαμβανόμενες'}, 'gen': {'συλλαμβανόμενων'},
                        'nom': {'συλλαμβανόμενες'}}}, 'sg': {
                'neut': {'voc': {'συλλαμβανόμενο'}, 'acc': {'συλλαμβανόμενο'}, 'gen': {'συλλαμβανόμενου'},
                         'nom': {'συλλαμβανόμενο'}},
                'masc': {'voc': {'συλλαμβανόμενε'}, 'acc': {'συλλαμβανόμενο'}, 'gen': {'συλλαμβανόμενου'},
                         'nom': {'συλλαμβανόμενος'}},
                'fem': {'voc': {'συλλαμβανόμενη'}, 'acc': {'συλλαμβανόμενη'}, 'gen': {'συλλαμβανόμενης'},
                        'nom': {'συλλαμβανόμενη'}}}}}
        )

    def test_verb_phgainw(self):
        self.assertEqual(
            verb.create_all_forms('πηγαίνω'),
            {'present': {'active': {'ind': {'sg': {'pri': {'πηγαίνω'}, 'sec': {'πηγαίνεις'}, 'ter': {'πηγαίνει'}},
                                            'pl': {'pri': {'πηγαίνουμε'}, 'sec': {'πηγαίνετε'},
                                                   'ter': {'πηγαίνουνε', 'πηγαίνουν'}}},
                                    'imp': {'sg': {'sec': {'πήγαινε'}}, 'pl': {'sec': {'πηγαίνετε'}}}}},
             'conjunctive': {'active': {'ind': {'sg': {'pri': {'πάω'}, 'sec': {'πας'}, 'ter': {'πάει'}},
                                                'pl': {'pri': {'πάμε'}, 'sec': {'πάτε'}, 'ter': {'παν', 'πάνε'}}},
                                        'imp': {'sg': {'sec': {'πήγαινε'}}, 'pl': {'sec': {'πηγαίνετε'}}}}}, 'aorist': {
                'active': {'ind': {'sg': {'pri': {'πήγα'}, 'sec': {'πήγες'}, 'ter': {'πήγε'}},
                                   'pl': {'pri': {'πήγαμε'}, 'sec': {'πήγατε'}, 'ter': {'πήγαν', 'πήγανε'}}}}},
             'paratatikos': {'active': {'ind': {'sg': {'pri': {'πήγαινα'}, 'sec': {'πήγαινες'}, 'ter': {'πήγαινε'}},
                                                'pl': {'pri': {'πηγαίναμε'}, 'sec': {'πηγαίνατε'},
                                                       'ter': {'πηγαίνανε', 'πήγαιναν'}}}}},
             'act_pres_participle': {'πηγαίνοντας'}}

        )

    def test_verb_prokeitai(self):
        self.assertEqual(
            verb.create_all_forms('πρόκειται'),
            {'present': {'passive': {'ind': {'sg': {'ter': {'πρόκειται'}}}}},
             'paratatikos': {'passive': {'ind': {'sg': {'ter': {'επρόκειτο'}}}}}}

        )

    def test_verb_symbainei(self):
        # self.maxDiff = None
        self.assertEqual(
            verb.create_all_forms('συμβαίνει'),
            {'present': {
                'active': {'ind': {'sg': {'ter': {'συμβαίνει'}}, 'pl': {'ter': {'συμβαίνουν', 'συμβαίνουνε'}}}}},
             'conjunctive': {'active': {'ind': {'sg': {'ter': {'συμβεί'}}, 'pl': {'ter': {'συμβούν'}}}}}, 'aorist': {
                'active': {'ind': {'sg': {'pri': {'σύνεβην'}, 'sec': {'σύνεβης'}, 'ter': {'σύνεβη'}},
                                   'pl': {'pri': {'συνέβημεν'}, 'sec': {'συνέβητε'}, 'ter': {'συνέβησαν'}}}}},
             'paratatikos': {'active': {'ind': {'sg': {'ter': {'συνέβαινε'}}, 'pl': {'ter': {'συνέβαιναν'}}}}}}

        )


if __name__ == '__main__':
    main()