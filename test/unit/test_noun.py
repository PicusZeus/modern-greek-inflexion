from unittest import TestCase
from modern_greek_inflexion.noun import noun


class NounTests(TestCase):
    def test_noun_gynaika(self):
        """should return dictionary with all possible cases"""
        self.assertDictEqual(
            noun.create_all('γυναίκα'),
            {'fem': {'sg': {'nom': {'γυναίκα'}, 'gen': {'γυναίκας'}, 'voc': {'γυναίκα'}, 'acc': {'γυναίκα'}},
                     'pl': {'nom': {'γυναίκες'}, 'gen': {'γυναικών'}, 'voc': {'γυναίκες'}, 'acc': {'γυναίκες'}}}}
        )

    def test_noun_mpousi(self):
        self.assertDictEqual(
            noun.create_all('μπούσι'),
            {'neut': {'pl': {'voc': {'μπούσια'}, 'acc': {'μπούσια'}, 'gen': {''}, 'nom': {'μπούσια'}},
                      'sg': {'voc': {'μπούσι'}, 'acc': {'μπούσι'}, 'gen': {''}, 'nom': {'μπούσι'}}}}
        )

    def test_noun_thyronoiksia(self):
        """with pluralia tantum you have to say it explicitly"""
        self.assertDictEqual(
            noun.create_all('θυρανοίξια', gender='neut_pl'),
            {'neut': {
                'pl': {'voc': {'θυρανοίξια'}, 'acc': {'θυρανοίξια'}, 'gen': {'θυρανοιξίων'}, 'nom': {'θυρανοίξια'}},
                'sg': {'voc': {''}, 'acc': {''}, 'gen': {''}, 'nom': {''}}}}
        )

    def test_noun_alytarchos(self):
        self.assertDictEqual(
            noun.create_all('αλύταρχος', gender='masc'),
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

    def test_noun_asthenhs(self):
        self.assertDictEqual(
            noun.create_all('ασθενής'),
            {'masc': {'sg': {'voc': {'ασθενή'}, 'gen': {'ασθενούς'}, 'nom': {'ασθενής'}, 'acc': {'ασθενή'}},
                      'pl': {'voc': {'ασθενείς'}, 'acc': {'ασθενείς'}, 'nom': {'ασθενείς'}, 'gen': {'ασθενών'}}}}
        )

    def test_noun_gymnasiarxhs(self):
        self.assertDictEqual(
            noun.create_all('γυμνασιάρχης'),
            {'masc': {
                'sg': {'acc': {'γυμνασιάρχη'}, 'gen': {'γυμνασιάρχη'}, 'voc': {'γυμνασιάρχα'}, 'nom': {'γυμνασιάρχης'}},
                'pl': {'acc': {'γυμνασιάρχες'}, 'gen': {'γυμνασιαρχών'}, 'voc': {'γυμνασιάρχες'},
                       'nom': {'γυμνασιάρχες'}}}}
        )

    def test_noun_andras(self):
        self.assertDictEqual(
            noun.create_all('άνδρας'),
            {'masc': {'pl': {'acc': {'άνδρες'}, 'gen': {'ανδρών'}, 'voc': {'άνδρες'}, 'nom': {'άνδρες'}},
                      'sg': {'nom': {'άνδρας'}, 'gen': {'άνδρα'}, 'acc': {'άνδρα'}, 'voc': {'άνδρα'}}}}
        )

    def test_noun_paidi(self):
        self.assertDictEqual(
            noun.create_all('παιδί'),
            {'neut': {'sg': {'nom': {'παιδί'}, 'acc': {'παιδί'}, 'voc': {'παιδί'}, 'gen': {'παιδιού'}},
                      'pl': {'nom': {'παιδιά'}, 'acc': {'παιδιά'}, 'voc': {'παιδιά'}, 'gen': {'παιδιών'}}}}
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
            noun.create_all('υπέρθημα', gender='neut'),
            {'neut': {'sg': {'nom': {'υπέρθημα'}, 'gen': {'υπερθήματος'}, 'voc': {'υπέρθημα'}, 'acc': {'υπέρθημα'}},
                      'pl': {'nom': {'υπερθήματα'}, 'gen': {'υπερθημάτων'}, 'acc': {'υπερθήματα'},
                             'voc': {'υπερθήματα'}}}}
        )

    def test_noun_lathos(self):

        self.assertDictEqual(
            noun.create_all('λάθος'),
            {'neut': {'sg': {'voc': {'λάθος'}, 'nom': {'λάθος'}, 'gen': {'λάθους'}, 'acc': {'λάθος'}},
                      'pl': {'voc': {'λάθη'}, 'nom': {'λάθη'}, 'gen': {'λαθών'}, 'acc': {'λάθη'}}}}
        )

    def test_noun_grammateas(self):

        self.assertDictEqual(
            noun.create_all('γραμματέας'),
            {'masc': {
                'pl': {'voc': {'γραμματείς'}, 'nom': {'γραμματείς'}, 'acc': {'γραμματείς'}, 'gen': {'γραμματέων'}},
                'sg': {'voc': {'γραμματέα'}, 'nom': {'γραμματέας'}, 'acc': {'γραμματέα'}, 'gen': {'γραμματέα'}}},
             'fem': {'pl': {'voc': {'γραμματείς'}, 'nom': {'γραμματείς'}, 'acc': {'γραμματείς'}, 'gen': {'γραμματέων'}},
                     'sg': {'voc': {'γραμματέα'}, 'nom': {'γραμματέας'}, 'acc': {'γραμματέα'},
                            'gen': {'γραμματέα', 'γραμματέως'}}}}
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
            noun.create_all('αρχαιολόγος'),
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
            noun.create_all('νηπιαγογός'),
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
            noun.create_all('ευρώ'),
            {'neut': {'sg': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}},
                      'pl': {'voc': {'ευρώ'}, 'gen': {'ευρώ'}, 'acc': {'ευρώ'}, 'nom': {'ευρώ'}}}}
        )

    def test_noun_filakas(self):
        self.assertDictEqual(
            noun.create_all('φύλακας'),
            {'masc': {'sg': {'voc': {'φύλακα'}, 'acc': {'φύλακα'}, 'nom': {'φύλακας'}, 'gen': {'φύλακα'}},
                      'pl': {'acc': {'φύλακες'}, 'voc': {'φύλακες'}, 'nom': {'φύλακες'}, 'gen': {'φυλάκων'}}}}
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
            noun.create_all('γεγονός'),
            {'neut': {'pl': {'gen': {'γεγονότων'}, 'acc': {'γεγονότα'}, 'nom': {'γεγονότα'}, 'voc': {'γεγονότα'}},
                      'sg': {'gen': {'γεγονότος'}, 'voc': {'γεγονός'}, 'nom': {'γεγονός'}, 'acc': {'γεγονός'}}}}
        )

    def test_noun_fonien(self):
        self.assertDictEqual(
            noun.create_all('φωνήεν'),
            {'neut': {'pl': {'acc': {'φωνήεντα'}, 'gen': {'φωνηέντων'}, 'nom': {'φωνήεντα'}, 'voc': {'φωνήεντα'}},
                      'sg': {'acc': {'φωνήεν'}, 'gen': {'φωνήεντος'}, 'nom': {'φωνήεν'}, 'voc': {'φωνήεν'}}}}
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
            {'neut': {'pl': {'nom': {''}, 'acc': {''}, 'voc': {''}, 'gen': {''}},
                      'sg': {'nom': {'ήμισυ'}, 'gen': {'ημίσεος'}, 'voc': {'ήμισυ'}, 'acc': {'ήμισυ'}}}}
        )

    def test_noun_delear(self):
        self.assertDictEqual(
            noun.create_all('δέλεαρ'),
            {'neut': {'sg': {'voc': {'δέλεαρ'}, 'nom': {'δέλεαρ'}, 'acc': {'δέλεαρ'}, 'gen': {'δελέατος'}},
                      'pl': {'voc': {'δελέατα'}, 'nom': {'δελέατα'}, 'acc': {'δελέατα'}, 'gen': {'δελεάτων'}}}}
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

