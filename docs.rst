 Doctest

    run ``python -m doctest -v docs.rst`` to test.

Usage
=====

VERB
+++++++++++++++++++++
>>> from modern_greek_inflexion.verb import verb

The verb module consists functions that create basic forms or all the forms for a single lemma, that has to be 1st person singular in present time, or, if it is a modal verb, in 3rd person, it recognizes conjugation types, irregular stems and creates all possible forms.

If you are interested in creating only basic forms, use:

>>> verb.create_all_basic_forms('βλέπω')
{'present': {'active': {'βλέπω'}, 'passive': {'βλέπομαι'}}, 'conjunctive': {'active': {'δω'}, 'passive': {'ιδωθώ'}}, 'aorist': {'active': {'είδα'}, 'passive': {'ειδώθηκα'}}, 'paratatikos': {'active': {'έβλεπα'}, 'passive': {'βλεπόμουν'}}, 'act_pres_participle': {'βλέποντας'}, 'arch_act_pres_participle': {'βλέπων/βλέπουσα/βλέπον'}, 'passive_perfect_participle': {'ιδωμένος'}}

If you are interested only in for example aorist, use dictionary keys
>>> verb.create_all_basic_forms('τραγουδάω')['aorist']
{'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}}

if there are alternative forms, they are included in a set
>>> len(verb.create_all_basic_forms('έρχομαι')['aorist']['active'])
2

You can also create all possible forms for a verb using ``verb.create_all`` method.

If you want to get all present simple forms active, indicative, singular
>>> verb.create_all_forms('κυβερνώ')['present']['active']['forms_ind']['sg']['sec']
{'κυβερνάς'}

It also caters for all possible participles
>>> verb.create_all_forms('καίω')['passive_perfect_participle']['sg']['masc']['nom']
'καμένος'

Participles are given as a string, but if there are alternatives, they are in a set
>>> len(verb.create_all_forms('κυβερνώ')['pass_pres_participle']['sg']['masc']['nom'])
2

Structure of the generated dictionary is:
the first level is 'present', 'conjunctive', 'aorist', 'paratatikos'
