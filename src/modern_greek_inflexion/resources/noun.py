from .variables import *
import os, pickle

this_dir, this_filename = os.path.split(__file__)

"""
     should use this list only if there is no other option, it's too small, but it's better than nothing. 
        Nouns have aklito flag you should use instead (if possible)
"""

n_grammar_lists_path = os.path.join(this_dir, 'lists', 'noun_grammar_lists.pickle')

n_nouns_masc_fem = os.path.join(this_dir, 'lists', 'nouns_masc_fem.pickle')

noun_grammar_lists = pickle.load(open(n_grammar_lists_path, 'rb'))

nouns_masc_fem = pickle.load(open(n_nouns_masc_fem, 'rb'))


aklita_gender = {'μαδιάμ': FEM, 'μωάμεθ': MASC, 'μάνατζερ': MASC, 'σερ': MASC, 'σεφ': MASC,
                 'ντετέκτιβ': MASC, 'ντεντέκτιβ': MASC, 'ρεπόρτερ': MASC, 'πλαζ': FEM,
                 'σεζόν': FEM, 'σπεσιαλιτέ': FEM, 'ρεσεψιόν': FEM}

irregular_nouns = {'σέβας': {NOM_SG: 'σέβας', NOM_PL: 'σέβη', GEN_SG: '', GENDERS: [NEUT]},
                   'σέλας': {NOM_SG: 'σέλας', NOM_PL: 'σέλατα,σέλαα', GEN_SG: 'σέλατος,σέλαος', GENDERS: [NEUT]},
                   'δείλι': {NOM_SG: 'δείλι', NOM_PL: '', GEN_SG: '', GENDERS: [NEUT]},
                   'Πάσχα': {NOM_SG: 'Πάσχα', NOM_PL: '', GEN_SG: '', GENDERS: [NEUT]},
                   'δόρυ': {NOM_SG: 'δόρυ', NOM_PL: 'δόρατα', GEN_SG: 'δόρατος', GENDERS: [NEUT]},
                   'ήμισυ': {NOM_SG: 'ήμισυ', NOM_PL: 'ημίσεα', GEN_SG: 'ημίσεος', GENDERS: [NEUT]},
                   'γης': {NOM_SG: 'γης', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDERS: [FEM]},
                   'γη': {NOM_SG: 'γη', NOM_PL: 'γαίες', GEN_SG: 'γης', GENDERS: [FEM]},
                   'αλλάς': {NOM_SG: 'αλλάς', NOM_PL: 'αλλάντες', GEN_SG: 'αλλάντος', GENDERS: [MASC]},
                   'χρως': {NOM_SG: 'χρως', NOM_PL: '', GEN_SG: 'χρωτός,χρωός', GENDERS: [MASC]},
                   'μάνα': {NOM_SG: 'μάνα', NOM_PL: 'μάνες,μανάδες', GEN_SG: 'μάνας', GENDERS: [FEM]},
                   'πλάνης': {NOM_SG: 'πλάνης', NOM_PL: 'πλάνητες', GEN_SG: 'πλάνητος', GENDERS: [MASC, FEM]},
                   'άστυ': {NOM_SG: 'άστυ', NOM_PL: 'άστη', GEN_SG: 'άστεως', GENDERS: [NEUT]},
                   'βράδυ': {NOM_SG: 'βράδυ', NOM_PL: 'βράδια', GEN_SG: 'βραδιού', GENDERS: [NEUT]},
                   'στάχυ': {NOM_SG: 'στάχυ', NOM_PL: 'στάχυα', GEN_SG: 'σταχυού', GENDERS: [NEUT]},
                   'δίχτυ': {NOM_SG: 'δίχτυ', NOM_PL: 'δίχτυα', GEN_SG: 'διχτυού', GENDERS: [NEUT]},
                   'δάκρυ': {NOM_SG: 'δάκρυ', NOM_PL: 'δάκρυα', GEN_SG: 'δακρύου', GENDERS: [NEUT]},
                   'άλως': {NOM_SG: 'άλως', NOM_PL: '', GEN_SG: 'άλω', GENDERS: [FEM]},
                   'πρωί': {NOM_SG: 'πρωί', NOM_PL: 'πρωινά', GEN_SG: 'πρωινού', GENDERS: [NEUT]},
                   'βράχος': {NOM_SG: 'βράχος', NOM_PL: 'βράχοι,βράχια', GEN_SG: 'βράχου', GENDERS: [MASC]},
                   'λόγος': {NOM_SG: 'λόγος', NOM_PL: 'λόγοι,λόγια', GEN_SG: 'λόγου', GENDERS: [MASC]},
                   'σανός': {NOM_SG: 'σανός', NOM_PL: 'σανά', GEN_SG: 'σάνου', GENDERS: [MASC]},
                   'χρόνος': {NOM_SG: 'χρόνος', NOM_PL: 'χρόνοι,χρόνια', GEN_SG: 'χρόνου', GENDERS: [MASC]},
                   'λαιμός': {NOM_SG: 'λαιμός', NOM_PL: 'λαιμοί,λαιμά', GEN_SG: 'λαιμού', GENDERS: [MASC]},
                   'πλούτος': {NOM_SG: 'πλούτος', NOM_PL: ',πλούτη', GEN_SG: 'πλούτου', GENDERS: [MASC]},
                   'καπνός': {NOM_SG: 'καπνός', NOM_PL: 'καπνοί,καπνά', GEN_SG: 'καπνού', GENDERS: [MASC]},
                   'νιότη': {NOM_SG: 'νιότη', NOM_PL: ',νιότα', GEN_SG: 'νιότης', GENDERS: [MASC]},
                   'γάλα': {NOM_SG: 'γάλα', NOM_PL: 'γάλατα,γάλακτα', GEN_SG: 'γάλατος', GENDERS: [MASC]},
                   'εσπέρας': {NOM_SG: 'εσπέρας', NOM_PL: '', GEN_SG: '', GENDERS: [MASC]},
                   'Γης': {NOM_SG: 'Γης', NOM_PL: 'Γαίες', GEN_SG: 'Γης', GENDERS: [FEM]},
                   'γυνή': {NOM_SG: 'γυνή', NOM_PL: 'γυναίκες', GEN_SG: 'γυναικός', GENDERS: [FEM]},
                   'Ζευς': {NOM_SG: 'Ζευς', NOM_PL: '', GEN_SG: 'Διός,Δίος', GENDERS: [MASC]},
                   'μις': {NOM_SG: 'μις', NOM_PL: 'μις', GEN_SG: 'μις', GENDERS: [MASC]},
                   'συς': {NOM_SG: 'συς', NOM_PL: 'σύες', GEN_SG: 'συός', GENDERS: [MASC]},

                   }

irregular_gen_sg = {'πατέρας': 'πατρός,πατέρα', 'πατήρ': 'πατρός', 'γάλα': 'γάλατος,γάλακτος'}

irregular_voc_sg = {'πατέρας': 'πάτερ,πατέρα', 'πατήρ': 'πάτερ', 'γυνή': 'γύναι'}

irregular_3rd_decl_roots = {'απτέρυξ': 'απτέρυγ', 'κύων': 'κυν', 'είρων': 'είρων', 'ινδικτιών': 'ινδικτιών',
                            'πατήρ': 'πατέρ', 'δρυς': 'δρυ', 'ισχύς': 'ισχύ', "οξύ": "οξέ", 'μήκων': 'μήκων',
                            'ύδωρ': 'ύδατ', 'ους': 'ωτ', 'ρις': 'ριν'}

plur_tant_neut = ('Χριστούγεννα', 'χριστούγεννα', 'νιάτα', 'βαλκάνια', 'Ιωάννινα', 'Γιάννενα', 'Γιάννινα')
