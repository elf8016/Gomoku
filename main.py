import checkwin
import interactive
# import review
import dodobird
import variable
import os


if __name__ == "__main__":
    os.system("clear")
    interactive.init()
    interactive.show_table()
    while 1:
        interactive.show_player()
        player = len(variable.track) % 2
        if player == 0:
            num1, num2 = interactive.show_input(1)
            interactive.print_piece_red(0,int(num1),int(num2))
        else:
            num1, num2 = interactive.show_input(2)
            interactive.print_piece_blue(0,int(num1),int(num2))
            
        # if dodobird.checkinput(input_list) == False:
        #     continue
        dodobird.save_position(num1, num2)
        input_list = [int(num1),int(num2)]
        winner, direction, pos = checkwin.checkwin(input_list)
        if winner == 0:
            continue
        interactive.print_line(winner, direction, pos)
        os.system("sleep 5")
        # if interactive.print_review() == 1:
        #     review.review()
        if interactive.print_replay() == 1:
            continue
        else:
            break
