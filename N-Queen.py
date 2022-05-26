n = int(input("Enter the number of n"))
board = []

def getBoard():
    for i in range(n):
        nthlist = []
        for j in range(n):
            nthlist.append(0)
        board.append(nthlist)\
        
def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print("")   
        
def isSafe(row,col):
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False
    # Queen appears in the northwest direction
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i= i-1
        j= j-1
        
    # Queen appears in the northeast direction
    i = row - 1
    j= col + 1
    
    while(i>=0 and j<n):
        if board[i][j] == 1:
            return False
        i = i - 1
        j= j + 1 
    
    # Queen appears in the southwest direction   
    i= row + 1    
    j = col -1 
    while(i<n and j>=0):
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1
    
    # Queen appears in the northeast direction
    i = row+1
    j = col + 1
    while(i<n and j<n):
        if board[i][j] == 1:
            return False
        
        i = i + 1
        j = j + 1
    return True    

def Put(n,count):
    if count==n:
        return True
        
    for i in range(n):
        for j in range(n):
            if isSafe(i,j):
                board[i][j] = 1
                count = count+1
                if Put(n,count)==True:
                    return True
                board[i][j] = 0
                count =count-1
    return False
    
getBoard()
Put(n,0)
printBoard()