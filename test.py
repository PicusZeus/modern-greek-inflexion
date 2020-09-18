from adjective import adjective
from noun.create_noun_basic import create_all_basic_noun_forms
from pronoun import create_pron_basic
from pronoun import pronoun
from verb import create_verb_list
from verb.greek_tables import greek_lemmata
from noun import noun
from verb.create_verb_forms import create_all_imperfect_non_passive_personal_forms, create_all_perf_non_past_personal_forms, create_all_past_personal_forms
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


    # for verb in greek_lemmata:
    #     res = create_verb_list.create_all_basic_forms(verb.strip())
    #     presens = res['present']
    #     pers_forms_pres, deponens = create_all_imperfect_non_passive_personal_forms(presens)
    #     if 'conjunctive' in res:
    #         conjunctive = res['conjunctive']
    #         perf_forms_pres = create_all_perf_non_past_personal_forms(conjunctive, deponens=deponens)
    #         print(perf_forms_pres)
    #     if 'aorist' in res:
    #         past_aor = create_all_past_personal_forms(res['aorist'], verb, 'perf', deponens=deponens)
    #         past_par = create_all_past_personal_forms(res['paratatikos'], verb, 'imperf', deponens=deponens)
    # VERBS #
    # check correctness of createing εξερράγη απεστάλη, συνέβη, συνελήφθη
    #     'αντενδείκνυμαι':
    #    'προτίθεμαι':
    #
    # zw = create_all_perf_non_past_personal_forms('ανεβώ')
    # print(zw)
    perf_forms_pres = create_all_imperfect_non_passive_personal_forms('ακούω')
    print(perf_forms_pres)