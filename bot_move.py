import random

def bot_pawn(board,height,width,player_location,enemy_location,difficulty):
    #DATA GATHERING
    pawn_list = []
    player=[]
    for i in player_location.keys():
        pawn_list.append(i)
    for i in player_location.values():
        player.append(i)
    #MOVEMENT
    if difficulty=="Easy":
        while True:
            pawn = random.choice(pawn_list)
            pawn_position = player_location[pawn]
            if pawn_position[0] + 1 < height or pawn_position[0] - 1 >= 0 or pawn_position[
                1] + 1 < width or pawn_position - 1 >= 0:
                if pawn_position[0] + 1 < height and pawn_position[0] - 1 >= 0 and pawn_position[1] + 1 < width and \
                        pawn_position[1] - 1 >= 0:
                    if board[(pawn_position[0] + 1)][(pawn_position[1])] != 0 and board[(pawn_position[0] - 1)][
                        (pawn_position[1])] != 0 and board[(pawn_position[0] + 1)][(pawn_position[1] + 1)] != 0 and \
                            board[(pawn_position[0])][(pawn_position[1] + 1)] != 0 and board[(pawn_position[0])][
                        (pawn_position[1] - 1)] != 0 and board[(pawn_position[0] - 1)][(pawn_position[1] - 1)] != 0:
                        if board[(pawn_position[0] + 1)][(pawn_position[1])][0] != "Y" or \
                                board[(pawn_position[0] - 1)][(pawn_position[1])][0] != "Y" or \
                                board[(pawn_position[0] + 1)][(pawn_position[1] + 1)][0] != "Y" or \
                                board[(pawn_position[0])][(pawn_position[1] + 1)][0] != "Y" or \
                                board[(pawn_position[0])][(pawn_position[1] - 1)][0] != "Y" or \
                                board[(pawn_position[0] - 1)][(pawn_position[1] - 1)][0] != "Y":
                            return (pawn)
                            break
                    elif board[(pawn_position[0] + 1)][(pawn_position[1])] == 0 or board[(pawn_position[0] - 1)][
                        (pawn_position[1])] == 0 or board[(pawn_position[0] + 1)][(pawn_position[1] + 1)] == 0 or \
                            board[(pawn_position[0])][(pawn_position[1] + 1)] == 0 or board[(pawn_position[0])][
                        (pawn_position[1] - 1)] == 0 or board[(pawn_position[0] - 1)][(pawn_position[1] - 1)] == 0:
                        return (pawn)
                        break
                else:
                    if pawn_position == [0, width]:
                        if board[(pawn_position[0]) + 1][(pawn_position[1])] != 0:
                            if board[(pawn_position[0]) + 1][(pawn_position[1])][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0]) + 1][(pawn_position[1])] == 0:
                            return (pawn)
                            break
                        elif board[(pawn_position[0])][(pawn_position[1]) - 1] != 0:
                            if board[(pawn_position[0])][(pawn_position[1]) - 1][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0])][(pawn_position[1]) - 1] == 0:
                            return (pawn)
                            break
                    elif pawn_position == [height, 0]:
                        if board[(pawn_position[0]) - 1][(pawn_position[1])] != 0:
                            if board[(pawn_position[0]) - 1][(pawn_position[1])][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0]) - 1][(pawn_position[1])] == 0:
                            return (pawn)
                            break
                        elif board[(pawn_position[0])][(pawn_position[1]) + 1] != 0:
                            if board[(pawn_position[0])][(pawn_position[1]) + 1][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0])][(pawn_position[1]) + 1] == 0:
                            return (pawn)
                            break
                    elif pawn_position == [height, width]:
                        if board[(pawn_position[0]) - 1][(pawn_position[1])] != 0:
                            if board[(pawn_position[0]) - 1][(pawn_position[1])][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0]) - 1][(pawn_position[1])] == 0:
                            return (pawn)
                            break
                        elif board[(pawn_position[0])][(pawn_position[1]) - 1] != 0:
                            if board[(pawn_position[0])][(pawn_position[1]) + 1][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0])][(pawn_position[1]) - 1] == 0:
                            return (pawn)
                            break
                    elif pawn_position == [0, 0]:
                        if board[(pawn_position[0]) + 1][(pawn_position[1])] != 0:
                            if board[(pawn_position[0]) + 1][(pawn_position[1])][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0]) + 1][(pawn_position[1])] == 0:
                            return (pawn)
                            break
                        elif board[(pawn_position[0])][(pawn_position[1]) + 1] != 0:
                            if board[(pawn_position[0])][(pawn_position[1]) + 1][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0])][(pawn_position[1]) + 1] == 0:
                            return (pawn)
                            break
    elif difficulty=="Normal" or difficulty=="Unfair":
        #GATHERING ENEMY LOCATION
        enemy=[]
        for i in enemy_location.values():
            enemy.append(i)
        #ANALYZE
        iteration=0
        flag=False
        for i in player:
            for j in enemy:
                if (abs(i[0]-j[0])==1 and i[1]-j[1]==0) or (abs(i[1]-j[1])==1 and i[0]-j[0]==0) or (abs(i[1]-j[1])==1 and abs(i[0]-j[0])==1):
                    pawn=pawn_list[iteration]
                    flag=True
                    return pawn
            iteration+=1
        if not flag:
            while True:
                pawn = random.choice(pawn_list)
                pawn_position = player_location[pawn]
                if pawn_position[0] + 1 < height or pawn_position[0] - 1 >= 0 or pawn_position[1] + 1 < width or pawn_position - 1 >= 0:
                    if pawn_position[0] + 1 < height and pawn_position[0] - 1 >= 0 and pawn_position[1] + 1 < width and pawn_position[1] - 1 >= 0:
                        if board[(pawn_position[0] + 1)][(pawn_position[1])] != 0 and board[(pawn_position[0] - 1)][
                            (pawn_position[1])] != 0 and board[(pawn_position[0] + 1)][(pawn_position[1] + 1)] != 0 and \
                                board[(pawn_position[0])][(pawn_position[1] + 1)] != 0 and board[(pawn_position[0])][
                            (pawn_position[1] - 1)] != 0 and board[(pawn_position[0] - 1)][(pawn_position[1] - 1)] != 0:
                            if board[(pawn_position[0] + 1)][(pawn_position[1])][0] != "Y" or \
                                    board[(pawn_position[0] - 1)][(pawn_position[1])][0] != "Y" or \
                                    board[(pawn_position[0] + 1)][(pawn_position[1] + 1)][0] != "Y" or \
                                    board[(pawn_position[0])][(pawn_position[1] + 1)][0] != "Y" or \
                                    board[(pawn_position[0])][(pawn_position[1] - 1)][0] != "Y" or \
                                    board[(pawn_position[0] - 1)][(pawn_position[1] - 1)][0] != "Y":
                                return (pawn)
                                break
                        elif board[(pawn_position[0] + 1)][(pawn_position[1])] == 0 or board[(pawn_position[0] - 1)][
                            (pawn_position[1])] == 0 or board[(pawn_position[0] + 1)][(pawn_position[1] + 1)] == 0 or \
                                board[(pawn_position[0])][(pawn_position[1] + 1)] == 0 or board[(pawn_position[0])][
                            (pawn_position[1] - 1)] == 0 or board[(pawn_position[0] - 1)][(pawn_position[1] - 1)] == 0:
                            return (pawn)
                            break
                    else:
                        if pawn_position==[0,width]:
                            if board[(pawn_position[0])+1][(pawn_position[1])]!=0:
                                if board[(pawn_position[0]) + 1][(pawn_position[1])][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])+1][(pawn_position[1])]==0:
                                return (pawn)
                                break
                            elif board[(pawn_position[0])][(pawn_position[1])-1]!=0:
                                if board[(pawn_position[0])][(pawn_position[1])-1][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])][(pawn_position[1])-1]==0:
                                return (pawn)
                                break
                        elif pawn_position==[height,0]:
                            if board[(pawn_position[0])-1][(pawn_position[1])]!=0:
                                if board[(pawn_position[0]) - 1][(pawn_position[1])][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])-1][(pawn_position[1])]==0:
                                return (pawn)
                                break
                            elif board[(pawn_position[0])][(pawn_position[1])+1]!=0:
                                if board[(pawn_position[0])][(pawn_position[1])+1][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])][(pawn_position[1])+1]==0:
                                return (pawn)
                                break
                        elif pawn_position==[height,width]:
                            if board[(pawn_position[0])-1][(pawn_position[1])]!=0:
                                if board[(pawn_position[0]) - 1][(pawn_position[1])][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])-1][(pawn_position[1])]==0:
                                return (pawn)
                                break
                            elif board[(pawn_position[0])][(pawn_position[1])-1]!=0:
                                if board[(pawn_position[0])][(pawn_position[1])+1][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])][(pawn_position[1])-1]==0:
                                return (pawn)
                                break
                        elif pawn_position==[0,0]:
                            if board[(pawn_position[0])+1][(pawn_position[1])]!=0:
                                if board[(pawn_position[0]) + 1][(pawn_position[1])][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])+1][(pawn_position[1])]==0:
                                return (pawn)
                                break
                            elif board[(pawn_position[0])][(pawn_position[1])+1]!=0:
                                if board[(pawn_position[0])][(pawn_position[1])+1][0] != "Y":
                                    return (pawn)
                                    break
                            elif board[(pawn_position[0])][(pawn_position[1])+1]==0:
                                return (pawn)
                                break
def bot_move(pawn,board,player_location,enemy_location,difficulty):
    # GATHERING ENEMY LOCATION
    pawn_list = []
    for i in player_location.keys():
        pawn_list.append(i)
    enemy_list=[]
    for i in enemy_location.keys():
        enemy_list.append(i)
    if difficulty=="Easy":
        x,y=player_location[pawn]
        x += random.randint(-2, 2)
        y += random.randint(-2, 2)
        return [x,y]
    elif difficulty=="Normal" or difficulty=="Unfair":
        enemy = []
        for i in enemy_location.values():
            enemy.append(i)
        # ANALYZE
        pawn_location=player_location[pawn]
        iteration=0
        flag=False
        for i in enemy:
            if (abs(i[0]-pawn_location[0])==1 and i[1]-pawn_location[1]==0) or (abs(i[1]-pawn_location[1])==1 and i[0]-pawn_location[0]==0) or (abs(i[1]-pawn_location[1])==1 and abs(i[0]-pawn_location[0])==1):
                target=enemy_list[iteration]
                target_location=enemy_location[target]
                flag=True
                return target_location
            iteration+=1
        if not flag:
            x, y = pawn_location
            x += random.randint(-2, 2)
            y += random.randint(-2, 2)
            return [x, y]
