#🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲
# This snippet is designed to generate a character for an rpg. 
# The game system is RuneQuest 3rd edition (1984) with Wiltsun Rune Quest (WRQ) quirks from 2020.
# Currently only available race is basic human
# The creations are then saved to a simple txt -file for easy access
# There is a simple interface to choose what to do.
# The user can generate as many charactes as he wants to.
#🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲

# don't need others, I think
from os import write
from random import randint
# File access and eg. round methods are needed at least
import sys 
import math

# Initialize the character roster
currentCharacters = []

#================================
#= The D6 Dice                  =
#================================

# Character characteristics are determined by casting a specific set six sided dice with modifiers
# This is the six sided die function to be deployed all over the script
def D6(dices):
    dieSum = 0
    for i in range(dices):
        dieSum += randint(1, 6)
    return dieSum

#================================ In rpg's, tables are important 
#= The Tables                   = Most things are looked up from a table
#================================ Here are the tables needed 

# Dexterity Strike Ranks
dexSrTable = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:3,11:3,12:3,13:3,14:3,15:3,16:2,17:2,18:2,19:2,20:1,21:1,22:1,23:1,24:1,25:1,30:1,31:1,32:1}
# Size Strike Ranks
sizSrTable = {1:3,2:3,3:3,4:3,5:3,6:3,7:3,8:3,9:3,10:2,11:2,12:2,13:2,14:2,15:2,16:1,17:1,18:1,19:1,20:1,21:1,22:1,23:1,24:1,25:1,26:1,27:1,28:1,29:1}
# Damage modifier table
damModTable = {1:"-D4", 2:"-D4", 3:"-D4", 4:"-D4", 5:"-D4", 6:"-D4", 7:"-D4", 8:"-D4", 9:"-D4", 10:"-D4", 11:"-D4", 12:"-D4", 13:"0", 14:"0", 15:"0", 16:"0", 17:"0", 18:"0", 19:"0", 20:"0", 21:"0", 22:"0", 23:"0", 24:"0", 25:"D4", 26:"D4", 27:"D4", 28:"D4", 29:"D4", 30:"D4", 31:"D4", 32:"D4", 33:"D6", 34:"D6", 35:"D6", 36:"D6", 37:"D6", 38:"D6", 39:"D6", 40:"D6", 41:"2D6", 42:"2D6", 43:"2D6", 44:"2D6", 45:"2D6", 46:"2D6", 47:"2D6", 48:"2D6", 49:"2D6", 50:"2D6", 51:"2D6", 52:"2D6", 53:"2D6", 54:"2D6", 55:"2D6", 56:"2D6", 57:"3D6"}
# Primary skill modifier table
primarySkillModTable = {1:-9, 2:-8, 3:-7, 4:-6, 5:-5, 6:-4, 7:-3, 8:-2, 9:-1, 10:0, 11:1, 12:2, 13:3, 14:4, 15:5, 16:6, 17:7, 18:8, 19:9, 20:10, 21:11, 22:12, 23:13, 24:14, 25:15, 26:16, 27:17, 28:18, 29:19, 30:20, 31:21, 32:22}
# Secondary skill modifier table
secondarySkillModTable = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:1, 12:1, 13:2, 14:2, 15:3, 16:3, 17:4, 18:4, 19:5, 20:5, 21:6, 22:6, 23:7, 24:7, 25:8, 26:8, 27:9, 28:9, 29:10, 30:10, 31:11, 32:11}
# Negative skill modifier table
negSkillModTable = {1:9, 2:8, 3:7, 4:6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0, 11:-1, 12:-2, 13:-3, 14:-4, 15:-5, 16:6, 17:7, 18:8, 19:-9, 20:-10, 21:-11, 22:-12, 23:-13, 24:-14, 25:-15, 26:-16, 27:-17, 28:-18, 29:-19, 30:-20, 31:-21, 32:-22}
# Hit points in hit locations
# FeeT
hitPointsFeet = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:6, 17:6, 18:6, 19:7, 20:7, 21:7, 22:8, 23:8, 24:8, 25:9, 26:9, 27:9, 28:10, 29:10, 30:10, 31:11, 32:11, 33:11, 34:12, 35:12, 36:12, 37:13, 38:13, 39:13, 40:14, 41:14, 42:14}
# Abdomen
hitPointsAbdomen = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:6, 17:6, 18:6, 19:7, 20:7, 21:7, 22:8, 23:8, 24:8, 25:9, 26:9, 27:9, 28:10, 29:10, 30:10, 31:11, 32:11, 33:11, 34:12, 35:12, 36:12, 37:13, 38:13, 39:13, 40:14, 41:14, 42:14}
# Chest
hitPointsChest = {1:2, 2:2, 3:2, 4:3, 5:3, 6:3, 7:4, 8:4, 9:4, 10:5, 11:5, 12:5, 13:6, 14:6, 15:6, 16:7, 17:7, 18:7, 19:8, 20:8, 21:8, 22:9, 23:9, 24:9, 25:10, 26:10, 27:10, 28:11, 29:11, 30:11, 31:12, 32:12, 33:12, 34:13, 35:13, 36:13, 37:14, 38:14, 39:14, 40:15, 41:15, 42:15}
# Hands
hitPointsHands = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:3, 11:3, 12:3, 13:4, 14:4, 15:4, 16:5, 17:5, 18:5, 19:6, 20:6, 21:6, 22:7, 23:7, 24:7, 25:8, 26:8, 27:8, 28:9, 29:9, 30:9, 31:10, 32:10, 33:10, 34:11, 35:11, 36:11, 37:12, 38:12, 39:12, 40:13, 41:13, 42:13}
# Head
hitPointsHead = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:6, 17:6, 18:6, 19:7, 20:7, 21:7, 22:8, 23:8, 24:8, 25:9, 26:9, 27:9, 28:10, 29:10, 30:10, 31:11, 32:11, 33:11, 34:12, 35:12, 36:12, 37:13, 38:13, 39:13, 40:14, 41:14, 42:14}

