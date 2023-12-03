"""
Transliteration is a type of conversion of a text from one script to another \
that involves swapping letters (thus trans- + liter-) in predictable ways.

This tool allows for transliteration from Cyrillic to Latin character sets \
according to the Transliteration Act of 2009.
"""

__author__ = "Deyan Nikolov"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "GPL (GNU General Public License)"
__version__ = "1.1"
__maintainer__ = "Deyan Nikolov"
__email__ = ""
__status__ = "Prototype"

from transliterator.trans import transliterate
from transliterator.gui import main as gui
