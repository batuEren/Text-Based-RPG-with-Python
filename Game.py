                # Middle Earth RPG #
                
Development = False # Turn to True to get the text play faster

# Imports #

import time
import sys
import os


# Classes #

class Player:
    def __init__(self, maxhp, speed, intel, race):
        self.maxhp = maxhp
        self.hp = maxhp
        self.speed = speed
        self.intel = intel
        self.race = race
        self.lv = 1
        self.xp = 0


# Definitions #

def MainMenu():
    os.system('cls')
    speak("WELCOME TO ",0.1)
    sleep(1)
    speak("MIDDLE EARTH\n\n",0.4)
    speak("#### By Batu Eren ####\n\n 1-New Game\n 2-Load Game\n 3-Help\n 4-Options\n 5-Exit\n\n",0.01)
    x = input(">>> ")
    check(x,5)
    while True:
        if x == "1":
            speak("Loading...\n",0.3)
            input("ENTER to continue.")
            os.system('cls')
            characterMake()
            break
        elif x == "2":
            speak("You don't have a save file.\n",0.1)
            sleep(1)
            speak("Actually I don't know if you have a save file.\n",0.1)
            speak("But there is something I know is ",0.1)
            sleep(1)
            speak("THERE IS NO SAVE SYSTEM IN THIS GAME",0.2)
            speak("\nSo I put you to new game.\n",0.1)
            input("ENTER to continue.")
            os.system('cls')
            characterMake()
            break
        elif x == "3":
            speak("Actually there is nothing to help, you will read the\ntexts and choose one of the options but this game is not going to tell\nyou the story you are going to understand it your self\ndon't worry it's easy.\n",0.01)
            x = input(">>> ")
        elif x == "4":
            speak("There is no options avaliable for this game.\nBut probably language options will be added.",0.01)
            x = input(">>> ")
        elif x == "5":
            exit
            
        
def characterMake():
    # Give speech affect####YAPILDI####
    speak("Hello\n",0.1)
    speak("I am Tholnin, who gives lives to souls\n",0.1)
    speak("Let's start with your name.\n",0.1)
    # Buraları class a çevir ####YAPILDI#### 
    speak("What is your name ",0.01)
    name = input(">>> ")    
    speak(("What,!?!? are you really the "),0.07)
    speak((name,"\n"),0.5)
    speak(("Oww My God are you the "),0.07)
    speak((name,"\n"),0.5)
    speak("The ",0.12)
    speak(name,0.12)
    speak(" who has done ... ",0.12)
    sleep(2)
    speak("NOTHING\n",0.3)
    sleep(3)
    speak("HAHHAHAHAHAHHAHAHAHAHAHHAHAHAHHAHAHAHHAHA\n",0.03)
    sleep(2)
    speak("This joke never gets old\n",0.1)
    sleep(2)
    speak("What would you do ?\n 1-Laugh with him\n 2-Don't do anything \n 3-Say \"#%*?!#+/#\"\n ",0.01)
    x = input(">>> ")
    check(x,3)
    if x == "1":
        speak("I liked you, your turn was a human but I am gonna make you a strong elf.\n",0.1)
        player = Player(30, 10, 15, "elf")
        input("ENTER to continue.")
        Game()
    if x == "2":        
        speak("Whatever as I think your turn is a man.\n",0.1)
        player = Player(25, 8, 10, "man")
        input("ENTER to continue.")
        Game()
    if x == "3":
        speak("You forget I am the stronger one in here. Your turn was to be a human.\nBut I am going to make you a little hobbit.\n",0.07)
        player = Player(10, 6, 5, "hobbit")
        input("ENTER to continue.")        
        Game()
        
def speak(x,y):
    if Development:
        for character in x:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    else:
        for character in x:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(y)
    # Comments, menus = 0.01
    # Fast Talker and Askings = 0.04
    # Normal Talker = 0.07
    # Slow Talker = 0.1

def Game():
    os.system('cls')
    speak("You are feeling warm ...\n",0.2)
    sleep(2)
    speak("You wake up at an inn.\n",0.03)
    speak("What would you do ?\n 1-Ask to barman which city is here. \n 2-Exit\n",0.01)
    x = input(">>> ")
    check(x,2)
    if x == "1":
        speak("Barman Says : ",0.03)
        sleep(1)
        speak("Here is Minas Tirith, but if you want to go somewhere,\nyou will need a map.",0.07)
        time.sleep(1)
        speak(" You can buy one from maket in this city.\n",0.07)
        speak("What would you do ? \n 1-Start A Fight \n 2-Go And Jump trough a cliff\n",0.07)
        x = input(">>> ")
        check(x,2)
        if x == "1":
            speak("You start the fight and get chrushed\nby a grand piano which is thrown by Saruman\n",0.07)
            time.sleep(2)
            speak("Then you die.",0.1)
            os.system('cls')
            speak("##GAME OVER##",0.2)
            time.sleep(3)
            exit
        else:
            speak("You go to the cliff and jump.\n",0.07)
            time.sleep(1)
            speak("Then you hit the Eagle who carries Frodo and Gandalf.\nThe Eagle falls and you all die.",0.05)
            os.system('cls')
            speak("##GAME OVER##",0.2)
            time.sleep(3)
            exit
    elif x == "2":
        speak("While you are going to exit the Barman Says : \n",0.1)
        sleep(1)
        speak("You haven't payed the bill.\n",0.1)
        speak("What would you do ?\n 1-Escape \n 2-Go near to the barman to pay it.\n",0.01)
        x = input(">>> ")
        check(x,2)
        if x == "1":
            speak("The guard follows you\n",0.01)
            speak("What would you do ?\n 1-Turn and fight \n 2-Go out of city(to escape)\n",0.01)
            x = input(">>> ")
            check(x,2)
            if x == "1":
                speak("While you are turning you get a hit from the guard and die.",0.07)
                os.system('cls')
                speak("##GAME OVER##",0.2)
                time.sleep(3)
                exit
            else:
                os.system('cls')
                speak("##YOU WINN##",0.2)
                time.sleep(3)
                exit
        else:
            speak("Barman Says : ",0.1)
            sleep(1)
            speak("I was joking. You don't have anything to pay.\n",0.07)
            speak("Then a arrow goes trough your eyes. Which is throwen by Legolas.\n",0.07)
            time.sleep(1)
            speak("And an other goes trough you. And you die",0.07)
            time.sleep(1)
            os.system('cls')
            speak("##GAME OVER##",0.2)
            time.sleep(3)
            exit

def check(x,y):
    while int(x) < 1 or int(x) > y:
        print("Invalid number please enter numbers 1 to ",y)
        x = int(input(">>> "))
    return x

def sleep(x):
    if Development:
        pass
    else:
        time.sleep(x)

# Game Loop #

def GameLoop():
    MainMenu()

GameLoop()
