import pickle
import os
from .variables import *

# these lists should be replaced with one comprehensive data class
this_dir, this_filename = os.path.split(__file__)
el_GR_path = os.path.join(this_dir, 'el_GR.pickle')
# el_GR_path = os.path.join(this_dir, 'big_greek_corpus.pickle')

greek_corpus = pickle.load(open(el_GR_path, 'rb'))

forms_with_alternatives = ('ακόμη', 'ακόμα', 'και', 'κι', 'τίποτα', 'τίποτε')
dictionary_with_alt = {'ακόμη': 'ακόμα', 'και': 'κι', 'τίποτα': 'τίποτε'}

irregular_adv = {
    'νωρίς': {COMP_ADV: 'νωρίτερα/νωρίτατα'}, 'άνω': {COMP_ADV: 'ανώτερα/ανώτατα', COMP: 'ανώτερος/ανώτατος'},
    'κάτω': {COMP_ADV: 'κατώτερα/κατώτατα', COMP: 'κατώτερος/κατώτατος'}}

aklita_num_alternatives = {'εφτά': 'επτά', 'οχτώ': 'οκτώ', 'εννιά': 'εννέα', 'δεκαέξι': 'δεκάξι',
                           'δεκαοχτώ': 'δεκαοκτώ', 'δεκαεννιά': 'δεκαεννέα', 'δεκαεφτά': 'δεκαεπτά'}

# these are not all the irregular verbs, but if you take into account compounds, most.


"""UNUSED"""

