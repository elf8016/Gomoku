import random


def get_answer() -> str:
    answer_list = []
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num_list)
    answer_list.append(num_list.pop())
    num_list.append(0)
    answer_list.extend(random.sample(num_list, 3))
    answer_strlist = [str(x) for x in answer_list]
    answer = "".join(answer_strlist)
    return answer


def check_Input(guess: str) -> bool:
    if (
        str.isdigit(guess) == False
        or len(guess) != 4
        or guess[0] == "0"
        or len(set(guess)) != 4
    ):
        return False


def check_ans(ans: str, guess: str) -> list:
    AB = [0] * 2
    for i in range(0, 4):
        for j in range(0, 4):
            if ans[i] == guess[j]:
                if i == j:
                    AB[0] += 1
                else:
                    AB[1] += 1
    if AB[0] == 4:
        print("YOU WON !!")
        quit()
    else:
        return AB


def interactive() -> str:
    while True:
        guess = input("\n\033[37mInput 4 num : ")
        if check_Input(guess) == False:
            print("\033[31mError!")
            continue
        else:
            return guess


if __name__ == "__main__":
    print(
        "Welcome to 1A2B\n1. Type 4 num\n2. First one connot be 0\n3.  Repeated num not allowed"
    )
    ans = get_answer()
    print(ans)
    while True:
        guess = interactive()
        print(guess)
        print("\033[37m{}A{}B Try again!!".format(*check_ans(ans, guess)))

