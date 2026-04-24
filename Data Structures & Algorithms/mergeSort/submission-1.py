# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        """print("left : ")
        for pair in pairs:
            print(pair.key)
        print ("\n")"""
        if len(pairs) <= 1:
            return pairs

        mid = ( int(len(pairs) / 2) if len(pairs) % 2 else (int(len(pairs) / 2) - 1) )
        #print ("mid left: ", mid)
        #print(pairs[0:mid + 1])
        left = self.mergeSort(pairs[0 : mid + 1])
        print ("length : ", len(pairs))
        print ("mid is now : ", mid)
        print ("left : ", 0 ,"to", mid)
        right = self.mergeSort(pairs[mid + 1 : len(pairs)])
        print ("length : ", len(pairs))
        print ("mid is now : ", mid)
        print ("right : ", mid + 1 , "to", len(pairs)-1)
        pairs = self.merge(left, right)
        #print(pairs)
        return pairs
    
    def merge(self, left : List[Pair], right : List[Pair]):
        #print(left[0].key , " , " , right[0].key)
        total_length = len(left) + len(right)
        whole = []
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                whole.append(left[i])
                i += 1
            else:
                whole.append(right[j])
                j += 1
            k += 1
        print("k:", k)
        while k < total_length:
            if i < len(left):
                whole.append(left[i])
                i += 1
            elif j < len(right) :
                whole.append(right[j])
                j += 1
            k += 1
        return whole