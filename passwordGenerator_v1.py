# !/usr/bin/python3

headerToInputSpacing = 20

class Generator:
    # Create the static screens the user will see.
    Screens = {
        'welcomeScreen' : """
\n\n
#----------------------------------------------------------------------------#
#                                                                            #
#                           PASSWORD GENERATOR                               #
#                     Created by - Matthew Beckwith                          #
#                                                                            #
#----------------------------------------------------------------------------#
\n\n
""",
        'newPasswordScreen' : """
\n\n
#----------------------------------------------------------------------------#
#                                                                            #
#                              NEW PASSWORD                                  #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
\n\n
""",
        'savePasswordScreen' : """
\n\n
#----------------------------------------------------------------------------#
#                                                                            #
#                            SAVING PASSWORD                                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
\n\n
""",
        'viewAllPasswordsScreen' : """
\n\n
#----------------------------------------------------------------------------#
#                                                                            #
#                          SHOW ALL PASSWORDS                                #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
\n\n
""",
        'findPasswordScreen' : """
\n\n
#----------------------------------------------------------------------------#
#                                                                            #
#                           FIND PASSWORD                                    #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
\n\n
"""
    }

    def basicMenu(self):
        choice = int(input("""
        What would you like to do?

        1 = Generate a New Password
        2 = Show all Passwords
        3 = Find a Password
        4 = Quit
        
        """))
        
        if(choice == 4):
            exit()
        else:
            print("\n" * 100)
            if(choice == 3):
                print(self.Screens['findPasswordScreen'])
                print("\n" * headerToInputSpacing)
                self.findPasswordMenu()
            elif(choice == 2):
                print(self.Screens['viewAllPasswordsScreen'])
                print("\n" * headerToInputSpacing)
                self.viewAllPasswordsMenu()
            elif(choice == 1):
                print(self.Screens['newPasswordScreen'])
                print("\n" * headerToInputSpacing)
                self.newPasswordMenu()
            else:
                print("Please Pick an appropriate option\n")
                self.basicMenu()

    def findPasswordMenu(self):
        choice = input("""
        What name did you save the password as?

             (type <back> to go back or <quit> to exit the program)
       
        """)
        
        if(choice == '<quit>'):
            exit()
        elif(choice == '<back>'):
            startProgram()
        else:
            print("Searching for " + choice)

    def viewAllPasswordsMenu(self):
        choice = int(input("""
        What would you like to do?

        1 = Go Back
        2 = Quit
        
        """))
        
        if(choice == 2):
            exit()
        elif(choice == 1):
            startProgram()
        else:
            print("\n" * 100)
            print("Please Pick an appropriate option\n")
            self.viewAllPasswordsMenu()

    def newPasswordMenu(self):
        choice = int(input("""
        What would you like to do?

        1 = Generate a General New Password
        2 = Generate a New Password WITH Special Characters
        3 = Generate a Phrase Based Password
        4 = Quit
        
        """))
        
        if(choice == 4):
            exit()
        else:
            print("\n" * 100)
            if(choice == 3):
                print(self.Screens['findPasswordScreen'])
                print("\n" * headerToInputSpacing)
                self.findPasswordMenu()
            elif(choice == 2):
                print(self.Screens['viewAllPasswordsScreen'])
                print("\n" * headerToInputSpacing)
                self.viewAllPasswordsMenu()
            elif(choice == 1):
                print(self.Screens['newPasswordScreen'])
                print("\n" * headerToInputSpacing)
                self.newPasswordMenu()
            else:
                print("Please Pick an appropriate option\n")
                self.basicMenu()

def startProgram():
    gen = Generator()
    print("\n" * 100)
    print(gen.Screens['welcomeScreen'])
    print("\n" * headerToInputSpacing)
    gen.basicMenu()

startProgram()
