class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux = {}
        array = [[] for _ in range(len(nums) + 1)]
        resultado = []
        for num in nums:
            aux[num] = aux.get(num, 0) + 1

        for num in aux.keys():
            array[aux[num]].append(num)
        for item in array:
            if item != []:
                resultado.extend(item)
        return resultado[-k:]