#================================
#= This is human -race class    =
#================================
class Human():
    # The constructor
    def __init__(self, name):
        # The name of the instance ie. the name of the character is important to have around
        self.name = name
        # Race on print too, since there will be other races also
        self.race = "Human"
        # Every human get initial race characteristics randomly generated as per RQ rules
        self.str = D6(3)
        self.con = D6(3)
        self.siz = D6(2)+6
        self.int = D6(2)+6
        self.pow = D6(3)
        self.dex = D6(3)
        self.app = D6(3)

        # Hitpoints are determined by characteristics, rounded up as per the rules
        self.hp = int(math.ceil((self.siz+self.con)/2))
        # Fatigue points
        self.fp = self.str+self.siz
        # Magic points
        self.mp = self.pow

        # Dexterity strike rank
        self.dsr = dexSrTable.get(self.dex)
        # Size strike rank
        self.ssr = sizSrTable.get(self.siz)
        # And melee strike rank is
        self.meleesr = self.dsr+self.ssr

        # The bigger and stronger = more damage done in melee!
        self.dmod = damModTable.get(self.str+self.siz)

        # Skill modifiers, there are seven
        # Agility 
        self.agilitySkillMod = primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str) + negSkillModTable.get(self.siz)
        # Communication
        self.communicationSkillMod = primarySkillModTable.get(self.int) + secondarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.app)
        # Knowledge
        self.knowledgeSkillMod = primarySkillModTable.get(self.int)
        # Magical
        self.magicalSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.dex)
        # Manipulation
        self.manipulationSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str)
        # Perception
        self.perceptionSkillMod = primarySkillModTable.get(self.int) + secondarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.con)
        # Stealth
        self.stealthSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str)

        # A character has hit locations each with it's hitpoints (and armorpoints but this dude is nude that way)
        # Looked up in a table
        # Hitlocs
        self.feetHp = hitPointsFeet.get(self.hp)
        self.abdomenHp = hitPointsAbdomen.get(self.hp)
        self.chestHp = hitPointsChest.get(self.hp)
        self.handsHp = hitPointsHands.get(self.hp)
        self.headHp = hitPointsHead.get(self.hp)

        # Finally, since I know no other way to accomplish this at this point...
        # Write the generated character name into an easily accessible list.
        currentCharacters.append(name)

