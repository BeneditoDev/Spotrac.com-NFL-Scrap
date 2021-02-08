import random

def veriHash(hash, dict):
    for hashie in dict.keys():
        if hash == hashie:
            return True
    return False

def makeHash(name1, name2, hashDb):
    len1 = len(name1)
    len2 = len(name2)
    hash = name1[0] + name2[0] + str(len1) + str(len2)
    if veriHash(hash, hashDb) == True:
        while True:
            hashTemp = hash + str(random.randint(1,9))
            if veriHash(hashTemp, hashDb) == False:
                hashDb[hashTemp] = "y"
                return hashTemp
    else:
        hashDb[hash] = "y"
        return hash
