import os, random

run = True
menu = True
play = False
rules = False

HP = 50
MAXHP = HP
ATK = 3
pot = 1
mana = 0
gold = 0
x, y = 0, 0
key = False
standing = True
buy = False
speak = False
boss = False

#  create maps
        # col0    #col1    #col2    # col3   #col4   #col5    #col x=6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"], # row y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills",    "mountain"], # row 1
       ["forest", "fields", "bridge", "plains", "hills",  "forest",   "hills"], # row 2
       ["plains", "shop",   "town",   "mayor",  "plains",  "hills",   "mountain"], # row 3
       ["plains", "fields", "fields", "plains", "hills",  "mountain", "mountain"],]# row 4

y_len = len(map)-1
x_len = len(map[0])-1

# enemy list
e_list = ['Goblin', 'Orc', 'Slime']

mobs = {
    "Goblin": {
        'hp': 15,
        'at': 3,
        'go': 8
    },
    "Orc": {
        'hp': 35,
        'at': 5,
        'go': 18
    },
    "Slime": {
        'hp': 30,
        'at': 2,
        'go': 12
    },
    # boss
    "Dragon": {
        'hp': 100,
        'at': 8,
        'go': 100
    },
}

# create biom
biom = {
    "plains": {
        "t": "PLAINS",
        "e": True,
    },
    "forest": {
        "t": "WOODS",
        "e": True,
    },
    "fields": {
        "t": "FIELDS",
        "e": False,
    },
    "bridge": {
        "t": "BRIDGE",
        "e": True,
    },
    "town": {
        "t": "TOWN CENTER",
        "e": False,
    },
    "shop": {
        "t": "SHOP",
        "e": False,
    },
    "mayor": {
        "t": "MAYOR",
        "e": False,
    },
    "cave": {
        "t": "CAVE",
        "e": False,
    },
    "mountain": {
        "t": "MOUNTAIN",
        "e": True,
    },
    "hills": {
        "t": "HILLS",
        "e": True,
    }

}

# print(y_len, x_len)

current_tile = map[y][x]
# print(current_tile)
name_of_tile = biom[current_tile]["t"]
# print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
# print(enemy_tile)

# player status - organize in future ::ref
def player_stat():
    pass

#  system features
def clear():
    os.system("cls")

def draw():
    print("xx--------------------------------xx")

# final boss
def cave():
    global boss, key, name, fight

    while boss:
        clear()
        draw()
        print("...HERE LIES THE CAVE OF THE DRAGON...")
        print("WHAT WILL YOU DO, " + name + "?")
        draw()
        if key:
            print("1 - USE KEY!")
        print("2 - TURN BACK!")
        draw()

        choice = input(">: ")

        if choice == '1':
            if key:
                fight = True
                battle()

        elif choice == '2':
            boss = False


def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("You're not strong enough to face the dragon yet!" + "\nCome back after you become stronger!")
            key = False
        else:
            print("You might defeat the dragon! Take this key, warrior! And find the cave...")
            key = True
            pass
        
        draw()
        print("1 - LEAVE")
        draw()

        choice = input("#: ")

        if choice == '1':
            speak = False

# shop func
def shop():
    global buy, gold, pot, mana, ATK

    while buy:
        clear()
        draw()
        print("WELCOME TO THE SHOP!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("MANA: " + str(mana))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30HP): 5 GOLD")
        print("2 - BUY MANA (50HP): 10 GOLD")
        print("3 - UPGRADE ATK (+2): 25 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input(">: ")

        if choice == '1':
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You bought potion!")
            else:
                print("You don't have money!")
            input(">: ")
            pass
        elif choice == '2':
            if gold >= 10:
                mana += 1
                gold -= 10
                print("You bought mana!")
            else:
                print("You don't have money!")
            input(">: ")
            pass
        elif choice == '3':
            if gold >= 25:
                ATK += 2
                gold -= 25
                print("You bought an upgrade!")
            else:
                print("You don't have money!")
            input(">: ")
            pass
        elif choice == '4':
            buy = False


# func for savin files
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(mana),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]
    # local io-filing
    f = open("save.txt", 'w')
    for item in list:
        f.write(item + "\n")
    f.close()

# heal func
def heal(amount):
    global HP
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + "'s HP refilled to " + str(HP) +"!")
    
