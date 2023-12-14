#! /usr/bin/python

"""
ONE MP3 FOR ONE FILE

# WHAT ?
    Create a mp3 file using Google Translate’s text-to-speech API.

# HOW TO USE ?
    pip install gTTS
    cd Downloads
    # gtts-cli --all # to list all languages
    python gTTS.py input.txt "fr"

# input.txt, pattern file
    Parler en public exige confiance, éloquence et préparation.
    L'orateur captive, inspire, persuade, impressionne, influence.
    La foule écoute attentivement, évalue, critique, apprécie.
    - Maîtriser l'art oratoire requiert pratique, patience, persévérance.
    - Prononcer discours impeccable exige diction précise, parfaite.
"""

# >  python gtts_file.py input.txt "fr"

import logging
import os
import re
import sys

from gtts import gTTS
from unidecode import unidecode

os.makedirs("mp3", exist_ok=True)


class TextConcatenator:
    def __init__(self, language, slow=True):
        self.language = language
        self.slow = slow

    @staticmethod
    def remove_accents(word):
        return unidecode(word)

    @staticmethod
    def remove_special_chars(file_name):
        return re.sub(r'[^a-zA-Z0-9 ]', '', file_name)

    def concatenate_text(self, text):
        print(f"{'-'*50}\n{text}\n{'-'*50}\n")
        lines = text.split('\n')
        file_name = lines[0][0:].strip()

        if file_name == '':
            print('Error: first line cannot be empty!')
            sys.exit()

        file_name = self.remove_accents(file_name)
        file_name = self.remove_special_chars(file_name) + '.mp3'

        concatenated_text = self._concatenate_lines(lines)
        self.create_mp3(concatenated_text, file_name)

    def _concatenate_lines(self, lines):
        concatenated_text = ''
        for line in lines:
            if line.startswith('#'):
                continue
            elif line.startswith('---'):
                break
            words = line.split(', ')
            line_with_commas = ', '.join(words) + ','
            concatenated_text += line_with_commas + ' '
        return concatenated_text.rstrip()

    def create_mp3(self, text, file_name):
        tts = gTTS(text=text, lang=self.language, slow=self.slow)
        tts.save(f'./mp3/{file_name}')
        print(f'File created ./mp3/{file_name}')


if __name__ == "__main__":
    logging.getLogger('gtts').setLevel(logging.DEBUG)

    file_name_input = sys.argv[1]
    target_language = sys.argv[2]

    with open(file_name_input, 'r', encoding='utf8') as file:
        text_content = file.read()

    text_content = text_content.split('---')[0]
    text_concatenator = TextConcatenator(language=target_language, slow=True)
    text_concatenator.concatenate_text(text_content)