#================================
#= This is orc -race class      = This is the WRQ orc, not slimy Tolkien-one
#================================
class Orc():
    # The constructor
    def __init__(self, name):
        # The name of the instance ie. the name of the character is important to have around
        self.name = name
        # Race on print too, since there will be other races also
        self.race = "Orc"
        # Every human get initial race characteristics randomly generated as per RQ rules
        self.str = D6(5)
        self.con = D6(3)+3
        self.siz = D6(2)+6
        self.int = D6(2)+6
        self.pow = D6(3)
        self.dex = D6(3)
        self.app = D6(3)

        # Hitpoints are determined by characteristics, rounded up as per the rules
        self.hp = int(math.ceil((self.siz+self.con)/2))
        # Fatigue points
        self.fp = self.str+self.siz
        # Magic points
        self.mp = self.pow

        # Dexterity strike rank
        self.dsr = dexSrTable.get(self.dex)
        # Size strike rank
        self.ssr = sizSrTable.get(self.siz)
        # And melee strike rank is
        self.meleesr = self.dsr+self.ssr

        # The bigger and stronger = more damage done in melee!
        self.dmod = damModTable.get(self.str+self.siz)

        # Skill modifiers, there are seven
        # Agility 
        self.agilitySkillMod = primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str) + negSkillModTable.get(self.siz)
        # Communication
        self.communicationSkillMod = primarySkillModTable.get(self.int) + secondarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.app)
        # Knowledge
        self.knowledgeSkillMod = primarySkillModTable.get(self.int)
        # Magical
        self.magicalSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.dex)
        # Manipulation
        self.manipulationSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str)
        # Perception
        self.perceptionSkillMod = primarySkillModTable.get(self.int) + secondarySkillModTable.get(self.pow) + secondarySkillModTable.get(self.con)
        # Stealth
        self.stealthSkillMod = primarySkillModTable.get(self.int) + primarySkillModTable.get(self.dex) + secondarySkillModTable.get(self.str)

        # A character has hit locations each with it's hitpoints (and armorpoints but this dude is nude that way)
        # Looked up in a table
        # Hitlocs
        self.feetHp = hitPointsFeet.get(self.hp)
        self.abdomenHp = hitPointsAbdomen.get(self.hp)
        self.chestHp = hitPointsChest.get(self.hp)
        self.handsHp = hitPointsHands.get(self.hp)
        self.headHp = hitPointsHead.get(self.hp)

        # Finally, since I know no other way to accomplish this at this point...
        # Write the generated character name into an easily accessible list.
        currentCharacters.append(name)


#================================ The dongle to write an object to a text file, line by line
#= Write to file                = All desired characters will be merely appended to the file
#================================ line by line

# function to do the write to file, argument is the character objects' name
def writeCharsToFile(name):

    # first the properties are extracted, objects can't be processed I think
    processIt = vars(name)
    # the objects properties are processed as key-value pairs in to this sort of buffer variable
    # the handy but not recommended %s-formatting is used
    toWrite = ("%s: %s \n" % item for item in processIt.items())
    
    # open or initiate the text file in append/text mode
    stream = open("characters.txt", "at")
    # the appending of mybuffer to the file
    stream.writelines(toWrite)
    # add an empty line after a character
    stream.writelines("\n")
    stream.close()

#================================ 
#= Display characters           = 
#================================ 

def showCharacters():
    print("Characters currently generated: \n")
    for i in range(len(currentCharacters)):
        print(currentCharacters[i])


#================================
#= The Interface Logic          =
#================================


## The Header ##
theHeader = '''
==========================================================
===                                                    ===
===          The RQ Character Generator v. 0.1         ===
===                                                    ===
==========================================================
'''

## The Menu ##
theMenu = '''
###########################################################
#                                                         #
#  1  -  Generate a Human character and write it to file  #
#                                                         #
#  2  -  Generate an Orc character and write it to file   #
#                                                         #
#  3  -  Display current session character names          #
#                                                         #
#  0  -  Quit                                             #
#                                                         #
###########################################################
'''

print(theHeader)

# On first run set end to 1
end = 1

while end != 0:
    try:
        print(theMenu)
        userInput = int(input("Please select an operation: "))

        if userInput == 1:
            userInputName = input("Enter name for Human character: ")
            # Initiate a new instance of the class, name it with the user input name
            userInputName = Human(userInputName)
            print("Did I generate?: ", userInputName)
            writeCharsToFile(userInputName)
        
        elif userInput == 2:
            userInputName = input("Enter name for Orc character: ")
            # Initiate a new instance of the class, name it with the user input name
            userInputName = Orc(userInputName)
            print("Did I generate?: ", userInputName)
            writeCharsToFile(userInputName)

        # Write last created character to file, since it's name is in the input variable    
        elif userInput == 3:
            showCharacters()

        elif userInput == 0:
            print("Bye!")
            break
        else:
            print("Enter 1, 2, 3 or 0.")
    except:
        print("Something went wrong... try again.")