# battle mode
def battle():
    global fight, play, run, HP, pot, mana, gold, boss
    # print("Commence fightin!")
    # input(">: ")
    if not boss:
        enemy =  random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]['hp']
    hpmax = hp
    atk = mobs[enemy]['at']
    g = mobs[enemy]['go']

    # fight loop
    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(MAXHP))
        print("POTIONS: " + str(pot))
        print("MANA: " + str(mana))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if mana > 0:
            print("3 - USE MANA (50HP)")
        if pot == 0 and mana == 0: print("NO ITEMS or MAGIC")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input(">: ")
            pass
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input(">: ")
            else:
                print("You don't have any potions!")
                input(">: ")

            pass
        elif choice == "3":
            if mana > 0:
                mana -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input(">: ")
            else:
                print("You have no mana!")
                input(">: ")
            pass

        # play-result
        if HP <= 0:
            print(enemy + " defeated " + name + "....")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input(">: Enter - Quit")
        pass

        if hp <= 0:
            print(name + " defeated " + enemy + "....")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("CONGRATULATIONS, YOU HAVE DEFEATED THE DRAGON!!!, " + name)
                boss = False
                play = False
                run = False
            input(">: ")
            clear()

# Game-loop
while run:

    while menu:
        clear()
        # print(y_len, x_len)
        print("xx--------------------------------xx\n"+"---------     GAMEDEMO     ---------\n"+"xx--------------------------------xx ")
        draw()
        print("1: NEW GAME")
        print("2: LOAD GAME")
        print("3: RULES")
        print("4: QUIT")
        draw()
        # pass
        if rules:
            print('This is a demo game. Please type the no. as shown.')
            rules = False
            choice = ""
            input(">: Press 'Enter' to go back!")
        else:
            choice = input("#: ")
        
        # pass
        if choice == '1':
            clear()
            name = input("What is your name mortal? : ")
            menu = False
            play = True
            x = 0; y = 0
        
        elif choice == '2':
            try:
                f = open('save.txt', 'r')
                load_list = f.readlines()

                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    mana = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = int(load_list[8][:-1])
                    # check load
                    # print(name, HP, ATK)
                    clear()
                    # print("LOCATION: "+ biom[map[y][x]]["t"])
                    draw()
                    print("   ^-^.-? WELCOME BACK, " + name + "!")
                    draw()
                    input(">: Enter to continue...")

                    menu = False
                    play = True
                
                else:
                    print("File seems to be corrupted. Start A New Game!")
                    input("> ")
            
            except OSError:
                print("No loadable save file.")
                input("> ") 

        elif choice == '3':
            clear()
            rules = True

        elif choice == '4':
            quit()

    while play:
        # print(name)
        save() # @autosave
        clear()

        # enemy spawn::
        if not standing:
            if biom[map[y][x]]['e']:
                if random.randint(0, 100) < 0: # less than 30 as value
                    fight = True
                    battle()
        
        if play:

            draw()
            print("- LOCATION: "+ biom[map[y][x]]["t"])
            print("- coordinates: ", x, y)
            draw()

            if name == "":
                name = "UNKNOWN-HERO"
            print("- NAME: " + name)
            print("- HP-HP: " + str(HP) + " /" + str(MAXHP))
            print("- ATTAK: " + str(ATK))
            print("- POTIN: " + str(pot))
            print("- MANA.: " + str(mana))
            print("- GOLD.: " + str(gold))

            print(":- Enter '0' to save and quit -:")
            draw()

            # player movement
            # print("\n")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            draw()
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if mana > 0:
                print("6 - USE MANA (50HP)")
            if pot == 0 and mana == 0: print("NO ITEMS or MAGIC")

            if map[y][x] == 'shop' or map[y][x] == 'mayor' or map[y][x] == 'cave':
                print("7 - INTERACT")
            draw()
                

            # destination
            dest = input("# ")

            if dest == '0':
                play = False
                menu = True
                save() # go back to menu save
                input(">: Enter to quit")
                # quit()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
                # else:
                #     # y = y_len # open border
                #     y = 0 # close border
                pass
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False

                pass
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False

                # else:
                #     # y = 0 open border
                #     y = y_len # close border
                pass
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
                pass
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("You have no potion!")
                input(">: ")
                standing = True
            elif dest == "6":
                if mana > 0:
                    mana -= 1
                    heal(50)
                else:
                    print("You have no mana!")
                input(">: ")
                standing = True
            elif dest == "7":
                if map[y][x] == 'shop':
                    buy = True
                    shop()
                if map[y][x] == 'mayor':
                    speak = True
                    mayor()
                if map[y][x] == 'cave':
                    boss = True
                    cave()
            else: standing = True
















