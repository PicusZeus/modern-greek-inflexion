import pickle

file = open('lekseis_kata_pos.pickle', 'rb')
kata_pos = pickle.load(file)
# its a dictionary pos: all words
def kata_pos_show(kata_pos):
    poses = [key for key in kata_pos.keys()]
    print(poses)
    return poses


def show_verbs():
    file = open('all_greek_verbs.pickle', 'rb')
    verbs = pickle.load(file)
    l = len(verbs)
    print(l)
    print(verbs[5000])

def show_nouns():
    file = open('all_greek_nouns.pickle', 'rb')
    nouns = pickle.load(file)
    l = len(nouns)
    print(l)
    print(nouns[2000:2005])


if __name__ == '__main__':
    kata_pos_show(kata_pos)
    #show_nouns()
    #kata_pos_show(kata_pos)
    """
    ['article' - file with all articles enumerated was created manually,
    , 'conj', - done - file contains a simple list with all conj
     'no_tag', - these are not many, either onomatopoeia or words used only in some sayings
     with no clear meanings, or direct borrowings from other languages used as sayings
     in translation logic I would recommend leaving them as they are and giving a 
     transcription, pickle only with a list
      'part', list created, comments in the create_part_list
      , 'excl', list created,
      
        'noun', - done, a list of partially parsed forms {'nom_sg': noun, 'gen_sg': '', 'nom_pl': '', 'gender': ''}
     'prep' done
     , 'adv', done, a simle list, comments in the file
     , 'pron', done, a pickle contains most pron as a list of {'inflected': True, 'forms': {'fem': 'δική', 'masc': 'δικός', 'neut': 'δικό'}}, but personal pronouns being too complicated are in a seprarate file
    'verb' - done - there are partially parsed into basic forms
    , 'quant' done - dictionary, consists of 3 lists     quant = {'quant': [], 'quant_adj': [], 'quant_noun': []}
    , 'properN', done - a list created, but there are not many proper names as of now in my db, in the future it can be expanded
     'adj', done, partially parsed as a list of    adj_temp = {'adj': 'masc,fem,neuter', 'comparative': '', 'adverb': '', 'adverb_comparative': ''}
      'adv,adj*' can be ignored, as they are the same, but much less than those created by adj parsing code
      , 'quant,noun', 'quant,adj', done together with quant
       'pron,noun', only eauto mou, all forms in the all_greek_personal_pron
        'adv,conj', only malista, can be added manually, as its rather a simple adverb
         'adv,adj'] only piotero, which actually doesnt exist, so can be ignored.
    
    
    
    
    """
