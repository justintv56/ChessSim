from random import* 
import copy
def moves(str, p, board):
    listMoves = [str,[p[0], p[1]]]
    
    if str == 'P':
        if p[0] < 7 and p[0] > 0:
            if board[p[0] + 1][p[1]] == '.':
                listMoves.append([p[0] + 1, p[1]])
                if p[0] == 1 and board[p[0] + 2][p[1]] == '.':
                    listMoves.append([p[0] + 2, p[1]])
            if p[1] > 0:
                if board[p[0] + 1][p[1] - 1] not in ['.', 'P', 'R', 'N', 'B', 'Q', 'K']:
                    listMoves.append([p[0] + 1, p[1] - 1])
            if p[1] < 7:
                 if board[p[0] + 1][p[1] + 1] not in ['.', 'P', 'R', 'N', 'B', 'Q', 'K']:
                    listMoves.append([p[0] + 1, p[1] + 1])
    if str == 'p':
        if p[0] < 7 and p[0] > 0:
             if board[p[0] - 1][p[1]] == '.':
                listMoves.append([p[0] - 1, p[1]])
                if p[0] == 6 and board[p[0] - 2][p[1]] == '.':
                    listMoves.append([p[0] - 2, p[1]])
             if p[1] > 0:
                if board[p[0] - 1][p[1] - 1] not in ['.', 'p', 'r', 'n', 'b', 'q', 'k']:
                    listMoves.append([p[0] - 1, p[1] - 1])
             if p[1] < 7:
                 if board[p[0] - 1][p[1] + 1]  not in ['.', 'p', 'r', 'n', 'b', 'q', 'k']:
                    listMoves.append([p[0] - 1, p[1] + 1])
                
                
    if str in ['B', 'b', 'q', 'Q']:
        a, b, piece = p[0], p[1], True
        while a < 7 and piece and b < 7:
            a+=1
            b+=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'B'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in['q', 'b'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True        
        while a > 0 and piece and b < 7:
            a-=1
            b+=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'B'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in['q', 'b'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True
        while a > 0 and piece and b > 0:
            a-=1
            b-=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'B'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in['q', 'b'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True         
        while a < 7 and piece and b > 0:
            a+=1
            b-=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'B'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in['q', 'b'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
    
                
    if str == 'N':
        if p[0] + 2 < 8 and p[1] + 1 < 8 and board[p[0] + 2][p[1] + 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 2, p[1] + 1])   
        if p[0] + 2 < 8 and p[1] - 1 >= 0 and board[p[0] + 2][p[1] - 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 2, p[1] - 1])   
        if p[0] + 1 < 8 and p[1] + 2 < 8 and board[p[0] + 1][p[1] + 2] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 1, p[1] + 2])   
        if p[0] + 1 < 8 and p[1] - 2 >= 0 and board[p[0] + 1][p[1] - 2] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 1, p[1] - 2])   
        if p[0] - 2 >= 0 and p[1] + 1 < 8 and board[p[0] - 2][p[1] + 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 2, p[1] + 1])   
        if p[0] - 2 >= 0 and p[1] - 1 >= 0 and board[p[0] - 2][p[1] - 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 2, p[1] - 1])   
        if p[0] - 1 >= 0 and p[1] + 2 < 8 and board[p[0] - 1][p[1] + 2] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 1, p[1] + 2])   
        if p[0] - 1 >= 0 and p[1] - 2 >= 0 and board[p[0] - 1][p[1] - 2] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 1, p[1] - 2])
    if str == 'n':
        if p[0] + 2 < 8 and p[1] + 1 < 8 and board[p[0] + 2][p[1] + 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 2, p[1] + 1])   
        if p[0] + 2 < 8 and p[1] - 1 >= 0 and board[p[0] + 2][p[1] - 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 2, p[1] - 1])   
        if p[0] + 1 < 8 and p[1] + 2 < 8 and board[p[0] + 1][p[1] + 2] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 1, p[1] + 2])   
        if p[0] + 1 < 8 and p[1] - 2 >= 0 and board[p[0] + 1][p[1] - 2] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 1, p[1] - 2])   
        if p[0] - 2 >= 0 and p[1] + 1 < 8 and board[p[0] - 2][p[1] + 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 2, p[1] + 1])   
        if p[0] - 2 >= 0 and p[1] - 1 >= 0 and board[p[0] - 2][p[1] - 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 2, p[1] - 1])   
        if p[0] - 1 >= 0 and p[1] + 2 < 8 and board[p[0] - 1][p[1] + 2] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 1, p[1] + 2])   
        if p[0] - 1 >= 0 and p[1] - 2 >= 0 and board[p[0] - 1][p[1] - 2] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 1, p[1] - 2])
    
                
    if str in ['R', 'r', 'q', 'Q']:
        a, b, piece = p[0], p[1], True
        while a < 7 and piece:
            a+=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'R'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in ['q', 'r'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True
        while a > 0 and piece:
            a-=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'R'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in ['q', 'r'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True
        while b < 7 and piece:
            b+=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'R'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in ['q', 'r'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
        a, b, piece = p[0], p[1], True
        while b > 0 and piece:
            b-=1
            if board[a][b] == '.':
                listMoves.append([a,b])
            elif str in['Q', 'R'] and board[a][b] in ['p', 'r', 'n', 'b', 'q', 'k']:
                piece = False
                listMoves.append([a,b])
            elif str in ['q', 'r'] and board[a][b] in ['P', 'R', 'N', 'B', 'Q', 'K']:
                piece = False
                listMoves.append([a,b])
            else:
                piece = False
                
                
    if str == 'K':
        if p[0] + 1 < 8 and board[p[0] + 1][p[1]] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 1, p[1]])
        if p[0] + 1 < 8 and p[1] + 1 < 8 and board[p[0] + 1][p[1] + 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 1, p[1] + 1])
        if p[0] + 1 < 8 and p[1] - 1 >= 0 and board[p[0] + 1][p[1] - 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] + 1, p[1] - 1])
        if p[0] - 1 >= 0 and board[p[0] - 1][p[1]] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 1, p[1]])
        if p[0] - 1 >= 0 and p[1] + 1 < 8 and board[p[0] - 1][p[1] + 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 1, p[1] + 1])
        if p[0] - 1 >= 0 and p[1] - 1 >= 0 and board[p[0] - 1][p[1] - 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0] - 1, p[1] - 1])
        if p[1] - 1 >= 0 and board[p[0]][p[1] - 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0], p[1] - 1])
        if p[1] + 1 < 8 and board[p[0]][p[1] + 1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            listMoves.append([p[0], p[1] + 1])
    if str == 'k':
        if p[0] + 1 < 8 and board[p[0] + 1][p[1]] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 1, p[1]])
        if p[0] + 1 < 8 and p[1] + 1 < 8 and board[p[0] + 1][p[1] + 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 1, p[1] + 1])
        if p[0] + 1 < 8 and p[1] - 1 >= 0 and board[p[0] + 1][p[1] - 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] + 1, p[1] - 1])
        if p[0] - 1 >= 0 and board[p[0] - 1][p[1]] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 1, p[1]])
        if p[0] - 1 >= 0 and p[1] + 1 < 8 and board[p[0] - 1][p[1] + 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 1, p[1] + 1])
        if p[0] - 1 >= 0 and p[1] - 1 >= 0 and board[p[0] - 1][p[1] - 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0] - 1, p[1] - 1])
        if p[1] - 1 >= 0 and board[p[0]][p[1] - 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0], p[1] - 1])
        if p[1] + 1 < 8 and board[p[0]][p[1] + 1] not in ['p', 'r', 'n', 'b', 'q', 'k']:
            listMoves.append([p[0], p[1] + 1])
    
    return listMoves

