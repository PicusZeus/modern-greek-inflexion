from modern_greek_inflexion.adjective import adjective
f
if __name__ == '__main__':
    # res = adjective.create_all('ωραίος')
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
    # perf_forms_pres = create_all_perf_non_past_personal_forms('σηκώσω/σηκωθώ')
    # print(perf_forms_pres)

    # res = quantifiers.create_all_adj_quant('εννιακόσια')
    # print(res)
    res = adjective.create_all('ωραίος')
    # res = noun.create_all('Χριστός', proper_name=True)
    print(res)