import variable
from typing import List
import os
import screen_change

outside_row = "\x1b[47;37m      —————————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————                            \x1b[0m"
outside_column = "\x1b[47;37m    \x1b[0m"
space = "\x1b[40;30m         │                                            │                                           │                                           │                                           │                                           │                                           │                                           │                                           │                                           │                                           ▕          \x1b[0m"
row = "\x1b[40;37m             ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————     ———————————————————————————————————————             \x1b[0m"
column = "\x1b[40;37m         │                                            │                                           │                                           │                                           │                                           │                                           │                                           │                                           │                                           │                                           ▕          \x1b[0m"
row_dirt = {
    0: 2,
    1: 20,
    2: 38,
    3: 56,
    4: 74,
    5: 92,
    6: 110,
    7: 128,
    8: 146,
    9: 164,
    10: 181,
}
col_dirt = {
    0: 1,
    1: 46,
    2: 90,
    3: 134,
    4: 178,
    5: 222,
    6: 266,
    7: 310,
    8: 354,
    9: 398,
    10: 442,
}
type1_row_dirt = {
    0: 14,
    1: 59,
    2: 103,
    3: 147,
    4: 191,
    5: 235,
    6: 279,
    7: 323,
    8: 367,
    9: 411,
    10: 455,
}
type1_col_dirt = {3: 44, 4: 62, 5: 80, 6: 98, 7: 116, 8: 134, 9: 152}
type2_row_dirt = {3: 104, 4: 149, 5: 193, 6: 237, 7: 281, 8: 325, 9: 369}
type2_col_dirt = {
    0: 7,
    1: 25,
    2: 43,
    3: 61,
    4: 79,
    5: 97,
    6: 115,
    7: 133,
    8: 151,
    9: 169,
    10: 187,
}
type3_row_dirt = {
    3: 44,
    4: 62,
    5: 80,
    6: 98,
    7: 116,
    8: 134,
    9: 152,
}
type3_col_dirt = {
    3: 102,
    4: 147,
    5: 191,
    6: 235,
    7: 279,
    8: 323,
    9: 367,
}


def print_at_position(text, row, column):
    command = f"printf '\\033[{row};{column}H{text}'"
    os.system(command)


def init():
    variable.chessboard = [[0 for i in range(0, 11)] for j in range(0, 11)]
    variable.track = []
    variable.count=0
    screen_change.screen_change()
    show_table()


