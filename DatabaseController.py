# !/usr/bin/python3
import sqlite3, time
from ui import UserInterface as ui

class Database:
    def save(password):
        today = time.strftime("%m/%d/%Y")

        conn = sqlite3.connect('savedPasswords.db')
        c = conn.cursor()

        ui.clearScreen()
        name = input("What Name would you like to store this password as?\n\n")
        ui.clearScreen()
        username = input("What Username (if any), would you like to save with this password?\n\n")
        ui.clearScreen()
        print(ui.Screen['verifySaveScreen']['header'])
        ui.innerSpace(8)
        print("Date: " + today)
        print("Name: " + name)
        print("Username: " + username)
        print("Password: " + password)
        ui.innerSpace(8)

        choice = 0

        while True:
            try:
                while(choice < 1) or (choice > ui.Screen['verifySaveScreen']['choice_count']):
                    choice = int(input(ui.Screen['verifySaveScreen']['menu']))
                break
            except ValueError:
                print(ui.Error['strOverInt'])

        if(choice == 1):
            c.execute("CREATE TABLE IF NOT EXISTS passwords (date TEXT, name TEXT, username TEXT, password TEXT)")
            c.execute("INSERT INTO passwords (date,name,username,password) VALUES (?,?,?,?)",(today,name,username,password))
            conn.commit()
            c.close()
            conn.close()
        elif(choice == 2):
            Database.save(password)
        else:
            quit()
