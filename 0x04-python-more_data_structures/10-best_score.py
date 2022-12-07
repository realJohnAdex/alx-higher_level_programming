#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(a_dictionary.values())
    max_key = [k for k, v in a_dictionary.items() if v == max_value]
    return max_key[0]
