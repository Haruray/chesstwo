import random
from bot_move import bot_move
from bot_move import bot_pawn

class Player():
    def __init__(self, symbol, position, job,bot=False):
        self.symbol = symbol
        self.position = position
        self.job = job
        self.bot=bot
    def chance_bonus(self,command):
        if command == "attack":
            if self.job == "Gladiator":
                return 30
            elif self.job=="Guardian":
                return -20
            elif self.job=="Ninja":
                return 10
        elif command=="defense":
            if self.job == "Gladiator":
                return 0
            elif self.job=="Guardian":
                return 30
            elif self.job=="Ninja":
                return -30

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
    global bot,difficulty,current_turn
    this_turn=globals()[current_turn] #USING "current_turn" AS A VARIABLE TO WORK WITH
    if current_turn=="player1":
        opponent=globals()["player2"]
    else:
        opponent=globals()["player1"]
    #PAWN CHOOSING
    #IF BOT THEN DO THIS
    if this_turn.bot==True: #BOT MOVEMENT
        pawn=bot_pawn(arena.board,arena.height,arena.width,this_turn.position,opponent.position,difficulty)#PAWN CHOOSING FROM MODULE
    else:
    #IF ITS PLAYER, THEN MANUAL CHOOSING. INPUT WILL BE VALIDATED
        while (True):
            pawn = input("What pawn to move : ")  # PLAYER MOVEMENT. UNTIL INPUT IS VALID
            if this_turn.position.get(pawn): #IF THE PAWN EXISTS, THEN INPUT IS VALID
                break
            else: #IF NOT VALID, THEN NO
                print("wrong pawn. Do it again")
    current_pawn_pos=this_turn.position.get(pawn) #TAKING CURRENT PAWN POSITION
    #MOVEMENT TIME. IF CURRENT TURN IS BOT, THEN DO THIS
    if this_turn.bot:
        x,y = bot_move(pawn,arena.board,player2.position,player1.position,difficulty) #MOVING USING bot_move MODULE
        validate = validate_move([x, y], current_pawn_pos) #RETURNING 2 VALUE. THE FIRST ONE IS BOOLEAN, THE OTHER ONE IS COMMAND (ATTACK OR MOVE)
        while not (validate[0]):  # validate movement
            x,y = bot_move(pawn,arena.board,player2.position,player1.position,difficulty)
            validate = validate_move([x, y], current_pawn_pos)
        command = validate[1]
    else:#if not bot, then player make a move
        print("move to? (left number then upper number. Example : 4 2) :", end=" ")
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
        this_turn.position[pawn] = [x, y]  # updating the new pos in player's pawn list

    elif command == "attack":
        if (special_move("attack")): #checking if the attack is successful
            print("SUCCESSFUL ATTACK!!!")
            if (special_move("defend")): #if defend=True, then you lost your pawn
                print("sorry...but you lost your pawn.")
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0 #updating arena by deleting dead pawns
                defeated_pawn = arena.board[x][y]
                opponent.position.pop(defeated_pawn)
                this_turn.position.pop(pawn)
                arena.board[x][y] = 0
            else: #if defend failed, then enemy die
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0
                #updating arena by deleting dead pawns and moving current pawn
                defeated_pawn = arena.board[x][y]
                opponent.position.pop(defeated_pawn)
                arena.board[x][y] = pawn
                this_turn.position[pawn] = [x, y]  # updating the new pos in player's pawn list

        elif (special_move("defend")): #failed attack, but successful defense
            print("Too bad,you lost your pawn")
            arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = 0
            this_turn.position.pop(pawn)
        else:
            print("Too bad. Nothing happens")

