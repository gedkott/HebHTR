# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from HebHTR import *

# Create new HebHTR object.
img = HebHTR('./yiddish.png')

# Infer words from image.
text = img.imgToWord(iterations=5, decoder_type='word_beam')