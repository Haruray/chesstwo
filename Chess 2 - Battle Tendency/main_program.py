import random
from bot_move import bot_pawn
from bot_move import bot_move
from bot_move import move_select

class Arena():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[" " for i in range(width)] for i in range(height)]
    def update_arena(self):
        for i in player1.pawn:
            self.board[(player1.pawn[i].position[0])][(player1.pawn[i].position[1])] = i
        for i in player2.pawn:
            self.board[(player2.pawn[i].position[0])][(player2.pawn[i].position[1])] = i
    def create_arena(self): #JUST PRINTING THE ARENA. DONT MIND THIS
        self.update_arena()
        print("  ", end=" ")
        for i in range(self.width):
            print(i, end="    ")
        i = 0
        print()
        for square in self.board:
            print(i, end="|")
            for pawn in square:
                if pawn == " ":
                    print(pawn, end="   |")
                else:
                    try:
                        test=pawn[3]
                        print(pawn, end="|")
                    except:
                        try:
                            test = pawn[1]
                            print(pawn,end=" |")
                        except:
                            print(pawn, end="  |")
            print()
            i += 1
class Player():
    def __init__(self,pawn,bot=False):
        self.pawn=pawn
        self.bot=bot
        self.bot_bonus=20

class Gladiator():
    def __init__(self, symbol,position):
        self.symbol=symbol
        self.move_limit=1
        self.survive=0
        self.turn_bonus=0
        self.counter=True
        self.position=position
    def chance_bonus(self,command):
        if command=="attack":
            return 30
        else:
            return 10
    def berserk(self):
        if self.turn_bonus!=0:
            return True
class Defender(Gladiator):
    def __init__(self,symbol,position):
        Gladiator.__init__(self,symbol,position)
        self.survive=10
    def chance_bonus(self,command):
        if command=="attack":
            return -10
        else:
            return 20
    def guard(self):
        if self.turn_bonus*10 >=50:
            return 50
        else:
            return self.turn_bonus*10

class Ninja(Gladiator):
    def __init__(self,symbol,position):
        Gladiator.__init__(self, symbol,position)
        self.move_limit=2
        self.counter=False
    def chance_bonus(self,command):
        if command=="attack":
            return 10
        else:
            return -20

def news():
    flag=False
    for i in player1.pawn:
        if player1.pawn[i].turn_bonus!=0:
            if not flag:
                print("<<Player 1 Info!>>")
            flag=True
            if player1.pawn[i].symbol[1]=="G":
                print(player1.pawn[i].symbol,"is in berserk!")
            elif player1.pawn[i].symbol[1]=="D":
                print(player1.pawn[i].symbol,"is holding ground for",player1.pawn[i].turn_bonus,"turn(s)!")
    flag=False
    for i in player2.pawn:
        if player2.pawn[i].turn_bonus!=0:
            if not flag:
                print("<<Player 2 Info!>>")
            flag=True
            if player2.pawn[i].symbol[1]=="G":
                print(player2.pawn[i].symbol,"is in berserk!")
            elif player2.pawn[i].symbol[1]=="D":
                print(player2.pawn[i].symbol,"is holding ground for",player2.pawn[i].turn_bonus,"turn(s)!")

