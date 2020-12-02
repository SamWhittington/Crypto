import textwrap

def decode(ciphertext,phrase):
    key = 'abcdefghijklmnopqrstuvwxyz'
    result, b,  a = '', [], []
    for n in range(0,26):
        for l in ciphertext:

            i = (key.index(l) - n) % 26
            result += key[i]
    
    a = textwrap.wrap(result, len(ciphertext))
    return [i for i in a if phrase in i]
