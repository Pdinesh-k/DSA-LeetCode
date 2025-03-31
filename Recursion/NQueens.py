class Solution():
    def display(self,board):
        arr = [["." for _ in range(len(board))] for _ in range(len(board))]
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]==True:
                    arr[i][j] = "Q"
        print(arr)
        
    def isSafe(self,board,row,col):
        #checking the vertical row
        for i in range(0,row):
            if board[i][col]:
                return False
        
        #checking for the left diagonal
        maxLeft = min(row,col)
        for i in range(1,maxLeft+1):
            if board[row-i][col-i]:
                return False
        #checking for the right diagonal
        maxRight = min(row,len(board)-col-1)
        for i in range(1,maxRight+1):
            if board[row-i][col+i]:
                return False
        return True
                
    def nQueens(self,row,board):
        if row == len(board):
            self.display(board)
            return
        for col in range(0,len(board)):
            if self.isSafe(board,row,col):
                board[row][col]=True
                self.nQueens(row+1,board)
                board[row][col]=False

n=4
sol = Solution()
board = [[False for _ in range(n)]for _ in range(n)]
sol.nQueens(0,board)