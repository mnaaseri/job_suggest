import re


def clean_text(text):
    chars_to_remove = ["\+", "\n", "\r", "\t", "\xa0", ":", ";", "/", "!", "\?", "؟", "\|", "»", "«", "\"", '[-+]?[0-9]+']
    for char in chars_to_remove:
        text = re.sub(char, " ", text)
    return text