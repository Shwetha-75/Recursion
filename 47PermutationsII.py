'''

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result=[]
        hash_map=defaultdict(int)
        for num in nums:
            hash_map[num]+=1
        self.helper(hash_map,nums,[],result)
        return result 
    def helper(self,hash_map:defaultdict,nums:list[int],sub_array:list[int],result:list[list[int]]):
        if len(sub_array)==len(nums):
            result.append(sub_array[::])
            return 
        for num in hash_map:
            if hash_map[num]>0:
                sub_array.append(num)
                hash_map[num]-=1
                self.helper(hash_map,nums,sub_array,result)
                sub_array.pop()
                hash_map[num]+=1
Solution().permuteUnique([1,1,2])
