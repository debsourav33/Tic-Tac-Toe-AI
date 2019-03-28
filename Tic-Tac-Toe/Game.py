def minimax(state):
    mx= -9
    action= -1

    for a in range(0,9):
        if state[a]==0:
            state[a]= 1

            score= mini(state)
            if max(mx, score)>mx:
                mx= score
                action= a

            state[a] = 0
    return action

def terminal_state(state):
    win= 0
    for i in range(0,3):
        if state[i]==state[i+3] and state[i+3]==state[i+6]:
            if state[i]!=0:
                return (1,state[i])
    for i in range(0,9,3):
        if state[i]==state[i+1] and state[i+1]==state[i+2]:
            if state[i] != 0:
                return (1,state[i])

    if state[0]==state[4] and state[4]==state[8]:
        if state[0] != 0:
            return (1, state[0])
    if state[2]==state[4] and state[4]==state[6]:
        if state[2]!= 0:
            return (1, state[2])

    filled= True
    for i in range(0,9):
        if state[i]== 0:
            return (0,0)


    return (1,0)

def maxi(state):
    status= terminal_state(state)

    if status[0]!=0:
        return status[1]

    mx = -1

    for a in range(0, 9):
        if state[a] == 0:
            state[a] = 1

            score= mini(state)
            mx= max(score,mx)


            state[a] = 0

    return mx

def mini(state):
    status= terminal_state(state)

    if status[0]!=0:
        return status[1]


    mn = 1
    for a in range(0, 9):
        if state[a] == 0:
            state[a] = -1

            score= maxi(state)
            mn= min(score,mn)

            state[a] = 0

    return mn

def print_board(state):
    for i in range(3):
        #print(state[i], end=" ")

        if state[i]== 0:
            print("_", end=" ")
        if state[i]== 1:
            print("X",end=" ")
        if state[i]== -1:
            print("0",end=" ")

    print("")
    for i in range(3,6):
        #print(state[i], end=" ")


        if state[i]== 0:
            print("_", end=" ")
        if state[i]== 1:
            print("X",end=" ")
        if state[i]== -1:
            print("0",end=" ")

    print("")
    for i in range(6,9):
        #print(state[i], end=" ")

        if state[i]== 0:
            print("_", end=" ")
        if state[i]== 1:
            print("X",end=" ")
        if state[i]== -1:
            print("0",end=" ")

    print("\n")

def game_over(state):
    status = terminal_state(state)
    if status[0]==1:
        if(status[1]==1):
            print("---Winner: AI---")
        elif status[1]==-1:
            print("---Winner: Human---")
        else:
            print("---Match Drawn---")

        return True

    return False


print("Board is interpreted as:")
for i in range(0,9):
    print(i+1,end=" ")
    if i%3==2:
        print("")

state= {}
for i in range(0,9):
    state[i]= 0

print("\nSelect a cell number to begin your move: ")


while True:
    while True:
        x = int(input())-1

        if state[x]!=0:
            print("Illegal Move!!! Blocked Cell.")
        else:
            state[x] = -1
            break

    print("Your move: ", x)
    print_board(state)


    if game_over(state):
        break

    action = minimax(state)
    print("AI's move: ",action)
    state[action] = 1
    print_board(state)

    if game_over(state):
        break