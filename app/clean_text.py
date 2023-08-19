import re

def clean_text(text):
    """
    Remove unwanted characters
    """
    text = re.sub(r"\+", " " ,text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\r", " ", text)
    text = re.sub(r"\t", " ", text)
    text = re.sub(r"\xa0", " ", text)
    text = re.sub(r":", " ", text)
    text = re.sub(r";", " ", text)
    text = re.sub(r"/", " ", text)
    text = re.sub(r"!", " ", text)
    text = re.sub(r"\?", " ", text)
    text = re.sub(r"؟", " ", text)
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"»", " ", text)
    text = re.sub(r"«", " ", text)
    text = re.sub(r"\"", " ", text)
    text = re.sub(r'[-+]?[0-9]+', " ", text)

    return text