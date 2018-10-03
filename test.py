last_pick='x'
postion_picked=''

def draw_board(board):
    print('\r\n')
    print('       |       |')
    print(' ' + board[6] + '     | ' + board[7] + '     | ' + board[8])
    print('       |       |')
    print('----------------------')
    print('       |       |')
    print(' ' + board[3] + '     | ' + board[4] + '     | ' + board[5])
    print('       |       |')
    print('----------------------')
    print('       |       |')
    print(' ' + board[0] + '     | ' + board[1] + '     | ' + board[2])
    print('       |       |')

def get_pick(board):
    global postion_picked
    msg ='It is player ' + last_pick +' turn to pic a an open square: '
    postion_picked=str(input(msg))
    while check_postion() == True:
        postion_picked=str(input(msg))

    
   
def check_postion():
    global postion_picked
    global last_pick
    if board[int(postion_picked)] in {'x','y'}: 
        print("Invalid Pick")
        return(True)
    else:
        board[int(postion_picked)] = last_pick
        if last_pick == 'x':
            last_pick = 'y'
        else:
            last_pick = 'x'
        return(False)
        
        
def check_if_over(board):
    check_board(board,0,1,2)
    check_board(board,3,4,5)
    check_board(board,6,7,8)
    check_board(board,0,4,8)
    check_board(board,2,4,6)
    check_board(board,0,3,6)
    check_board(board,1,4,7)
    check_board(board,2,5,8)
    end_game=True
    for i in range(9):
        if board[i] not in  {'x','y'}:
            end_game = False
    if end_game:    
        print("Game Over no one wins") 
        exit(0)   
    
    
    
def check_board(board,a,b,c):
    if (board[a] == "x" and board[b] == "x" and board[c] == "x"):
        draw_board(board)
        print("Game Over Player X wins")
        exit(0)
    elif (board[a] == "y" and board[b] == "y" and board[c] == "y"):
        draw_board(board)
        print("Game Over Player Y wins")
        exit(0)

def start_game():
    while True:
        get_pick(board)
        draw_board(board)
        check_if_over(board)

if __name__ == '__main__':
    board=[]
    
    for i in range(10):
        board.append(str(i))
    draw_board(board)
    start_game()
    
    

    
