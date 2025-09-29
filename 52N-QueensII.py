'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

'''

class Solution:
    def __init__(self):
        self.count=0
    def totalNQueens(self, n: int) -> int:
        subset=[["." for _ in range(n)] for _ in range(n)]
        cols=set()
        pos_dia=set()
        neg_dia=set()
        self.helper(subset,0,cols,pos_dia,neg_dia,n)
        return self.count

    def helper(self,subset:list[str],row:int,cols:set,pos_dia:set,neg_dia:set,n:int):
        if row==n:
            self.count+=1
            return 
        for col in range(n):
            if col in cols or (row+col) in pos_dia or (row-col) in neg_dia:
                continue 
            cols.add(col)
            pos_dia.add(row+col)
            neg_dia.add(row-col)
            subset[row][col]='Q'
            self.helper(subset,row+1,cols,pos_dia,neg_dia,n)
            subset[row][col]="."
            cols.remove(col)
            pos_dia.remove(row+col)
            neg_dia.remove(row-col)

class TestApp:
      def testCaseOne(self):
          assert Solution().totalNQueens(4)==2
      def testCaseTwo(self):
          assert Solution().totalNQueens(1)==1