def move_pawn():
    global current_turn, bot, difficulty
    this_turn = globals()[current_turn]  # USING "current_turn" AS A VARIABLE TO WORK WITH
    if current_turn == "player1":
        opponent = globals()["player2"]
    else:
        opponent = globals()["player1"]
    # PAWN CHOOSING
    # IF BOT THEN DO THIS
    if this_turn.bot == True:  # BOT MOVEMENT
        select=bot_pawn(arena.board,arena.height,arena.width,this_turn.pawn,opponent.pawn,difficulty)#PAWN CHOOSING FROM MODULE
        pawn=select[0]
    else:
        # IF ITS PLAYER, THEN MANUAL CHOOSING. INPUT WILL BE VALIDATED
        while (True):
            pawn = input("What pawn to move : ")  # PLAYER MOVEMENT. UNTIL INPUT IS VALID
            if this_turn.pawn.get(pawn):  # IF THE PAWN EXISTS, THEN INPUT IS VALID
                break
            else:  # IF NOT VALID, THEN NO
                print("wrong pawn. Do it again")
    current_pawn_pos = this_turn.pawn[pawn].position  # TAKING CURRENT PAWN POSITION
    # MOVEMENT TIME. IF CURRENT TURN IS BOT, THEN DO THIS
    while True:
        try:
            if this_turn.bot:
                c=move_select(this_turn.pawn,pawn,difficulty,select[1])
            else:
                c = int(input("Do you want to 1)Move, or 2)Hold Ground?: "))
            if c==1 or c==2:
                break
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    if c==1:
        if this_turn.bot:
            x, y = bot_move(pawn, arena.board, player2.pawn, player1.pawn,difficulty)  # MOVING USING bot_move MODULE
            validate = validate_move([x, y], this_turn.pawn[pawn])  # RETURNING 2 VALUE. THE FIRST ONE IS BOOLEAN, THE OTHER ONE IS COMMAND (ATTACK OR MOVE)
            while not (validate[0]):  # validate movement
                x, y = bot_move(pawn, arena.board, player2.pawn, player1.pawn,difficulty)
                validate=validate_move([x, y], this_turn.pawn[pawn])
            command = validate[1]
        else:  # if not bot, then player make a move
            print("move to? (left number then upper number. Example : 4 2) :", end=" ")
            while True:
                try:
                    x, y = map(int, input().split())  # movement
                    validate = validate_move([x, y], this_turn.pawn[pawn])
                    while not (validate[0]):  # validate movement
                        print("cant move there. Do it again")
                        x, y = map(int, input().split())
                        validate = validate_move([x, y], current_pawn_pos)
                    break
                except:
                    print("Input invalid. Try again")
            command = validate[1]

        if command == "move":
            arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = " "  # erasing pawn in previous pos
            arena.board[x][y] = pawn  # updating the new pos in arena
            this_turn.pawn[pawn].position = [x, y]  # updating the new pos in player's pawn list

        elif command == "attack":
            target_pawn = opponent.pawn[arena.board[x][y]]
            ally_pawn = this_turn.pawn[pawn]
            if (special_move("attack",ally_pawn,target_pawn)):  # checking if the attack is successful
                print("SUCCESSFUL ATTACK!!!")
                if (special_move("defend",ally_pawn,target_pawn)) and ally_pawn.counter:  # if defend=True, then you lost your pawn
                    print("sorry...but you lost your pawn.")
                    arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = " "  # updating arena by deleting dead pawns
                    defeated_pawn = arena.board[x][y]
                    opponent.pawn.pop(defeated_pawn)
                    this_turn.pawn.pop(pawn)
                    arena.board[x][y] = " "
                else:  # if defend failed, then enemy die
                    if ally_pawn.symbol[1] == "G":
                        ally_pawn.turn_bonus += 3
                    arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = " "
                    # updating arena by deleting dead pawns and moving current pawn
                    defeated_pawn = arena.board[x][y]
                    opponent.pawn.pop(defeated_pawn)
                    arena.board[x][y] = pawn
                    this_turn.pawn[pawn].position = [x, y]  # updating the new pos in player's pawn list

            elif (special_move("defend",ally_pawn,target_pawn)) and ally_pawn.counter:  # failed attack, but successful defense
                print("Too bad,you lost your pawn")
                if target_pawn.symbol[1]=="G":
                    target_pawn.turn_bonus+=3
                elif target_pawn.symbol[1] == "D":
                    target_pawn.turn_bonus = 0
                arena.board[(current_pawn_pos[0])][(current_pawn_pos[1])] = " "
                this_turn.pawn.pop(pawn)
            else:
                print("Too bad. Nothing happens")
                if target_pawn.symbol[1] == "D":
                    target_pawn.turn_bonus = 0

        check=this_turn.pawn.get(pawn)
        if check:
            if this_turn.pawn[pawn].symbol[1] == "D":
                this_turn.pawn[pawn].turn_bonus = 0
    else:
        print("You chooses to Hold Ground")
        if this_turn.pawn[pawn].symbol[1]=="D":
            this_turn.pawn[pawn].turn_bonus+=1
    decrease_gladiator_berserk()

