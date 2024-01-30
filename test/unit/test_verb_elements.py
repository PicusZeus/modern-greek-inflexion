from unittest import TestCase

from modern_greek_inflexion.verb.create.forms.basic.create_basic_aorist_passive import create_basic_aorist_passive


class VerbTestElements(TestCase):

    def test_aorist_ir(self):
        self.assertEqual(
            create_basic_aorist_passive('φυσάω', 'φυσηθ,φυσηχτ'),
            {'φυσήθηκα', 'φυσήχτηκα'},
        )

    def test_aorist_reg(self):
        self.assertEqual(
            create_basic_aorist_passive('βαστάω', 'βαστηχτ,βασταχτ'),
            {'βαστήχτηκα', 'βαστάχτηκα'}

        )