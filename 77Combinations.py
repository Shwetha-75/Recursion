'''

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

'''

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        array=[i for i in range(1,n+1)]
        result=[]
        self.helper(array,result,[],n,0,k)
        return result
    def helper(self,array:list[int],result:list[list[int]],subset:list[int],n:int,index:int,k:int):
        if index==n:
           if len(subset)==k:
               result.append(subset[::])
           return 
        subset.append(array[index])
        self.helper(array,result,subset,n,index+1,k)
        subset.pop()
        self.helper(array,result,subset,n,index+1,k)
class TestApp:
      def testCaseOne(self):
          assert Solution().combine(4,2)
        
        