def decrease_gladiator_berserk():
    for i in player1.pawn:
        if player1.pawn[i].symbol[1]=="G":
            if player1.pawn[i].turn_bonus!=0:
                player1.pawn[i].turn_bonus-=1
    for i in player2.pawn:
        if player2.pawn[i].symbol[1]=="G":
            if player2.pawn[i].turn_bonus!=0:
                player2.pawn[i].turn_bonus-=1

def validate_move(move_pos, this_pawn):
    # this is too long but here's a summary
    # if you are a ninja, you can move 2 blocks away from your position. if you are not a ninja, then only 1 block.
    # if you stumble upon an enemy, then it will automatically detected as an attack
    # you also cant move to a block that is occupied by a friendly pawn
    move_limit = this_pawn.move_limit
    current_pos = this_pawn.position
    if (abs(move_pos[0] - current_pos[0]) > move_limit) or (abs(move_pos[1] - current_pos[1]) > move_limit) or move_pos[0] < 0 or \
            move_pos[1] < 0 or move_pos[0] > arena.height - 1 or move_pos[1] > arena.width - 1:  # if movement exceed the move_limit or the arena size, then it will return a false value
        k = [False, "none"]
        return (k)
    else:
        if (arena.board[(move_pos[0])][(move_pos[1])] != " ") and (arena.board[(move_pos[0])][(move_pos[1])][0] != this_pawn.symbol[0]):  # if there is an enemy, then attack
            k = [True, "attack"]
            return (k)
        elif (arena.board[(move_pos[0])][(move_pos[1])] != " ") and (arena.board[(move_pos[0])][(move_pos[1])][0] == this_pawn.symbol[0]):  # if there is your own ally in target location, then it will return a false value
            k = [False, "none"]
            return (k)
        else:
            k = [True, "move"]  # if there is none, then move
            return (k)
def special_move(command,ally_pawn,target_pawn):
    #rng shit
    if command == "attack":
        chance = round(random.random() * 100)  # chance percentage
        chance+= ally_pawn.chance_bonus(command) - target_pawn.survive
        if target_pawn.symbol[1]=="D":
            chance-=target_pawn.guard()
        if ally_pawn.symbol[1]=="G":
            if ally_pawn.berserk():
                chance=100
        #if difficulty == "Unfair" and this_turn.bot==True: chance+=this_turn.bot_bonus
        if chance>=100: chance=100 #MAXIMUM CHANCE VALUE IS 100
        elif chance<0: chance=0 #MINIMUM CHANCE VALUE IS 0
        roullete = [True for i in range(chance)]  # roullete of true and false. It will be filled with True for "chance" times
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick

    elif command == "defend":
        chance = round(random.random() * 100)  # chance percentage
        chance += target_pawn.chance_bonus(command)
        if target_pawn.symbol[1]=="D":
            chance += target_pawn.guard()
        if target_pawn.symbol[1]=="G":
            if target_pawn.berserk():
                chance=100
        #if difficulty == "Unfair" and opponent.bot==True: chance += opponent.bot_bonus
        if chance >= 100: chance = 100
        elif chance<0:chance=0
        roullete = [True for i in range(chance)]  # roullete of true and false
        for i in range((100 - chance)):
            roullete.append(False)
        return (random.choice(roullete))  # random pick

#===============MAIN MENU================
print("Wants to play againts 1)Other player, or 2)bot?")
c=int(input())
if c==2:
    #BOT SETUP
    bot=True
    print("Select difficulty: 1)Easy, or 2)Normal?")
    c=int(input())
    if c==1: difficulty="Easy"
    elif c==2: difficulty="Normal"
else:
    bot=False #IF PLAYER DOESNT PLAY AGAINTS BOT, THEN THE VALUE WILL BE FALSE

