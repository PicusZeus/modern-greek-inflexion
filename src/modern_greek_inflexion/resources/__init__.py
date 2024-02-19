import re

import pickle
import os
from .variables import *

# these lists should be replaced with one comprehensive data class
this_dir, this_filename = os.path.split(__file__)
el_GR_path = os.path.join(this_dir, 'el_GR.pickle')
# el_GR_path = os.path.join(this_dir, 'big_greek_corpus.pickle')

greek_corpus = pickle.load(open(el_GR_path, 'rb'))

# these are not all the irregular verbs, but if you take into account compounds, most.

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)
