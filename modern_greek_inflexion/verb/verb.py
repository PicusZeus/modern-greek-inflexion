from .create_verb_list import create_all_basic_forms


def create_basic_forms(verb):
    return create_all_basic_forms(verb)


def create_all_forms(verb):
    basic_forms = create_all_basic_forms(verb)

    present_active = {}
    present_passive = {}

    conjunctive_active = {}
    conjunctive_passive = {}

    aorist_active = {}
    aorist_passive = {}

    paratatikos_active = {}
    paratatikos_passive = {}

    active_present_participle = {}
    passive_perfect_pariciple = {}



