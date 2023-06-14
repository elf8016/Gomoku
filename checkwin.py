import variable
import interactive
import variable


def checkwin(point):
    y = 0
    x = 0
    player = 0
    times = 1
    y = int(point[0])
    x = int(point[1])
    player = variable.chessboard[y][x]

    # 右
    for i in range(1, 5):
        x = x + 1
        if x < 11 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    # 讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    # 左
    for i in range(1, 5):
        x = x - 1
        if x >= 0 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    if times == 5:
        return 2
    else:
        # 讓 x,y ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        times = 1

    # 上
    for i in range(1, 5):
        y = y - 1
        if y >= 0 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    # 讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    # 下
    for i in range(1, 5):
        y = y + 1
        if y < 11 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    if times == 5:
        return 1
    else:
        # 讓 x,y ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        times = 1

    # 右上
    for i in range(1, 5):
        x = x + 1
        y = y - 1
        if x < 11 and y >= 0 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    # 讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    # 左下
    for i in range(1, 5):
        x = x - 1
        y = y + 1
        if x >= 0 and y < 11 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    if times == 5:
        return 4
    else:
        # 讓 x,y ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        times = 1

    # 右下
    for i in range(1, 5):
        x = x + 1
        y = y + 1
        if x < 11 and y < 11 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break

    # 讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    # 左上
    for i in range(1, 5):
        x = x - 1
        y = y - 1
        if x >= 0 and y >= 0 and variable.chessboard[y][x] == player:
            times += 1
        else:
            break
    if times == 5:
        return 3
    else:
        return 0

    ##if __name__ == "__main__":
    interactive.init()
    variable.chessboard1 = variable.chessboard
    # checkwin(variable.chessboard1,variable.chessboard2)
    # print (variable.chessboard1)
    print(variable.chessboard1)
    print(variable.chessboard1)
    # print(interactive.show(variable.chessboard1))
