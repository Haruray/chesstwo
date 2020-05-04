import random
import os
from bot_move import bot_move
from bot_move import bot_pawn

class Player():
    def __init__(self, symbol, position, job):
        self.symbol = symbol
        self.position = position
        self.job = job

class Arena():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[0 for i in range(width)] for i in range(height)]

    def update_arena(self):
        for i in player1.position:
            self.board[(player1.position[i][0])][(player1.position[i][1])] = i
        for i in player2.position:
            self.board[(player2.position[i][0])][(player2.position[i][1])] = i

    def create_arena(self): #JUST PRINTING THE ARENA. DONT MIND THIS
        self.update_arena()
        print("  ", end=" ")
        for i in range(self.width):
            print(i, end="   ")
        i = 0
        print()
        for square in self.board:
            print(i, end="||")
            for pawn in square:
                if pawn == 0:
                    print(pawn, end="  |")
                else:
                    try:
                        test=pawn[2]
                        print(pawn, end="|")
                    except:
                        print(pawn,end=" |")
            print()
            i += 1


def move_pawn(player_sym):
    global bot,difficulty
    if player_sym== player2.symbol and bot: #BOT MOVEMENT
        pawn=bot_pawn(arena.board,arena.height,arena.width,player2.position,player1.position,difficulty)#PAWN CHOOSING
    else:
        while (True):
            if player_sym==player1.symbol:
                pawns=[]
                for i in player1.position.keys():
                    pawns.append(i)
                pawn = input("What pawn to move : ") #PLAYER MOVEMENT. UNTIL INPUT IS VALID
                try: #VALIDATION USING ERROR EXCEPTION
                    pawns.index(pawn)
                except:
                    print("wrong pawn. Do it again")
                    pawn="None"
                if pawn!="None":
                    break
    if player_sym == player1.symbol:
        current_pawn_pos = player1.position[pawn]  # take current position
    else:
        current_pawn_pos = player2.position[pawn]
    if player_sym== player2.symbol and bot: #bot movement
        x,y = bot_move(pawn,arena.board,player2.position,player1.position,difficulty)
        validate = validate_move([x, y], current_pawn_pos)
        while not (validate[0]):  # validate movement
            x,y = bot_move(pawn,arena.board,player2.position,player1.position,difficulty)
            validate = validate_move([x, y], current_pawn_pos)
        command = validate[1]
    else:
        print("move to? (left number then upper number) :", end=" ") #if not bot, then player make a move
        x, y = map(int, input().split())  # movement
        validate = validate_move([x, y], current_pawn_pos)

        while not (validate[0]):  # validate movement
            print("cant move there. Do it again")
            x, y = map(int, input().split())
            validate = validate_move([x, y], current_pawn_pos)
        command = validate[1]

    if command == "move":
        arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0  # erasing pawn in previous pos
        arena.board[x][y] = pawn  # updating the new pos in arena
        if player_sym == player1.symbol:
            player1.position[pawn] = [x, y]  # updating the new pos in player's pawn list
        else:
            player2.position[pawn] = [x, y]
    elif command == "attack":
        if (special_move("attack")): #checking if the attack is successful
            print("SUCCESSFUL ATTACK!!!")
            if (special_move("defend")): #if defend=True, then you lost your pawn
                print("sorry...but you lost your pawn.")
                if player_sym == "X":
                    arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0 #updating arena by deleting dead pawns
                    defeated_pawn = arena.board[x][y]
                    player2.position.pop(defeated_pawn)
                    player1.position.pop(pawn)
                    arena.board[x][y] = 0
                else:
                    arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0 #updating arena by deleting dead pawns
                    defeated_pawn = arena.board[x][y]
                    player1.position.pop(defeated_pawn)
                    player2.position.pop(pawn)
                    arena.board[x][y] = 0
            else: #if defend failed, then enemy die
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0
                if player_sym == player1.symbol: #updating arena by deleting dead pawns and moving current pawn
                    defeated_pawn = arena.board[x][y]
                    player2.position.pop(defeated_pawn)
                    arena.board[x][y] = pawn
                    player1.position[pawn] = [x, y]  # updating the new pos in player's pawn list
                else:
                    defeated_pawn = arena.board[x][y] #updating arena by deleting dead pawns and moving current pawn
                    player1.position.pop(defeated_pawn)
                    arena.board[x][y] = pawn
                    player2.position[pawn] = [x, y]
        elif (special_move("defend")): #failed attack, but successful defense
            print("Too bad,you lost your pawn")
            if player_sym == player1.symbol:
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0
                player1.position.pop(pawn)
            else:
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0
                player1.position.pop(pawn)
        else:
            print("Too bad. Nothing happens")


