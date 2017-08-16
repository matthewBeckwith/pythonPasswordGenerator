# !/usr/bin/python3

import random

class Generator:
    Fragments = {
        'characters' : [
            'a','b','c','d','e','f','g',
            'h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u',
            'v','w','x','y','z',
            '1','2','3','4','5','6','7','8','9','0',
            'A','B','C','D','E','F','G',
            'H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U',
            'V','W','X','Y','Z'
        ],
        'special_characters' : [
            '%','/','-','.','(',')','#','_'
        ]
    }
    
    Phrase_Fragments = {
        'nounFragments' : [
            'man',
            'woman',
            'dog',
            'cat',
            'boy',
            'girl',
            'bird',
            'mall',
            'store',
            'carlot',
            'home',
            'school',
            'taco',
            'chuckecheese',
            'yoyo',
            'pencil',
            'pen',
            'dad',
            'son',
            'brother',
            'mom',
            'sister',
            'police'
        ],
        'verbFragments' : [
            'ran',
            'swam',
            'slept',
            'sleep',
            'shot',
            'loved',
            'thought',
            'study',
            'studied',
            'smell',
            'ate',
            'eat',
            'call',
            'called',
            'yell',
            'yelled',
            'play',
            'plays',
            'played',
            'calls',
            'yells',
            'shoots',
            'shoot',
            'read',
            'write',
            
        ],
        'neutralFragments' : [
            'the',
            'a',
            'up',
            'even',
            'though',
            'because',
            'if',
            'and',
            'then',
            'why'
        ]
    }

    def GenerateBasic(self):
        newPassword = []

        while(len(newPassword) <= 16):
            newPassword.append(self.Fragments['characters'][random.randrange(0,len(self.Fragments['characters']))])

        newPassword = ''.join(newPassword)
        
        return newPassword

    def GenerateSpecial(self):
        newPassword = []
        count = 5

        while(len(newPassword) <= 16):
            if(len(newPassword) % count == 4):
                newPassword.append(self.Fragments['special_characters'][random.randrange(0,len(self.Fragments['special_characters']))])
            else:
                newPassword.append(self.Fragments['characters'][random.randrange(0,len(self.Fragments['characters']))])

        newPassword = ''.join(newPassword)
        
        return newPassword

    def GeneratePhrase(self):
        newPassword = []

        while(len(newPassword) <= 4):
            if(len(newPassword) == 0 or len(newPassword) == 3):
                newPassword.append(self.Phrase_Fragments['neutralFragments'][random.randrange(0,len(self.Phrase_Fragments['neutralFragments']))])
            elif(len(newPassword) == 1):
                newPassword.append(self.Phrase_Fragments['nounFragments'][random.randrange(0,len(self.Phrase_Fragments['nounFragments']))])
            else:
                newPassword.append(self.Phrase_Fragments['verbFragments'][random.randrange(0,len(self.Phrase_Fragments['verbFragments']))])

        newPassword = ''.join(newPassword)
        
        return newPassword
