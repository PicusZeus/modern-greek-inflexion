from unittest import TestCase

from icecream import ic

from modern_greek_inflexion import verb


def present_act(v):
    return verb.create_all_forms(v)['present']['active']['ind']


def present_pass(v):
    return verb.create_all_forms(v)['present']['passive']['ind']


class VerbTestPresAct(TestCase):

    # CON1_ACT
    def test_verb_blepw(self):
        self.assertDictEqual(
            present_act('βλέπω'),
            {'pl': {'pri': {'βλέπουμε', 'βλέπομε'},
                    'sec': {'βλέπετε'},
                    'ter': {'βλέπουνε', 'βλέπουν'}},
             'sg': {'pri': {'βλέπω'}, 'sec': {'βλέπεις'}, 'ter': {'βλέπει'}}},
        )

    # CON2A_ACT
    def test_verb_pernaw(self):
        self.assertDictEqual(
            present_act('περνάω'),
            {'pl': {'pri': {'περνάμε', 'περνούμε'},
                    'sec': {'περνάτε'},
                    'ter': {'περνούνε', 'περνάνε', 'περνούν', 'περνάν'}},
             'sg': {'pri': {'περνώ', 'περνάω'},
                    'sec': {'περνάς'},
                    'ter': {'περνάει', 'περνά'}}},
        )

    # CON2AK_ACT
    def test_verb_kathistw(self):
        self.assertDictEqual(
            present_act('καθιστώ'),
            {'pl': {'pri': {'καθιστάμε', 'καθιστούμε'},
                    'sec': {'καθιστάτε'},
                    'ter': {'καθιστούν'}},
             'sg': {'pri': {'καθιστώ'}, 'sec': {'καθιστάς'}, 'ter': {'καθιστά'}}}
            ,
            ic()
        )

    # CON2B_ACT

    def test_verb_syntelw(self):
        self.assertDictEqual(
            present_act('συντελώ'),
            {'pl': {'pri': {'συντελούμε'},
                    'sec': {'συντελείτε'},
                    'ter': {'συντελούνε', 'συντελούν'}},
             'sg': {'pri': {'συντελώ'}, 'sec': {'συντελείς'}, 'ter': {'συντελεί'}}}

        )

    # CON2B_ACT + CON2A_ACT
    def test_verb_lalw(self):
        self.assertDictEqual(
            present_act('λαλώ'),
            {'pl': {'pri': {'λαλάμε', 'λαλούμε'},
                    'sec': {'λαλάτε', 'λαλείτε'},
                    'ter': {'λαλούνε', 'λαλάν', 'λαλάνε', 'λαλούν'}},
             'sg': {'pri': {'λαλώ', 'λαλάω'},
                    'sec': {'λαλείς', 'λαλάς'},
                    'ter': {'λαλάει', 'λαλεί', 'λαλά'}}}
        )

    # CON2C_ACT
    def test_verb_ftaiw(self):
        self.assertDictEqual(
            present_act('φταίω'),
            {'pl': {'pri': {'φταίμε'}, 'sec': {'φταίτε'}, 'ter': {'φταιν', 'φταίνε'}},
             'sg': {'pri': {'φταίω'}, 'sec': {'φταις'}, 'ter': {'φταίει'}}}

        )

    # CON2D_ACT
    def test_verb_plhrw(self):
        self.assertDictEqual(
            present_act('πληρώ'),
            {'pl': {'pri': {'πληρούμε'}, 'sec': {'πληρούτε'}, 'ter': {'πληρούν'}},
             'sg': {'pri': {'πληρώ'}, 'sec': {'πληροίς'}, 'ter': {'πληροί'}}}

        )

    def test_verb_diabiw(self):
        self.assertDictEqual(
            present_act('διαβιώ'),
            {'pl': {'pri': {'διαβιούμε'}, 'sec': {'διαβιούτε'}, 'ter': {'διαβιούν'}},
             'sg': {'pri': {'διαβιώ'}, 'sec': {'διαβιοίς'}, 'ter': {'διαβιοί'}}}

        )