def removeMove(list1, piece, start, stop):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][0] == piece:
                if list1[i][1] == start:
                    if list1[i][j] == stop:
                        x = stop
                        l = i
                    else:
                        continue
                else: 
                    continue
            else:
                continue
    list1[l].remove(x)
    return list1
    
    
def findMoves(board):
     move3 = []
     for i in range(8):
        for j in range(8):
            if board[i][j] != '.':
                move3.append(moves(board[i][j], [i, j], board))
     return move3
 
def findUpper(move):
    upper1 = []
    for i in range(len(move)):
        if move[i][0] in ['P', 'R', 'N', 'B', 'Q', 'K'] and len(move[i]) > 2:
            upper1.append(move[i])
    return upper1

def findLower(move):
    lower1 = []
    for i in range(len(move)):
        if move[i][0] in ['p', 'r', 'n', 'b', 'q', 'k'] and len(move[i]) > 2:
            lower1.append(move[i])
    return lower1

def play(posO, pos, board): 
    board2 = copy.deepcopy(board)
    board2[pos[0]][pos[1]] = board2[posO[0]][posO[1]]
    board2[posO[0]][posO[1]] = '.'
    board2 = promote(board2)
    return board2

def checkU(board, upper):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                king = [i, j]
    for i in range(len(upper)):
        for j in range(2, len(upper[i])):
            if upper[i][j] == king:
                return True
    
    return False

