 Doctest

    run ``python -m doctest -v docs.rst`` to test.

Usage
=====

VERB
==============

>>> from modern_greek_inflexion.verb import verb

The verb module consists functions that create basic forms or all the forms for a single lemma, that has to be 1st person singular in present time, or, if it is a modal verb, in 3rd person, it recognizes conjugation types, irregular stems and creates all possible forms.
The result of these function is a dictionary, with keys that exactly correlate to grammatical structures. As this library was created mainly for the purpose of feeding a db, it is a preferable way to structure the output, as class based approach would need more work and would not help in the main goal of this library. It can be though refactored to class based output, if there is such a need.

BASIC VERB
+++++++++++

If you are interested in creating only basic forms, use:

>>> verb.create_all_basic_forms('βλέπω')
{'present': {'active': {'βλέπω'}, 'passive': {'βλέπομαι'}}, 'conjunctive': {'active': {'δω'}, 'passive': {'ιδωθώ'}}, 'aorist': {'active': {'είδα'}, 'passive': {'ειδώθηκα'}}, 'paratatikos': {'active': {'έβλεπα'}, 'passive': {'βλεπόμουν'}}, 'act_pres_participle': {'βλέποντας'}, 'arch_act_pres_participle': {'βλέπων/βλέπουσα/βλέπον'}, 'passive_perfect_participle': {'ιδωμένος'}}

If you are interested only in for example aorist, use dictionary keys

>>> verb.create_all_basic_forms('τραγουδάω')['aorist']
{'active': {'τραγούδησα'}, 'passive': {'τραγουδήθηκα'}}

if there are alternative forms, they are included in a set

>>> len(verb.create_all_basic_forms('έρχομαι')['aorist']['active'])
2

ALL VERB FORMS
++++++++++++++++

You can also create all possible forms for a verb using ``verb.create_all`` method. Forms are always given in a set.

If you want to get all present simple forms active, indicative, singular

>>> verb.create_all_forms('κυβερνώ')['present']['active']['ind']['sg']['sec']
{'κυβερνάς'}

It also caters for all possible participles, if there are alternative forms, the set includes them all

>>> verb.create_all_forms('καίω')['passive_perfect_participle']['sg']['masc']['nom']
{'καμένος'}

>>> len(verb.create_all_forms('κυβερνώ')['pass_pres_participle']['sg']['masc']['nom'])
2

STRUCTURE OF THE DICTIONARY WITH VERB FORMS
++++++++++++++++++++++++++++++++++++++++++++++++++

* TIME

Structure of the generated dictionary in the first level is:
'present', 'conjunctive', 'aorist', 'paratatikos' for personal inflexion (if such categories are correct for a given verb).

>>> [time for time in ['present', 'conjunctive', 'aorist', 'paratatikos'] if time in verb.create_all_forms('διαβάζω')]
['present', 'conjunctive', 'aorist', 'paratatikos']

* VOICE

Next there is division into active and passive voice through keys "active" and "passive".

>>> [voice for voice in ['active', 'passive'] if voice in verb.create_all_forms('διαβάζω')['present']]
['active', 'passive']

* MOOD

