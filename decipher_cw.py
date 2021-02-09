import re
from re import findall

def decipher_this(string):
    
    arr = []
    string_split = string.split(' ')
    
    for i in string_split: 
        arr1 = []
        
        first_letter = chr(int(''.join(findall('\d', i))))
        mixed_word = i.replace(''.join(findall('\d', i)), first_letter)
        
        try:
            for j in mixed_word:
                arr1.append(j)
                
            arr1[1], arr1[-1] = arr1[-1], arr1[1]
            
            arr.append(''.join(arr1))
        except:
            arr.append(mixed_word)
            
    return ' '.join(arr)
        
