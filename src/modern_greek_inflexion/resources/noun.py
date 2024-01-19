from .variables import *
import os, pickle

this_dir, this_filename = os.path.split(__file__)

"""
     should use this list only if there is no other option, it's too small, but it's better than nothing. 
        Nouns have aklito flag you should use instead (if possible)
"""

n_grammar_lists_path = os.path.join(this_dir, 'noun_grammar_lists.pickle')

n_nouns_masc_fem = os.path.join(this_dir, 'nouns_masc_fem.pickle')

noun_grammar_lists = pickle.load(open(n_grammar_lists_path, 'rb'))

nouns_masc_fem = pickle.load(open(n_nouns_masc_fem, 'rb'))


aklita_gender = {'μαδιάμ': FEM, 'μωάμεθ': MASC, 'μάνατζερ': MASC, 'σερ': MASC, 'σεφ': MASC,
                 'ντετέκτιβ': MASC, 'ντεντέκτιβ': MASC, 'ρεπόρτερ': MASC, 'πλαζ': FEM,
                 'σεζόν': FEM, 'σπεσιαλιτέ': FEM, 'ρεσεψιόν': FEM}

irregular_nouns = {'σέβας': {NOM_SG: 'σέβας', NOM_PL: 'σέβη', GEN_SG: '', GENDER: NEUT},
                   'σέλας': {NOM_SG: 'σέλας', NOM_PL: 'σέλατα,σέλαα', GEN_SG: 'σέλατος,σέλαος', GENDER: NEUT},
                   'δείλι': {NOM_SG: 'δείλι', NOM_PL: '', GEN_SG: '', GENDER: NEUT},
                   'Πάσχα': {NOM_SG: 'Πάσχα', NOM_PL: '', GEN_SG: '', GENDER: NEUT},
                   'δόρυ': {NOM_SG: 'δόρυ', NOM_PL: 'δόρατα', GEN_SG: 'δόρατος', GENDER: NEUT},
                   'ήμισυ': {NOM_SG: 'ήμισυ', NOM_PL: 'ημίσεα', GEN_SG: 'ημίσεος', GENDER: NEUT},
                   'γης': {NOM_SG: 'γης', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDER: FEM},
                   'γη': {NOM_SG: 'γη', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDER: FEM},
                   'αλλάς': {NOM_SG: 'αλλάς', NOM_PL: 'αλλάντες', GEN_SG: 'αλλάντος', GENDER: MASC},
                   'χρως': {NOM_SG: 'χρως', NOM_PL: '', GEN_SG: 'χρωτός,χρωός', GENDER: MASC},
                   'κάλως': {NOM_SG: 'κάλως', NOM_PL: 'κάλως', GEN_SG: 'κάλω', GENDER: MASC},
                   'μάνα': {NOM_SG: 'μάνα', NOM_PL: 'μάνες,μανάδες', GEN_SG: 'μάνας', GENDER: FEM},
                   'πλάνης': {NOM_SG: 'πλάνης', NOM_PL: 'πλάνητες', GEN_SG: 'πλάνητος', GENDER: MASC_FEM},
                   'άστυ': {NOM_SG: 'άστυ', NOM_PL: 'άστη', GEN_SG: 'άστεως', GENDER: NEUT},
                   'βράδυ': {NOM_SG: 'βράδυ', NOM_PL: 'βράδια', GEN_SG: 'βραδιού', GENDER: NEUT},
                   'στάχυ': {NOM_SG: 'στάχυ', NOM_PL: 'στάχυα', GEN_SG: 'σταχυού', GENDER: NEUT},
                   'δίχτυ': {NOM_SG: 'δίχτυ', NOM_PL: 'δίχτυα', GEN_SG: 'διχτυού', GENDER: NEUT},
                   'δάκρυ': {NOM_SG: 'δάκρυ', NOM_PL: 'δάκρυα', GEN_SG: 'δακρύου', GENDER: NEUT},
                   'άλως': {NOM_SG: 'άλως', NOM_PL: '', GEN_SG: 'άλω', GENDER: FEM},
                   'πρωί': {NOM_SG: 'πρωί', NOM_PL: 'πρωινά', GEN_SG: 'πρωινού', GENDER: NEUT},
                   'βράχος': {NOM_SG: 'βράχος', NOM_PL: 'βράχοι,βράχια', GEN_SG: 'βράχου', GENDER: MASC},
                   'λόγος': {NOM_SG: 'λόγος', NOM_PL: 'λόγοι,λόγια', GEN_SG: 'λόγου', GENDER: MASC},
                   'σανός': {NOM_SG: 'σανός', NOM_PL: 'σανά', GEN_SG: 'σάνου', GENDER: MASC},
                   'χρόνος': {NOM_SG: 'χρόνος', NOM_PL: 'χρόνοι,χρόνια', GEN_SG: 'χρόνου', GENDER: MASC},
                   'λαιμός': {NOM_SG: 'λαιμός', NOM_PL: 'λαιμοί,λαιμά', GEN_SG: 'λαιμού', GENDER: MASC},
                   'πλούτος': {NOM_SG: 'πλούτος', NOM_PL: ',πλούτη', GEN_SG: 'πλούτου', GENDER: MASC},
                   'καπνός': {NOM_SG: 'καπνός', NOM_PL: 'καπνοί,καπνά', GEN_SG: 'καπνού', GENDER: MASC},
                   'νιότη': {NOM_SG: 'νιότη', NOM_PL: ',νιότα', GEN_SG: 'νιότης', GENDER: MASC},
                   'γάλα': {NOM_SG: 'γάλα', NOM_PL: 'γάλατα,γάλακτα', GEN_SG: 'γάλατος', GENDER: MASC},
                   'εσπέρας': {NOM_SG: 'εσπέρας', NOM_PL: '', GEN_SG: '', GENDER: MASC},
                   'Γης': {NOM_SG: 'Γης', NOM_PL: 'Γαίες', GEN_SG: 'Γης', GENDER: FEM},
                   'γυνή': {NOM_SG: 'γυνή', NOM_PL: 'γυναίκες', GEN_SG: 'γυναικός', GENDER: FEM},
                   'Ζευς': {NOM_SG: 'Ζευς', NOM_PL: '', GEN_SG: 'Διός,Δίος', GENDER: MASC},
                   'μις': {NOM_SG: 'μις', NOM_PL: 'μις', GEN_SG: 'μις', GENDER: MASC},
                   'συς': {NOM_SG: 'συς', NOM_PL: 'σύες', GEN_SG: 'συός', GENDER: MASC},

                   }

irregular_gen_sg = {'πατέρας': 'πατρός,πατέρα', 'πατήρ': 'πατρός', 'γάλα': 'γάλατος,γάλακτος'}

irregular_voc_sg = {'πατέρας': 'πάτερ,πατέρα', 'πατήρ': 'πάτερ', 'γυνή': 'γύναι'}

irregular_3rd_decl_roots = {'απτέρυξ': 'απτέρυγ', 'κύων': 'κυν', 'είρων': 'είρων', 'ινδικτιών': 'ινδικτιών',
                            'πατήρ': 'πατέρ', 'δρυς': 'δρυ', 'ισχύς': 'ισχύ', "οξύ": "οξέ", 'μήκων': 'μήκων',
                            'ύδωρ': 'ύδατ', 'ους': 'ωτ', 'ρις': 'ριν'}

plur_tant_neut = ('Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια', 'Ιωάννινα', 'Γιάννενα', 'Γιάννινα')
