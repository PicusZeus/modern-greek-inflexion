from unittest import TestCase

from modern_greek_inflexion import Noun
from modern_greek_inflexion.resources.variables import MASC, NEUT, FEM, FEM_SG, NEUT_SG, NEUT_PL, MASC_FEM


class NounTests(TestCase):

    def test_noun_kalos(self):
        self.assertDictEqual(
            Noun('κάλως', gender=MASC).all(),
            {'masc': {'sg': {'nom': {'κάλως'},
                             'acc': {'κάλων'},
                             'gen': {'κάλω'}, 'voc': {'κάλως'}},
                      'pl': {'nom': {'κάλω'}, 'acc': {'κάλως'}, 'voc': {'κάλω'}, 'gen': {'κάλων'}}}},
        )

    def test_noun_gynaika(self):
        """should return dictionary with all possible cases"""
        self.assertDictEqual(
            Noun('γυναίκα').all(),
            {'fem': {'sg': {'nom': {'γυναίκα'}, 'gen': {'γυναίκας'}, 'voc': {'γυναίκα'}, 'acc': {'γυναίκα'}},
                     'pl': {'nom': {'γυναίκες'}, 'gen': {'γυναικών'}, 'voc': {'γυναίκες'}, 'acc': {'γυναίκες'}}}},
        )

    def test_noun_deka(self):
        self.assertDictEqual(
            Noun('δέκα', gender=NEUT, aklito='aklito').all(),
            {'neut': {'pl': {'nom': {'δέκα'}, 'voc': {'δέκα'}, 'gen': {'δέκα'}, 'acc': {'δέκα'}},
                      'sg': {'nom': {'δέκα'}, 'voc': {'δέκα'}, 'gen': {'δέκα'}, 'acc': {'δέκα'}}}}

        )

    def test_noun_rhgas(self):
        self.assertDictEqual(
            Noun('ρήγας', gender=MASC).all(),
            {'masc':
                 {'sg': {'nom': {'ρήγας'}, 'gen': {'ρήγα'}, 'voc': {'ρήγα'}, 'acc': {'ρήγα'}},
                  'pl': {'nom': {'ρηγάδες'}, 'gen': {'ρηγάδων'}, 'voc': {'ρηγάδες'}, 'acc': {'ρηγάδες'}}}})

    def test_noun_mpousi(self):
        self.assertDictEqual(
            Noun('μπούσι').all(),
            {'neut': {'pl': {'voc': {'μπούσια'}, 'acc': {'μπούσια'}, 'gen': {''}, 'nom': {'μπούσια'}},
                      'sg': {'voc': {'μπούσι'}, 'acc': {'μπούσι'}, 'gen': {''}, 'nom': {'μπούσι'}}}}
        )

    def test_noun_tha(self):
        self.assertDictEqual(
            Noun('θα', gender=NEUT_PL, aklito=True).all(),
            {'neut': {'sg': {'gen': {''}, 'acc': {''}, 'nom': {''}, 'voc': {''}},
                      'pl': {'acc': {'θα'}, 'gen': {'θα'}, 'nom': {'θα'}, 'voc': {'θα'}}}}

        )

    def test_noun_gialakias(self):
        self.assertDictEqual(
            Noun('γυαλάκιας').all(),
            {'masc': {
                'pl': {'nom': {'γυαλάκηδες'}, 'acc': {'γυαλάκηδες'}, 'voc': {'γυαλάκηδες'}, 'gen': {'γυαλάκηδων'}},
                'sg': {'nom': {'γυαλάκιας'}, 'voc': {'γυαλάκια'}, 'gen': {'γυαλάκια'}, 'acc': {'γυαλάκια'}}}},

        )

    def test_noun_kanagias(self):
        self.assertDictEqual(
            Noun('κανάγιας').all(),
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
            Noun('αντίπαπας').all(),
            {'masc': {'pl': {'acc': {'αντιπαπάδες'},
                             'gen': {'αντιπαπάδων'},
                             'nom': {'αντιπαπάδες'},
                             'voc': {'αντιπαπάδες'}},
                      'sg': {'acc': {'αντίπαπα'},
                             'gen': {'αντίπαπα'},
                             'nom': {'αντίπαπας'},
                             'voc': {'αντίπαπα'}}}}
        )

    def test_noun_serbika(self):
        self.assertDictEqual(
            Noun('σερβικά').all(),
            {'neut': {'pl': {'acc': {'σερβικά'},
                             'gen': {'σερβικών'},
                             'nom': {'σερβικά'},
                             'voc': {'σερβικά'}},
                      'sg': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}}}},
        )

    def test_noun_pais(self):
        self.assertDictEqual(
            Noun('παις', gender=MASC).all(),
            {'masc': {'pl': {'acc': {'παίδες'},
                             'gen': {'παίδων'},
                             'nom': {'παίδες'},
                             'voc': {'παίδες'}},
                      'sg': {'acc': {'παίδα'},
                             'gen': {'παιδός'},
                             'nom': {'παις'},
                             'voc': {'παι'}}}},

        )

    def test_noun_egkuos(self):
        self.assertDictEqual(
            Noun('έγκυος', gender=FEM).all(),
            {'fem': {'pl': {'acc': {'εγκύους', 'έγκυους'},
                            'gen': {'εγκύων', 'έγκυων'},
                            'nom': {'έγκυοι'},
                            'voc': {'έγκυοι'}},
                     'sg': {'acc': {'έγκυο'},
                            'gen': {'εγκύου'},
                            'nom': {'έγκυος'},
                            'voc': {'έγκυε'}}}}

        )

    def test_noun_sus(self):
        self.assertDictEqual(
            Noun('συς').all(),
            {'fem': {'pl': {'gen': {'συών'}, 'nom': {'σύες'}, 'voc': {'σύες'}, 'acc': {'σύες'}},
                     'sg': {'gen': {'συός'}, 'nom': {'συς'}, 'voc': {'συ'}, 'acc': {'συ', 'συν'}}},
             'masc': {'pl': {'gen': {'συών'}, 'nom': {'σύες'}, 'voc': {'σύες'}, 'acc': {'σύες'}},
                      'sg': {'gen': {'συός'}, 'nom': {'συς'}, 'voc': {'συ'}, 'acc': {'συ', 'συν'}}}}

        )

    def test_noun_limenarxhs(self):

        self.assertDictEqual(
            Noun('λιμενάρχης', gender=MASC_FEM).all(),
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
            Noun('διαφωνών').all(),
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
            Noun('κηδεμόνας', gender=MASC_FEM).all(),
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
            Noun('ρις').all(),
            {'fem': {'pl': {'acc': {'ρίνες'},
                            'gen': {'ρινών'},
                            'nom': {'ρίνες'},
                            'voc': {'ρίνες'}},
                     'sg': {'acc': {'ρίνα'},
                            'gen': {'ρινός'},
                            'nom': {'ρις'},
                            'voc': {'ρι'}}}}

        )

    def test_noun_orash(self):
        self.assertDictEqual(
            Noun('όραση').all(),
            {'fem': {'pl': {'acc': {'οράσεις'},
                            'gen': {'οράσεων'},
                            'nom': {'οράσεις'},
                            'voc': {'οράσεις'}},
                     'sg': {'acc': {'όραση'},
                            'gen': {'οράσεως', 'όρασης'},
                            'nom': {'όρασις', 'όραση'},
                            'voc': {'όραση'}}}}

        )

    def test_noun_polh(self):
        self.assertDictEqual(
            Noun('πόλη').all(),
            {'fem': {'pl': {'acc': {'πόλεις'},
                            'gen': {'πόλεων'},
                            'nom': {'πόλεις'},
                            'voc': {'πόλεις'}},
                     'sg': {'acc': {'πόλη', 'πόλιν'},
                            'gen': {'πόλεως', 'πόλης'},
                            'nom': {'πόλη', 'πόλις'},
                            'voc': {'πόλη'}}}}

        )

    def test_noun_magio(self):
        self.assertDictEqual(
            Noun('μαγιό', gender=NEUT, aklito=True).all(),
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
            Noun('άνθος').all(),
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
            Noun('άγχος').all(),
            {'neut': {'pl': {'acc': {'άγχη'}, 'nom': {'άγχη'}, 'voc': {'άγχη'}},
                      'sg': {'acc': {'άγχος'},
                             'gen': {'άγχους'},
                             'nom': {'άγχος'},
                             'voc': {'άγχος'}}}}

        )

    def test_noun_embadon(self):
        self.assertDictEqual(
            Noun('εμβαδόν').all(),
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
            Noun('μίλι').all(),
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
            Noun('άλας', gender=NEUT).all(),
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
            Noun('χάρις').all(),
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
            Noun('κατηγορουμένη').all(),
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
            Noun('ερωμένη').all(),
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
            Noun('υπνάκος').all(),
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
            Noun('νύφη').all(),
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
            Noun('βαρύμαγκας').all(),
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
            Noun('αμφορέας').all(),
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
            Noun('πέστροφα').all(),
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
            Noun('αρθρίτιδα').all(),
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
            Noun('μαμά').all(),
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
            Noun('σοφία').all(),
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
            Noun('γιαγιά').all(),
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
            Noun('πείνα').all(),
            {'fem': {'pl': {'acc': {'πείνες'},
                            'gen': {''},
                            'nom': {'πείνες'},
                            'voc': {'πείνες'}},
                     'sg': {'acc': {'πείνα'},
                            'gen': {'πείνας'},
                            'nom': {'πείνα'},
                            'voc': {'πείνα'}}}}

        )


    def test_noun_anthropas(self):
        # laika should not get a gen on os
        self.assertDictEqual(
            Noun("άνθρωπας", gender=MASC).all(),
            {'masc': {'pl': {'acc': {'άνθρωπες'},
                             'gen': {'ανθρώπων'},
                             'nom': {'άνθρωπες'},
                             'voc': {'άνθρωπες'}},
                      'sg': {'acc': {'άνθρωπα'},
                             'gen': {'άνθρωπα'},
                             'nom': {'άνθρωπας'},
                             'voc': {'άνθρωπα'}}}}

        )


    def test_noun_upezwkws(self):
        self.assertDictEqual(
            Noun('υπεζωκώς', gender=MASC).all(),
            {'masc': {'pl': {'acc': {'υπεζωκότες'},
                             'gen': {'υπεζωκότων'},
                             'nom': {'υπεζωκότες'},
                             'voc': {'υπεζωκότες'}},
                      'sg': {'acc': {'υπεζωκότα'},
                             'gen': {'υπεζωκότος'},
                             'nom': {'υπεζωκώς'},
                             'voc': {'υπεζωκώς'}}}},
        )

    def test_noun_therapeuon(self):
        self.assertDictEqual(
            Noun('θεράπων').all(),
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
            Noun('προπάππους').all(),
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
            Noun('απόπλους').all(),
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
            Noun('ρίψασπις', gender=MASC).all(),
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
            Noun('καπετάνιος').all(),
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
            Noun('μπουλούκμπασης').all(),
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
            Noun('πρύτανης', gender=MASC_FEM).all(),
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
            Noun('τσοπάνης').all(),
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
            Noun('νοικοκύρης').all(),
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
            Noun('λαχειοπώλης').all(),
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
            Noun('χωροφύλακας').all(),
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
            Noun('πατέρας').all(),
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
            Noun('αέρας').all(),
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
            Noun('θυρανοίξια', gender=NEUT_PL).all(),
            {'neut': {
                'pl': {'voc': {'θυρανοίξια'}, 'acc': {'θυρανοίξια'}, 'gen': {'θυρανοιξιών'}, 'nom': {'θυρανοίξια'}},
                'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}}}}
        )

    def test_noun_xaos(self):
        """-os neuter sg tantum"""
        self.assertDictEqual(
            Noun('χάος', gender=NEUT_SG).all(),
            {'neut': {
                'pl': {'acc': {''}, 'nom': {''}, 'voc': {''}},
                'sg': {'acc': {'χάος'}, 'gen': {'χάους'}, 'nom': {'χάος'}, 'voc': {'χάος'}}}
            }
        )

    def test_noun_olon(self):
        """-on neuter sg tantum"""
        self.assertDictEqual(
            Noun('όλον', gender=NEUT_SG).all(),
            {'neut':
                 {'pl':
                      {'acc': {''}, 'nom': {''}, 'voc': {''}},
                  'sg':
                      {'acc': {'όλον'}, 'gen': {'όλου'}, 'nom': {'όλον'}, 'voc': {'όλον'}}
                  }
             })

    def test_noun_paron(self):
        self.assertDictEqual(
            Noun('παρόν', gender=NEUT).all(),
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
        self.assertDictEqual(Noun('αλιεύς').all(),
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
            Noun('ημίφως', gender=NEUT_SG).all(),
            {'neut':
                 {'pl':
                      {'acc': {''}, 'nom': {''}, 'voc': {''}},
                  'sg': {'acc': {'ημίφως'}, 'gen': {'ημίφωτος'}, 'nom': {'ημίφως'}, 'voc': {'ημίφως'}}}}
        )

    def test_noun_alytarchos(self):
        self.assertDictEqual(
            Noun('αλύταρχος', gender=MASC).all(),
            {'masc': {'sg': {'nom': {'αλύταρχος'}, 'acc': {'αλύταρχο'}, 'voc': {'αλύταρχε'}, 'gen': {'αλύταρχου'}},
                      'pl': {'nom': {'αλύταρχοι'}, 'acc': {'αλύταρχους'}, 'voc': {'αλύταρχοι'}, 'gen': {'αλύταρχων'}}}}
        )

    def test_noun_estiator(self):
        self.assertDictEqual(
            Noun('εστιάτωρ').all(),
            {'masc': {'sg': {'gen': {'εστιάτορος'}, 'acc': {'εστιάτορα'}, 'voc': {'εστιάτορ'}, 'nom': {'εστιάτωρ'}},
                      'pl': {'gen': {'εστιατόρων'}, 'acc': {'εστιάτορες'}, 'voc': {'εστιάτορες'},
                             'nom': {'εστιάτορες'}}}}
        )

    def test_noun_kontes(self):
        self.assertDictEqual(
            Noun('κόντες').all(),
            {'masc': {'pl': {'nom': {'κόντηδες'}, 'gen': {'κόντηδων'}, 'voc': {'κόντηδες'}, 'acc': {'κόντηδες'}},
                      'sg': {'nom': {'κόντες'}, 'gen': {'κόντε'}, 'voc': {'κόντε'}, 'acc': {'κόντε'}}}}
        )

    def test_noun_belhnekes(self):
        self.assertDictEqual(
            Noun('βεληνεκές').all(),
            {'neut': {'pl': {'gen': {'βεληνεκών'}, 'voc': {'βεληνεκή'}, 'acc': {'βεληνεκή'}, 'nom': {'βεληνεκή'}},
                      'sg': {'gen': {'βεληνεκούς'}, 'voc': {'βεληνεκές'}, 'acc': {'βεληνεκές'}, 'nom': {'βεληνεκές'}}}}
        )

    def test_noun_pappous(self):
        self.assertDictEqual(
            Noun('παππούς').all(),
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
            Noun('ασθενής').all(),
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
            Noun('αφέντης').all(),
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
            Noun('βηξ', gender=MASC).all(),
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
            Noun('γυμνασιάρχης', gender=MASC).all(),
            {'masc': {
                'sg': {'acc': {'γυμνασιάρχη'}, 'gen': {'γυμνασιάρχη'}, 'voc': {'γυμνασιάρχα'}, 'nom': {'γυμνασιάρχης'}},
                'pl': {'acc': {'γυμνασιάρχες'}, 'gen': {'γυμνασιαρχών'}, 'voc': {'γυμνασιάρχες'},
                       'nom': {'γυμνασιάρχες'}}}},
        )

    def test_noun_andras(self):
        self.assertDictEqual(
            Noun('άνδρας').all(),
            {'masc': {'pl': {'acc': {'άνδρες'}, 'gen': {'ανδρών'}, 'voc': {'άνδρες'}, 'nom': {'άνδρες'}},
                      'sg': {'nom': {'άνδρας'}, 'gen': {'άνδρα', 'ανδρός'}, 'acc': {'άνδρα'}, 'voc': {'άνδρα'}}}}
        )

    def test_noun_paidi(self):
        self.assertDictEqual(
            Noun('παιδί').all(),
            {'neut': {'sg': {'nom': {'παιδί'}, 'acc': {'παιδί'}, 'voc': {'παιδί'}, 'gen': {'παιδιού'}},
                      'pl': {'nom': {'παιδιά'}, 'acc': {'παιδιά'}, 'voc': {'παιδιά'}, 'gen': {'παιδιών'}}}},
        )

    def test_noun_dolario(self):
        self.assertDictEqual(
            Noun('δολάριο').all(),
            {'neut': {'pl': {'gen': {'δολαρίων'}, 'acc': {'δολάρια'}, 'nom': {'δολάρια'}, 'voc': {'δολάρια'}},
                      'sg': {'gen': {'δολαρίου'}, 'acc': {'δολάριο'}, 'nom': {'δολάριο'}, 'voc': {'δολάριο'}}}}
        )

    def test_noun_mathima(self):
        self.assertDictEqual(
            Noun('μάθημα').all(),
            {'neut': {'sg': {'gen': {'μαθήματος'}, 'acc': {'μάθημα'}, 'nom': {'μάθημα'}, 'voc': {'μάθημα'}},
                      'pl': {'gen': {'μαθημάτων'}, 'acc': {'μαθήματα'}, 'nom': {'μαθήματα'}, 'voc': {'μαθήματα'}}}}
        )

    def test_noun_yperthima(self):
        """
        sometimes there are no inflected form in our greek_corpus, in this situation gender info is required in order
        generate correct forms
        """
        self.assertDictEqual(
            Noun('υπέρθημα', gender=NEUT).all(),
            {'neut': {'sg': {'nom': {'υπέρθημα'}, 'gen': {'υπερθήματος'}, 'voc': {'υπέρθημα'}, 'acc': {'υπέρθημα'}},
                      'pl': {'nom': {'υπερθήματα'}, 'gen': {'υπερθημάτων'}, 'acc': {'υπερθήματα'},
                             'voc': {'υπερθήματα'}}}},
        )

    def test_noun_lathos(self):
        self.assertDictEqual(
            Noun('λάθος').all(),
            {'neut': {'sg': {'voc': {'λάθος'}, 'nom': {'λάθος'}, 'gen': {'λάθους'}, 'acc': {'λάθος'}},
                      'pl': {'voc': {'λάθη'}, 'nom': {'λάθη'}, 'gen': {'λαθών'}, 'acc': {'λάθη'}}}}

        )

    def test_noun_grammateas(self):
        self.assertDictEqual(
            Noun('γραμματέας', gender=MASC_FEM).all(),
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
            Noun('συνέντευξη').all(),
            {'fem':
                 {'sg': {'nom': {'συνέντευξη', 'συνέντευξις'},
                         'gen': {'συνέντευξης', 'συνεντεύξεως'},
                         'voc': {'συνέντευξη'},
                         'acc': {'συνέντευξη'}},
                  'pl': {'nom': {'συνεντεύξεις'}, 'gen': {'συνεντεύξεων'}, 'voc': {'συνεντεύξεις'},
                         'acc': {'συνεντεύξεις'}}}}
        )

    def test_noun_xarh(self):
        self.assertDictEqual(
            Noun('χρήση').all(),
            {'fem': {'pl': {'nom': {'χρήσεις'}, 'acc': {'χρήσεις'}, 'gen': {'χρήσεων'}, 'voc': {'χρήσεις'}},
                     'sg': {'nom': {'χρήσις', 'χρήση'}, 'acc': {'χρήσιν', 'χρήση'}, 'gen': {'χρήσης', 'χρήσεως'}, 'voc': {'χρήση'}}}}

        )

    def test_noun_anthropos(self):
        self.assertDictEqual(
            Noun('άνθρωπος').all(),
            {'masc': {'sg': {'nom': {'άνθρωπος'}, 'gen': {'ανθρώπου'}, 'acc': {'άνθρωπο'}, 'voc': {'άνθρωπε'}},
                      'pl': {'nom': {'άνθρωποι'}, 'gen': {'ανθρώπων'}, 'acc': {'ανθρώπους'}, 'voc': {'άνθρωποι'}}}}
        )

    def test_noun_arxaiologos(self):
        self.assertDictEqual(
            Noun('αρχαιολόγος', gender=MASC_FEM).all(),
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
            Noun('ψήφος').all(),
            {'fem': {'pl': {'acc': {'ψήφους'}, 'gen': {'ψήφων'}, 'voc': {'ψήφοι'}, 'nom': {'ψήφοι'}},
                     'sg': {'voc': {'ψήφε'}, 'gen': {'ψήφου'}, 'acc': {'ψήφο'}, 'nom': {'ψήφος'}}}}
        )

    def test_noun_nipiagogos(self):
        self.assertDictEqual(
            Noun('νηπιαγογός', gender=MASC_FEM).all(),
            {'fem': {'sg': {'acc': {'νηπιαγογό'}, 'nom': {'νηπιαγογός'}, 'voc': {'νηπιαγογέ'}, 'gen': {'νηπιαγογού'}},
                     'pl': {'acc': {'νηπιαγογούς'}, 'nom': {'νηπιαγογοί'}, 'voc': {'νηπιαγογοί'},
                            'gen': {'νηπιαγογών'}}},
             'masc': {'sg': {'acc': {'νηπιαγογό'}, 'nom': {'νηπιαγογός'}, 'voc': {'νηπιαγογέ'}, 'gen': {'νηπιαγογού'}},
                      'pl': {'acc': {'νηπιαγογούς'}, 'nom': {'νηπιαγογοί'}, 'voc': {'νηπιαγογοί'},
                             'gen': {'νηπιαγογών'}}}}
        )

    def test_noun_ipologistis(self):
        self.assertDictEqual(
            Noun('υπολογιστής').all(),
            {'masc': {
                'sg': {'voc': {'υπολογιστή'}, 'gen': {'υπολογιστή'}, 'acc': {'υπολογιστή'}, 'nom': {'υπολογιστής'}},
                'pl': {'voc': {'υπολογιστές'}, 'gen': {'υπολογιστών'}, 'acc': {'υπολογιστές'}, 'nom': {'υπολογιστές'}}}}
        )

    def test_noun_taksitzis(self):
        self.assertDictEqual(
            Noun('ταξιτζής').all(),
            {'masc': {
                'pl': {'gen': {'ταξιτζήδων'}, 'acc': {'ταξιτζήδες'}, 'nom': {'ταξιτζήδες'}, 'voc': {'ταξιτζήδες'}},
                'sg': {'gen': {'ταξιτζή'}, 'acc': {'ταξιτζή'}, 'nom': {'ταξιτζής'}, 'voc': {'ταξιτζή'}}}}
        )

    def test_noun_anaptiras(self):
        self.assertDictEqual(
            Noun('αναπτήρας').all(),
            {'masc': {'sg': {'acc': {'αναπτήρα'}, 'voc': {'αναπτήρα'}, 'nom': {'αναπτήρας'}, 'gen': {'αναπτήρα'}},
                      'pl': {'acc': {'αναπτήρες'}, 'voc': {'αναπτήρες'}, 'nom': {'αναπτήρες'}, 'gen': {'αναπτήρων'}}}}
        )

    def test_noun_euro(self):
        self.assertDictEqual(
            Noun('ευρώ', aklito=True).all(),
            {'neut': {'sg': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}},
                      'pl': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}}}}
        )

    def test_noun_filakas(self):
        self.assertDictEqual(
            Noun('φύλακας', gender=MASC_FEM).all(),
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
            Noun('πυροσβεστής', gender=MASC_FEM).all(),
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
            Noun('καφές').all(),
            {'masc': {'sg': {'voc': {'καφέ'}, 'nom': {'καφές'}, 'gen': {'καφέ'}, 'acc': {'καφέ'}},
                      'pl': {'voc': {'καφέδες'}, 'nom': {'καφέδες'}, 'gen': {'καφέδων'}, 'acc': {'καφέδες'}}}}
        )

    def test_noun_dakru(self):
        self.assertDictEqual(
            Noun('δάκρυ').all(),
            {'neut': {'pl': {'acc': {'δάκρυα'}, 'nom': {'δάκρυα'}, 'voc': {'δάκρυα'}, 'gen': {'δακρύων'}},
                      'sg': {'gen': {'δακρύου'}, 'nom': {'δάκρυ'}, 'voc': {'δάκρυ'}, 'acc': {'δάκρυ'}}}}
        )

    def test_noun_gegonos(self):
        self.assertDictEqual(
            Noun('γεγονός', gender=NEUT).all(),
            {'neut': {'pl': {'gen': {'γεγονότων'}, 'acc': {'γεγονότα'}, 'nom': {'γεγονότα'}, 'voc': {'γεγονότα'}},
                      'sg': {'gen': {'γεγονότος'}, 'voc': {'γεγονός'}, 'nom': {'γεγονός'}, 'acc': {'γεγονός'}}}}
        )

    def test_noun_fonien(self):
        self.assertDictEqual(
            Noun('φωνήεν', gender=NEUT).all(),
            {'neut': {'pl': {'acc': {'φωνήεντα'}, 'gen': {'φωνηέντων'}, 'nom': {'φωνήεντα'}, 'voc': {'φωνήεντα'}},
                      'sg': {'acc': {'φωνήεν'}, 'gen': {'φωνήεντος'}, 'nom': {'φωνήεν'}, 'voc': {'φωνήεν'}}}},

        )

    def test_noun_oksi(self):
        self.assertDictEqual(
            Noun('οξύ').all(),
            {'neut': {'pl': {'gen': {'οξέων'}, 'voc': {'οξέα'}, 'nom': {'οξέα'}, 'acc': {'οξέα'}},
                      'sg': {'gen': {'οξέος'}, 'voc': {'οξύ'}, 'nom': {'οξύ'}, 'acc': {'οξύ'}}}}
        )

    def test_noun_autokinito(self):
        self.assertDictEqual(
            Noun('αυτοκίνητο').all(),
            {'neut': {'sg': {'nom': {'αυτοκίνητο'}, 'voc': {'αυτοκίνητο'}, 'gen': {'αυτοκινήτου', 'αυτοκίνητου'},
                             'acc': {'αυτοκίνητο'}},
                      'pl': {'nom': {'αυτοκίνητα'}, 'voc': {'αυτοκίνητα'}, 'gen': {'αυτοκινήτων', 'αυτοκίνητων'},
                             'acc': {'αυτοκίνητα'}}}}
        )

    def test_noun_ous(self):
        self.assertDictEqual(
            Noun('ους').all(),
            {'neut': {'pl': {'voc': {'ώτα'}, 'nom': {'ώτα'}, 'gen': {'ωτών'}, 'acc': {'ώτα'}},
                      'sg': {'voc': {'ους'}, 'nom': {'ους'}, 'gen': {'ωτός'}, 'acc': {'ους'}}}}
        )

    def test_noun_hmisi(self):
        self.assertDictEqual(
            Noun('ήμισυ').all(),
            {'neut': {'pl': {'nom': {'ημίσεα'}, 'acc': {'ημίσεα'}, 'voc': {'ημίσεα'}, 'gen': {'ημισέων'}},
                      'sg': {'nom': {'ήμισυ'}, 'gen': {'ημίσεος'}, 'voc': {'ήμισυ'}, 'acc': {'ήμισυ'}}}}
        )

    def test_noun_delear(self):
        self.assertDictEqual(
            Noun('δέλεαρ', gender=NEUT).all(),
            {'neut': {'sg': {'voc': {'δέλεαρ'}, 'nom': {'δέλεαρ'}, 'acc': {'δέλεαρ'}, 'gen': {'δελέατος'}},
                      'pl': {'voc': {'δελέατα'}, 'nom': {'δελέατα'}, 'acc': {'δελέατα'}, 'gen': {'δελεάτων'}}}},
        )

    def test_noun_ekkremon(self):
        self.assertDictEqual(
            Noun('ακρεμών').all(),
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
            Noun('βραδύπους').all(),
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
            Noun('πλούτος').all(),
            {'masc': {'sg': {'nom': {'πλούτος'}, 'gen': {'πλούτου'}, 'acc': {'πλούτο'}, 'voc': {'πλούτε'}},
                      'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}}},
             'neut': {'pl': {'nom': {'πλούτη'}, 'gen': {'πλουτών'}, 'acc': {'πλούτη'}, 'voc': {'πλούτη'}}}}
        )

    def test_noun_xronos(self):
        self.assertDictEqual(
            Noun('χρόνος').all(),
            {'masc': {'pl': {'nom': {'χρόνοι'}, 'voc': {'χρόνοι'}, 'acc': {'χρόνους'},
                             'gen': {'χρόνων', 'χρονών', 'χρόνω', 'χρονώ'}},
                      'sg': {'nom': {'χρόνος'}, 'gen': {'χρόνου'}, 'voc': {'χρόνε'}, 'acc': {'χρόνο', 'χρόνον'}}},
             'neut': {'pl': {'nom': {'χρόνια'}, 'voc': {'χρόνια'}, 'acc': {'χρόνια'},
                             'gen': {'χρόνων', 'χρονών', 'χρόνω', 'χρονώ'}}}},
            # ic(Noun('χρόνος'))
        )

    def test_noun_farfalo(self):
        self.assertDictEqual(
            Noun('φαρφάλω', gender=FEM).all(),
            {'fem': {'pl': {'acc': {'φαρφάλες'}, 'nom': {'φαρφάλες'}, 'voc': {'φαρφάλες'}},
                     'sg': {'acc': {'φαρφάλω'},
                            'gen': {'φαρφάλως'},
                            'nom': {'φαρφάλω'},
                            'voc': {'φαρφάλω'}}}}

        )

    def test_noun_resepsion(self):
        self.assertDictEqual(
            Noun('ρεσεψιόν', gender=FEM, aklito=True).all(),
            {'fem':
                 {'pl':
                      {'voc': {'ρεσεψιόν'}, 'gen': {'ρεσεψιόν'}, 'nom': {'ρεσεψιόν'}, 'acc': {'ρεσεψιόν'}},
                  'sg':
                      {'voc': {'ρεσεψιόν'}, 'gen': {'ρεσεψιόν'}, 'nom': {'ρεσεψιόν'}, 'acc': {'ρεσεψιόν'}}}}

        )

    def test_presbus(self):
        self.assertDictEqual(
            Noun('πρέσβυς', gender=MASC).all(),
            {'masc': {'pl': {'gen': {'πρέσβεων'}, 'nom': {'πρέσβεις'}, 'acc': {'πρέσβεις'}, 'voc': {'πρέσβεις'}},
                      'sg': {'gen': {'πρέσβεως'}, 'nom': {'πρέσβυς'}, 'voc': {'πρέσβυ'}, 'acc': {'πρέσβυν'}}}},

        )

    def test_polis(self):
        self.assertDictEqual(
            Noun('πόλις').all(),
            {'fem': {'sg': {'nom': {'πόλις'}, 'voc': {'πόλι'}, 'gen': {'πόλεως'}, 'acc': {'πόλιν'}},
                     'pl': {'nom': {'πόλεις'}, 'voc': {'πόλεις'}, 'gen': {'πόλεων'}, 'acc': {'πόλεις'}}}}

        )

    def test_ixthus(self):
        self.assertDictEqual(
            Noun('ιχθύς').all(),
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
            Noun('πρέσβης').all(),
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
            Noun('ξεχασιά', gender=FEM_SG).all(),
            {'fem': {'pl': {'acc': {''}, 'gen': {''}, 'nom': {''}, 'voc': {''}},
                     'sg': {'acc': {'ξεχασιά'},
                            'gen': {'ξεχασιάς'},
                            'nom': {'ξεχασιά'},
                            'voc': {'ξεχασιά'}}}}

        )
