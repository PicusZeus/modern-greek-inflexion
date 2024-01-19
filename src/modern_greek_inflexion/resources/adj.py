from .variables import *

import os, pickle

this_dir, this_filename = os.path.split(__file__)


n_adj_grammar_lists = os.path.join(this_dir, 'adj_grammar_lists.pickle')


adj_grammar_lists = pickle.load(open(n_adj_grammar_lists, 'rb'))

irregular_comparatives = {'καλό': 'καλύτερος/άριστος',
                          'κακό': 'χειρότερος,ήσσων/χείριστος,ήκιστος',
                          'απλό': 'απλούστερος/απλούστατος',
                          'μεγάλο': 'μεγαλύτερος/μέγιστος',
                          'πολύ': 'περισσότερος/-',
                          'λίγο': 'λιγότερος/ελάχιστος',
                          'μέγα': 'μεγαλύτερος/μέγιστος',
                          'πρώτο': 'πρωτύτερος/πρώτιστος',
                          'ταχύ': 'ταχύτερος/ταχύτατος,τάχιστος'}

irregular_comparative_adverbs = {'κακό': 'χειρότερα,ήσσον,ήττον/κάκιστα,ήκιστα',
                                 'καλό': 'καλύτερα,κάλλιον,κάλλιο/άριστα',
                                 'λίγο': 'λιγότερο/ελάχιστα', 'πολύ': 'περισσότερο/-'}


adj_basic_template = {SG: {
    MASC: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''
    },
    FEM: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''},
    NEUT: {
        NOM: '',
        GEN: '',
        ACC: '',
        VOC: ''}
},
    PL: {
        MASC: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''},
        FEM: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        },
        NEUT: {
            NOM: '',
            GEN: '',
            ACC: '',
            VOC: ''
        }
    }}