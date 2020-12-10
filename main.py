# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Iruoghene Godson Edewor
# Section:		411
# Assignment:		main.py
# Date:		11 17 2020
from math import *
import random
import time
player = 100
monster = 1000
potion = 0
coins = 10000

# spins for the potion
def rpotion():
    potion = random.randint(1,4)
    return potion

# codes for the admin mode
def admin():
    global player
    global monster
    print("\nWelcome admin.\n")
    print("You are fighting a monster defeat it.")
    while(True):
        if(player <= 0 or monster <= 0):
            break
        dmg = random.randint(1,6)
        print("\nNow Monster attacks with %.0f damage\n"% dmg)
        player -= dmg

        print("You have %.0f health"% player)

        # gives the admins a variety of extreme powers
        choice = int(input("\n\n1.Attack Monster\n2.Change monster health\n3.Change player health\n4.Deploy Special Attack\n5.Change Coins\n6.Shock Absorption\n7.Back to player\nEnter selection:"))
        if (choice == 1):
            playerdmg = int(input("\nNow attack the monster: "))
            monster -= playerdmg
            print("\nYou gave the monster %.0f damage\n"% playerdmg)

            print("Monster now has %.0f health\n"% monster)
        elif (choice == 2):
            monster = int(input("\nWhat do you want the new Monster's health to be: "))

            print("\nMonster now has %.0f health\n" % monster)
        elif (choice == 3):
            player = int(input("\nWhat do you want the new Player's health to be: "))

            print("\nPlayer now has %.0f health\n" % player)
        elif (choice == 4):
            print("Special Attack")
            print("\nSpecial Attack:Half Life")
            halflife = monster / 2
            monster -= halflife
            print("\nYou gave the monster %.0f damage\n"% halflife)

            print("Monster has %.0f health\n"% monster)

        elif (choice == 5):
            coins = int(input("\nHow many coins do you want to gain: "))

        elif (choice == 6):
            print("\nShock Absorption Activate")
            shock = dmg
            player += shock
            print("\nYou absorbed %.0f monster damage so you have %.0f health left\n"% (dmg, player))

        elif (choice == 7):
            break
        elif (choice >= 8 or choice <= 0):
            print("\nInvalid input.")

# the actual game engine
def rungame(choice):
    # creates some variables and calls others
    global player
    global monster
    global coins
    counter = 0
    potion = 0
    playerdmg = 0
    # gets the inputted choice and prints based on it or calls admin
    if(choice == 1):
        potion = rpotion()
        if(potion == 1):
            print("\nYou get a major strength potion.\n")
        if (potion == 2):
            print("\nYou get a minor strength potion.\n")
        if (potion == 3):
            print("\nYou get a reduced strength potion.\n")
    if(choice == 2):
            print("\nYou get no potion.\n")
    if(choice == 3):
            admin()
    print("You are fighting a monster defeat it.")

    while(True):
        # breaks if the player o monster is dead
        if player<=0 or monster<=0:
            break

        # determines how hard the monster hits
        print("\nMonster Attacking...")
        time.sleep(3)
        dmg = random.randint(1,6)

        print("\nNow Monster attacks with %.0f damage\n"% dmg)
        player-=dmg

        print("You have %.0f health"%player)

        # chooses whether to attack, endgame or admin
        nchoice = int(input("\nDo you want to attack the monster Yes(1) or No(2) or End Game(3): "))
        while(nchoice>4 or nchoice<1):
            print("\nInvalid input")
            nchoice = int(input("\nDo you want to attack the monster Yes(1) or No(2) or End Game(3): "))
        if nchoice == 3:
            break
        # player attacks based on what potion they got
        if(nchoice==1):
            counter+=1
            coins-=coins/4
            print("\nPlayer attacking...")

            if (potion == 1):
                playerdmg = random.randint(0,101)
            if (potion == 2):
                playerdmg = random.randint(0, 61)
            if (potion == 3):
                playerdmg = random.randint(0,26)
            if (choice == 2):
                playerdmg = random.randint(0,51)

            monster-=playerdmg
            print("\nYou gave the monster %.0f damage\n"% playerdmg)

            print("Monster has %.0f health\n"% monster)

        elif(nchoice == 4):
            admin()

        # a counter is kept per attack if it gets high enough, you deploy a special attack
        if(counter == 10):
            nwchoice = int(input("\nDo you want to deploy Your Special Attack Yes(1) or No(2): "))
            while nwchoice>3 or nwchoice<1:
                print("\nInvalid input")
                nwchoice = int(input("\nDo you want to deploy Your Special Attack Yes(1) or No(2): "))
            if(nwchoice == 1):
                print("\nSpecial Attack: Half Life")
                halflife = monster/2
                monster -= halflife
                print("\nYou gave the monster %.0f damage\n"% halflife)

                print("Monster has %.0f health\n"% monster)
                counter = 0
        # same here, but its even stronger this time
        if(counter == 20):
            nwchoice = int(input("\nDepoly Shock Absorption Yes(1) or No(2): "))
            while nwchoice>3 or nwchoice<1:
                print("\nInvalid input")
                nwchoice = int(input("\nDepoly Shock Absorption Yes(1) or No(2): "))
            if(nwchoice == 1):
                print("\nShock Absorption Activate")
                shock = dmg
                player+=shock
                print("\nYou absorbed %.0f monster damage so you have %.0f health left"%(dmg,player))
            counter = 0


# prints opening statements
print("Monster RPG")
print("Before you fight the boss you need potions\n\nIf you get major strength potion you can attack twice as hard-(At most 100 damage)\n\nIf you get minor strength potion you can attack with 10 more damage(At most 60 damage)\n\nIf you get a reduction potion your attack damage will be cut in half(At most 25 damage)\n\nIf you do not get a potion you can only do 50 damage")

# gets the players choice to spin or not
choice = int(input("\nDo you want to spin Yes(1) or No(2): "))
while choice>3 or choice<1:
    print("\nInvalid input.")
    choice = int(input("\nDo you want to spin Yes(1) or No(2): "))

rungame(choice)

if(player<=0):
    print("\n\nYou are dead.")
elif(player>0 and monster>0):
    print("\n\nYou have ended the game")
else:
    print("\n\nYou have defeated the Monster")
    print("You have %.0f health left"%player)
    print("You have gained %.0f coins" % coins)