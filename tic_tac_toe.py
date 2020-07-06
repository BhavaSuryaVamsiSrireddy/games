print("*** WELCOME TO THE TIC TAC TOE ***")
print("please enter the size of the board")

size = int(input())

itr = ((size * size)//2)+1
board = []
k = 0
f = 0
print(itr)

for i in range(size):
    sl = []
    for j in range(size):
        k = k + 1
        sl.append(k)
    board.append(sl)

    
for i in range(size):
    for j in range(size):
        print(board[i][j],end=" ")
    print("\n")

def row_search(sym):
    for i in board:
        c = i.count(sym)
        if c == len(i):
            global f
            f = 1
            print(sym+" won the game")
            break
    return f

def column_search(sym):
    for i in range(size):
        ce = []
        for j in range(size):
            ce.append(board[j][i])
        c = ce.count(sym)
        if c == size:
            global f
            f = 1
            print(sym+" won the game")
            break
    return f

def diagonal_search(sym):
    pd = []
    sd = []
    for i in range(size):
        for j in range(size):
            if (i == j):
                pd.append(board[i][j])
            if ((i + j) == (size - 1)): 
                sd.append(board[i][j])
    pc = pd.count(sym)
    sc = sd.count(sym)
    if pc == size or sc == size :
        global f
        f = 1
        print(sym+" won the game")
    return f

def change(num,sym):
    for i in board:
        if num in i:
            index = i.index(num)
            i[index] = sym

for t in range(itr):
    x_num = int(input("Enter the number to place x"))
    change(x_num,'x')
    
    for i in range(size):
        for j in range(size):
            print(board[i][j],end=" ")
        print("\n")
    
    row_search('x')
    if  f == 1:
        break
    
    column_search('x')
    if  f == 1:
        break
    
    diagonal_search('x')
    if  f == 1:
        break

    if(t==4):
        break
    
    y_num = int(input("Enter the number to place o"))
    change(y_num,'o')
    
    for i in range(size):
        for j in range(size):
            print(board[i][j],end=" ")
        print("\n")
    
    row_search('y')
    if f == 1:
        break
    
    column_search('y')
    if  f == 1:
        break
    
    diagonal_search('y')
    if  f == 1:
        break

if f==0:
    print("tie")



