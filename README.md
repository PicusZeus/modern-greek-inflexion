![Tests](https://github.com/PicusZeus/modern-greek-inflexion/actions/workflows/tests.yml/badge.svg)
 

# Modern-greek-inflexion

Python 3 library for recognizing inflexion types and for creating all possible inflected forms for Modern Greek words.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modern-greek-inflexion.

```bash
pip install modern-greek-inflexion
```

## Usage

see [docs.rst](https://github.com/PicusZeus/modern_greek_inflexion/blob/master/docs.rst)

## Unittests
run 
>python -m unittest

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Change Log
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

