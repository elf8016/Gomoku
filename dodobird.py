import variable


def save_position(str1, str2):
    variable.track.append([])
    i = len(variable.track) - 1
    if (i % 2) == 0:  # player1
        variable.chessboard[int(str1)][int(str2)] = 1
        variable.track[i].append(str1)
        variable.track[i].append(str2)
    elif (i % 2) == 1:  # player2
        variable.chessboard[int(str1)][int(str2)] = 2
        variable.track[i].append(str1)
        variable.track[i].append(str2)


def checkinput(list1: list):
    if len(list1) != 2:
        print("Wrong input type!", end=" ")
        return False
    elif (str.isdigit(list1[0]) == False) or (str.isdigit(list1[1]) == False):
        print("Wrong input type!", end=" ")
        return False
    elif int(list1[0]) > 10 or int(list1[1]) > 10:
        print("Out of range!!", end=" ")
        return False
    elif variable.chessboard[int(list1[0])][int(list1[1])] != 0:
        print("This place already has a chess!", end=" ")
        return False
    else:
        return True


# 2nd version
