# !/usr/bin/python3

class UserInterface:
    def clearScreen(space = 100):
        return print("\n" * space)

    def innerSpace(space = 20):
        return print("\n" * space)

    Screen = {
        'welcomeScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                           PASSWORD GENERATOR                               #
#                     Created by - Matthew Beckwith                          #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                       What would you like to do?

1 = Generate a New Password
2 = Show all Passwords
3 = Find a Password
4 = Quit

""",
            'choice_count' : 4
        },
        'newPasswordScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                              NEW PASSWORD                                  #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                       What would you like to do?

1 = Generate a General New Password
2 = Generate a New Password WITH Special Characters
3 = Generate a Phrase Based Password
4 = Quit

""",
            'choice_count' : 4
        },
        'savePasswordScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                            SAVING PASSWORD                                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                       What would you like to do?

1 = SAVE this Password
2 = Reroll a New Generic Password
3 = Reroll a New Password WITH Special Characters
4 = Reroll a New Phrase Based Password
5 = Back
6 = Quit

""",
            'choice_count' : 6
        },
        'verifySaveScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                        VERIFY SAVE INFORMATION                             #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                       What would you like to do?

1 = SAVE this Password with this Information
2 = Re-Enter Save Information
3 = Quit WITHOUT Saving

""",
            'choice_count' : 3
        },
        'viewAllPasswordsScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                          SHOW ALL PASSWORDS                                #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                       What would you like to do?

1 = Go Back
2 = Quit

""",
            'choice_count' : 2
        },
        'findPasswordScreen' : {
            'header' : """
#----------------------------------------------------------------------------#
#                                                                            #
#                           FIND PASSWORD                                    #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
""",
            'menu' : """
                What name did you save the password as?

(type <back> to go back or <quit> to exit the program)

""",
            'choice_count' : -1
        }
    }

    Error = {
        'noValue' : """
            There was no Value Entered, Please Try Again.
        """,
        'strOverInt' : """
            Please Enter a Number
        """
    }
