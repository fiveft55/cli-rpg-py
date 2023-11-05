import os

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
key = 0

#  create maps
        # col0    #col1    #col2    # col3   #col4   #col5    #col x=6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"], # row y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills",    "mountain"], # row 1
       ["forest", "fields", "bridge", "plains", "hills",  "forest",   "hills"], # row 2
       ["plains", "shop",   "town",   "mayor",  "plains",  "hills",   "mountain"], # row 3
       ["plains", "fields", "fields", "plains", "hills",  "mountain", "mountain"],]# row 4

y_len = len(map)-1
x_len = len(map[0])-1

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

# player status 
def player_stat():
    pass

#  system features
def clear():
    os.system("cls")

def draw():
    print("xx--------------------------------xx")

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
        save() # @autosave
        # print(name)
        clear()

        draw()
        print("- LOCATION: "+ biom[map[y][x]]["t"])
        print("- coordinates: ", x, y)
        draw()

        if name == "":
            name = "UNKNOWN-HERO"
        print("- NAME: " + name)
        print("- HP-HP: " + str(HP) + " /" + str(MAXHP))
        print("- ATTCK: " + str(ATK))
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
            # else:
            #     # y = y_len # open border
            #     y = 0 # close border
            pass
        elif dest == "2":
            if x < x_len:
                x += 1
            pass
        elif dest == "3":
            if y < y_len:
                y += 1
            # else:
            #     # y = 0 open border
            #     y = y_len # close border
            pass
        elif dest == "4":
            if x > 0:
                x -= 1
            pass