class VerbTestPresPass(TestCase):

    # 1 pass CON1_PASS + CON1_PASS_ARCH
    def test_verb_dexomai(self):
        self.assertDictEqual(
            present_pass('δέχομαι'),
            {'pl': {'pri': {'δεχόμεθα', 'δεχόμαστε'},
                    'sec': {'δεχόσαστε', 'δέχεστε', 'δέχεσθε'},
                    'ter': {'δέχονται'}},
             'sg': {'pri': {'δέχομαι'},
                    'sec': {'δέχεσαι'},
                    'ter': {'δέχεται'}}}

        )

    # CON2A_PASS

    def test_verb_phdiemai(self):
        self.assertDictEqual(
            present_pass('πηδιέμαι'),
            {'pl': {'pri': {'πηδιόμαστε'},
                    'sec': {'πηδιόσαστε', 'πηδιέστε'},
                    'ter': {'πηδιόνται', 'πηδιούνται'}},
             'sg': {'pri': {'πηδιέμαι'},
                    'sec': {'πηδιέσαι'},
                    'ter': {'πηδιέται'}}}

        )

    # pure CON2AB_PASS
    def test_verb_ktwmai(self):
        self.assertDictEqual(
            present_pass('κτώμαι'),
            {'pl': {'pri': {'κτώμεθα', 'κτόμαστε'},
                    'sec': {'κτάσθε', 'κτάστε'},
                    'ter': {'κτώνται'}},
             'sg': {'pri': {'κτώμαι'}, 'sec': {'κτάσαι'}, 'ter': {'κτάται'}}}

        )

    # mixed CON2A_PASS and CON2AB_PASS

    def test_verb_apoktwmai(self):
        self.assertDictEqual(
            present_pass('αποκτώμαι'),
            {'pl': {'pri': {'αποκτόμαστε', 'αποκτιόμαστε', 'αποκτώμεθα'},
                    'sec': {'αποκτάσθε', 'αποκτιέστε', 'αποκτιόσαστε', 'αποκτάστε'},
                    'ter': {'αποκτιόνται', 'αποκτώνται', 'αποκτιούνται'}},
             'sg': {'pri': {'αποκτώμαι', 'αποκτιέμαι'},
                    'sec': {'αποκτάσαι', 'αποκτιέσαι'},
                    'ter': {'αποκτάται', 'αποκτιέται'}}}
            ,

        )

    # pure CON2B_PASS
    def test_verb_afairoumai(self):
        self.assertDictEqual(
            present_pass('αφαιρούμαι'),
            {'pl': {'pri': {'αφαιρούμαστε'}, 'sec': {'αφαιρείστε'}, 'ter': {'αφαιρούνται'}},
             'sg': {'pri': {'αφαιρούμαι'}, 'sec': {'αφαιρείσαι'}, 'ter': {'αφαιρείται'}}}
            ,
        )

    # CON2B_PASS + CON2B_PASS_ARCH
    def test_verb_ofeloumai(self):
        self.assertDictEqual(
            present_pass('ωφελώ'),
            {'pl': {'pri': {'ωφελούμεθα', 'ωφελούμαστε'},
                    'sec': {'ωφελείστε', 'ωφελείσθε'},
                    'ter': {'ωφελούνται'}},
             'sg': {'pri': {'ωφελούμαι'}, 'sec': {'ωφελείσαι'}, 'ter': {'ωφελείται'}}}

            ,

        )

    # CON2C_PASS

    def test_verb_koimamai(self):
        self.assertDictEqual(
            present_pass('κοιμάμαι'),
            {'pl': {'pri': {'κοιμούμαστε', 'κοιμόμαστε'},
                    'sec': {'κοιμόσαστε', 'κοιμάστε'},
                    'ter': {'κοιμόνται', 'κοιμούνται'}},
             'sg': {'pri': {'κοιμούμαι', 'κοιμάμαι'},
                    'sec': {'κοιμάσαι'},
                    'ter': {'κοιμάται'}}}
            ,
        )

    # CON2D_PASS

    def test_verb_epitithemai(self):
        self.assertDictEqual(
            present_pass('επιτίθεμαι'),
            {'pl': {'pri': {'επιτιθέμαστε', 'επιτιθέμεθα'},
                    'sec': {'επιτίθεστε', 'επιτίθεσθε'},
                    'ter': {'επιτίθενται'}},
             'sg': {'pri': {'επιτίθεμαι'}, 'sec': {'επιτίθεσαι'}, 'ter': {'επιτίθεται'}}}

            ,
        )

    # CON2E_PASS
    def test_verb_antikathistamai(self):
        self.assertDictEqual(
            present_pass('αντικαθίσταμαι'),
            {'pl': {'pri': {'αντικαθιστόμαστε', 'αντικαθιστάμεθα'},
                    'sec': {'αντικαθίσταστε', 'αντικαθίστασθε'},
                    'ter': {'αντικαθίστανται'}},
             'sg': {'pri': {'αντικαθίσταμαι'},
                    'sec': {'αντικαθίστασαι'},
                    'ter': {'αντικαθίσταται'}}}

            ,
        )

    # CON2F_PASS
    def test_verb_isoumaii(self):
        self.assertDictEqual(
            present_pass('ισούμαι'),
            {'pl': {'pri': {'ισούμαστε', 'ισούμεθα'},
                    'sec': {'ισούσθε', 'ισούστε'},
                    'ter': {'ισούνται'}},
             'sg': {'pri': {'ισούμαι'}, 'sec': {'ισούσαι'}, 'ter': {'ισούται'}}}
            ,
        )
