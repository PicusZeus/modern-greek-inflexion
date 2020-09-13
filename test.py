from adjective import adjective
from noun.create_noun_basic import create_all_basic_noun_forms
from pronoun import create_pron_basic
from pronoun import pronoun
from verb import create_verb_list
from verb.greek_tables import greek_lemmata
from noun import noun
if __name__ == '__main__':
    # res = adjective.create_all('ωραίος')
    # print(res)

    # words = ('άνθρωπος', 'αρχαιολόγος', 'ψήφος', 'νηπιαγογός', 'υπολογιστής', 'ταξιτζής', 'δάσος', 'σκέλος', 'αναπτήρας', 'βασιλιάς',
    #          'βασιλεύς', 'μηχανή', 'πόλη', 'κατάσταση', 'λέξη', 'βραδιά', 'δολάριο', 'θέατρο', 'ευρώ', 'βιβλίο', 'παιδί',
    #          'τραπέζι', 'μάθημα', 'ρήμα', 'γράψιμο', 'άστυ', 'Κυριακή',  'αλεπού', 'αγώνας', 'ταμίας', 'φύλακας',
    #          'ψαράς', 'ρήγας', 'ναύτης', 'μαθητής', 'φούρναρης', 'μανάβης', 'παπουτσής', 'δουλευτής', 'συγγενής',
    #          'καφές', 'αντίλαλος', 'άνεμος', 'διάμετρος', 'Φρόσω', 'κυρά', 'κρέας', 'φως', 'γάλα', 'φωνήεν', 'καθήκον',
    #          'καθεστώς', 'δάκρυ', 'γεγονός', 'οξύ', 'ον', 'Ζευς', 'λόγος', 'σανός', 'ους', 'σέλας', 'αφέντης', 'μυς',
    #          'σέβας', 'σέλας', 'δείλι', 'Πάσχα', 'δόρυ', 'αυτοκίνητο', 'ήμισυ', 'οξύ', 'ήπαρ', 'πυρ', 'δέλεαρ', 'σανός',
    #          'χρόνος', 'πλούτος', 'νιότη')
    # for word in words:
    #     res = noun.create_all(word)
    #     print(res)
    #
    # res = create_pron_basic.create_basic_forms('πας')
    # print(res)


    for verb in greek_lemmata:

        res = create_verb_list.create_all_basic_forms(verb.strip())
        print(res)
    # VERBS #
    # check correctness of createing εξερράγη απεστάλη, συνέβη, συνελήφθη
    #     'αντενδείκνυμαι':
    #    'προτίθεμαι':
    #