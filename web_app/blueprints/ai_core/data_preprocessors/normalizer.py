
from typing import Dict, List


class normalizer:

    _special_characters = {'"': " ", "-": " - ", "+": " + ", ":": " ", ".": " ", "(": " ",
                           ",": " ", "[": " ", "]": " ", "{": " ", "}": " ", "?": " ", "!": " ", "`": " ", "\\": " ",
                           "/": " ", "&": " ", "^": " ", "%": " % ", "$": " $ ", "#": " # ", "@": " @ ", "~": " ",
                           "|": " ", "<": " ", ">": " ",
                           "“": " ",  # Backward double quote thingy
                           "”": " ",  # Forward double quote thingy
                           "\u200a": " ",  # Hair Space
                           "\u200b": "",  # Zero-Width Space
                           "\u200c": "",  # Zero-Width Non-Joiner
                           "\u200d": "",  # Zero-Width Joiner
                           "\u200e": "",  # Left-To-Right Mark
                           "\u200f": "",  # Right-To-Left Mark
                           "\xa0": " "}  # No-Break space

    def __init__(self):
        pass

    def normalize_characters(self, data: Dict[str, List[str]]) -> Dict[str, List[str]]:
        for group, sentences in data.items():
            for index in range(len(sentences)):
                for anomaly, normal_form in self._special_characters.items():
                    sentences[index] = sentences[index].replace(anomaly, normal_form)
                sentences[index] = " ".join(sentences[index].split())

        return data