Next keys indicate either indicative 'ind' (though for conjunctive it's not entirely appropriate) forms or imperative forms 'imp' (if exists).

>>> [pos for pos in ['ind', 'imp'] if pos in verb.create_all_forms('διαβάζω')['present']['active']]
['ind', 'imp']

* NUMBER

Next keys indicate singular and plural forms ('sg', 'pl'):

>>> [num for num in ['sg', 'pl'] if num in verb.create_all_forms('διαβάζω')['present']['active']['ind']]
['sg', 'pl']

* PERSON

Next level of keys indicate persons, 1st = 'pri', 2nd = 'sec', 3rd = 'ter':

>>> [per for per in ['pri', 'sec', 'ter'] if per in verb.create_all_forms('διαβάζω')['present']['active']['ind']['sg']]
['pri', 'sec', 'ter']

Forms themselves are given in a set, which consists of a single or more (alternative) forms:

>>> isinstance(verb.create_all_forms('διαβάζω')['present']['active']['ind']['sg']['pri'], set)
True

PARTICIPLES
++++++++++++++++

This function also returns all participles:

Active present participle, that is an adverbial form, is given under a key "act_pres_participle", in a set.

>>> verb.create_all_forms('διαβάζω')['act_pres_participle']
{'διαβάζοντας'}

In some cases verbs form archaic active present participle, that is adjectival, if it exists you will find it under the key "arch_act_pres_participle".
Forms are given in a dictionary that have an analogous structure to that of adjective (see ADJECTIVE section)

>>> verb.create_all_forms('βλέπω')['arch_act_pres_participle']['sg']['masc']['nom']
{'βλέπων'}

Also there are cases where archaic active aorist participle exists, then it is found under the key "active_aorist_participle"

>>> verb.create_all_forms('συνέρχομαι')['active_aorist_participle']['sg']['masc']['gen']
{'συνελθόντος'}

>>> verb.create_all_forms('δουλεύω')['active_aorist_participle']['sg']['fem']['nom']
{'δουλεύσασα'}

Also there are cases where archaic passive aorist participle is still in usage, then it is under the key "passive_aorist_participle".

>>> verb.create_all_forms('γεννάω')['passive_aorist_participle']['sg']['masc']['nom']
{'γεννηθείς'}

More verbs do possess passive present participle, but by no means all, these participles are found under the key "pass_pres_participle"

>>> verb.create_all_forms('κοιμάμαι')['pass_pres_participle']['sg']['masc']['nom']
{'κοιμούμενος'}

And the most common adjectival participle in Modern Greek, that is passive perfect participle, can be found under the key "passive_perfect_participle"

>>> verb.create_all_forms('μαγειρεύω')['passive_perfect_participle']['sg']['masc']['gen']
{'μαγειρεμένου'}

Sometimes there are alternative passive perfect participle, especially when an archaic form with reduplication survived

>>> [part for part in ['γραμμένος', 'γεγραμμένος'] if part in verb.create_all_forms('γράφω')['passive_perfect_participle']['sg']['masc']['nom']]
['γραμμένος', 'γεγραμμένος']


ADJECTIVE
=================

>>> from modern_greek_inflexion.adjective import adjective

The adjective module has to methods for creating basic forms of an adjective and for creating all possible forms.
In order to create basic forms use "create_all_basic_forms", input must be masculine sing nominative form.

>>> adjective.create_all_basic_forms('όμορφος')
{'adj': 'όμορφος/όμορφη/όμορφο', 'comparative': 'ομορφότερος/ομορφότατος', 'adverb': 'όμορφα', 'adverb_comparative': 'ομορφότερα/ομορφότατα'}

Here adj genders are given divided by / in this order masc/fem/neuter
Comparative and comparative adverbs are given (if exist) with a slash, that divides comparative forms from superlatives.
If there are some alternative forms, they are divided with a coma.

If you want to create all the forms, use "create_all" method.

As a result you are given a dictionary with all forms derived from a lemma form (that has to be masc sing nom)

POSITIVE DEGREE
+++++++++++++++++++

Under the key "adj", all adjective forms in the positive degree
All forms are structured number => gender => case

>>> adjective.create_all('καλός')['adj']['sg']['masc']['gen']
{'καλού'}

There are two numbers, singular ('sg') and plural ('pl')

>>> [number for number in ['sg', 'pl'] if number in adjective.create_all('καλός')['adj']]
['sg', 'pl']

There are three genders, masculine ('masc'), feminine ('fem'), neuter ('neut')

>>> [gender for gender in ['masc', 'fem', 'neut'] if gender in adjective.create_all('καλός')['adj']['sg']]
['masc', 'fem', 'neut']

There are 4 cases, nominative ('nom'), genitive ('gen'), accusative ('acc'), vocative ('voc')

>>> [case for case in ['nom', 'gen', 'acc', 'voc'] if case in adjective.create_all('καλός')['adj']['sg']['masc']]
['nom', 'gen', 'acc', 'voc']

Form or forms are given in a set

>>> [form for form in ['κακή', 'κακιά'] if form in adjective.create_all('κακός')['adj']['sg']['fem']['nom']]
['κακή', 'κακιά']

COMPARATIVES
+++++++++++++++

Comparative adjectival forms are structured in the same way as basic adjectives and are given only if a adjectives do create synthetic comparative and superlative forms.
Comparative forms can be accessed by the key "comp" that is the comparative degree, and 'superl', that is the superlative degree.

>>> [comp for comp in ['comp', 'superl'] if comp in adjective.create_all('κακός')]
['comp', 'superl']

>>> adjective.create_all('καλός')['superl']['sg']['fem']['gen']
{'άριστης'}

ADVERBS
++++++++++
Adverb(s) are given under the "adv" key. Adverbs for comparative and superlative degree are given (if exist) under the keys "comp_adv" and "superl_adv"

>>> [adv for adv in ['adv', 'comp_adv', 'superl_adv'] if adv in adjective.create_all('κακός')]
['adv', 'comp_adv', 'superl_adv']

>>> [adv for adv in ['τάχιστα', 'ταχύτατα'] if adv in adjective.create_all('ταχύς')['superl_adv']]
['τάχιστα', 'ταχύτατα']


