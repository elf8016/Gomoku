import variable
import interactive


def checkwin (ll,point):
    y = 0
    x = 0
    player = 0
    times = 1
    center = [0,0]
    y = int(point[0])
    x = int(point[1])
    center[0] = y
    center[1] = x
    player = ll[y][x]

    # 右
    for i in range(1,5):
        x = x + 1
        if x < 11 and ll[y][x] == player:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    #左
    for i in range(1,5):

        x = x - 1
        if x >= 0 and ll[y][x] == player:
            times += 1
            center[0] = y       #!!讓center保持在最左邊    
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最左邊
        center[1] = center[1] + 2
        return(player,2,center)
    else:
    #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        center[0] = y
        center[1] = x
        times = 1

    #上
    for i in range(1,5):
        y = y - 1
        if y >= 0 and ll[y][x] == player:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    # 下
    for i in range(1,5):
        y = y + 1
        if y < 11 and ll[y][x] == player:
            times += 1
            center[0] = y        #!!讓center保持在最下邊
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最下邊
        center[0] = center[0] - 2
        return(player,1,center)
    else:
        #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        center[0] = y
        center[1] = x
        times = 1
    
    #右上
    for i in range(1,5):
        x = x + 1
        y = y - 1
        if x < 11 and y >= 0 and ll[y][x] == player:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    #左下
    for i in range(1,5):
        x = x - 1
        y = y + 1
        if x >= 0 and y <= 11 and ll[y][x] == player :
            times += 1
            center[0] = y       #!!讓center保持在最左下邊
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最左下邊
        center[0] = center[0] - 2
        center[1] = center[1] + 2
        return(player,4,center)
    else:
        #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = int(point[0])
        x = int(point[1])
        center[0] = y
        center[1] = x
        times = 1
    
    #右下
    for i in range(1,5):
        x = x + 1
        y = y + 1
        if x < 11 and y < 11 and ll[y][x] == player:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = int(point[0])
    x = int(point[1])

    #左上
    for i in range(1,5):
        x = x - 1
        y = y - 1
        if x >= 0 and y >= 0 and ll[y][x] == player:
            times += 1
            center[0] = y         #!!讓center保持在最左上邊
            center[1] = x
        else:
            break
    if times == 5:
        #!!center在最左上邊
        center[0] = center[0] + 2
        center[1] = center[1] + 2
        return(player,3,center)
    else:
        center[0] = y
        center[1] = x
        return(0,0,center)
    
