def game(ans) :
    C = 0
    while C == 0  :
        A = 0
        B = 0 
        guess = input("\033[37mInput 4 num : ") 
        if str.isdigit(guess) == False : 
            print('\033[31merror!! 4 !num! plz',)
            continue
        if len(guess) != 4 :
            print('\033[31merror!! !4! num plz',)
            continue
        for i  in range(0,4) :
            for j in range(0,4):
                if ans[i] == guess[j] :
                    if i == j :
                        A = A + 1
                    else : 
                        B = B + 1
        if A == 4 :
            print("Won!!")
            C = C + 1
        else : 
            print( A,end='')
            print('A',end='')
            print(B,end='')
            print('B, ',end='')
            print('try again, ',end='')
def generateans() : 
    from random import randint
    c = ''
    while len(c) < 4 : 
        b = randint(0,9)
        if len(c) == 0 :
            if b == 0 :
                continue
        c = c + str(b)
        setc = set(c)
        if len(c) != len(setc) :
            c=''
            continue
    return c
genans = generateans()
game(genans)