print("Each player maximum pawn is 10.")
#PLAYER SETUP
for player in [1,2]:
    print("========================PLAYER " + str(player) + "========================")
    limit=10
    g,d,n=[0,0,0]
    while limit!=0:
        if player==2 and bot:
            g=random.randint(3,6)
        else:
            print("How many Gladiators do you want? (limit left:",limit,"): ",end="")
            g=int(input())
        limit-=g
        if limit<0:
            print("Limit exceeded. Try again.")
            limit = 10
        elif limit==0:
            print("Limit reached")
            break
        else:
            if player == 2 and bot:
                d=random.randint(3,4)
            else:
                print("How many Defenders do you want? (limit left:", limit, "): ",end="")
                d=int(input())
            limit-=d
            if limit < 0:
                print("Limit exceeded. Try again.")
                limit = 10
            elif limit == 0:
                print("Limit reached")
                break
            else:
                if player == 2 and bot:
                    n = limit
                else:
                    print("How many Ninjas do you want? (limit left:", limit, "): ",end="")
                    n= int(input())
                limit-=n
                if limit<0:
                    print("Limit exceeded. Try again.")
                    limit=10
                elif limit>0:
                    print("Limit not reached. Try again.")
                    limit=10
                elif limit == 0:
                    print("Limit reached")
    p_pawn_list={}
    arena=Arena(8,6)
    pos_list=[[i for i in range(arena.width)] for i in range(2)]
    for i in range(1,g+1):
        if i<=arena.width:
            choice = random.choice(pos_list[0])
            pos_list[0].pop(pos_list[0].index(choice))
            if player==1:
                p_pawn_list["1G"+str(i)]=Gladiator("1G"+str(i),[arena.height-2,choice])
            elif player==2:
                p_pawn_list["2G" + str(i)] = Gladiator("2G" + str(i), [1, choice])
        else:
            choice = random.choice(pos_list[1])
            pos_list[1].pop(pos_list[1].index(choice))
            if player==1:
                p_pawn_list["1G"+str(i)]=Gladiator("1G"+str(i),[arena.height-1,choice])
            elif player==2:
                p_pawn_list["2G" + str(i)] = Gladiator("2G" + str(i), [0, choice])

    for i in range(1,d+1):
        if g+i<=arena.width:
            choice = random.choice(pos_list[0])
            pos_list[0].pop(pos_list[0].index(choice))
            if player==1:
                p_pawn_list["1D"+str(i)]=Defender("1D"+str(i),[arena.height-2,choice])
            elif player==2:
                p_pawn_list["2D"+str(i)]=Defender("2D"+str(i),[1,choice])
        else:
            choice = random.choice(pos_list[1])
            pos_list[1].pop(pos_list[1].index(choice))
            if player==1:
                p_pawn_list["1D"+str(i)]=Defender("1D"+str(i),[arena.height-1,choice])
            elif player==2:
                p_pawn_list["2D"+str(i)]=Defender("2D"+str(i),[0,choice])

    for i in range(1,n+1):
        if g+d+i <= arena.width:
            choice = random.choice(pos_list[0])
            pos_list[0].pop(pos_list[0].index(choice))
            if player==1:
                p_pawn_list["1N" + str(i)] = Ninja("1N" + str(i), [arena.height - 2, choice])
            elif player==2:
                p_pawn_list["2N" + str(i)] = Ninja("2N" + str(i), [1, choice])
        else:
            choice = random.choice(pos_list[1])
            pos_list[1].pop(pos_list[1].index(choice))
            if player == 1:
                p_pawn_list["1N" + str(i)] = Ninja("1N" + str(i), [arena.height - 1, choice])
            elif player == 2:
                p_pawn_list["2N" + str(i)] = Ninja("2N" + str(i), [0, choice])

    if player==1:
        player1=Player(p_pawn_list)
    else:
        player2 = Player(p_pawn_list,bot)

#MAIN GAME
arena.create_arena()
current_turn = "player1"
while (True): #GAME STARTS
    if current_turn == "player1":
        print("========================PLAYER 1 TURN========================")
        news()
        move_pawn() #MOVING PAWN BY CALLING move_pawn FUNCTION
        arena.create_arena() #CREATING ARENA AGAIN
        #WINNING CHECK
        if len(player1.pawn)==0:
            print("PLAYER 2 WINS!!!")
            break
        elif len(player2.pawn)==0:
            print("PLAYER 1 WINS!!!")
            break
        else:
            current_turn = "player2" #SWITCHING TURN

    elif current_turn == "player2":
        print("========================PLAYER 2 TURN========================")
        news()
        move_pawn()
        arena.create_arena()
        if len(player1.pawn)==0:
            print("PLAYER 2 WINS!!!")
            break
        elif len(player2.pawn)==0:
            print("PLAYER 1 WINS!!!")
            break
        else:
            current_turn = "player1"