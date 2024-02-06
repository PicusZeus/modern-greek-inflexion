![Tests](https://github.com/PicusZeus/modern-greek-inflexion/actions/workflows/tests.yml/badge.svg)
![Downloads](https://img.shields.io/pypi/dm/modern-greek-inflexion)
![python version](https://img.shields.io/pypi/pyversions/modern-greek-inflexion)
![GitHub License](https://img.shields.io/github/license/picuszeus/modern-greek-inflexion)
# Modern-greek-inflexion

Python 3 library for recognizing inflexion types and for creating inflected forms for Modern Greek words (verbs, adjectives, nouns etc.).
The application is implemented in a web app you can find [here](https://ellinika.com.pl).
The application requires from a user to be fed with a basic, existing Greek Lemma to work. 
Internally it works thanks to a big corpus on which it tests forms it tries to create. Thanks to it the program gives mostly good results, especially in comparison 
to all the other "conjugation" engines.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modern-greek-inflexion.

```bash
pip install modern-greek-inflexion
```

## Usage

see [docs.rst](https://github.com/PicusZeus/modern-greek-inflexion/blob/master/docs.rst) or tests.

## Unittests
run 
>python -m unittest

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Change Log

 * 1.0.5 A bug, that caused problems in aorist formation for compound verbs from βαίνω fixed.
 * 1.0.4 Added logic for multiple root formation in verbs on -άρω (σοκάρω, σοκαρίζω, σοκαρίσω), now the app will try to create also imperfect forms with a root on 'ιζ'. The Experiment with extending the core language check corpus failed miserably, as all the corpora I tried (even these from the EU) are unfortunately full of typos and orthographic errors, which, when used, introduced into the app huge problems. Next time I will try to use some NLTK magic and frequency lists to try them again.
 * 1.0.3 The problem with verbs with prefix para fixed by adding a flag to verb.create_all_forms para. If there is possibility, that there are two different verbs (like παραβλέπω/παραβλέψω and παραβλέπω/παραδώ), you have to set flag para to True. Fixed issue with non existent imper aor sg of compound verbs with βαίνω (like παρεμβαίνω).
 * 1.0.2 Updated list of irregular past passive participles, deleted most of them as they're not needed anymore and in places they would cause incorrect participle formation.
 * 1.0.1 Project is mature enough, some issue with dependency accentuation module fixed.
 * 0.9.4 Revised library of endings, added support for archaioprepes passive for verbs of type 'θέτω'.
 * 0.9.3 Added support for not very frequently used passive present imperative sg, added support for paratatikos for verbs on ώμαι.
 * 0.9.2 Update focused mainly on paratatikos, now it should deal better with lesser used conjugation types, mainly archaic. Also in passive paratatikos archaic endings 'to' and 'nto' are added to the verbs of basic conjugation types if they are found in corpus (like κυβερνείτο ή κυκλοφορείτο). Fixed issue with some modal verbs.
 * 0.9.1-alpha Substantial update mainly for code readability, but also many bugs fixed in the verb module.
 * 0.8.1  Big update. A lot of changes in verb module in most aspects. Creating perf roots should be more reliable, also added full support for archaic conjugation on ow (πληρώ, ζηλώ, ισούμαι). 
 * 0.7.3-beta Verbs are now forced to create passive paratatikos if there is passive present. 
 * 0.7.3-alpha Fixed bug which prevented participle to decline properly, added athematic participle for bainw.
 * 0.7.2   Fixed bugs that prevented some verbs from creating present passive forms, also verbs of type 'ίσταμαι' now provide all the possible forms together with pass aor participle (stas, stasa, stan).
 * 0.7.1-beta   Redesigned and much improved verb module. More accurate but also more eager to reproduce participles.
 * 0.6.15  Redesigned working with prefixes when creating basic verb forms.
 * 0.6.14  Modification in verb module, with special emphasis on syntheta from exw and agw, that sometimes were unrecognized correctly. Now fixed.
 * 0.6.13  Updated accentuation module, fixed issues with improper reduplication of pparticiples and some bug fixing in verb module.
 * 0.6.12  Updated grammar lists for correct accentuation of proparoxytona nouns on -os, fixed bug affecting one syllable forms of verbs.
 * 0.6.11  Better handling of archaic passive aorist, now creates it for more verbs with existing such a form.
 * 0.6.10  New conjugation type only for verbs of type kathistw, better handling, doesnt generate non existent inflected forms. 
 * 0.6.9   Improved handling of movable accent in some of adjective groups and of feminine -os adjectives.
 * 0.6.8   Minor review of pronoun module
 * 0.6.7   Minor bug fixing
 * 0.6.6   Minor bug fixing
 * 0.6.5   Improved handling of proper names, and reduplicated participles.
 * 0.6.4   Further improvements in the third declension, especially for nouns on -is
 * 0.6.3   Fixed minor issues, pluralia tantum now covered more extensively
 * 0.6.2   Fixed an issue with the lacking list of masc_fem nouns
 * 0.6.1   Extensively revised and fixed adjective and noun modules, now it covers multiple plural forms, also the app now deals better with accentuation of genitives, especially in feminine gender. Now uses extensive lists scraped from Wikileksiko for correct accentuation and for such issues as existence of genitives and the form of vocative ending in declension on -os.
 * 0.5.571 Quite a few fixes concerning mainly arxaioprepes types of adjective inflexions, 
 * 0.5.570 Fixed issues with aklita on i
 * 0.5.569 Fixed issues with adj on ous (arxaioprepes)
 * 0.5.568 Fixed issues with less regular adjective femina on a after consonants
 * 0.5.567 Fixes in proper_nouns on ous
 * 0.5.566 Small fixes to pronoun handling
 * 0.5.565 Changed wordlist (expanded), fixes in verb module (more liberal construction of aorist root) and in adjective module so that it can deal better with former participles used as adjectives now.
 * 0.5.555 Added irregular stem δεω and fixed declination of participles on ών
 * 0.5.554 Added irregular stem for gernw
 * 0.5.553 Fixes within irregular stems.
 * 0.5.552 Fixes for verbs on -υν and some irregularities (θάβω).
 * 0.5.550 Handling of elliptic verbs introduced, a list was used, other minor upgrades.
 * 0.5.546 Fixed issue with accentuation when there is possibility, that 'i' can be reproduced as consonant (teleiwnw)
 * 0.5.545 Fixed bug that prevented augmentation in past perf participles that begin on ψ ξ.
 * 0.5.544 Fixed bug with some derivatives of menw.
 * 0.5.543 Fixed bug with participles of pathainw, pethenw
 * 0.5.542 Improved recreating of sigmatic roots for passive imper.
 * 0.5.541 added prefixes in accentuation model. Small improvements in verb module.
 * 0.5.540 updated accentuation module.
 * 0.5.539 Added prefix antikata, improved inflexion on w, ois, oi
 * 0.5.537 Improved handling for isthmi
 * 0.5.535 If cannot create past pass part from pass root, try do it from act root (sthnw).
 * 0.5.533 Added irregular passive roots (klept-klap, fer-ferth)
 * 0.5.532 Improved handling of verbs on aro (aor iso), also ago is created correctly.
 * 0.5.530 Added handling for loan verbs on aro to add a common perf root on risw.
 * 0.5.527 Added logic to create imperative forms on ete for roots on r, n, if there is no form with te.
 * 0.5.526 Fixed bug when logic for t/th alternation was applied to different verbs
 * 0.5.525 Some addition to irregular roots
 * 0.5.521 Fixed bug with aorist on hn, where basic form was given with hn not h.
 * 0.5.520 Labainw and lambanw fixed.
 * 0.5.519 Again bugs with thita/tau in deponens, fixed for now.
 * 0.5.518 improved handling of thita to tau mutual existence in pass roots. 
 * 0.5.517 fixed bazw, it has passive in historical times.
 * 0.5.516 added irregular root pair ftheir fthar
 * 0.5.515 added double handling for passive perfect roots that and with t, but can sometimes endwith th. Added pass perf particple handling for roots that end on gx.
 * 0.5.511 Fixed issue with passive future wrong con recognition, improved handling of augmentation of passive perf. part.
 * 0.5.500 Fixed issue with augmented prefixes where a changes to h.
 * 0.5.499 Fixed issue with participles and passive aorist in verbs that consist of exw and agw.
 * 0.5.490 Added masc exceptions for us, os, and better handling of fem on is ews.
 * 0.5.485 Fixed bug with aorist forms of deponens when multiple roots
 * 0.5.475 Fixing issue with augmented prefixes (in modern-greek-accentuation library)
 * 0.5.460 Minor improvements to code readability.
 * 0.5.450 Bugs in verbs, imperatives for longer verbs in con2b concjuntive, clash paw and pw, solved.
 * 0.5.425 Improved handling of passive perfect participles, when there are more than one.
 * 0.5.405 Fixed issues with monotonic constraints on pronouns and adverbs, removed gen pl from adj on hs, iko
 * 0.5.40 Fixed inner augmentation (eggrafo, syllambano)
 * 0.5.33 Fixed handling of 2 syllables on ao (spao) and improved augment handling.
 * 0.5.32 Fixed handling of a irregularities in pao verb.
 * 0.5.31 Fixed issue with missing acc in us/hs eis noun inflexion type.
 * 0.5.3 Fixed issue with incorrect inflexion of nouns on 'hs/us and eis'.
 * 0.5.2 Fixed bug with accentuation of composita like katexo and paraeimai.
 * 0.5.1 Updated accentuation module, fixed bug with eimai, fixed bug with aorist participles.
 * 0.5.0 Updated accentuation module, that deals better with augmentation of verbs.
 * 0.4.9 Improved accentuation handling, improved handling of sg only nouns.
 * 0.4.8 Added optional flag aklito for nouns and adjectives (boolean).
 * 0.4.7 Bug fixes, added: adj on wr, verbs (aor and parat) on arw
 * 0.4.6 Bug with single syllable verbs fixed
 * 0.4.5 Small improvements, fixing bug with endings eimai, added adv pron and smaller improvements
 * 0.4.0 Code refactored, changed import paths, fixing bug causing problems with imports
 * 0.3.0 Fixed bug when a possible prefix of a verb is identical with a verb itself, minor refactoring of the code
 * 0.2.6 Fixed handling of indeclinable nouns (those on r, n etc were ignored)
 * 0.2.5 Added surname handling
 * 0.2.4 Minor fixes, updated requirements, updated word lists
 * 0.2.3 Added a more comprehensive corpus of the Greek words utilizing wikileksiko corpus, small improvements to the handling of prefixes in verbs
 * 0.2.2 Fixed exceptions message
 * 0.2.1 Fixes in verb module, mainly to modal verbs but also some minor issues resolved also. Added custom exceptions in exceptions module

 * 0.1.15 Added handling for ancient adjectives from 3rd declination (is, itos, ks, kos), and also for attic declination
 * 0.1.14 Added logic for contracted ancient adjectives on ous, oun, some minor improvements
 * 0.1.13 Added logic for resolving inflexion type of adjective that cannot be helped by corpus
 * 0.1.12 Fixed issue with adj on hs with feminine on issa, and error which occurred if an adj doesnt have an adverb
 * 0.1.11 Fixed bug in adjectives, where not existent superlative would lead to a crash
 * 0.1.10 Fixes to numerals, now doesn't return alternative forms
 * 0.1.9 Refactored numerals, minor fixes in noun and adj
 * 0.1.8 Minor fixes in noun, now works better with additional info on gender and inflection.
 * 0.1.6 Fixed issue with path to pickled db, db included in package
 * 0.1.4 Fixed issue with dependencies, fixed path to greek_corpus db.
 * 0.1.3 Added es, ous neutral nouns, fixed issue with hs, eis nouns, added new pronoun paradigms, added flag 'aklito' for nouns and adjectives.
 * 0.1.2 Fixed issue with double vocatives in some two syllable proper masculine names
 * 0.1.1 Initial release