def validate_move(move_pos, current_pos):
    # this is too long but here's a summary
    # if you are a ninja, you can move 2 blocks away from your position. if you are not a ninja, then only 1 block.
    # if you stumble upon an enemy, then it will automatically detected as an attack
    # you also cant move to a block that is occupied by a friendly pawn
    global current_turn
    this_turn=globals()[current_turn]
    if this_turn.job=="Ninja":
        move_limit=2
    else:
        move_limit=1
    if (abs(move_pos[0] - current_pos[0]) > move_limit) or (abs(move_pos[1] - current_pos[1]) > move_limit) or move_pos[0] < 0 or \
            move_pos[1] < 0 or move_pos[0] > arena.height-1 or move_pos[1] > arena.width-1: #if movement exceed the move_limit or the arena size, then it will return a false value
        k = [False, "none"]
        return (k)
    else:
        if (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (
                arena.board[(move_pos[0])][(move_pos[1])][0] != this_turn.symbol): #if there is an enemy, then attack
            k = [True, "attack"]
            return (k)
        elif (arena.board[(move_pos[0])][(move_pos[1])] != 0) and (arena.board[(move_pos[0])][(move_pos[1])][0] == this_turn.symbol): #if there is your own ally in target location, then it will return a false value
            k = [False, "none"]
            return (k)
        else:
            k = [True, "move"] #if there is none, then move
            return (k)

def special_move(command):
    global current_turn
    this_turn = globals()[current_turn] #TAKING current_turn VARIABLE TO WORK WITH
    #rng shit
    if command == "attack":
        chance = round(random.random() * 100)  # chance percentage
        chance+= this_turn.chance_bonus(command)
        if chance>=100: chance=100 #MAXIMUM CHANCE VALUE IS 100
        elif chance<0: chance=0 #MINIMUM CHANCE VALUE IS 0
        roullete = [True for i in range(chance)]  # roullete of true and false. It will be filled with True for "chance" times
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick

    elif command == "defend":
        chance = round(random.random() * 100)  # chance percentage
        if this_turn.job=="Gladiator":
            chance=0
        else:
            chance += this_turn.chance_bonus(command)
        if chance >= 100: chance = 100
        elif chance<0:chance=0
        roullete = [True for i in range(chance)]  # roullete of true and false
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick


# MAIN PROGRAM
#BASIC SETUP
arena = Arena(10, 6)
y_default_pos= {"Y1": [9, 1], "Y2": [9, 2], "Y3": [9, 3], "Y4": [9, 4],"Y5": [8, 1],"Y6": [8, 2],"Y7": [8, 3],"Y8": [8, 4],"Y9": [7, 2],"Y10": [7, 3],"Y11": [6, 2],"Y12": [6, 3]}
x_default_pos={"X1": [0, 1], "X2": [0, 2], "X3": [0, 3], "X4": [0, 4],"X5": [1, 1],"X6": [1, 2],"X7": [1, 3],"X8": [1, 4],"X9": [2, 2],"X10": [2, 3],"X11": [3, 2],"X12": [3, 3]}
#MAIN MENU
print("Wants to play againts 1)Other player, or 2)bot?")
c=int(input())
if c==2:
    #BOT SETUP
    bot=True
    print("Select difficulty: 1)Easy, or 2)Normal?")
    c=int(input())
    if c==1: difficulty="Easy"
    else: difficulty="Normal"
else:
    bot=False #IF PLAYER DOESNT PLAY AGAINTS BOT, THEN THE VALUE WILL BE FALSE
print("1)custom job, or 2)default?")
c = int(input())
if c == 1:
    #IF AGAINTS OTHER HUMAN PLAYER, THEN THIS IS CUSTOM JOB CHOICE
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
    #IF ITS AGAINTS BOT, THEN THE CHOICE WILL BE RANDOM
    else:
        c=random.randint(1,3) #RANDOM GENERATOR BETWEEN 1-3
    if c == 1:
        print("Player Y chooses Gladiator!")
        player2 = Player("Y", y_default_pos, "Gladiator",bot)
    elif c == 2:
        print("Player Y chooses Guardian!")
        player2 = Player("Y", y_default_pos, "Guardian",bot)
    else:
        print("Player Y chooses Ninja!")
        player2 = Player("Y", y_default_pos, "Ninja",bot)

else:#DEFAULT JOB
    player1 = Player("X", x_default_pos, "Gladiator")
    player2 = Player("Y", y_default_pos, "Gladiator",bot)

#SETTING UP THE GAME
arena.create_arena()
current_turn = "player1"

while (True): #GAME STARTS
    if current_turn == "player1":
        os.system("cls")
        print("=====================PLAYER 1 TURN========================")
        move_pawn(player1.symbol) #MOVING PAWN BY CALLING move_pawn FUNCTION
        arena.create_arena() #CREATING ARENA AGAIN
        current_turn = "player2" #SWITCHING TURN

    elif current_turn == "player2":
        print("=====================PLAYER 2 TURN========================")
        move_pawn(player2.symbol)
        arena.create_arena()
        current_turn = "player1"
