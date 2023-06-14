import checkwin
import interactive
import review
import dodobird
import variable
import os


if __name__ == "__main__":
    os.system("clear")
    interactive.init()
    interactive.show(variable.chessboard)
    while 1:
        player = len(variable.track) % 2
        if player == 0:
            position = input("Player1: ")
        else:
            position = input("Player2: ")
        if position == "track":
            print(variable.chessboard)
            print(variable.track)
            continue
        input_list = position.split(",")
        if dodobird.checkinput(input_list) == False:
            continue
        dodobird.save_position(input_list[0], input_list[1])
        os.system("clear")
        interactive.show(variable.chessboard)
        if checkwin.checkwin(input_list) == 0:
            continue
        replay = input("Review or no (Y/N): ")
        if replay == 'Y' or replay == 'y':
            os.system("clear")
            review.review(variable.track)
        again = input("Play again? (Y/N): ")
        if again == 'Y'or again == 'y':
            os.system("clear")
            interactive.init()
            interactive.show(variable.chessboard)
            continue
        else:
            break
