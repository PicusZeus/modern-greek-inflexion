![Tests](https://github.com/PicusZeus/modern-greek-inflexion/actions/workflows/tests.yml/badge.svg)
![Downloads](https://img.shields.io/pypi/dm/modern-greek-inflexion)
![python version](https://img.shields.io/pypi/pyversions/modern-greek-inflexion)
![GitHub License](https://img.shields.io/github/license/picuszeus/modern-greek-inflexion)
# Modern-greek-inflexion

Python 3 library for recognizing inflexion types and for creating all possible inflected forms for Modern Greek words (verbs, adjectives, nouns etc.).
It has nothing to do with AI. To avoid creating non-existent (though maybe possible forms) it checks its results with a orthographic
dictionary. The application is implemented in a web app you can find [here](https://ellinika.com.pl).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modern-greek-inflexion.

```bash
pip install modern-greek-inflexion
```

## Usage

see [docs.rst](https://github.com/PicusZeus/modern-greek-inflexion/blob/master/docs.rst)

## Unittests
run 
>python -m unittest

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Change Log
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

