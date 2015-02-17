
def encrypt(message, key):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if message == "":
        raise ValueError("can not encrypt empty string")

    if key == 0:
        raise ValueError("offset must not be zero")

    cipher = alfabet[key:] + alfabet[:key]
    ciphertext = ""
    for letter in message.upper():
        if letter not in alfabet:
            ciphertext += letter
        else:
            ciphertext += cipher[alfabet.index(letter)]
    #print ciphertext
    return ciphertext

#encrypt(message="jag ser en apa", key=3)



def decrypt(message, key):

    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if message == "":
        raise ValueError("can not decrypt empty string")

    if key == 0:
        raise ValueError("offset must not be zero")

    key = key - (key * 2)

    cipher = alfabet[key:] + alfabet[:key]
    ciphertext = ""
    for letter in message.upper():
        if letter not in alfabet:
            ciphertext += letter
        else:
            ciphertext += cipher[alfabet.index(letter)]
    #print ciphertext
    return ciphertext.lower()

#decrypt(message="MDJ VHU HQ DSD", key=3)


def bruteforce(message):
    wordlist = open("/usr/share/dict/words").read().splitlines()
    i = 1
    while i < 25:
        i += 1
        m = decrypt(message, i).split()
        maxwords = len(m)

        words = 0
        for word in m:
            if word in wordlist:
                words += 1

        if words/float(maxwords) > 0.7:
            print " ".join(m)


message = "I stepped on a Corn Flake, now I'm a Cereal Killer"
ciphertext = encrypt(message, 5)

bruteforce(ciphertext)
