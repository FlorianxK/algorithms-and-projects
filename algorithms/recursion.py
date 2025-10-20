from typing import List
class Solution:
    def oneton(self, n:int):
        if n < 1:
            return ""
        return self.oneton(n-1) + str(n) + " "

    def meanarray(self, arr:List,n:int):
        if n == 1:
            return arr[n-1]
        else:
            return (self.meanarray(arr,n-1)*(n-1)+arr[n-1]) / n

    def sumnaturalnumb(self, n:int):
        if n == 1:
            return 1
        return self.sumnaturalnumb(n-1) + n

    def dectobin(self, n:int):
        if n == 0:
            return 0
        else:
            return n % 2 + 10 * (int(self.dectobin(n//2)))

    def combSum(self, nums, target):
        res = []
        sol = []

        def backtrack(i):
            sumSol = sum(sol)
            if sumSol == target:
                res.append(sol[:])
                return
            if i == len(nums) or sumSol > target:
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i) 
            sol.pop()
        
        backtrack(0)
        return res


def main():
    s = Solution()
    print("skip")
    nums = [2,3,6,7]
    target = 7
    print(s.combSum(nums,target))
     

if __name__=="__main__":
    main()