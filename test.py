#! /usr/bin/python

"""
# WHAT ?
    Create a mp3 file using Google Translate’s text-to-speech API.

# HOW TO USE ?
    pip install gTTS
    cd Downloads
    # gtts-cli --all # to list all languages
    python ~/snap/deep-translator/gTTS.py input.txt "it"

# input.txt, pattern file
    # Quanto? / Quanta? / Quanti? / Quante? (How much? / How many?)
    Quanto costa questo libro? (How much does this book cost?)
    Quanti anni hai? (How old are you?)
"""


import logging
import os
import re
import sys

from gtts import gTTS
from unidecode import unidecode

# Enable logging for gTTS
logging.getLogger('gtts').setLevel(logging.DEBUG)
os.makedirs("mp3", exist_ok=True)

def remover_acentos(palavra):
    # unidecode que converte caracteres Unicode (inclusive os acentuados) para caracteres ASCII, removendo os acentos.
    return unidecode(palavra)


def remove_special_characters(file_name):
    # Remove special characters and returns only letters and numbers.
    return re.sub(r'[^a-zA-Z0-9 ]', '_', file_name)


def transliterator(text, file_name, language, slow):
    if text == '':
        print('Error: first line cannot be empty!')
        sys.exit()
    file_name = remover_acentos(text)
    file_name = remove_special_characters(file_name) + '.mp3'

    # Create mp3 file
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save('./mp3/'+file_name)


if __name__ == "__main__":
    # Get command-line arguments
    file_name = sys.argv[1]  # NAME FILE
    language = sys.argv[2]  # LANGUAGE

    # Read input file and store text in a string
    count = 0
    with open(file_name, 'r', encoding='utf8') as fp:
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            print(line.strip())
            transliterator(line.strip(), file_name, language, slow=False)
