# !/usr/bin/python3

from ui import UserInterface as ui
from generator import Generator as gen
from DatabaseController import Database as db

def drawScreen(SCREEN, option = None):
    ui.clearScreen()
    print(ui.Screen[SCREEN]['header'])

    if(option != None):
        print("New Password: " + option)

    ui.innerSpace()

    choice = 0

    while True:
        try:
            if(SCREEN == 'findPasswordScreen'):
                choice = input(ui.Screen[SCREEN]['menu'])
                break
            else:
                while(choice < 1) or (choice > ui.Screen[SCREEN]['choice_count']):
                    choice = int(input(ui.Screen[SCREEN]['menu']))
                break
        except ValueError:
            print(ui.Error['strOverInt'])

    if(SCREEN == 'welcomeScreen'):
        if(choice == 1):
            drawScreen('newPasswordScreen')
        elif(choice == 2):
            db.getAll()
            drawScreen("welcomeScreen")
        elif(choice == 3):
            drawScreen('findPasswordScreen')
        else:
            quit()
    elif(SCREEN == 'newPasswordScreen'):
        if(choice == 1):
            newPassword = gen.GenerateBasic()
        elif(choice == 2):
            newPassword = gen.GenerateSpecial()
        elif(choice == 3):
            newPassword = gen.GeneratePhrase()
        else:
            quit()

        drawScreen('savePasswordScreen',newPassword)

    elif(SCREEN == 'savePasswordScreen'):
        if(choice == 1):
            db.save(option)
        elif(choice == 2):
            newPassword = gen.GenerateBasic()
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 3):
            newPassword = gen.GenerateSpecial()
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 4):
            newPassword = gen.GeneratePhrase()
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 5):
            drawScreen('newPasswordScreen')
        else:
            quit()
    elif(SCREEN == 'findPasswordScreen'):
        db.searchDB(choice)
        drawScreen("welcomeScreen")

drawScreen("welcomeScreen")
