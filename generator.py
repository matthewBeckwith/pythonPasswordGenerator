# !/usr/bin/python3
from words import Words
import random

class Generator:
    def GenerateBasic():
        newPassword = []

        while(len(newPassword) <= 16):
            newPassword.append(Words.characters[random.randrange(0,len(Words.characters))])

        newPassword = ''.join(newPassword)

        return newPassword

    def GenerateSpecial():
        newPassword = []
        count = 5

        while(len(newPassword) <= 16):
            if(len(newPassword) % count == 4):
                newPassword.append(Words.special_characters[random.randrange(0,len(Words.special_characters))])
            else:
                newPassword.append(Words.characters[random.randrange(0,len(Words.characters))])

        newPassword = ''.join(newPassword)

        return newPassword

    def GeneratePhrase():
        newPassword = []
# Phrase Structure = P-N-V-P-N
        while(len(newPassword) <= 4):
            if(len(newPassword) == 0 or len(newPassword) == 3):
                newPassword.append(Words.prepositions[random.randrange(0,len(Words.prepositions))])
            elif(len(newPassword) == 1 or len(newPassword) == 4):
                newPassword.append(Words.nouns[random.randrange(0,len(Words.nouns))])
            else:
                newPassword.append(Words.verbs[random.randrange(0,len(Words.verbs))])

        newPassword = ''.join(newPassword)

        return newPassword
