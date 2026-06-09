class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [[] for _ in range(n)]
        sufix = [[] for _ in range(n)]
        res = [[] for _ in range(n)]
        for i in range(n):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 1, -1, -1):
            if i == (n - 1):
                sufix[i] = 1
            else:
                sufix[i] = nums[i + 1] * sufix[i + 1]
        for i in range(n):
            res[i] = prefix[i] * sufix[i]
        return res