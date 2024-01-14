from unittest import TestCase

# from icecream import ic

from modern_greek_inflexion import noun
from modern_greek_inflexion.resources.resources import MASC, NEUT, FEM, FEM_SG, NEUT_SG, NEUT_PL, MASC_FEM, greek_corpus


class NounTests(TestCase):

    def test_noun_kalos(self):
        self.assertDictEqual(
            noun.create_all('κάλως', gender=MASC),
            {'masc': {'sg': {'nom': {'κάλως'},
                             'acc': {'κάλω'},
                             'gen': {'κάλω'}, 'voc': {'κάλως'}},
                      'pl': {'nom': {'κάλως'}, 'acc': {'κάλως'}, 'voc': {'κάλως'}, 'gen': {'κάλων'}}}},
        )

    def test_noun_gynaika(self):
        """should return dictionary with all possible cases"""
        self.assertDictEqual(
            noun.create_all('γυναίκα'),
            {'fem': {'sg': {'nom': {'γυναίκα'}, 'gen': {'γυναίκας'}, 'voc': {'γυναίκα'}, 'acc': {'γυναίκα'}},
                     'pl': {'nom': {'γυναίκες'}, 'gen': {'γυναικών'}, 'voc': {'γυναίκες'}, 'acc': {'γυναίκες'}}}},
        )

    def test_noun_rhgas(self):
        self.assertDictEqual(
            noun.create_all('ρήγας', gender='masc'),
            {'masc':
                 {'sg': {'nom': {'ρήγας'}, 'gen': {'ρήγα'}, 'voc': {'ρήγα'}, 'acc': {'ρήγα'}},
                  'pl': {'nom': {'ρηγάδες'}, 'gen': {'ρηγάδων'}, 'voc': {'ρηγάδες'}, 'acc': {'ρηγάδες'}}}})

    def test_noun_mpousi(self):
        self.assertDictEqual(
            noun.create_all('μπούσι'),
            {'neut': {'pl': {'voc': {'μπούσια'}, 'acc': {'μπούσια'}, 'gen': {''}, 'nom': {'μπούσια'}},
                      'sg': {'voc': {'μπούσι'}, 'acc': {'μπούσι'}, 'gen': {''}, 'nom': {'μπούσι'}}}}
        )

    def test_noun_gialakias(self):
        self.assertDictEqual(
            noun.create_all('γυαλάκιας'),
            {'masc': {
                'pl': {'nom': {'γυαλάκηδες'}, 'acc': {'γυαλάκηδες'}, 'voc': {'γυαλάκηδες'}, 'gen': {'γυαλάκηδων'}},
                'sg': {'nom': {'γυαλάκιας'}, 'voc': {'γυαλάκια'}, 'gen': {'γυαλάκια'}, 'acc': {'γυαλάκια'}}}},

        )

    def test_noun_kanagias(self):
        self.assertDictEqual(
            noun.create_all('κανάγιας'),
            {'masc': {'pl': {'acc': {'κανάγηδες', 'κανάγιες'},
                             'gen': {'καναγίων', 'κανάγηδων'},
                             'nom': {'κανάγηδες', 'κανάγιες'},
                             'voc': {'κανάγηδες', 'κανάγιες'}},
                      'sg': {'acc': {'κανάγια'},
                             'gen': {'κανάγια'},
                             'nom': {'κανάγιας'},
                             'voc': {'κανάγια'}}}},

        )

    def test_noun_antipapas(self):
        self.assertDictEqual(
            noun.create_all('αντιπάπας'),
            {'masc': {'pl': {'acc': {'αντιπάπες'},
                             'gen': {'αντιπαπών'},
                             'nom': {'αντιπάπες'},
                             'voc': {'αντιπάπες'}},
                      'sg': {'acc': {'αντιπάπα'},
                             'gen': {'αντιπάπα'},
                             'nom': {'αντιπάπας'},
                             'voc': {'αντιπάπα'}}}},
        )

    def test_noun_serbika(self):
        self.assertDictEqual(
            noun.create_all('σερβικά'),
            {'neut': {'pl': {'acc': {'σερβικά'},
                             'gen': {'σερβικών'},
                             'nom': {'σερβικά'},
                             'voc': {'σερβικά'}},
                      'sg': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}}}},
        )

    def test_noun_pais(self):
        self.assertDictEqual(
            noun.create_all('παις', gender=MASC),
            {'masc': {'pl': {'acc': {'παίδες'},
                             'gen': {'παίδων'},
                             'nom': {'παίδες'},
                             'voc': {'παίδες'}},
                      'sg': {'acc': {'παίδα'},
                             'gen': {'παιδός'},
                             'nom': {'παις'},
                             'voc': {'παι'}}}}

        )
    def test_noun_limenarxhs(self):
        self.assertDictEqual(
            noun.create_all('λιμενάρχης', gender=MASC_FEM),
            {'fem': {'pl': {'acc': {'λιμενάρχες'},
                            'gen': {'λιμεναρχών'},
                            'nom': {'λιμενάρχες'},
                            'voc': {'λιμενάρχες'}},
                     'sg': {'acc': {'λιμενάρχη'},
                            'gen': {'λιμενάρχου'},
                            'nom': {'λιμενάρχης'},
                            'voc': {'λιμενάρχα'}}},
             'masc': {'pl': {'acc': {'λιμενάρχες'},
                             'gen': {'λιμεναρχών'},
                             'nom': {'λιμενάρχες'},
                             'voc': {'λιμενάρχες'}},
                      'sg': {'acc': {'λιμενάρχη'},
                             'gen': {'λιμενάρχου', 'λιμενάρχη'},
                             'nom': {'λιμενάρχης'},
                             'voc': {'λιμενάρχα'}}}},
        )

    def test_noun_diafwnwn(self):
        self.assertDictEqual(
            noun.create_all('διαφωνών'),
            {'masc': {'pl': {'acc': {'διαφωνούντες'},
                             'gen': {'διαφωνούντων'},
                             'nom': {'διαφωνούντες'},
                             'voc': {'διαφωνούντες'}},
                      'sg': {'acc': {'διαφωνούντα'},
                             'gen': {'διαφωνούντος'},
                             'nom': {'διαφωνών'},
                             'voc': {'διαφωνών'}}}}
        )

    def test_noun_kidemonas(self):
        self.assertDictEqual(
            noun.create_all('κηδεμόνας', gender=MASC_FEM),
            {'fem': {'pl': {'acc': {'κηδεμόνες'},
                            'gen': {'κηδεμόνων'},
                            'nom': {'κηδεμόνες'},
                            'voc': {'κηδεμόνες'}},
                     'sg': {'acc': {'κηδεμόνα'},
                            'gen': {'κηδεμόνος'},
                            'nom': {'κηδεμόνας'},
                            'voc': {'κηδεμόνα'}}},
             'masc': {'pl': {'acc': {'κηδεμόνες'},
                             'gen': {'κηδεμόνων'},
                             'nom': {'κηδεμόνες'},
                             'voc': {'κηδεμόνες'}},
                      'sg': {'acc': {'κηδεμόνα'},
                             'gen': {'κηδεμόνα', 'κηδεμόνος'},
                             'nom': {'κηδεμόνας'},
                             'voc': {'κηδεμόνα'}}}},
        )

    def test_noun_ris(self):
        self.assertDictEqual(
            noun.create_all('ρις'),
            {'fem': {'pl': {'acc': {'ρίνες'},
                            'gen': {'ρινών'},
                            'nom': {'ρίνες'},
                            'voc': {'ρίνες'}},
                         'sg': {'acc': {'ρίνα'},
                            'gen': {'ρινός'},
                            'nom': {'ρις'},
                            'voc': {'ρι'}}}}

        )
    def test_noun_polh(self):
        self.assertDictEqual(
            noun.create_all('πόλη'),
            {'fem': {'pl': {'acc': {'πόλεις'},
                            'gen': {'πόλεων'},
                            'nom': {'πόλεις'},
                            'voc': {'πόλεις'}},
                     'sg': {'acc': {'πόλη'},
                            'gen': {'πόλεως', 'πόλης'},
                            'nom': {'πόλη'},
                            'voc': {'πόλη'}}}}

        )

    def test_noun_magio(self):
        self.assertDictEqual(
            noun.create_all('μαγιό', gender=NEUT, aklito=True),
            {'neut': {'pl': {'acc': {'μαγιό'},
                             'gen': {'μαγιό'},
                             'nom': {'μαγιό'},
                             'voc': {'μαγιό'}},
                      'sg': {'acc': {'μαγιό'},
                             'gen': {'μαγιό'},
                             'nom': {'μαγιό'},
                             'voc': {'μαγιό'}}}}

        )

    def test_noun_anthos(self):
        self.assertDictEqual(
            noun.create_all('άνθος'),
            {'neut': {'pl': {'acc': {'άνθη'},
                             'gen': {'ανθέων'},
                             'nom': {'άνθη'},
                             'voc': {'άνθη'}},
                      'sg': {'acc': {'άνθος'},
                             'gen': {'άνθους'},
                             'nom': {'άνθος'},
                             'voc': {'άνθος'}}}}

        )

    def test_noun_agxos(self):
        self.assertDictEqual(
            noun.create_all('άγχος'),
            {'neut': {'pl': {'acc': {'άγχη'}, 'nom': {'άγχη'}, 'voc': {'άγχη'}},
                      'sg': {'acc': {'άγχος'},
                             'gen': {'άγχους'},
                             'nom': {'άγχος'},
                             'voc': {'άγχος'}}}}

        )

    def test_noun_embadon(self):
        self.assertDictEqual(
            noun.create_all('εμβαδόν'),
            {'neut': {'pl': {'acc': {'εμβαδά'},
                             'gen': {'εμβαδών'},
                             'nom': {'εμβαδά'},
                             'voc': {'εμβαδά'}},
                      'sg': {'acc': {'εμβαδόν'},
                             'gen': {'εμβαδού'},
                             'nom': {'εμβαδόν'},
                             'voc': {'εμβαδόν'}}}}

        )

    def test_noun_mili(self):
        self.assertDictEqual(
            noun.create_all('μίλι'),
            {'neut': {'pl': {'acc': {'μίλια'},
                             'gen': {'μιλίων'},
                             'nom': {'μίλια'},
                             'voc': {'μίλια'}},
                      'sg': {'acc': {'μίλι'},
                             'gen': {'μιλίου'},
                             'nom': {'μίλι'},
                             'voc': {'μίλι'}}}}

        )

    def test_noun_alas(self):
        self.assertDictEqual(
            noun.create_all('άλας', gender=NEUT),
            {'neut': {'pl': {'acc': {'άλατα'},
                             'gen': {'αλάτων'},
                             'nom': {'άλατα'},
                             'voc': {'άλατα'}},
                      'sg': {'acc': {'άλας'},
                             'gen': {'άλατος'},
                             'nom': {'άλας'},
                             'voc': {'άλας'}}}}

        )

    def test_noun_xaris(self):
        self.assertDictEqual(
            noun.create_all('χάρις'),
            {'fem': {'pl': {'acc': {'χάριτες'},
                            'gen': {'χαρίτων'},
                            'nom': {'χάριτες'},
                            'voc': {'χάριτες'}},
                     'sg': {'acc': {'χάριν'},
                            'gen': {'χάριτος'},
                            'nom': {'χάρις'},
                            'voc': {'χάρι'}}}}

        )

    def test_noun_kathgoroumenh(self):
        self.assertDictEqual(
            noun.create_all('κατηγορουμένη'),
            {'fem': {'pl': {'acc': {'κατηγορούμενες'},
                            'gen': {'κατηγορουμένων'},
                            'nom': {'κατηγορούμενες'},
                            'voc': {'κατηγορούμενες'}},
                     'sg': {'acc': {'κατηγορουμένη'},
                            'gen': {'κατηγορουμένης'},
                            'nom': {'κατηγορουμένη'},
                            'voc': {'κατηγορουμένη'}}}}

        )

    def test_noun_erwmenh(self):
        self.assertDictEqual(
            noun.create_all('ερωμένη'),
            {'fem': {'pl': {'acc': {'ερωμένες'},
                            'gen': {'ερωμένων'},
                            'nom': {'ερωμένες'},
                            'voc': {'ερωμένες'}},
                     'sg': {'acc': {'ερωμένη'},
                            'gen': {'ερωμένης'},
                            'nom': {'ερωμένη'},
                            'voc': {'ερωμένη'}}}}

        )

    def test_noun_upnakos(self):
        self.assertDictEqual(
            noun.create_all('υπνάκος'),
            {'masc': {'pl': {'acc': {'υπνάκους'},
                             'gen': {'υπνάκων'},
                             'nom': {'υπνάκοι'},
                             'voc': {'υπνάκοι'}},
                      'sg': {'acc': {'υπνάκο'},
                             'gen': {'υπνάκου'},
                             'nom': {'υπνάκος'},
                             'voc': {'υπνάκο', 'υπνάκε'}}}}

        )

    def test_noun_nufi(self):
        self.assertDictEqual(
            noun.create_all('νύφη'),
            {'fem': {'pl': {'acc': {'νυφάδες', 'νύφες'},
                            'gen': {'νυφάδων'},
                            'nom': {'νυφάδες', 'νύφες'},
                            'voc': {'νυφάδες', 'νύφες'}},
                     'sg': {'acc': {'νύφη'},
                            'gen': {'νύφης'},
                            'nom': {'νύφη'},
                            'voc': {'νύφη'}}}}

        )

    def test_noun_barymangas(self):
        self.assertDictEqual(
            noun.create_all('βαρύμαγκας'),
            {'masc': {'pl': {'acc': {'βαρύμαγκες'},
                             'gen': {'βαρύμαγκων'},
                             'nom': {'βαρύμαγκες'},
                             'voc': {'βαρύμαγκες'}},
                      'sg': {'acc': {'βαρύμαγκα'},
                             'gen': {'βαρύμαγκα'},
                             'nom': {'βαρύμαγκας'},
                             'voc': {'βαρύμαγκα'}}}}

        )

    def test_noun_amforeas(self):
        self.assertDictEqual(
            noun.create_all('αμφορέας'),
            {'masc': {'pl': {'acc': {'αμφορείς'},
                             'gen': {'αμφορέων'},
                             'nom': {'αμφορείς'},
                             'voc': {'αμφορείς'}},
                      'sg': {'acc': {'αμφορέα'},
                             'gen': {'αμφορέως', 'αμφορέα'},
                             'nom': {'αμφορέας'},
                             'voc': {'αμφορέα'}}}}

        )

    def test_noun_pestrofa(self):
        self.assertDictEqual(
            noun.create_all('πέστροφα'),
            {'fem': {'pl': {'acc': {'πέστροφες'},
                            'gen': {''},
                            'nom': {'πέστροφες'},
                            'voc': {'πέστροφες'}},
                     'sg': {'acc': {'πέστροφα'},
                            'gen': {'πέστροφας'},
                            'nom': {'πέστροφα'},
                            'voc': {'πέστροφα'}}}}

        )

    def test_noun_arthridida(self):
        self.assertDictEqual(
            noun.create_all('αρθρίτιδα'),
            {'fem': {'pl': {'acc': {'αρθρίτιδες'},
                            'gen': {'αρθρίτιδων'},
                            'nom': {'αρθρίτιδες'},
                            'voc': {'αρθρίτιδες'}},
                     'sg': {'acc': {'αρθρίτιδα'},
                            'gen': {'αρθρίτιδας'},
                            'nom': {'αρθρίτιδα'},
                            'voc': {'αρθρίτιδα'}}}}

        )

    def test_noun_mama(self):
        self.assertDictEqual(
            noun.create_all('μαμά'),
            {'fem': {'pl': {'acc': {'μαμάδες'},
                            'gen': {'μαμάδων'},
                            'nom': {'μαμάδες'},
                            'voc': {'μαμάδες'}},
                     'sg': {'acc': {'μαμά'},
                            'gen': {'μαμάς'},
                            'nom': {'μαμά'},
                            'voc': {'μαμά'}}}}

        )

    def test_noun_sofia(self):
        self.assertDictEqual(
            noun.create_all('σοφία'),
            {'fem': {'pl': {'acc': {'σοφίες'},
                            'gen': {'σοφιών'},
                            'nom': {'σοφίες'},
                            'voc': {'σοφίες'}},
                     'sg': {'acc': {'σοφία'},
                            'gen': {'σοφίας'},
                            'nom': {'σοφία'},
                            'voc': {'σοφία'}}}}

        )

    def test_noun_giagia(self):
        self.assertDictEqual(
            noun.create_all('γιαγιά'),
            {'fem': {'pl': {'acc': {'γιαγιάδες', 'γιαγιές'},
                            'gen': {'γιαγιάδων'},
                            'nom': {'γιαγιάδες', 'γιαγιές'},
                            'voc': {'γιαγιάδες', 'γιαγιές'}},
                     'sg': {'acc': {'γιαγιά'},
                            'gen': {'γιαγιάς'},
                            'nom': {'γιαγιά'},
                            'voc': {'γιαγιά'}}}},
        )

    def test_noun_peina(self):
        self.assertDictEqual(
            noun.create_all('πείνα'),
            {'fem': {'pl': {'acc': {'πείνες'},
                            'gen': {''},
                            'nom': {'πείνες'},
                            'voc': {'πείνες'}},
                     'sg': {'acc': {'πείνα'},
                            'gen': {'πείνας'},
                            'nom': {'πείνα'},
                            'voc': {'πείνα'}}}}

        )

    def test_noun_upezwkws(self):
        self.assertDictEqual(
            noun.create_all('υπεζωκώς', gender=MASC),
            {'masc': {'pl': {'acc': {'υπεζωκότες'},
                             'gen': {'υπεζωκότων'},
                             'nom': {'υπεζωκότες'},
                             'voc': {'υπεζωκότες'}},
                      'sg': {'acc': {'υπεζωκότα'},
                             'gen': {'υπεζωκότος'},
                             'nom': {'υπεζωκώς'},
                             'voc': {'υπεζωκώς'}}}}

        )

    def test_noun_therapeuon(self):
        self.assertDictEqual(
            noun.create_all('θεράπων'),
            {'masc': {'pl': {'acc': {'θεράποντες'},
                             'gen': {'θεραπόντων'},
                             'nom': {'θεράποντες'},
                             'voc': {'θεράποντες'}},
                      'sg': {'acc': {'θεράποντα'},
                             'gen': {'θεράποντος'},
                             'nom': {'θεράπων'},
                             'voc': {'θεράπων'}}}}

        )

    def test_noun_propappous(self):
        self.assertDictEqual(
            noun.create_all('προπάππους'),
            {'masc': {'pl': {'acc': {'προπαππούδες'},
                             'gen': {'προπαππούδων'},
                             'nom': {'προπαππούδες'},
                             'voc': {'προπαππούδες'}},
                      'sg': {'acc': {'προπάππου'},
                             'gen': {'προπάππου'},
                             'nom': {'προπάππους'},
                             'voc': {'προπάππου'}}}}

        )

    def test_noun_apoplous(self):
        self.assertDictEqual(
            noun.create_all('απόπλους'),
            {'masc': {'pl': {'acc': {'απόπλους'},
                             'gen': {'απόπλων'},
                             'nom': {'απόπλοι'},
                             'voc': {'απόπλοι'}},
                      'sg': {'acc': {'απόπλου'},
                             'gen': {'απόπλου'},
                             'nom': {'απόπλους'},
                             'voc': {'απόπλου'}}}}

        )

    def test_noun_ripsaspis(self):
        self.assertDictEqual(
            noun.create_all('ρίψασπις', gender=MASC),
            {'masc': {'pl': {'acc': {'ριψάσπιδες'},
                             'gen': {'ριψασπίδων'},
                             'nom': {'ριψάσπιδες'},
                             'voc': {'ριψάσπιδες'}},
                      'sg': {'acc': {'ριψάσπιδα'},
                             'gen': {'ριψάσπιδος'},
                             'nom': {'ρίψασπις'},
                             'voc': {'ρίψασπι'}}}}

        )

    def test_noun_kapetanios(self):
        self.assertDictEqual(
            noun.create_all('καπετάνιος'),
            {'masc': {'pl': {'acc': {'καπετάνιους', 'καπεταναίους'},
                             'gen': {'καπεταναίων', 'καπετάνιων'},
                             'nom': {'καπετάνιοι', 'καπεταναίοι'},
                             'voc': {'καπετάνιοι', 'καπεταναίοι'}},
                      'sg': {'acc': {'καπετάνιο'},
                             'gen': {'καπετάνιου'},
                             'nom': {'καπετάνιος'},
                             'voc': {'καπετάνιο', 'καπετάνιε'}}}},
        )

    def test_noun_mpouloukpashs(self):
        self.assertDictEqual(
            noun.create_all('μπουλούκμπασης'),
            {'masc': {'pl': {'acc': {'μπουλουκμπασήδες'},
                             'gen': {'μπουλουκμπασήδων'},
                             'nom': {'μπουλουκμπασήδες'},
                             'voc': {'μπουλουκμπασήδες'}},
                      'sg': {'acc': {'μπουλούκμπαση'},
                             'gen': {'μπουλούκμπαση'},
                             'nom': {'μπουλούκμπασης'},
                             'voc': {'μπουλούκμπαση'}}}}

        )

    def test_noun_prutanhs(self):
        self.assertDictEqual(
            noun.create_all('πρύτανης', gender=MASC_FEM),
            {'fem': {'pl': {'acc': {'πρυτάνεις'},
                            'gen': {'πρυτάνεων'},
                            'nom': {'πρυτάνεις'},
                            'voc': {'πρυτάνεις'}},
                     'sg': {'acc': {'πρύτανη'},
                            'gen': {'πρυτάνεως'},
                            'nom': {'πρύτανης'},
                            'voc': {'πρύτανη'}}},
             'masc': {'pl': {'acc': {'πρυτάνεις'},
                             'gen': {'πρυτάνεων'},
                             'nom': {'πρυτάνεις'},
                             'voc': {'πρυτάνεις'}},
                      'sg': {'acc': {'πρύτανη'},
                             'gen': {'πρυτάνεως', 'πρύτανη'},
                             'nom': {'πρύτανης'},
                             'voc': {'πρύτανη'}}}},

        )

    def test_noun_tsapanhs(self):
        self.assertDictEqual(
            noun.create_all('τσοπάνης'),
            {'masc': {'pl': {'acc': {'τσοπάνηδες', 'τσοπαναραίους'},
                             'gen': {'τσοπάνηδων', 'τσοπαναραίων'},
                             'nom': {'τσοπάνηδες', 'τσοπαναραίοι'},
                             'voc': {'τσοπάνηδες', 'τσοπαναραίοι'}},
                      'sg': {'acc': {'τσοπάνη'},
                             'gen': {'τσοπάνη'},
                             'nom': {'τσοπάνης'},
                             'voc': {'τσοπάνη'}}}}

        )

    def test_noun_noikokurhs(self):
        self.assertDictEqual(
            noun.create_all('νοικοκύρης'),
            {'masc': {'pl': {'acc': {'νοικοκύρηδες', 'νοικοκυραίους'},
                             'gen': {'νοικοκυραίων', 'νοικοκύρηδων'},
                             'nom': {'νοικοκυραίοι', 'νοικοκύρηδες'},
                             'voc': {'νοικοκυραίοι', 'νοικοκύρηδες'}},
                      'sg': {'acc': {'νοικοκύρη'},
                             'gen': {'νοικοκύρη'},
                             'nom': {'νοικοκύρης'},
                             'voc': {'νοικοκύρη'}}}}

        )

    def test_noun_laxeiopolis(self):
        self.assertDictEqual(
            noun.create_all('λαχειοπώλης'),
            {'masc': {'pl': {'acc': {'λαχειοπώλες', 'λαχειοπώληδες'},
                             'gen': {'λαχειοπώληδων', 'λαχειοπωλών'},
                             'nom': {'λαχειοπώλες', 'λαχειοπώληδες'},
                             'voc': {'λαχειοπώλες', 'λαχειοπώληδες'}},
                      'sg': {'acc': {'λαχειοπώλη'},
                             'gen': {'λαχειοπώλη'},
                             'nom': {'λαχειοπώλης'},
                             'voc': {'λαχειοπώλη'}}}}

        )

    def test_noun_xorofulakas(self):
        self.assertDictEqual(
            noun.create_all('χωροφύλακας'),
            {'masc': {'pl': {'acc': {'χωροφυλάκους', 'χωροφύλακες'},
                             'gen': {'χωροφυλάκων'},
                             'nom': {'χωροφυλάκοι', 'χωροφύλακες'},
                             'voc': {'χωροφυλάκοι', 'χωροφύλακες'}},
                      'sg': {'acc': {'χωροφύλακα'},
                             'gen': {'χωροφύλακα'},
                             'nom': {'χωροφύλακας'},
                             'voc': {'χωροφύλακα'}}}}

        )

    def test_noun_pateras(self):
        self.assertDictEqual(
            noun.create_all('πατέρας'),
            {'masc': {'pl': {'acc': {'πατέρες', 'πατεράδες'},
                             'gen': {'πατεράδων', 'πατέρων'},
                             'nom': {'πατέρες', 'πατεράδες'},
                             'voc': {'πατέρες', 'πατεράδες'}},
                      'sg': {'acc': {'πατέρα'},
                             'gen': {'πατέρα', 'πατρός'},
                             'nom': {'πατέρας'},
                             'voc': {'πατέρα', 'πάτερ'}}}}

        )

    def test_noun_aeras(self):
        self.assertDictEqual(
            noun.create_all('αέρας'),
            {'masc': {'pl': {'acc': {'αέρηδες', 'αέρες'},
                             'gen': {'αέρων', 'αέρηδων'},
                             'nom': {'αέρηδες', 'αέρες'},
                             'voc': {'αέρηδες', 'αέρες'}},
                      'sg': {'acc': {'αέρα'},
                             'gen': {'αέρα', 'αέρος'},
                             'nom': {'αέρας'},
                             'voc': {'αέρα'}}}}

        )

    def test_noun_thyronoiksia(self):
        """with pluralia tantum you have to say it explicitly"""
        self.assertDictEqual(
            noun.create_all('θυρανοίξια', gender=NEUT_PL),
            {'neut': {
                'pl': {'voc': {'θυρανοίξια'}, 'acc': {'θυρανοίξια'}, 'gen': {'θυρανοιξιών'}, 'nom': {'θυρανοίξια'}},
                'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}}}}
        )

    def test_noun_xaos(self):
        """-os neuter sg tantum"""
        self.assertDictEqual(
            noun.create_all('χάος', gender=NEUT_SG),
            {'neut': {
                'pl': {'acc': {''}, 'nom': {''}, 'voc': {''}},
                'sg': {'acc': {'χάος'}, 'gen': {'χάους'}, 'nom': {'χάος'}, 'voc': {'χάος'}}}
            }
        )

    def test_noun_olon(self):
        """-on neuter sg tantum"""
        self.assertDictEqual(
            noun.create_all('όλον', gender=NEUT_SG),
            {'neut':
                 {'pl':
                      {'acc': {''}, 'nom': {''}, 'voc': {''}},
                  'sg':
                      {'acc': {'όλον'}, 'gen': {'όλου'}, 'nom': {'όλον'}, 'voc': {'όλον'}}
                  }
             })



    def test_noun_paron(self):
        self.assertDictEqual(
            noun.create_all('παρόν', gender=NEUT),
            {'neut': {'pl': {'acc': {'παρόντα'},
                             'gen': {'παρόντων'},
                             'nom': {'παρόντα'},
                             'voc': {'παρόντα'}},
                      'sg': {'acc': {'παρόν'},
                             'gen': {'παρόντος'},
                             'nom': {'παρόν'},
                             'voc': {'παρόν'}}}},

        )

    def test_noun_alieus(self):
        self.assertDictEqual(noun.create_all('αλιεύς'),
            {'masc': {'pl': {'acc': {'αλιείς'},
                             'gen': {'αλιέων'},
                             'nom': {'αλιείς'},
                             'voc': {'αλιείς'}},
                      'sg': {'acc': {'αλιέα'},
                             'gen': {'αλιέως'},
                             'nom': {'αλιεύς'},
                             'voc': {'αλιεύ'}}}}

        )

    def test_noun_hmifws(self):
        """-ws neuter sg tantum"""
        self.assertDictEqual(
            noun.create_all('ημίφως', gender=NEUT_SG),
            {'neut':
                 {'pl':
                      {'acc': {''}, 'nom': {''}, 'voc': {''}},
                  'sg': {'acc': {'ημίφως'}, 'gen': {'ημίφωτος'}, 'nom': {'ημίφως'}, 'voc': {'ημίφως'}}}}
        )

    def test_noun_alytarchos(self):
        self.assertDictEqual(
            noun.create_all('αλύταρχος', gender=MASC),
            {'masc': {'sg': {'nom': {'αλύταρχος'}, 'acc': {'αλύταρχο'}, 'voc': {'αλύταρχε'}, 'gen': {'αλύταρχου'}},
                      'pl': {'nom': {'αλύταρχοι'}, 'acc': {'αλύταρχους'}, 'voc': {'αλύταρχοι'}, 'gen': {'αλύταρχων'}}}}
        )

    def test_noun_estiator(self):
        self.assertDictEqual(
            noun.create_all('εστιάτωρ'),
            {'masc': {'sg': {'gen': {'εστιάτορος'}, 'acc': {'εστιάτορα'}, 'voc': {'εστιάτορ'}, 'nom': {'εστιάτωρ'}},
                      'pl': {'gen': {'εστιατόρων'}, 'acc': {'εστιάτορες'}, 'voc': {'εστιάτορες'},
                             'nom': {'εστιάτορες'}}}}
        )

    def test_noun_kontes(self):
        self.assertDictEqual(
            noun.create_all('κόντες'),
            {'masc': {'pl': {'nom': {'κόντηδες'}, 'gen': {'κόντηδων'}, 'voc': {'κόντηδες'}, 'acc': {'κόντηδες'}},
                      'sg': {'nom': {'κόντες'}, 'gen': {'κόντε'}, 'voc': {'κόντε'}, 'acc': {'κόντε'}}}}
        )

    def test_noun_belhnekes(self):
        self.assertDictEqual(
            noun.create_all('βεληνεκές'),
            {'neut': {'pl': {'gen': {'βεληνεκών'}, 'voc': {'βεληνεκή'}, 'acc': {'βεληνεκή'}, 'nom': {'βεληνεκή'}},
                      'sg': {'gen': {'βεληνεκούς'}, 'voc': {'βεληνεκές'}, 'acc': {'βεληνεκές'}, 'nom': {'βεληνεκές'}}}}
        )

    def test_noun_pappous(self):
        self.assertDictEqual(
            noun.create_all('παππούς'),
            {'masc': {'pl': {'acc': {'παππούδες'},
                             'gen': {'παππούδων'},
                             'nom': {'παππούδες'},
                             'voc': {'παππούδες'}},
                      'sg': {'acc': {'παππού'},
                             'gen': {'παππού'},
                             'nom': {'παππούς'},
                             'voc': {'παππού'}}}}

        )

    def test_noun_asthenhs(self):
        self.assertDictEqual(
            noun.create_all('ασθενής'),
            {'fem': {'pl': {'acc': {'ασθενείς'},
                            'gen': {'ασθενών'},
                            'nom': {'ασθενείς'},
                            'voc': {'ασθενείς'}},
                     'sg': {'acc': {'ασθενή'},
                            'gen': {'ασθενούς'},
                            'nom': {'ασθενής'},
                            'voc': {'ασθενή'}}},
             'masc': {'pl': {'acc': {'ασθενείς'},
                             'gen': {'ασθενών'},
                             'nom': {'ασθενείς'},
                             'voc': {'ασθενείς'}},
                      'sg': {'acc': {'ασθενή'},
                             'gen': {'ασθενούς', 'ασθενή'},
                             'nom': {'ασθενής'},
                             'voc': {'ασθενή'}}}}

        )

    def test_noun_afenths(self):
        self.assertDictEqual(
            noun.create_all('αφέντης'),
            {'masc': {'pl': {'acc': {'αφεντάδες', 'αφέντες'},
                             'gen': {'αφεντών', 'αφεντάδων'},
                             'nom': {'αφεντάδες', 'αφέντες'},
                             'voc': {'αφεντάδες', 'αφέντες'}},
                      'sg': {'acc': {'αφέντη'},
                             'gen': {'αφέντη'},
                             'nom': {'αφέντης'},
                             'voc': {'αφέντη'}}}}

        )

    def test_noun_bhks(self):
        self.assertDictEqual(
            noun.create_all('βηξ', gender=MASC),
            {'masc': {'pl': {'acc': {'βήχες'},
                             'gen': {'βηχών'},
                             'nom': {'βήχες'},
                             'voc': {'βήχες'}},
                      'sg': {'acc': {'βήχα'},
                             'gen': {'βηχός'},
                             'nom': {'βηξ'},
                             'voc': {'βηξ'}}}}

        )

    def test_noun_gymnasiarxhs(self):
        self.assertDictEqual(
            noun.create_all('γυμνασιάρχης', gender=MASC),
            {'masc': {
                'sg': {'acc': {'γυμνασιάρχη'}, 'gen': {'γυμνασιάρχη'}, 'voc': {'γυμνασιάρχα'}, 'nom': {'γυμνασιάρχης'}},
                'pl': {'acc': {'γυμνασιάρχες'}, 'gen': {'γυμνασιαρχών'}, 'voc': {'γυμνασιάρχες'},
                       'nom': {'γυμνασιάρχες'}}}},
        )

    def test_noun_andras(self):
        self.assertDictEqual(
            noun.create_all('άνδρας'),
            {'masc': {'pl': {'acc': {'άνδρες'}, 'gen': {'ανδρών'}, 'voc': {'άνδρες'}, 'nom': {'άνδρες'}},
                      'sg': {'nom': {'άνδρας'}, 'gen': {'άνδρα', 'ανδρός'}, 'acc': {'άνδρα'}, 'voc': {'άνδρα'}}}}
        )

    def test_noun_paidi(self):
        self.assertDictEqual(
            noun.create_all('παιδί'),
            {'neut': {'sg': {'nom': {'παιδί'}, 'acc': {'παιδί'}, 'voc': {'παιδί'}, 'gen': {'παιδιού'}},
                      'pl': {'nom': {'παιδιά'}, 'acc': {'παιδιά'}, 'voc': {'παιδιά'}, 'gen': {'παιδιών'}}}},
        )


    def test_noun_dolario(self):
        self.assertDictEqual(
            noun.create_all('δολάριο'),
            {'neut': {'pl': {'gen': {'δολαρίων'}, 'acc': {'δολάρια'}, 'nom': {'δολάρια'}, 'voc': {'δολάρια'}},
                      'sg': {'gen': {'δολαρίου'}, 'acc': {'δολάριο'}, 'nom': {'δολάριο'}, 'voc': {'δολάριο'}}}}
        )

    def test_noun_mathima(self):
        self.assertDictEqual(
            noun.create_all('μάθημα'),
            {'neut': {'sg': {'gen': {'μαθήματος'}, 'acc': {'μάθημα'}, 'nom': {'μάθημα'}, 'voc': {'μάθημα'}},
                      'pl': {'gen': {'μαθημάτων'}, 'acc': {'μαθήματα'}, 'nom': {'μαθήματα'}, 'voc': {'μαθήματα'}}}}
        )

    def test_noun_yperthima(self):
        """
        sometimes there are no inflected form in our greek_corpus, in this situation gender info is required in order
        generate correct forms
        """
        self.assertDictEqual(
            noun.create_all('υπέρθημα', gender=NEUT),
            {'neut': {'sg': {'nom': {'υπέρθημα'}, 'gen': {'υπερθήματος'}, 'voc': {'υπέρθημα'}, 'acc': {'υπέρθημα'}},
                      'pl': {'nom': {'υπερθήματα'}, 'gen': {'υπερθημάτων'}, 'acc': {'υπερθήματα'},
                             'voc': {'υπερθήματα'}}}},
        )

    def test_noun_lathos(self):
        self.assertDictEqual(
            noun.create_all('λάθος'),
            {'neut': {'sg': {'voc': {'λάθος'}, 'nom': {'λάθος'}, 'gen': {'λάθους'}, 'acc': {'λάθος'}},
                      'pl': {'voc': {'λάθη'}, 'nom': {'λάθη'}, 'gen': {'λαθών'}, 'acc': {'λάθη'}}}}

        )

    def test_noun_grammateas(self):
        self.assertDictEqual(
            noun.create_all('γραμματέας', gender=MASC_FEM),
            {'masc': {
                'pl': {'voc': {'γραμματείς'}, 'nom': {'γραμματείς'}, 'acc': {'γραμματείς'}, 'gen': {'γραμματέων'}},
                'sg': {'voc': {'γραμματέα'}, 'nom': {'γραμματέας'}, 'acc': {'γραμματέα'},
                       'gen': {'γραμματέα', 'γραμματέως'}}},
                'fem': {
                    'pl': {'voc': {'γραμματείς'}, 'nom': {'γραμματείς'}, 'acc': {'γραμματείς'}, 'gen': {'γραμματέων'}},
                    'sg': {'voc': {'γραμματέα'}, 'nom': {'γραμματέας'}, 'acc': {'γραμματέα'},
                           'gen': {'γραμματέως'}}}},
        )

    def test_noun_synenteuksi(self):
        self.assertDictEqual(
            noun.create_all('συνέντευξη'),
            {'fem': {'sg': {'nom': {'συνέντευξη'}, 'gen': {'συνέντευξης', 'συνεντεύξεως'}, 'voc': {'συνέντευξη'},
                            'acc': {'συνέντευξη'}},
                     'pl': {'nom': {'συνεντεύξεις'}, 'gen': {'συνεντεύξεων'}, 'voc': {'συνεντεύξεις'},
                            'acc': {'συνεντεύξεις'}}}}
        )

    def test_noun_anthropos(self):
        self.assertDictEqual(
            noun.create_all('άνθρωπος'),
            {'masc': {'sg': {'nom': {'άνθρωπος'}, 'gen': {'ανθρώπου'}, 'acc': {'άνθρωπο'}, 'voc': {'άνθρωπε'}},
                      'pl': {'nom': {'άνθρωποι'}, 'gen': {'ανθρώπων'}, 'acc': {'ανθρώπους'}, 'voc': {'άνθρωποι'}}}}
        )

    def test_noun_arxaiologos(self):
        self.assertDictEqual(
            noun.create_all('αρχαιολόγος', gender=MASC_FEM),
            {'fem': {
                'sg': {'acc': {'αρχαιολόγο'}, 'gen': {'αρχαιολόγου'}, 'voc': {'αρχαιολόγε'}, 'nom': {'αρχαιολόγος'}},
                'pl': {'acc': {'αρχαιολόγους'}, 'gen': {'αρχαιολόγων'}, 'voc': {'αρχαιολόγοι'},
                       'nom': {'αρχαιολόγοι'}}}, 'masc': {
                'sg': {'acc': {'αρχαιολόγο'}, 'gen': {'αρχαιολόγου'}, 'voc': {'αρχαιολόγε'}, 'nom': {'αρχαιολόγος'}},
                'pl': {'acc': {'αρχαιολόγους'}, 'gen': {'αρχαιολόγων'}, 'voc': {'αρχαιολόγοι'},
                       'nom': {'αρχαιολόγοι'}}}}
        )

    def test_noun_psifos(self):
        self.assertDictEqual(
            noun.create_all('ψήφος'),
            {'fem': {'pl': {'acc': {'ψήφους'}, 'gen': {'ψήφων'}, 'voc': {'ψήφοι'}, 'nom': {'ψήφοι'}},
                     'sg': {'voc': {'ψήφε'}, 'gen': {'ψήφου'}, 'acc': {'ψήφο'}, 'nom': {'ψήφος'}}}}
        )

    def test_noun_nipiagogos(self):
        self.assertDictEqual(
            noun.create_all('νηπιαγογός', gender=MASC_FEM),
            {'fem': {'sg': {'acc': {'νηπιαγογό'}, 'nom': {'νηπιαγογός'}, 'voc': {'νηπιαγογέ'}, 'gen': {'νηπιαγογού'}},
                     'pl': {'acc': {'νηπιαγογούς'}, 'nom': {'νηπιαγογοί'}, 'voc': {'νηπιαγογοί'},
                            'gen': {'νηπιαγογών'}}},
             'masc': {'sg': {'acc': {'νηπιαγογό'}, 'nom': {'νηπιαγογός'}, 'voc': {'νηπιαγογέ'}, 'gen': {'νηπιαγογού'}},
                      'pl': {'acc': {'νηπιαγογούς'}, 'nom': {'νηπιαγογοί'}, 'voc': {'νηπιαγογοί'},
                             'gen': {'νηπιαγογών'}}}}
        )

    def test_noun_ipologistis(self):
        self.assertDictEqual(
            noun.create_all('υπολογιστής'),
            {'masc': {
                'sg': {'voc': {'υπολογιστή'}, 'gen': {'υπολογιστή'}, 'acc': {'υπολογιστή'}, 'nom': {'υπολογιστής'}},
                'pl': {'voc': {'υπολογιστές'}, 'gen': {'υπολογιστών'}, 'acc': {'υπολογιστές'}, 'nom': {'υπολογιστές'}}}}
        )

    def test_noun_taksitzis(self):
        self.assertDictEqual(
            noun.create_all('ταξιτζής'),
            {'masc': {
                'pl': {'gen': {'ταξιτζήδων'}, 'acc': {'ταξιτζήδες'}, 'nom': {'ταξιτζήδες'}, 'voc': {'ταξιτζήδες'}},
                'sg': {'gen': {'ταξιτζή'}, 'acc': {'ταξιτζή'}, 'nom': {'ταξιτζής'}, 'voc': {'ταξιτζή'}}}}
        )

    def test_noun_anaptiras(self):
        self.assertDictEqual(
            noun.create_all('αναπτήρας'),
            {'masc': {'sg': {'acc': {'αναπτήρα'}, 'voc': {'αναπτήρα'}, 'nom': {'αναπτήρας'}, 'gen': {'αναπτήρα'}},
                      'pl': {'acc': {'αναπτήρες'}, 'voc': {'αναπτήρες'}, 'nom': {'αναπτήρες'}, 'gen': {'αναπτήρων'}}}}
        )

    def test_noun_euro(self):
        self.assertDictEqual(
            noun.create_all('ευρώ', aklito=True),
            {'neut': {'sg': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}},
                      'pl': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}}}}
        )

    def test_noun_filakas(self):
        self.assertDictEqual(
            noun.create_all('φύλακας', gender=MASC_FEM),
            {'fem': {'pl': {'acc': {'φύλακες'},
                            'gen': {'φυλάκων'},
                            'nom': {'φύλακες'},
                            'voc': {'φύλακες'}},
                     'sg': {'acc': {'φύλακα'},
                            'gen': {'φύλακος'},
                            'nom': {'φύλακας'},
                            'voc': {'φύλακα'}}},
             'masc': {'pl': {'acc': {'φύλακες'},
                             'gen': {'φυλάκων'},
                             'nom': {'φύλακες'},
                             'voc': {'φύλακες'}},
                      'sg': {'acc': {'φύλακα'},
                             'gen': {'φύλακος', 'φύλακα'},
                             'nom': {'φύλακας'},
                             'voc': {'φύλακα'}}}}

        )

    def test_noun_purosbesths(self):
        self.assertDictEqual(
            noun.create_all('πυροσβεστής', gender=MASC_FEM),
            {'fem': {'pl': {'acc': {'πυροσβεστές'},
                            'gen': {'πυροσβεστών'},
                            'nom': {'πυροσβεστές'},
                            'voc': {'πυροσβεστές'}},
                     'sg': {'acc': {'πυροσβεστή'},
                            'gen': {'πυροσβεστού'},
                            'nom': {'πυροσβεστής'},
                            'voc': {'πυροσβεστή'}}},
             'masc': {'pl': {'acc': {'πυροσβεστές'},
                             'gen': {'πυροσβεστών'},
                             'nom': {'πυροσβεστές'},
                             'voc': {'πυροσβεστές'}},
                      'sg': {'acc': {'πυροσβεστή'},
                             'gen': {'πυροσβεστή', 'πυροσβεστού'},
                             'nom': {'πυροσβεστής'},
                             'voc': {'πυροσβεστή'}}}}

        )

    def test_noun_kafes(self):
        self.assertDictEqual(
            noun.create_all('καφές'),
            {'masc': {'sg': {'voc': {'καφέ'}, 'nom': {'καφές'}, 'gen': {'καφέ'}, 'acc': {'καφέ'}},
                      'pl': {'voc': {'καφέδες'}, 'nom': {'καφέδες'}, 'gen': {'καφέδων'}, 'acc': {'καφέδες'}}}}
        )

    def test_noun_dakru(self):
        self.assertDictEqual(
            noun.create_all('δάκρυ'),
            {'neut': {'pl': {'acc': {'δάκρυα'}, 'nom': {'δάκρυα'}, 'voc': {'δάκρυα'}, 'gen': {'δακρύων'}},
                      'sg': {'gen': {'δακρύου'}, 'nom': {'δάκρυ'}, 'voc': {'δάκρυ'}, 'acc': {'δάκρυ'}}}}
        )

    def test_noun_gegonos(self):
        self.assertDictEqual(
            noun.create_all('γεγονός', gender=NEUT),
            {'neut': {'pl': {'gen': {'γεγονότων'}, 'acc': {'γεγονότα'}, 'nom': {'γεγονότα'}, 'voc': {'γεγονότα'}},
                      'sg': {'gen': {'γεγονότος'}, 'voc': {'γεγονός'}, 'nom': {'γεγονός'}, 'acc': {'γεγονός'}}}}
        )

    def test_noun_fonien(self):
        self.assertDictEqual(
            noun.create_all('φωνήεν', gender=NEUT),
            {'neut': {'pl': {'acc': {'φωνήεντα'}, 'gen': {'φωνηέντων'}, 'nom': {'φωνήεντα'}, 'voc': {'φωνήεντα'}},
                      'sg': {'acc': {'φωνήεν'}, 'gen': {'φωνήεντος'}, 'nom': {'φωνήεν'}, 'voc': {'φωνήεν'}}}},

        )

    def test_noun_oksi(self):
        self.assertDictEqual(
            noun.create_all('οξύ'),
            {'neut': {'pl': {'gen': {'οξέων'}, 'voc': {'οξέα'}, 'nom': {'οξέα'}, 'acc': {'οξέα'}},
                      'sg': {'gen': {'οξέος'}, 'voc': {'οξύ'}, 'nom': {'οξύ'}, 'acc': {'οξύ'}}}}
        )

    def test_noun_autokinito(self):
        self.assertDictEqual(
            noun.create_all('αυτοκίνητο'),
            {'neut': {'sg': {'nom': {'αυτοκίνητο'}, 'voc': {'αυτοκίνητο'}, 'gen': {'αυτοκινήτου', 'αυτοκίνητου'},
                             'acc': {'αυτοκίνητο'}},
                      'pl': {'nom': {'αυτοκίνητα'}, 'voc': {'αυτοκίνητα'}, 'gen': {'αυτοκινήτων', 'αυτοκίνητων'},
                             'acc': {'αυτοκίνητα'}}}}
        )

    def test_noun_ous(self):
        self.assertDictEqual(
            noun.create_all('ους'),
            {'neut': {'pl': {'voc': {'ώτα'}, 'nom': {'ώτα'}, 'gen': {'ωτών'}, 'acc': {'ώτα'}},
                      'sg': {'voc': {'ους'}, 'nom': {'ους'}, 'gen': {'ωτός'}, 'acc': {'ους'}}}}
        )

    def test_noun_hmisi(self):
        self.assertDictEqual(
            noun.create_all('ήμισυ'),
            {'neut': {'pl': {'nom': {'ημίσεα'}, 'acc': {'ημίσεα'}, 'voc': {'ημίσεα'}, 'gen': {'ημισέων'}},
                      'sg': {'nom': {'ήμισυ'}, 'gen': {'ημίσεος'}, 'voc': {'ήμισυ'}, 'acc': {'ήμισυ'}}}}
        )

    def test_noun_delear(self):
        self.assertDictEqual(
            noun.create_all('δέλεαρ', gender=NEUT),
            {'neut': {'sg': {'voc': {'δέλεαρ'}, 'nom': {'δέλεαρ'}, 'acc': {'δέλεαρ'}, 'gen': {'δελέατος'}},
                      'pl': {'voc': {'δελέατα'}, 'nom': {'δελέατα'}, 'acc': {'δελέατα'}, 'gen': {'δελεάτων'}}}},
        )

    def test_noun_ekkremon(self):
        self.assertDictEqual(
            noun.create_all('ακρεμών'),
            {'masc': {'pl': {'acc': {'ακρεμόνες'},
                             'gen': {'ακρεμόνων'},
                             'nom': {'ακρεμόνες'},
                             'voc': {'ακρεμόνες'}},
                      'sg': {'acc': {'ακρεμόνα'},
                             'gen': {'ακρεμόνος'},
                             'nom': {'ακρεμών'},
                             'voc': {'ακρεμών'}}}}

        )

    def test_noun_bradupous(self):
        self.assertDictEqual(
            noun.create_all('βραδύπους'),
            {'masc': {'pl': {'acc': {'βραδύποδες'},
                             'gen': {'βραδυπόδων'},
                             'nom': {'βραδύποδες'},
                             'voc': {'βραδύποδες'}},
                      'sg': {'acc': {'βραδύποδα'},
                             'gen': {'βραδύποδος'},
                             'nom': {'βραδύπους'},
                             'voc': {'βραδύπους'}}}}

        )

    def test_noun_ploutos(self):
        self.assertDictEqual(
            noun.create_all('πλούτος'),
            {'masc': {'sg': {'nom': {'πλούτος'}, 'gen': {'πλούτου'}, 'acc': {'πλούτο'}, 'voc': {'πλούτε'}},
                      'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}}},
             'neut': {'pl': {'nom': {'πλούτη'}, 'gen': {'πλουτών'}, 'acc': {'πλούτη'}, 'voc': {'πλούτη'}}}}
        )

    def test_noun_xronos(self):
        self.assertDictEqual(
            noun.create_all('χρόνος'),
            {'masc': {'pl': {'nom': {'χρόνοι'}, 'voc': {'χρόνοι'}, 'acc': {'χρόνους'},
                             'gen': {'χρόνων', 'χρονών', 'χρόνω', 'χρονώ'}},
                      'sg': {'nom': {'χρόνος'}, 'gen': {'χρόνου'}, 'voc': {'χρόνε'}, 'acc': {'χρόνο', 'χρόνον'}}},
             'neut': {'pl': {'nom': {'χρόνια'}, 'voc': {'χρόνια'}, 'acc': {'χρόνια'},
                             'gen': {'χρόνων', 'χρονών', 'χρόνω', 'χρονώ'}}}}
        )

    def test_noun_farfalo(self):
        self.assertDictEqual(
            noun.create_all('φαρφάλω', gender=FEM),
            {'fem': {'pl': {'acc': {'φαρφάλες'}, 'nom': {'φαρφάλες'}, 'voc': {'φαρφάλες'}},
                     'sg': {'acc': {'φαρφάλω'},
                            'gen': {'φαρφάλως'},
                            'nom': {'φαρφάλω'},
                            'voc': {'φαρφάλω'}}}}

        )

    def test_noun_resepsion(self):
        self.assertDictEqual(
            noun.create_all('ρεσεψιόν', gender=FEM, aklito=True),
            {'fem':
                 {'pl':
                      {'voc': {'ρεσεψιόν'}, 'gen': {'ρεσεψιόν'}, 'nom': {'ρεσεψιόν'}, 'acc': {'ρεσεψιόν'}},
                  'sg':
                      {'voc': {'ρεσεψιόν'}, 'gen': {'ρεσεψιόν'}, 'nom': {'ρεσεψιόν'}, 'acc': {'ρεσεψιόν'}}}}

        )

    def test_presbus(self):
        self.assertDictEqual(
            noun.create_all('πρέσβυς', gender=MASC),
            {'masc': {'pl': {'gen': {'πρέσβεων'}, 'nom': {'πρέσβεις'}, 'acc': {'πρέσβεις'}, 'voc': {'πρέσβεις'}},
                      'sg': {'gen': {'πρέσβεως'}, 'nom': {'πρέσβυς'}, 'voc': {'πρέσβυ'}, 'acc': {'πρέσβυν'}}}},

        )

    def test_polis(self):
        self.assertDictEqual(
            noun.create_all('πόλις'),
            {'fem': {'sg': {'nom': {'πόλις'}, 'voc': {'πόλι'}, 'gen': {'πόλεως'}, 'acc': {'πόλιν'}},
                     'pl': {'nom': {'πόλεις'}, 'voc': {'πόλεις'}, 'gen': {'πόλεων'}, 'acc': {'πόλεις'}}}}

        )

    def test_ixthus(self):
        self.assertDictEqual(
            noun.create_all('ιχθύς'),
            {'masc': {'pl': {'acc': {'ιχθύες'},
                         'gen': {'ιχθύων'},
                         'nom': {'ιχθύες'},
                         'voc': {'ιχθύες'}},
                  'sg': {'acc': {'ιχθύ', 'ιχθύν'},
                         'gen': {'ιχθύος'},
                         'nom': {'ιχθύς'},
                         'voc': {'ιχθύ'}}}}

        )

    def test_presbhs(self):
        self.assertDictEqual(
            noun.create_all('πρέσβης'),
            {'fem': {'pl': {'acc': {'πρέσβεις'},
                            'gen': {'πρέσβεων'},
                            'nom': {'πρέσβεις'},
                            'voc': {'πρέσβεις'}},
                     'sg': {'acc': {'πρέσβη'},
                            'gen': {'πρέσβεως'},
                            'nom': {'πρέσβης'},
                            'voc': {'πρέσβη'}}},
             'masc': {'pl': {'acc': {'πρέσβεις'},
                             'gen': {'πρέσβεων'},
                             'nom': {'πρέσβεις'},
                             'voc': {'πρέσβεις'}},
                      'sg': {'acc': {'πρέσβη'},
                             'gen': {'πρέσβη', 'πρέσβεως'},
                             'nom': {'πρέσβης'},
                             'voc': {'πρέσβη'}}}}

        )

    def test_peira(self):
        self.assertDictEqual(
            noun.create_all('ξεχασιά', gender=FEM_SG),
            {'fem': {'pl': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'acc': {'ξεχασιά'},
                            'gen': {'ξεχασιάς'},
                            'nom': {'ξεχασιά'},
                            'voc': {'ξεχασιά'}}}}

        )
