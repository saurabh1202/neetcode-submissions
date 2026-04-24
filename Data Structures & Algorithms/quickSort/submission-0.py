# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[pair], start, end):
        if end - start + 1 <= 1:
            return pairs

        pivot = pairs[end] 
        #print(pivot)
        left = start
        i = start

        while i < end:
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left = left + 1
            i = i + 1
        pairs[end] = pairs[left]
        pairs[left] = pivot
        """
        print('-------------------')
        for pair in pairs:
            print(pair.key)
        print('-------------------')
        print ("left :", left)
        """
        self.quickSortHelper(pairs, start, left - 1)
        self.quickSortHelper(pairs, left + 1, end)
    

