import time
import random
import os
playerhealth = 100
weapondmg = 5
allouttime = 0
healthposion = 10
playername = "Null"
lastletter = "null"
attackdmg = random.randint(1,weapondmg)
shielddmg = random.randint(1,4)
ma = True

def gamesetup():
    global playername
    print("Hello! Welcome to QuillStrike")
    print("You are in Quilland. A taribale monstor has attacked your vialge\nThe elder said that the mostonr is looking for the power gem\nand that he will do everything to find it. You are destend to destroy the mosntor\n")
    print("Type your name in:")
    playername = input("")
def monsterattack():
    global lastletter
    global playerhealth
    global ma
    global monsterdmg
    global attackdmg
    global shielddmg
    if ma <= 0:
        print("You are dead. The land of Quillstike is destroed")
        ma = False
    else:
        print("It is time for the mostor to attack")
        monsterdmgadd = random.randint(1,10)
        monsterdmg = 5
        if lastletter == "a" or lastletter == "A":
            monsterdmg = monsterdmg * 1.5
        if monsterdmgadd == 3:
            monsterdmg = monsterdmg * 1.5
        playerhealth = playerhealth - monsterdmg
        print("It does", monsterdmg)

def monsterBattle(monsterName, dmg, monsterhp):
    global weapondmg
    global playerhealth
    global allouttime
    global healthposion
    global lastletter
    global ma
    attackdmgr = 0
    monsterdmg = random.randint(1,dmg)
    while ma == True:
        if monsterhp <= 0:
            print("Good Job, you have won the mostor! You have won 1 bitcoin my bitcoin wallet: Q2k7jL4uY9eT8ZfV6n3m5H1aW0c")
            ma = False
        attackdmg = random.randint(1,weapondmg)
        shielddmg = random.randint(1,4)
        print("Hello", playername)
        print("Your helth is ", playerhealth)
        print("You are in battle with",monsterName,". The monster has", monsterhp," health. Will you...")
        print("[B]lock with shield(if attacker attacks, may lessen an amount of damage from the attacker)")
        print("[A]ll out attack(will do massive damage but leaves you exhausted. Being exhasted means if attacker attacks, they do 1.5 times more damage.)")
        print("[R]egular attack")
        print("[D]efence and counter(will do significantly less damage but enemy damage is also reduced.)")
        print("[U]se health potion")
        print("[E]xit the game")
        battle_do = input()
        if battle_do == "A" or battle_do == "a":
            if allouttime <= 0:
                print("You go on an all out attack")
                time.sleep(0.5)
                miss = random.randint(1,10)
                monsterdmg = monsterdmg * 2
                allouttime = 15
                if miss <= 5:
                    print("You race after ",monsterName," and slice, cut, and go all fury at you but you missed!")
                else:
                    attackdmgr = (attackdmg * 1.2)
                    monsterhp = monsterhp - attackdmgr
                    print("You cut, slice, and turn into a tornado of death. You do ",attackdmgr, " at the monster." )

            else:
                print("Sorry, you canot do more allout attacks until", allouttime ,"rounds")
        elif battle_do == "R" or battle_do =="r":
            miss = random.randint(1,1000)
            if miss <= 200:
                print("You do a regualr attack")
                print("But You miss")
            else:
                attackdmgr = attackdmg * 1.5
                print("You do a regualr attack")
                print("You use your sowrd to slice him, and do ", attackdmgr, "damage")
                monsterhp = monsterhp - attackdmgr
        elif battle_do == "U" or battle_do == "u":
            if healthposion == 0:
                print("you drink the health poision and gain 10 healrth")
                playerhealth  = playerhealth + 10
                healthposion = 11
            else:
                print("sorry, wait ", healthposion, "more rounds to have the health posion")
        elif battle_do == "E" or battle_do == "e":
            print("Ok, thanks for playing, the land of quillstrike is destroyed!")
            ma = False

#        elif battle_do == ""
        if allouttime > 0:
            allouttime = allouttime - 1
        if healthposion > 0:
            healthposion - 1
        time.sleep(1)
        monsterattack()
gamesetup()
monsterBattle("goblin", 10, 100)