import hashlib
import itertools

def password_cracker(hash):
    for length in range(6):
        for candidate in map("".join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length)):
            if hashlib.sha1(candidate.encode()).hexdigest() == hash:
                return candidate