def validate_move(move_pos, current_pos):
    global current_turn
    #this is too long but here's a summary
    #if you are a ninja, you can move 2 blocks away from your position. if you are not a ninja, then only 1 block.
    #if you stumble upon an enemy, then it will automatically detected as an attack
    #you also cant move to a block that is occupied by a friendly pawn
    if current_turn == "X":
        if not (player1.job == "Ninja"):
            if (abs(move_pos[0] - current_pos[0]) > 1) or (abs(move_pos[1] - current_pos[1]) > 1) or move_pos[0] < 0 or \
                    move_pos[1] < 0 or move_pos[0] > arena.height-1 or move_pos[1] > arena.width-1:
                k = [False, "none"]
                return (k)
            else:
                if (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (
                        arena.board[(move_pos[0])][(move_pos[1])][0] != current_turn):
                    k = [True, "attack"]
                    return (k)
                elif (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (arena.board[(move_pos[0])][(move_pos[1])][0] == current_turn):
                    k = [False, "none"]
                    return (k)
                else:
                    k = [True, "move"]
                    return (k)
        else:
            if (abs(move_pos[0] - current_pos[0]) > 2) or (abs(move_pos[1] - current_pos[1]) > 2) or move_pos[0] < 0 or \
                    move_pos[1] < 0 or move_pos[0] > arena.height-1 or move_pos[1] > arena.width-1:
                k = [False, "none"]
                return (k)
            else:
                if (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (
                        arena.board[(move_pos[0])][(move_pos[1])][0] != current_turn):
                    k = [True, "attack"]
                    return (k)
                elif (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (arena.board[(move_pos[0])][(move_pos[1])][0] == current_turn):
                    k = [False, "none"]
                    return (k)
                else:
                    k = [True, "move"]
                    return (k)
    else:
        if not (player2.job == "Ninja"):
            if (abs(move_pos[0] - current_pos[0]) > 1) or (abs(move_pos[1] - current_pos[1]) > 1) or move_pos[0] < 0 or \
                    move_pos[1] < 0 or move_pos[0] > arena.height or move_pos[1] > arena.width:
                k = [False, "none"]
                return (k)
            else:
                if (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (
                        arena.board[(move_pos[0])][(move_pos[1])][0] != current_turn):
                    k = [True, "attack"]
                    return (k)
                elif (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (arena.board[(move_pos[0])][(move_pos[1])][0] == current_turn):
                    k = [False, "none"]
                    return (k)
                else:
                    k = [True, "move"]
                    return (k)
        else:
            if (abs(move_pos[0] - current_pos[0]) > 2) or (abs(move_pos[1] - current_pos[1]) > 2) or move_pos[0] < 0 or \
                    move_pos[1] < 0 or move_pos[0] > arena.height or move_pos[1] > arena.width:
                k = [False, "none"]
                return (k)
            else:
                if (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (
                        arena.board[(move_pos[0])][(move_pos[1])][0] != current_turn):
                    k = [True, "attack"]
                    return (k)
                elif (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (arena.board[(move_pos[0])][(move_pos[1])][0] == current_turn):
                    k = [False, "none"]
                    return (k)
                else:
                    k = [True, "move"]
                    return (k)


def special_move(command):
    global current_turn
    #rng shit
    if command == "attack":
        chance = round(random.random() * 100)  # chance percentage
        if current_turn == "X":
            if player1.job == "Gladiator":
                if chance <= 70:
                    chance += 30
                elif chance >= 70 and chance <= 90:
                    chance += 10
            elif player1.job == "Guardian":
                if chance >= 60:
                    chance -= 20
            elif player1.job == "Ninja":
                if chance <= 60:
                    chance += 10
        else:
            if player2.job == "Gladiator":
                if chance <= 70:
                    chance += 30
                elif chance >= 70 and chance <= 90:
                    chance += 10
            elif player2.job == "Guardian":
                if chance >= 60:
                    chance -= 20
            elif player2.job == "Ninja":
                if chance <= 60:
                    chance += 10

        roullete = [True for i in range(chance)]  # roullete of 1 and 0
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick
    elif command == "defend":
        chance = round(random.random() * 100)  # chance percentage
        if current_turn == "Y":
            if player1.job == "Gladiator":
                chance = 10
            elif player1.job == "Guardian":
                if chance <= 40:
                    chance += 30
                elif chance >= 40 and chance <= 70:
                    chance += 10
            elif player1.job == "Ninja":
                if chance >= 30:
                    chance -= 30
        else:
            if player2.job == "Guardian":
                if chance <= 70:
                    chance += 30
                elif chance >= 70 and chance <= 90:
                    chance += 10
            elif player2.job == "Gladiator":
                chance = 10
            elif player2.job == "Ninja":
                if chance >= 20:
                    chance -= 20
        roullete = [True for i in range(chance)]  # roullete of 1 and 0
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick


# MAIN PROGRAM
arena = Arena(10, 6)
y_default_pos= {"Y1": [9, 1], "Y2": [9, 2], "Y3": [9, 3], "Y4": [9, 4],"Y5": [8, 1],"Y6": [8, 2],"Y7": [8, 3],"Y8": [8, 4],"Y9": [7, 2],"Y10": [7, 3],"Y11": [6, 2],"Y12": [6, 3]}
x_default_pos={"X1": [0, 1], "X2": [0, 2], "X3": [0, 3], "X4": [0, 4],"X5": [1, 1],"X6": [1, 2],"X7": [1, 3],"X8": [1, 4],"X9": [2, 2],"X10": [2, 3],"X11": [3, 2],"X12": [3, 3]}
print("Wants to play againts 1)Other player, or 2)bot?")
c=int(input())
if c==2:bot=True
print("Select difficulty: 1)Easy, or 2)Normal?")
c=int(input())
if c==1: difficulty="Easy"
else: difficulty="Normal"
print("1)custom job, or 2)default?")
c = int(input())
if c == 1:
    print("Player X, whats your job? 1) Gladiator, 2)Guardian, or 3)Ninja?")
    c = int(input())
    if c == 1:
        player1 = Player("X", x_default_pos, "Gladiator")
    elif c == 2:
        player1 = Player("X", x_default_pos, "Guardian")
    else:
        player1 = Player("X", x_default_pos, "Ninja")
    if not bot:
        print("Player Y, whats your job? 1) Gladiator, 2)Guardian, or 3)Ninja?")
        c = int(input())
    else: c=random.randint(1,3)
    if c == 1:
        print("Player Y chooses Gladiator!")
        player2 = Player("Y", y_default_pos, "Gladiator")
    elif c == 2:
        print("Player Y chooses Guardian!")
        player2 = Player("Y", y_default_pos, "Guardian")
    else:
        print("Player Y chooses Ninja!")
        player2 = Player("Y", y_default_pos, "Ninja")
else:
    player1 = Player("X", x_default_pos, "Gladiator")
    player2 = Player("Y", y_default_pos, "Gladiator")

arena.create_arena()
current_turn = player1.symbol

while (True):
    if current_turn == player1.symbol:
        os.system("cls")
        print("=====================PLAYER 1 TURN========================")
        move_pawn(player1.symbol)
        arena.create_arena()
        current_turn = player2.symbol

    elif current_turn == player2.symbol:
        print("=====================PLAYER 2 TURN========================")
        move_pawn(player2.symbol)
        arena.create_arena()
        current_turn = player1.symbol