def show_table():
    print("\x1bc")
    print(outside_row)
    print(outside_row)
    print(outside_column, space, outside_column)
    print(outside_column, space, outside_column)
    print(outside_column, space, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    for i in range(0, 17):
        print(outside_column, column, outside_column)
    print(outside_column, row, outside_column)
    print(outside_column, space, outside_column)
    print(outside_column, space, outside_column)
    print(outside_column, space, outside_column)
    print(outside_row)
    print(outside_row)


def show_player():
    if (variable.count % 2) == 0:
        print_player1()
        variable.count + 1

    elif (variable.count % 2) == 1:
        print_player2()
        variable.count + 1


def print_piece_red(type,row, col):
    color="\x1b[40;31m"
    if type==1:
        color="\x1b[05;40;31m"
    row = row_dirt[row]
    col = col_dirt[col]
    print_at_position(color+"■■■■■■■■■■■■■■\x1b[0m", row, col + 8)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 1, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 2, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 3, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 4, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 5, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 6, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 7, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 8, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 9, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 10, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■\x1b[0m", row + 11, col + 8)


def print_piece_blue(type,row, col):
    color="\x1b[40;34m"
    if type==1:
        color="\x1b[05;40;34m"
    row = row_dirt[row]
    col = col_dirt[col]
    print_at_position(color+"■■■■■■■■■■■■■■\x1b[0m", row, col + 8)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 1, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 2, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 3, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 4, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 5, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 6, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 7, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 8, col)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 9, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■■■■■■■■■■■\x1b[0m", row + 10, col + 3)
    print_at_position(color+"■■■■■■■■■■■■■■\x1b[0m", row + 11, col + 8)


def print_player2():
    print_at_position("\x1b[44;34m                  ■■■■■■\x1b[0m", 2, 502)
    for i in range(3, 20):
        print_at_position("\x1b[44;34m   \x1b[0m", i, 500)
    for i in range(3, 10):
        print_at_position("\x1b[44;34m   \x1b[0m", i, 525)
    print_at_position("\x1b[44;34m                    ■■■■■■\x1b[0m", 10, 500)
    for i in range(540,561):
        print_at_position("\x1b[44;34m   \x1b[0m", 2, i)
        print_at_position("\x1b[44;34m   \x1b[0m", 10, i)
        print_at_position("\x1b[44;34m   \x1b[0m", 19, i)
    for i in range(2, 10):
        print_at_position("\x1b[44;34m   \x1b[0m", i, 560)
    for i in range(10,20):    
        print_at_position("\x1b[44;34m   \x1b[0m", i, 540)
    for i in range(5, 8):
        print_at_position("\x1b[44;34m■■■■■■\x1b[0m", i, 570)
    for i in range(14, 17):
        print_at_position("\x1b[44;34m■■■■■■\x1b[0m", i, 570)


def print_player1():
    print_at_position("\x1b[41;31m                  ■■■■■■\x1b[0m", 2, 502)
    for i in range(3, 20):
        print_at_position("\x1b[41;31m   \x1b[0m", i, 500)
    for i in range(3, 10):
        print_at_position("\x1b[41;31m   \x1b[0m", i, 525)
    print_at_position("\x1b[41;31m                    ■■■■■■\x1b[0m", 10, 500)
    for i in range(2, 20):
        print_at_position("\x1b[41;31m   \x1b[0m", i, 550)
    for i in range(5, 8):
        print_at_position("\x1b[41;31m■■■■■■\x1b[0m", i, 570)
    for i in range(14, 17):
        print_at_position("\x1b[41;31m■■■■■■\x1b[0m", i, 570)


def print_winner(winner):
    red="\x1b[41;31m"
    blue="\x1b[44;34m"
    if winner==1:
        color=red
        for i in range(2, 20):
            print_at_position(color+"   \x1b[0m", i, 550)
    elif winner==2:
        color=blue
        for i in range(540,561):
            print_at_position(color+"   \x1b[0m", 2, i)
            print_at_position(color+"   \x1b[0m", 10, i)
            print_at_position(color+"   \x1b[0m", 19, i)
        for i in range(2, 10):
            print_at_position(color+"   \x1b[0m", i, 560)
        for i in range(10,20):    
            print_at_position(color+"   \x1b[0m", i, 540)   

    print_at_position(color+"                  ■■■■■■\x1b[0m", 2, 502)
    for i in range(3, 20):
        print_at_position(color+"   \x1b[0m", i, 500)
    for i in range(3, 10):
        print_at_position(color+"   \x1b[0m", i, 525)
    print_at_position(color+"                    ■■■■■■\x1b[0m", 10, 500)
    
        
    positions = [
    (2, 580), (3, 580),
    (4, 581), (5, 581),
    (6, 582), (7, 582),
    (8, 583), (9, 583),
    (10, 584), (11, 584),
    (12, 585), (13, 585),
    (14, 586), (15, 586),
    (16, 587), (17, 587),
    (18, 588), (19, 588)
    ]

    for position in positions:
        row, column = position
        print_at_position(color+"   \x1b[0m", row, column)
        print_at_position(color+"   \x1b[0m", row, column+22)
        
    positions = [
        (19, 591), (18, 591),
        (17, 592), (16, 592),
        (15, 593), (14, 593),
        (13, 594), (12, 594),
        (11, 595), (10, 595),
        (9, 596), (8, 596),
        (7, 597), (6, 597),
        (5, 598), (4, 598),
        (3, 599), (2, 599)
    ]

    for position in positions:
        row, column = position
        print_at_position(color+"   \x1b[0m", row, column)
        print_at_position(color+"   \x1b[0m", row, column+22)
        
    for i in range(2,20):
        print_at_position(color+"   \x1b[0m", i, 642)
    for i in range(638,646):
        print_at_position(color+"   \x1b[0m", 2, i)
        print_at_position(color+"   \x1b[0m", 19, i)
    for i in range(2,20):    
        print_at_position(color+"   \x1b[0m", i, 665)
        print_at_position(color+"   \x1b[0m", i, 686)
    print_at_position(color+"   \x1b[0m", 2, 666)
    print_at_position(color+"   \x1b[0m", 3, 667)
    print_at_position(color+"   \x1b[0m", 4, 668)
    print_at_position(color+"   \x1b[0m", 5, 669)
    print_at_position(color+"   \x1b[0m", 6, 670)
    print_at_position(color+"   \x1b[0m", 7, 671)
    print_at_position(color+"   \x1b[0m", 8, 672)
    print_at_position(color+"   \x1b[0m", 9, 673)
    print_at_position(color+"   \x1b[0m", 10, 674)
    print_at_position(color+"   \x1b[0m", 11, 675)
    print_at_position(color+"   \x1b[0m", 12, 676)
    print_at_position(color+"   \x1b[0m", 13, 677)
    print_at_position(color+"   \x1b[0m", 14, 678)
    print_at_position(color+"   \x1b[0m", 15, 679)
    print_at_position(color+"   \x1b[0m", 16, 680)
    print_at_position(color+"   \x1b[0m", 17, 681)
    print_at_position(color+"   \x1b[0m", 18, 682)
    print_at_position(color+"   \x1b[0m", 19, 683)
    for i in range(2,17):
        print_at_position(color+"   \x1b[0m", i, 703)
    for i in range(19,20):
        print_at_position(color+"   \x1b[0m", i, 703)
    for i in range(2,17):
        print_at_position(color+"   \x1b[0m", i, 713)
    for i in range(19,20):
        print_at_position(color+"   \x1b[0m", i, 713)
    


def print_line(winner, type, position):
    print_winner(winner)
    if type == 1:
        position[0] = type1_row_dirt[position[0]]
        position[1] = type1_col_dirt[position[1]]
        for i in range(position[1] - 38, position[1] + 38):
            print_at_position("\x1b[05;40;33m■■■■\x1b[0m", i, position[0])
    if type == 2:
        position[0] = type2_row_dirt[position[0]]
        position[1] = type2_col_dirt[position[1]]
        for i in range(position[0] - 92, position[0] + 92):
            print_at_position("\x1b[43;33m■\x1b[0m", position[1], i)
    if type == 3:
        position[0] = type3_row_dirt[position[0]]
        position[1] = type3_col_dirt[position[1]]
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 37, position[1] - 92
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 36, position[1] - 90
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 35, position[1] - 87
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 34, position[1] - 85
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 33, position[1] - 82
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 32, position[1] - 80
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 31, position[1] - 77
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 30, position[1] - 75
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 29, position[1] - 72
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 28, position[1] - 70
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 27, position[1] - 67
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 26, position[1] - 65
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 25, position[1] - 62
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 24, position[1] - 60
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 23, position[1] - 57
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 22, position[1] - 55
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 21, position[1] - 52
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 20, position[1] - 50
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 19, position[1] - 47
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 18, position[1] - 45
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 17, position[1] - 42
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 16, position[1] - 40
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 15, position[1] - 37
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 14, position[1] - 35
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 13, position[1] - 32
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 12, position[1] - 30
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 11, position[1] - 27
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 10, position[1] - 25
        )
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 9, position[1] - 22)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 8, position[1] - 20)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 7, position[1] - 17)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 6, position[1] - 15)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 5, position[1] - 12)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 4, position[1] - 10)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 3, position[1] - 7)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 2, position[1] - 5)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 1, position[1] - 2)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0], position[1])
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 1, position[1] + 3)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 2, position[1] + 5)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 3, position[1] + 8)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 4, position[1] + 10)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 5, position[1] + 13)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 6, position[1] + 15)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 7, position[1] + 18)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 8, position[1] + 20)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 9, position[1] + 23)
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 10, position[1] + 25
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 11, position[1] + 28
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 12, position[1] + 30
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 13, position[1] + 33
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 14, position[1] + 35
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 15, position[1] + 38
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 16, position[1] + 40
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 17, position[1] + 43
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 18, position[1] + 45
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 19, position[1] + 48
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 20, position[1] + 50
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 21, position[1] + 53
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 22, position[1] + 55
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 23, position[1] + 58
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 24, position[1] + 60
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 25, position[1] + 63
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 26, position[1] + 65
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 27, position[1] + 68
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 28, position[1] + 70
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 29, position[1] + 73
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 30, position[1] + 75
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 31, position[1] + 78
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 32, position[1] + 80
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 33, position[1] + 83
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 34, position[1] + 85
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 35, position[1] + 88
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 36, position[1] + 90
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 37, position[1] + 93
        )
    if type == 4:
        position[0] = type3_row_dirt[position[0]]
        position[1] = type3_col_dirt[position[1]]
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 37, position[1] - 92
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 36, position[1] - 90
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 35, position[1] - 87
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 34, position[1] - 85
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 33, position[1] - 82
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 32, position[1] - 80
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 31, position[1] - 77
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 30, position[1] - 75
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 29, position[1] - 72
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 28, position[1] - 70
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 27, position[1] - 67
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 26, position[1] - 65
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 25, position[1] - 62
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 24, position[1] - 60
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 23, position[1] - 57
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 22, position[1] - 55
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 21, position[1] - 52
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 20, position[1] - 50
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 19, position[1] - 47
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 18, position[1] - 45
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 17, position[1] - 42
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 16, position[1] - 40
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 15, position[1] - 37
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 14, position[1] - 35
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 13, position[1] - 32
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 12, position[1] - 30
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 11, position[1] - 27
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] + 10, position[1] - 25
        )
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 9, position[1] - 22)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 8, position[1] - 20)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 7, position[1] - 17)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 6, position[1] - 15)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 5, position[1] - 12)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 4, position[1] - 10)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 3, position[1] - 7)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 2, position[1] - 5)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] + 1, position[1] - 2)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0], position[1])
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 1, position[1] + 3)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 2, position[1] + 5)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 3, position[1] + 8)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 4, position[1] + 10)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 5, position[1] + 13)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 6, position[1] + 15)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 7, position[1] + 18)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 8, position[1] + 20)
        print_at_position("\x1b[43;33m■■■■■■\x1b[0m", position[0] - 9, position[1] + 23)
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 10, position[1] + 25
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 11, position[1] + 28
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 12, position[1] + 30
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 13, position[1] + 33
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 14, position[1] + 35
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 15, position[1] + 38
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 16, position[1] + 40
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 17, position[1] + 43
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 18, position[1] + 45
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 19, position[1] + 48
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 20, position[1] + 50
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 21, position[1] + 53
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 22, position[1] + 55
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 23, position[1] + 58
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 24, position[1] + 60
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 25, position[1] + 63
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 26, position[1] + 65
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 27, position[1] + 68
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 28, position[1] + 70
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 29, position[1] + 73
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 30, position[1] + 75
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 31, position[1] + 78
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 32, position[1] + 80
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 33, position[1] + 83
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 34, position[1] + 85
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 35, position[1] + 88
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 36, position[1] + 90
        )
        print_at_position(
            "\x1b[43;33m■■■■■■\x1b[0m", position[0] - 37, position[1] + 93
        )