def checkL(board, lower):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'K':
                king = [i, j]
    for i in range(len(lower)):
        for j in range(len(lower[i])):
            if lower[i][j] == king:
                return True
    return False

def moreThanTwo(list4):
    list5 = []
    for i in range(len(list4)):
        if len(list4[i]) > 2:
            list5.append(list4[i])
    return list5

def draw(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] in ['R', 'r', 'q', 'Q', 'p', 'P']:
                return False
    return True

def promote(board):
    board2 = copy.deepcopy(board)
    choice = ['q', 'r', 'n', 'b']
    choice2 = ['Q', 'R', 'N', 'B']
    for i in range(8):
        if(board2[0][i] == 'p'):
            board2[0][i] = choice[randint(0, 3)]
    for i in range(8):
        if(board2[7][i] == 'P'):
            board2[7][i] = choice2[randint(0, 3)]
    return board2
    


board = [["R", "N", "B", "Q", "K", "B", "N", "R"], ["P","P","P","P","P","P","P","P",], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], ["p","p","p","p","p","p","p","p",], ["r", "n", "b", "q", "k", "b", "n", "r"]]
#board = [[".", "N", "B", "Q", "K", "B", ".", "R"], ["R","P","P",".","P","q",".","N",], [".", ".", ".", "P", ".", ".", ".", "."], ["P", ".", ".", ".", ".", ".", "P", "P"], [".", ".", "p", ".", "p", ".", ".", "p"], ["n", ".", ".", ".", ".", ".", ".", "."], ["p","p",".","p",".","p","p",".",], ["r", ".", "b", ".", "k", "b", "n", "r"]]
#board = [[".", ".", ".", ".", ".", ".", ".", "."], [".","k",".","K",".",".",".",".",], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".",".",".",".",".",".","P",".",], [".", ".", ".", ".", ".", ".", ".", "."]]
for i in range(len(board)):
    for j in range(len(board[0])):
        
        print(board[i][j], end = "")
    print()
print()

x = 1
mate = False
while not mate:
#for p in range(1):
    move, upper, lower, next1, worked = [], [], [], [], False
    x *= -1
    if x < 0:
        bot = 'upper'
    else:
        bot = 'lower'
    
    move = findMoves(board)
    upper = findUpper(move)  
    lower = findLower(move)
    
    while(not worked):
    #for i in range(1):
        boardCheck = copy.deepcopy(board)
      #  print(boardCheck)
        if bot == 'upper':
            ran = randint(0, len(upper) - 1)
            nran = randint(2,len(upper[ran]) - 1)
            next1.append(upper[ran][0])
            next1.append(upper[ran][1])
            next1.append(upper[ran][nran])
            
        else:
            ran = randint(0, len(lower) - 1)
            nran = randint(2,len(lower[ran]) - 1)
            next1.append(lower[ran][0])
            next1.append(lower[ran][1])
            next1.append(lower[ran][nran])
            
       # upper, lower = [], []
        if bot == 'upper':
            boardCheck = play(next1[1], next1[2], boardCheck)
            lowerTest = findLower(findMoves(boardCheck))
            if not checkL(boardCheck, lowerTest):
                board = play(next1[1], next1[2], board)
                worked = True
            else:
                upper = removeMove(upper, next1[0], next1[1], next1[2])
                upper = moreThanTwo(upper)

        if bot == 'lower':
            boardCheck = play(next1[1], next1[2], boardCheck)
            upperTest = findUpper(findMoves(boardCheck))
            if not checkU(boardCheck, upperTest): 
                board = play(next1[1], next1[2], board)
                worked = True
            else:
                lower = removeMove(lower, next1[0], next1[1], next1[2])
                lower = moreThanTwo(lower)
        
        next1, upperTest, lowerTest = [], [], []


        if len(lower) == 0 and checkU(board, upper):
            mate = True
            break
        elif len(lower) == 0:
            break
        if len(upper) == 0 and checkL(board, lower):
            mate = True
            break
        elif len(upper) == 0:
            break
           
    
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end = "")
        print()
    print()

    
    next1, upper, lower, move = [], [], [], []
    
    if draw(board):
        break
if mate:
    if bot == 'upper':
        print('Checkmate! White Wins.')
    else:
        print('Checkmate! Black Wins.')
else:
    print('Draw.')
    #mate = True 