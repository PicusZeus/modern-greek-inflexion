import re

import pickle
import os
from .variables import *

this_dir, this_filename = os.path.split(__file__)
el_GR_path = os.path.join(this_dir, 'lists', 'el_GR.pickle')

greek_corpus = pickle.load(open(el_GR_path, 'rb'))

greek_pattern = re.compile('[ά-ώ|α-ω]', re.IGNORECASE)
