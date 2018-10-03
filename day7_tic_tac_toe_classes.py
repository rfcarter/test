last_pick='x'
postion_picked=''
board=[]  
current_player=''

class Players():
    def __init__(self): 
        self.player1=''
        self.player2=''
        
    
    def get_players(self):
        global current_player
        self.player1=str(input("Player 1 please enter your name: "))
        self.player2=str(input("Player 2 please enter your name: "))
        current_player = self.player1

class  Board():

    def __init__(self,board): 
        self.board=board
        self.msg =''
        self.end_game=''
                      
    def draw_board(self):
        print('\r\n')
        print('       |       |')
        print(' ' + self.board[6] + '     | ' + self.board[7] + '     | ' + self.board[8])
        print('       |       |')
        print('----------------------')
        print('       |       |')
        print(' ' + self.board[3] + '     | ' + self.board[4] + '     | ' + self.board[5])
        print('       |       |')
        print('----------------------')
        print('       |       |')
        print(' ' + self.board[0] + '     | ' + self.board[1] + '     | ' + self.board[2])
        print('       |       |')

    def get_pick(self):
        global postion_picked
        self.msg ='It is player ' + current_player +' turn to pic an open square: '
        postion_picked=str(input(self.msg))
        
   
    def check_postion(self):
        global postion_picked
        global last_pick
        global current_player
        if board[int(postion_picked)] in {'x','y'}: 
            print("Invalid Pick")
            return(True)
        else:
            board[int(postion_picked)] = last_pick
            if last_pick == 'x':
                last_pick = 'y'
                current_player = players.player2
            else:
                last_pick = 'x'
                current_player = players.player1
        return(False)     
        
    def check_if_over(self):
        self.check_board(0,1,2)
        self.check_board(3,4,5)
        self.check_board(6,7,8)
        self.check_board(0,4,8)
        self.check_board(2,4,6)
        self.check_board(0,3,6)
        self.check_board(1,4,7)
        self.check_board(2,5,8)
        self.end_game=True
        for i in range(9):
            if self.board[i] not in  {'x','y'}:
                self.end_game = False
        if self.end_game:    
            print("Game Over no one wins") 
            exit(0)   
   
    def check_board(self,a,b,c):
        global current_player
        if (board[a] == "x" and board[b] == "x" and board[c] == "x"):
            self.draw_board()
            print("Game Over Player " + players.player1 + " wins")
            exit(0)
        elif (board[a] == "y" and board[b] == "y" and board[c] == "y"):
            self.draw_board()
            print("Game Over Player " + players.player2 + " wins")
            exit(0)

def start_game():
    while True:
        game_board.get_pick()
        while game_board.check_postion() == True:
            game_board.postion_picked=str(input(self.msg))  
        game_board.draw_board()
        game_board.check_if_over()

if __name__ == '__main__':
    
    players=Players()
    players.get_players()
    for i in range(9):
        board.append(str(i))
    game_board=Board(board)
    game_board.draw_board()
    start_game()