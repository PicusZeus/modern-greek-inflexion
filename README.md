 # Modern-greek-inflexion

Python 3 library for recognizing inflexion types and for creating all possible inflected forms for Modern Greek words.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modern-greek-inflexion.

```bash
pip install modern-greek-inflexion
```

## Usage

see [docs.rst](https://github.com/PicusZeus/modern_greek_inflexion/blob/master/docs.rst)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Change Log
 * 0.1.12 Fixed issue with adj on hs with feminin on issa, and error which occured if an adj doesnt have an adverb
 * 0.1.11 Fixed bug in adjectives, where not existent superlative would lead to a crash
 * 0.1.10 Fixes to numerals, now doesn't return alternative forms
 * 0.1.9 Refactored numerals, minor fixes in noun and adj
 * 0.1.8 Minor fixes in noun, now works better with additional info on gender and inflection.
 * 0.1.6 Fixed issue with path to pickled db, db included in package
 * 0.1.4 Fixed issue with dependencies, fixed path to greek_corpus db.
 * 0.1.3 Added es, ous neutral nouns, fixed issue with hs, eis nouns, added new pronoun paradigms, added flag 'aklito' for nouns and adjectives.
 * 0.1.2 Fixed issue with double vocatives in some two syllable proper masculine names
 * 0.1.1 Initial release

