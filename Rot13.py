import string
 
T = str.maketrans(
    string.ascii_uppercase + string.ascii_lowercase,
    string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
    string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
)
 
def rot13(message):
    return message.translate(T)
