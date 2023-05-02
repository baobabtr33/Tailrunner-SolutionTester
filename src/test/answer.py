answer =  {
1 :  """
class Solution:
    def listSum(self, lst: List[int]) -> int:  
        return sum(lst)
""",

2: """
class Solution:
    def validParentheses(self, s: str) -> bool:
        stack = collections.deque()
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if stack and stack.pop() == char:
                    pass
                else:
                    return False
                
        return False if len(stack) else True
""",

3: """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        slow, fast = 0, 1
        while fast < len(prices):
            ret = max(ret, prices[fast]-prices[slow])
            if prices[fast] < prices[slow]:
                slow = fast
            fast += 1
        return ret
""",

4: """
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlen = 0 
        for i in range(len(nums)): 
            if i > maxlen:
                return False
            maxlen = max(maxlen, nums[i]+i)
        return True
""",

5: """
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums):
            return nums
        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
""",

6: """
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
""",

7: """
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       return len(s.split()[-1])
""",

8: """
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(index, path):
            ret.append(path)
            
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0,[])
        return ret
""",

9: """
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict() 
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            #                    집 하나 스킵하고 체크 해야 되니까. 
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp.popitem()[1]
""",

10: """
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_len = len(grid)
        y_len = len(grid[0])
        
        def searchLand(i,j):
            if grid[i][j] == "1":
                grid[i][j] = "0" # update grid world
                if i + 1 < x_len:
                    searchLand(i + 1, j) # recursive 
                if j + 1 < y_len:
                    searchLand(i, j + 1)
                if i - 1 >= 0:
                    searchLand(i-1, j)
                if j - 1 >= 0:
                    searchLand(i, j - 1)
        
        count = 0
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == "1":
                    searchLand(i,j)
                    count += 1
                    
        return count
""",

11: """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
""",

12: """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
""",

13: """
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])
        ret = 0
        max_val = intervals[0][1]
        for i in range(1, len(intervals)):
            if max_val > intervals[i][0]:
                ret += 1
            else:
                max_val = intervals[i][1]
        return ret
""",

14: """
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])
""",

15: """
class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        ones = binary.count("1")
        total = len(binary)
        return ones + total - 1
""",

16: """
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        base = [[1],[1,1]]
        if numRows == 1:
            return [[1]]

        for i in range(2,numRows):
            tmp = [1]
            for j in range(i-1):
                t = base[i-1][j]+base[i-1][j+1]
                tmp.append(t)
            tmp.append(1)
            base.append(tmp)
            
        return base
""",

17: """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1
""",

18: """
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.pointer = 1
        self.reuse = []

    def popSmallest(self) -> int:
        ret = 0
        print(self.reuse)
        if self.reuse:
            ret = heapq.heappop(self.reuse)
            return ret
        ret = self.pointer
        self.pointer += 1 
        return ret

    def addBack(self, num: int) -> None:
        if num not in self.reuse and num < self.pointer:
            heapq.heappush(self.reuse, num)
"""
}