greek_pers_pronouns = [

    ['εγώ', ['εγώ', 'ppron12:sg:nom:m.f.n:pri:akc']],
    ['μου', ['εγώ', 'ppron12:sg:gen:m.f.n:pri:nakc:npraep']],
    ['εμένα', ['εγώ', 'ppron12:sg:gen.acc:m.f.n:pri:akc:npraep']],
    ['μένα', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:akc:praep']],
    ['με', ['εγώ', 'ppron12:sg:acc:m.f.n:pri:nakc:npraep']],
    ['εμείς', ['εμείς', 'ppron12:pl:nom:m.f.n:pri:akc']],
    ['εμάς', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:npraep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:akc:praep']],
    ['μας', ['εμείς', 'ppron12:pl:gen.acc:m.f.n:pri:nakc:npraep']],

    ['εσύ', ['εσύ', 'ppron12:sg:nom:m.f.n:sec:akc']],
    ['σου', ['εσύ', 'ppron12:sg:gen:m.f.n:sec:nakc:npraep']],
    ['εσένα', ['εσύ', 'ppron12:sg:gen.acc:m.f.n:sec:akc:npraep']],
    ['σένα', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:akc:praep']],
    ['σε', ['εσύ', 'ppron12:sg:acc:m.f.n:sec:nakc:npraep']],

    ['εσείς', ['εσείς', 'ppron12:pl:nom:m.f.n:sec:akc']],
    ['εσάς', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:akc:npraep']],

    ['σας', ['εσείς', 'ppron12:pl:acc:m.f.n:sec:akc:praep']],

    ['σας', ['εσείς', 'ppron12:pl:gen.acc:m.f.n:sec:nakc:npraep']],

    # nom
    ['αυτός', ['αυτός', 'ppron3:sg:nom:m:ter:akc']],
    ['τoς', ['αυτός', 'ppron3:sg:nom:m:ter:nakc']],
    ['το', ['αυτός', 'ppron3:sg:nom.acc:n:ter:nakc:npraep']],
    ['αυτό', ['αυτός', 'ppron3:sg:nom.acc:n:ter:akc']],
    ['αυτή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:akc']],
    ['τή', ['αυτός', 'ppron3:sg:nom.acc:f:ter:nakc']],
    # gen
    ['αυτού', ['αυτός', 'ppron3:pl:gen:n.m:ter:akc:praep:npraep']],
    ['του', ['αυτός', 'ppron3:sg:gen:n.m:ter:nakc:npraep']],

    ['αυτής', ['αυτός', 'ppron3:sg:gen:f:ter:akc']],
    ['της', ['αυτός', 'ppron3:sg:gen:f:ter:nakc:npraep']],
    # acc
    ['αυτόν', ['αυτός', 'ppron3:sg:acc:m:ter:akc:npraep:praep']],
    ['αυτήν', ['αυτός', 'ppron3:sg:acc:f:ter:akc']],
    ['τήν', ['αυτός', 'ppron3:sg:acc:f:ter:nakc:npraep']],
    ['τον', ['αυτός', 'ppron3:sg:gen:n:ter:nakc:npraep']],

    # nom
    ['αυτοί', ['αυτός', 'ppron3:pl:nom:m:ter:akc']],
    ['αυτές', ['αυτός', 'ppron3:pl:nom.acc:f:ter:akc']],
    ['τοι', ['αυτός', 'ppron3:pl:nom:m:ter:nakc']],
    ['τες', ['αυτός', 'ppron3:pl:nom:f:ter:nakc']],
    ['τα', ['αυτός', 'ppron3:pl:nom.acc:n:ter:nakc:npraep']],
    ['αυτά', ['αυτός', 'ppron3:pl:nom.acc:n:ter:akc']],

    # gen
    ['αυτών', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:akc']],
    ['τους', ['αυτός', 'ppron3:pl:gen:m.f.n:ter:nakc:npraep']],

    # acc
    ['τους', ['αυτός', 'ppron3:pl:acc:m:ter:nakc:npraep']],
    ['αυτούς', ['αυτός', 'ppron3:pl:acc:m:ter:akc']],
    ['τις', ['αυτός', 'ppron3:pl:acc:f:ter:nakc:npraep']],
    ['τες', ['αυτός', 'ppron3:pl:acc:f:ter:nakc:npraep']],

]

quant = ['δύο,δυο', 'έξι', 'δέκα', 'ένας/μία/ένα', 'επτά,εφτά', 'οχτώ,οκτώ', 'δεκαεφτά,δεκαεπτά', 'δεκαοχτώ,δεκαοκτώ',
         'εκατόν,εκατό', 'εννέα,εννιά', 'μηδέν', 'πέντε',
         'τρεις/τρία', 'δεκάξι,δεκαέξι', 'δώδεκα', 'είκοσι', 'ένδεκα,έντεκα', 'εξήντα', 'ογδόντα', 'πενήντα',
         'σαράντα', 'τριάντα', 'ενάμισης/μιάμιση/ενάμισι', 'ενενήντα', 'τέσσερις/τέσσερα', 'δεκαεννέα,δεκαεννιά',
         'δεκαπέντε',
         'δεκατρείς/δεκατρία', 'εβδομήντα', 'δεκατέσσερις/δεκατέσσερα']

quant_adj = ['έκτος', 'διπλός', 'ένατος', 'όγδοος', 'πρώτος', 'πέμπτος', 'τρίτος', 'δέκατος', 'έβδομος', 'εξαπλός',
             'τριπλός', 'δεκαπλός', 'δεύτερος', 'εικοστός', 'επταπλός', 'τέταρτος', 'διπλάσιος', 'δωδέκατος',
             'εκατοστός', 'ενδέκατος', 'εξηκοστός', 'πενταπλός', 'τετραπλός', 'χιλιοστός', 'εξαπλάσιος', 'τριακοστός',
             'τριπλάσιος', 'δεκαπλάσιος', 'ενενηκοστός', 'επταπλάσιος', 'ογδοηκοστός', 'διακοσιοστός', 'εβδομηκοστός',
             'εξακοσιοστός', 'πενταπλάσιος', 'τετραπλάσιος', 'εικοσαπλάσιος', 'ενδεκαπλάσιος', 'τεσσαρακοστός',
             'τριακοσιοστός', 'τετρακοσιοστός', 'εκατομμυριοστός', 'εκατονταπλάσιος']

quant_noun = ['δυάδα', 'εξάδα', 'δεκάδα', 'οκτάδα', 'τριάδα', 'μυριάδα', 'πεντάδα', 'τετράδα', 'χιλιάδα',
              'δωδεκάδα', 'εικοσάδα', 'εικοσαριά', 'εκατοντάδα', 'εκατομμύριο', 'δισεκατομμύριο', 'τρισεκατομμύριο',
              'τετρακισεκατομμύριο', 'πεντακισεκατομμύριο', 'δυάδα', 'εξάδα', 'δεκάδα', 'οκτάδα', 'τριάδα', 'μυριάδα',
              'πεντάδα', 'τετράδα', 'χιλιάδα', 'δωδεκάδα', 'εικοσάδα', 'εικοσαριά', 'εκατοντάδα', 'δισεκατομμύριο',
              'εκατομμύριο', 'τρισεκατομμύριο']

hundreds = ['διακόσια', 'τριακόσια', 'τετρακόσια', 'πεντακόσια', 'εξακόσια', 'εφτακόσια,επτακόσια', 'οχτακόσια',
            'εννιακόσια', 'χίλια']

alternative_syllables = {'οκτ': 'οχτ', 'επτ': 'εφτ'}
