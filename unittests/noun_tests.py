from unittest import TestCase, main

from modern_greek_inflexion.noun import noun

res = noun.create_all('γυναίκα')
print(res)

class NounTests(TestCase):
    def test_noun_gynaika(self):
        """should return dictionary with all possible cases"""
        self.assertEqual(
            noun.create_all('γυναίκα'),
            {'fem': {'sg': {'nom': 'γυναίκα', 'gen': 'γυναίκας', 'voc': 'γυναίκα', 'acc': 'γυναίκα'},
                     'pl': {'nom': 'γυναίκες', 'acc': 'γυναίκες', 'voc': 'γυναίκες', 'gen': 'γυναικών'}}}

        )

    def test_noun_andras(self):
        self.assertEqual(
            noun.create_all('άνδρας'),
            {'masc': {'pl': {'acc': 'άνδρες',
                             'gen': 'ανδρών',
                             'nom': 'άνδρες',
                             'voc': 'άνδρες'},
                      'sg': {'acc': 'άνδρα',
                             'gen': 'άνδρα',
                             'nom': 'άνδρας',
                             'voc': 'άνδρα'}}}
        )

    def test_noun_paidi(self):

        self.assertEqual(
            noun.create_all('παιδί'),
            {'neut': {'sg': {'nom': 'παιδί', 'gen': 'παιδιού', 'voc': 'παιδί', 'acc': 'παιδί'},
                      'pl': {'nom': 'παιδιά', 'acc': 'παιδιά', 'voc': 'παιδιά', 'gen': 'παιδιών'}}}

        )

    def test_noun_dolario(self):

        self.assertEqual(
            noun.create_all('δολάριο'),
            {'neut': {'sg': {'nom': 'δολάριο', 'gen': 'δολαρίου', 'voc': 'δολάριο', 'acc': 'δολάριο'},
                      'pl': {'nom': 'δολάρια', 'acc': 'δολάρια', 'voc': 'δολάρια', 'gen': 'δολαρίων'}}}

        )

    def test_noun_mathima(self):

        self.assertEqual(
            noun.create_all('μάθημα'),
            {'neut': {'sg': {'nom': 'μάθημα', 'gen': 'μαθήματος', 'voc': 'μάθημα', 'acc': 'μάθημα'},
                      'pl': {'nom': 'μαθήματα', 'acc': 'μαθήματα', 'voc': 'μαθήματα', 'gen': 'μαθημάτων'}}
             }

        )

    def test_noun_lathos(self):

        self.assertEqual(
            noun.create_all('λάθος'),
            {'neut': {'sg': {'nom': 'λάθος', 'gen': 'λάθους', 'voc': 'λάθος', 'acc': 'λάθος'},
                      'pl': {'nom': 'λάθη', 'acc': 'λάθη', 'voc': 'λάθη', 'gen': 'λαθών'}}
             }

        )
    def test_noun_grammateas(self):

        self.assertEqual(
            noun.create_all('γραμματέας'),
            {'masc': {'sg': {'nom': 'γραμματέας', 'gen': 'γραμματέα', 'voc': 'γραμματέα', 'acc': 'γραμματέα'},
                      'pl': {'nom': 'γραμματείς', 'acc': 'γραμματείς', 'voc': 'γραμματείς', 'gen': 'γραμματέων'}},
             'fem': {'sg': {'nom': 'γραμματέας', 'gen': 'γραμματέα,γραμματέως', 'voc': 'γραμματέα', 'acc': 'γραμματέα'},
                     'pl': {'nom': 'γραμματείς', 'acc': 'γραμματείς', 'voc': 'γραμματείς', 'gen': 'γραμματέων'}}}

        )
    def test_noun_synenteuksi(self):

        self.assertEqual(
            noun.create_all('συνέντευξη'),
            {'fem': {'sg': {'nom': 'συνέντευξη', 'gen': 'συνέντευξης,συνεντεύξεως', 'voc': 'συνέντευξη',
                            'acc': 'συνέντευξη'},
                     'pl': {'nom': 'συνεντεύξεις', 'acc': 'συνεντεύξεις', 'voc': 'συνεντεύξεις',
                            'gen': 'συνεντεύξεων'}}}

        )

    def test_noun_anthropos(self):
        self.assertEqual(
            noun.create_all('άνθρωπος'),
            {'masc': {'sg': {'nom': 'άνθρωπος', 'gen': 'ανθρώπου', 'voc': 'άνθρωπε', 'acc': 'άνθρωπο'},
                      'pl': {'nom': 'άνθρωποι', 'acc': 'ανθρώπους', 'voc': 'άνθρωποι', 'gen': 'ανθρώπων'}}}

        )

    def test_noun_arxaiologos(self):
        self.assertEqual(
            noun.create_all('αρχαιολόγος'),
            {'fem': {'sg': {'nom': 'αρχαιολόγος', 'gen': 'αρχαιολόγου', 'voc': 'αρχαιολόγε', 'acc': 'αρχαιολόγο'},
                     'pl': {'nom': 'αρχαιολόγοι', 'acc': 'αρχαιολόγους', 'voc': 'αρχαιολόγοι', 'gen': 'αρχαιολόγων'}},
             'masc': {'sg': {'nom': 'αρχαιολόγος', 'gen': 'αρχαιολόγου', 'voc': 'αρχαιολόγε', 'acc': 'αρχαιολόγο'},
                      'pl': {'nom': 'αρχαιολόγοι', 'acc': 'αρχαιολόγους', 'voc': 'αρχαιολόγοι', 'gen': 'αρχαιολόγων'}}}

        )

    def test_noun_psifos(self):
        self.assertEqual(
            noun.create_all('ψήφος'),
            {'fem': {'sg': {'nom': 'ψήφος', 'gen': 'ψήφου', 'voc': 'ψήφε', 'acc': 'ψήφο'},
                     'pl': {'nom': 'ψήφοι', 'acc': 'ψήφους', 'voc': 'ψήφοι', 'gen': 'ψήφων'}}}

        )
    def test_noun_nipiagogos(self):
        self.assertEqual(
            noun.create_all('νηπιαγογός'),
            {'fem': {'sg': {'nom': 'νηπιαγογός', 'gen': 'νηπιαγογού', 'voc': 'νηπιαγογέ', 'acc': 'νηπιαγογό'},
                     'pl': {'nom': 'νηπιαγογοί', 'acc': 'νηπιαγογούς', 'voc': 'νηπιαγογοί', 'gen': 'νηπιαγογών'}},
             'masc': {'sg': {'nom': 'νηπιαγογός', 'gen': 'νηπιαγογού', 'voc': 'νηπιαγογέ', 'acc': 'νηπιαγογό'},
                      'pl': {'nom': 'νηπιαγογοί', 'acc': 'νηπιαγογούς', 'voc': 'νηπιαγογοί', 'gen': 'νηπιαγογών'}}}
        )

    def test_noun_ipologistis(self):
        self.assertEqual(
            noun.create_all('υπολογιστής'),
            {'masc': {'sg': {'nom': 'υπολογιστής', 'gen': 'υπολογιστή', 'voc': 'υπολογιστή', 'acc': 'υπολογιστή'},
                      'pl': {'nom': 'υπολογιστές', 'acc': 'υπολογιστές', 'voc': 'υπολογιστές', 'gen': 'υπολογιστών'}}}
        )

    def test_noun_taksitzis(self):
        self.assertEqual(
            noun.create_all('ταξιτζής'),
            {'masc': {'sg': {'nom': 'ταξιτζής', 'gen': 'ταξιτζή', 'voc': 'ταξιτζή', 'acc': 'ταξιτζή'},
                      'pl': {'nom': 'ταξιτζήδες', 'acc': 'ταξιτζήδες', 'voc': 'ταξιτζήδες', 'gen': 'ταξιτζήδων'}}}

        )

    def test_noun_dasos(self):
        self.assertEqual(
            noun.create_all('δάσος'),
            {'neut': {'sg': {'nom': 'δάσος', 'gen': 'δάσους', 'voc': 'δάσος', 'acc': 'δάσος'},
                      'pl': {'nom': 'δάση', 'acc': 'δάση', 'voc': 'δάση', 'gen': 'δασών'}}}

        )
    def test_noun_basilias(self):
        self.assertEqual(
            noun.create_all('βασιλιάς'),
            {'masc': {'sg': {'nom': 'βασιλιάς', 'gen': 'βασιλιά', 'voc': 'βασιλιά', 'acc': 'βασιλιά'},
                      'pl': {'nom': 'βασιλιάδες', 'acc': 'βασιλιάδες', 'voc': 'βασιλιάδες', 'gen': 'βασιλιάδων'}}}

        )
    def test_noun_anaptiras(self):
        self.assertEqual(
            noun.create_all('αναπτήρας'),
            {'masc': {'sg': {'nom': 'αναπτήρας', 'gen': 'αναπτήρα', 'voc': 'αναπτήρα', 'acc': 'αναπτήρα'},
                      'pl': {'nom': 'αναπτήρες', 'acc': 'αναπτήρες', 'voc': 'αναπτήρες', 'gen': 'αναπτήρων'}}}

        )

    def test_noun_euro(self):
        self.assertEqual(
            noun.create_all('ευρώ'),
            {'neut': {'sg': {'nom': 'ευρώ', 'gen': 'ευρώ', 'voc': 'ευρώ', 'acc': 'ευρώ'},
                      'pl': {'nom': 'ευρώ', 'acc': 'ευρώ', 'voc': 'ευρώ', 'gen': 'ευρώ'}}}

        )

    def test_noun_fournaris(self):
        self.assertEqual(
            noun.create_all('φούρναρης'),
            {'masc': {'sg': {'nom': 'φούρναρης', 'gen': 'φούρναρη', 'voc': 'φούρναρη', 'acc': 'φούρναρη'},
                      'pl': {'nom': 'φουρνάρηδες', 'acc': 'φουρνάρηδες', 'voc': 'φουρνάρηδες', 'gen': 'φουρνάρηδων'}}}

        )

    def test_noun_filakas(self):
        self.assertEqual(
            noun.create_all('φύλακας'),
            {'masc': {'sg': {'nom': 'φύλακας', 'gen': 'φύλακα', 'voc': 'φύλακα', 'acc': 'φύλακα'},
                      'pl': {'nom': 'φύλακες', 'acc': 'φύλακες', 'voc': 'φύλακες', 'gen': 'φυλάκων'}}}

        )

    def test_noun_kafes(self):
        self.assertEqual(
            noun.create_all('καφές'),
            {'masc': {'sg': {'nom': 'καφές', 'gen': 'καφέ', 'voc': 'καφέ', 'acc': 'καφέ'},
                      'pl': {'nom': 'καφέδες', 'acc': 'καφέδες', 'voc': 'καφέδες', 'gen': 'καφέδων'}}}

        )
    def test_noun_dakru(self):
        self.assertEqual(
            noun.create_all('δάκρυ'),
            {'neut': {'sg': {'nom': 'δάκρυ', 'gen': 'δακρύου', 'voc': 'δάκρυ', 'acc': 'δάκρυ'},
                      'pl': {'nom': 'δάκρυα', 'acc': 'δάκρυα', 'voc': 'δάκρυα', 'gen': 'δακρύων'}}}

        )

    def test_noun_gegonos(self):
        self.assertEqual(
            noun.create_all('γεγονός'),
            {'neut': {'sg': {'nom': 'γεγονός', 'gen': 'γεγονότος', 'voc': 'γεγονός', 'acc': 'γεγονός'},
                      'pl': {'nom': 'γεγονότα', 'acc': 'γεγονότα', 'voc': 'γεγονότα', 'gen': 'γεγονότων'}}}

        )

    def test_noun_fonien(self):
        self.assertEqual(
            noun.create_all('φωνήεν'),
            {'neut': {'sg': {'nom': 'φωνήεν', 'gen': 'φωνήεντος', 'voc': 'φωνήεν', 'acc': 'φωνήεν'},
                      'pl': {'nom': 'φωνήεντα', 'acc': 'φωνήεντα', 'voc': 'φωνήεντα', 'gen': 'φωνηέντων'}}}

        )

    def test_noun_oksi(self):
        self.assertEqual(
            noun.create_all('οξύ'),
            {'neut': {'sg': {'nom': 'οξύ', 'gen': 'οξέος', 'voc': 'οξύ', 'acc': 'οξύ'},
                      'pl': {'nom': 'οξέα', 'acc': 'οξέα', 'voc': 'οξέα', 'gen': 'οξέων'}}}

        )

    def test_noun_autokinito(self):
        self.assertEqual(
            noun.create_all('αυτοκίνητο'),
            {'neut': {
                'sg': {'nom': 'αυτοκίνητο', 'gen': 'αυτοκίνητου,αυτοκινήτου', 'voc': 'αυτοκίνητο', 'acc': 'αυτοκίνητο'},
                'pl': {'nom': 'αυτοκίνητα', 'acc': 'αυτοκίνητα', 'voc': 'αυτοκίνητα',
                       'gen': 'αυτοκίνητων,αυτοκινήτων'}}}

        )
    def test_noun_ous(self):
        self.assertEqual(
            noun.create_all('ους'),
            {'neut': {'sg': {'nom': 'ους', 'gen': 'ωτός', 'voc': 'ους', 'acc': 'ους'},
                      'pl': {'nom': 'ώτα', 'acc': 'ώτα', 'voc': 'ώτα', 'gen': 'ωτών'}}}

        )
    def test_noun_hmisi(self):
        self.assertEqual(
            noun.create_all('ήμισυ'),
            {'neut': {'sg': {'nom': 'ήμισυ', 'gen': 'ημίσεος', 'voc': 'ήμισυ', 'acc': 'ήμισυ'},
                      'pl': {'nom': '', 'acc': '', 'voc': '', 'gen': ''}}}

        )
    def test_noun_delear(self):
        self.assertEqual(
            noun.create_all('δέλεαρ'),
            {'neut': {'sg': {'nom': 'δέλεαρ', 'gen': 'δελέατος', 'voc': 'δέλεαρ', 'acc': 'δέλεαρ'},
                      'pl': {'nom': 'δελέατα', 'acc': 'δελέατα', 'voc': 'δελέατα', 'gen': 'δελεάτων'}}}

        )
    def test_noun_ploutos(self):
        self.assertEqual(
            noun.create_all('πλούτος'),
            {'masc': {'sg': {'nom': 'πλούτος', 'gen': 'πλούτου', 'voc': 'πλούτε', 'acc': 'πλούτο'},
                      'pl': {'nom': '', 'acc': '', 'voc': ''}},
             'neut': {'pl': {'nom': 'πλούτη', 'acc': 'πλούτη', 'voc': 'πλούτη', 'gen': 'πλουτών'}}}

        )
    def test_noun_xronos(self):
        self.assertEqual(
            noun.create_all('χρόνος'),
            {'masc': {'sg': {'nom': 'χρόνος', 'gen': 'χρόνου', 'voc': 'χρόνε', 'acc': 'χρόνο,χρόνον'},
                      'pl': {'nom': 'χρόνοι', 'acc': 'χρόνους', 'voc': 'χρόνοι', 'gen': 'χρόνων,χρονών,χρόνω,χρονώ'}},
             'neut': {'pl': {'nom': 'χρόνια', 'acc': 'χρόνια', 'voc': 'χρόνια', 'gen': 'χρόνω,χρόνων,χρονώ,χρονών'}}}

        )


if __name__ == "__main__":
    main()