import codecs

def encrypter(string):
    # Make a dictionary mapping the alphabet to it's reverse:
    abc = 'abcdefghijklmnopqrstuvwxyz'
    di = dict(zip(abc, abc[::-1])) 

    # Encode the string using the rot-13 cipher found in codecs
    encry = codecs.encode(string, 'rot_13')
    
    # Apply dictionary onto encry
    a = []
    for letter in encry:
        print(letter)
        if letter != ' ':
            a.append(di.get(letter))
        else:
            a.append(' ')
    
    return ''.join(a)
