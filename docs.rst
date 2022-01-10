 Doctest

    run ``python -m doctest -v docs.rst`` to test.

Usage
=====

VERB
==============

>>> from src.verb import verb

The verb module consists of functions that create basic forms or all the forms for a single lemma, that has to be 1st person singular in present time, or, if it is a modal verb, in 3rd person, it recognizes conjugation types, irregular stems and creates all possible forms.
The result of these function is a dictionary, with keys that exactly correlate to grammatical structures. As this library was created mainly for the purpose of feeding a db, it is a preferable way to structure the output, as class based approach would need more work and would not help in the main goal of this library. It can be though refactored to class based output, if there is such a need.

The verb module consists of functions that create basic forms or all the forms for a single lemma, that has to be 1st person singular in present time, or, if it is a modal verb, in 3rd person, it recognizes conjugation types, irregular stems and creates all possible forms.
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

>>> from src.adjective import adjective

The adjective module has to methods for creating basic forms of an adjective and for creating all possible forms.
In order to create basic forms use "create_all_basic_forms", input must be masculine sing nominative form.

>>> adjective.create_all_basic_forms('όμορφος')
{'adj': 'όμορφος/όμορφη/όμορφο', 'comparative': 'ομορφότερος/ομορφότατος', 'adverb': 'όμορφα', 'adverb_comparative': 'ομορφότερα/ομορφότατα'}

Here adj genders are given divided by / in this order masc/fem/neuter
Comparative and comparative adverbs are given (if exist) with a slash, that divides comparative forms from superlatives.
If there are some alternative forms, they are divided with a coma.

If you want to create all the forms, use "create_all" method.

As a result you are given a dictionary with all forms derived from a lemma form (that has to be masc sing nom)

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


NOUN
======

>>> from src.noun import noun

The noun module consists of functions that create basic forms or all the forms from a single lemma, that has to be nom sg of a given noun (or pluralis if its pluralis tantum)
They return dictionaries with forms.

The noun module consists of functions that create basic forms or all the forms from a single lemma, that has to be nom sg of a given noun (or pluralis if its pluralis tantum)
They return dictionaries with forms.

BASIC NOUN
+++++++++++++++

If you want to recognize only gender and declination type, use 'create_all_basic_forms' method. Instead of giving a name of declination type, it returns gender, genitive singular and nom_plural.

>>> noun.create_all_basic_forms('οδός')
{'nom_sg': 'οδός', 'gen_sg': 'οδού', 'nom_pl': 'οδοί', 'gender': 'fem'}

ALL FORMS
++++++++++++

If you want to return all forms, use ``create_all`` method. It also takes as an argument a noun sg (or plural if its pluralis tantum).

STRUCTURE
+++++++++++

It returns a dictionary structured a bit differently than adjectives, because here the first layer of keys indicate gender:

>>> list(noun.create_all('γυναίκα').keys())
['fem']

It is done so, because some nouns can be in different genders, and so it is the basic differentiation for them (like diplokilta or profession names).

>>> [gender for gender in ['masc', 'neut'] if gender in noun.create_all('χρόνος').keys()]
['masc', 'neut']

The next layer of keys are those indicating number ('sg', 'pl')

>>> [number for number in ['sg', 'pl'] if number in noun.create_all('γυναίκα')['fem']]
['sg', 'pl']

And at the end there are cases: nominative ('nom'), genitive ('gen'), accusative ('acc'), vocative ('voc')

>>> [case for case in ['nom', 'gen', 'acc', 'voc'] if case in noun.create_all('άντρας')['masc']['sg']]
['nom', 'gen', 'acc', 'voc']

And in the end you have a form (or forms if there are multiple options) in a set

>>> noun.create_all('παιδί')['neut']['sg']['gen']
{'παιδιού'}

>>> [form for form in ['τάξης', 'τάξεως'] if form in noun.create_all('τάξη')['fem']['sg']['gen']]
['τάξης', 'τάξεως']

If a paradigm is defective, that is if a noun do not create some form or can be found only in plural or singular, then structure of the dictionary exists, but the sets include empty string

>>> noun.create_all('νους')['masc']['pl']['nom']
{''}

PROPER NOUN
==============

