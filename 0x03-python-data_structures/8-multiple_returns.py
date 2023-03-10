#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence_len == 0:
        tup = (sentence_len, None)
    else:
        tup = (sentence_len, sentence[0])
    return tup


if __name__ == "__main__":
    multiple_returns()
