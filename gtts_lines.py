#! /usr/bin/python

"""
MULTIPLE MP3 FOR EACH LINE

# WHAT ?
    Create a mp3 file using Google Translate’s text-to-speech API.

# HOW TO USE ?
    pip install gTTS
    cd Downloads
    # gtts-cli --all # to list all languages
    python gtts_lines.py input.txt "it"

# input.txt, pattern file
    # Quanto? / Quanta? / Quanti? / Quante? (How much? / How many?)
    Quanto costa questo libro? (How much does this book cost?)
    Quanti anni hai? (How old are you?)
"""

# >  python gtts_lines.py input.txt "fr"

import os
import re
import sys

from gtts import gTTS
from unidecode import unidecode


os.makedirs("mp3", exist_ok=True)


class TextTransliterator:
    def __init__(self, language, slow=False):
        self.language = language
        self.slow = slow

    @staticmethod
    def remove_accents(word):
        return unidecode(word)

    @staticmethod
    def remove_special_chars(file_name):
        reg = re.sub(r'[^a-zA-Z0-9 ]', '_', file_name)  # no accents
        reg = re.sub(r'_{2,}', '_', reg)  # multiple _
        return re.sub(r'^_+|_+$', '', reg)  # strip _

    def transliterate_text(self, text, line_count):
        file_name = self.remove_accents(text)
        file_name = self.remove_special_chars(file_name)[:30] + '.mp3'
        self.create_mp3(text, file_name)

    def create_mp3(self, text, file_name):
        tts = gTTS(text=text, lang=self.language, slow=self.slow)
        tts.save(f'./mp3/{line_count}_{file_name}')


if __name__ == "__main__":
    file_name_input = sys.argv[1]
    target_language = sys.argv[2]

    transliterator = TextTransliterator(language=target_language, slow=False)
    line_count = 0

    with open(file_name_input, 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # strip spaces
            if not line or line.startswith('#'):
                continue  # Ignore whitespaces and comment lines
            print(line)
            line_count += 1
            transliterator.transliterate_text(line.strip(), line_count)