Proper nouns behave mostly in the same way as nouns, but since in this group there are many exceptions in gender endings as well as many aklita, if you can use flags: ``proper_noun`` and ``proper_noun_gender``. The first one is boolean, and can help especially in vocatives. The second one helps with indeclinable words borrowed from other languages and with common exceptions like names of islands.

>>> list(noun.create_all('Μύκονος').keys())
['masc']

which is of course incorrect, so in such cases use poroper_name_gender flag

>>> list(noun.create_all('Μύκονος', gender='fem').keys())
['fem']

Also proper masc names on os can have a different vocative then normal nouns

>>> noun.create_all('Γιώργος')['masc']['sg']['voc']
{'Γιώργε'}

which is incorrect, so in such cases use proper_name flag

>>> noun.create_all('Γιώργος', proper_name=True)['masc']['sg']['voc']
{'Γιώργο'}

The two flags can be used independently

QUANTIFIERS
==================

>>> from src.quantifiers import quantifiers

Among quantifiers there are adjectival quantifiers ('ένας') and noun quantifiers ('δεκάδα'), and so this module has two function for those two groups, as logic that would be able to recognize to which group a quantifier belongs, though possible, does not really offer much advantage to anyone. If I am wrong, it can always be added.

Among quantifiers there are adjectival quantifiers ('ένας') and noun quantifiers ('δεκάδα'), and so this module has two function for those two groups, as logic that would be able to recognize to which group a quantifier belongs, though possible, does not really offer much advantage to anyone. If I am wrong, it can always be added.

NOUN QUANTIFIERS
++++++++++++++++++

These are simply nouns and so the resulting dictionary with forms will be analogous to that of nouns

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_num('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_num('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_num('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_num('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

>>> quantifiers.create_all_noun_quant('χιλιάδα')['fem']['pl']['nom']
{'χιλιάδες'}

Adjectival quantifiers are actually adjectives, but some additional logic had to be added. If there are alternative versions of a quantifier (as is quite often the case), both are versions are given.

>>> [q for q in ['οχτακόσιους', 'οκτακόσιους'] if q in quantifiers.create_all_adj_quant('οχτακόσια')['adj']['pl']['masc']['acc']]
['οχτακόσιους', 'οκτακόσιους']

Some of these quantifiers, especially ordinal numbers have also adverb

>>> quantifiers.create_all_adj_quant('δεύτερος')['adv']
{'δεύτερον'}

and sometimes even comparatives

>>> quantifiers.create_all_adj_quant('πρώτος')['comp']['sg']['masc']['nom']
{'πρωτύτερος'}

PRONOUNS
+++++++++++++

>>> from src.pronoun import pronoun

There is wide variety of pronoun inflexions and they are quite different from adjectives. There is only

There is wide variety of pronoun inflexions and they are quite different from adjectives. There is only ``create_all`` module available, as there is no point in some "basic" forms for them. Structure of a resulting dictionary is analogous to that of the ``adjective.create_all`` method, but is one layer more shallow.

>>> pronoun.create_all('οποίος')['sg']['fem']['gen']
{'οποίας'}

PERSONAL PRONOUNS
=====================

These forms are highly irregular and possess differentiation on weak and strong versions, and so if you want to get weak pronouns, use ``strong`` flag, which is ``True`` by default.

>>> pronoun.create_all('εσύ')['sg']['nd']['gen']
{'εσένα'}

>>> pronoun.create_all('εσύ', strong=False)['sg']['nd']['gen']
{'σου'}


ADVERBS
+++++++

>>> from src.adverb import adverb

Adverbs that are created by adjectives are created catered for in adjective module. here should be directed all other adverbs. Method used to give all forms is as always

Adverbs that are created by adjectives are created catered for in adjective module. here should be directed all other adverbs. Method used to give all forms is as always ``create_all``, but most of the time it will be only the given adverb itself.

>>> adverb.create_all('ποτέ')
{'adv': {'ποτέ'}}

In few cases when adverb forms comparatives or even superlatives

>>> adverb.create_all('κάτω')['comp']['sg']['fem']['gen']
{'κατώτερης'}


OTHER POSES
++++++++++

Other poses such as conjunctions, particles, prepositions and so forth do not need any kind of stemmer, but maybe it would be a good idea, to add a funcionality, that would provide alternative forms for these kind of words (ακόμη/ακόμα κτλ), and in case of prepositions information on the case it requires, and also maybe a list of conjunctions that consists of two or more words?