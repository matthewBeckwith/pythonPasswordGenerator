# !/usr/bin/python3

from ui import UserInterface as ui
from generator import Generator as gen

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
            drawScreen('viewAllPasswordsScreen')
        elif(choice == 3):
            drawScreen('findPasswordScreen')
        else:
            quit()
    elif(SCREEN == 'newPasswordScreen'):
        if(choice == 1):
            newPassword = gen.GenerateBasic(gen)
        elif(choice == 2):
            newPassword = gen.GenerateSpecial(gen)
        elif(choice == 3):
            newPassword = gen.GeneratePhrase(gen)
        else:
            quit()

        drawScreen('savePasswordScreen',newPassword)
        
    elif(SCREEN == 'savePasswordScreen'):
        if(choice == 1):
            print("Saving Password")
        elif(choice == 2):
            newPassword = gen.GenerateBasic(gen)
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 3):
            newPassword = gen.GenerateSpecial(gen)
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 4):
            newPassword = gen.GeneratePhrase(gen)
            drawScreen('savePasswordScreen',newPassword)
        elif(choice == 5):
            drawScreen('newPasswordScreen')
        else:
            quit()
    elif(SCREEN == 'viewAllPasswordsScreen'):
        if(choice == 1):
            drawScreen("welcomeScreen")
        else:
            quit()
    elif(SCREEN == 'findPasswordScreen'):
        print("Finding " + choice + "...")


drawScreen("welcomeScreen")
