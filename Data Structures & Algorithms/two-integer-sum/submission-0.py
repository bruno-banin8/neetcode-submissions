class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in aux and aux[difference] != i:
                return [aux[difference], i]
            else:
                aux[n] = i