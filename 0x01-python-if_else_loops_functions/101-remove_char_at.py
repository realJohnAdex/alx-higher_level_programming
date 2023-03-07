#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy str, removing character at position n"""
    i = 0
    copy = ''
    for ch in str:
        if n == i:
            pass
        else:
            copy += ch
        i += 1
    return (copy)
