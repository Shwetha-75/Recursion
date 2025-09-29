'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such 
that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

'''

class Solution:
    def __init__(self):
        self.res=[]
    def solveNQueens(self, n: int) -> list[list[str]]:
        # res=[]
        for i in range(n):
            matrix=[["0" for _ in range(n)] for _ in range(n)]
            matrix[0][i]="1"
            self.helper(1,n,matrix)
        res=[]
        for i in range(len(self.res)):
            for j in range(n):
                self.res[i][j]="".join(self.res[i][j]).replace("0",".").replace("1","Q")
            res.append(self.res[i])
        return res
            
        
    def checkTop(self,row:int,col:int,matrix:list[list[int]]):
        if row<0: return True 
        if matrix[row][col]=="1": return False 
        return self.checkTop(row-1,col,matrix)
    def checkTopLeft(self,row:int,col:int,matrix:list[list[int]]):
        if col<0 or row<0: return True 
        if matrix[row][col]=="1": return False 
        return self.checkTopLeft(row-1,col-1,matrix)
    def checkLeft(self,row:int,col:int,matrix:list[list[int]]):
        if col<0: return True 
        if matrix[row][col]=="1": return False 
        return self.checkLeft(row,col-1,matrix)
    def checkTopRight(self,row:int,col:int,matrix:list[list[int]],n:int):
        if col==n or row<0: return True 
        if matrix[row][col]=="1": return False 
        return self.checkTopRight(row-1,col+1,matrix,n)
    
    def helper(self,row:int,n:int,matrix:list[list[int]]):
        if row == n: 
            self.res.append([rows[:] for rows in matrix])
            return 
        for col in range(n):
            top_left=self.checkTopLeft(row-1,col-1,matrix)
            top=self.checkTop(row-1,col,matrix)
            top_right=self.checkTopRight(row-1,col+1,matrix,n) 
            left=self.checkLeft(row,col-1,matrix)
            if top_left and top and top_right and  left:
                matrix[row][col]="1"
                self.helper(row+1,n,matrix)
                matrix[row][col]="0"

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result=[]
        subset=[["." for _ in range(n)] for _ in range(n)]
        cols=set()
        pos_dia=set()
        neg_dia=set()
        self.helper(result,subset,0,cols,pos_dia,neg_dia,n)
        return result

    def helper(self,res:list[list[str]],subset:list[str],row:int,cols:set,pos_dia:set,neg_dia:set,n:int):
        if row==n:
            res.append(["".join(r) for r in subset])
            return 
        for col in range(n):
            if col in cols or (row+col) in pos_dia or (row-col) in neg_dia:
                continue 
            cols.add(col)
            pos_dia.add(row+col)
            neg_dia.add(row-col)
            subset[row][col]='Q'
            self.helper(res,subset,row+1,cols,pos_dia,neg_dia,n)
            subset[row][col]="."
            cols.remove(col)
            pos_dia.remove(row+col)
            neg_dia.remove(row-col)
        
        
class TestApp:
      def testCaseOne(self):
          assert Solution().solveNQueens(4)==[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
      def testCaseTwo(self):
          assert Solution().solveNQueens(1)==[["Q"]]      
      def testCaseThree(self):
          assert Solution().solveNQueens(5)==[["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]          
            
