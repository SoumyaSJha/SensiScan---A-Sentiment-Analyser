
from nltk.tokenize import TweetTokenizer

def tokenize(text):
    tknzr = TweetTokenizer(strip_handles=True, reduce_len=True, preserve_case=False)
    return tknzr.tokenize(text)

