class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        
    def push(self, val: int) -> None:
        nums = self.heap
        nums.append(val)
        i = len(nums) - 1
        while i > 1:
            if nums[i] < nums[i // 2]:
                nums[i // 2], nums[i] = nums[i], nums[i // 2]
            else:
                break
            i = i // 2
        
    def pop(self) -> int:
        nums = self.heap
        #print("length of nums is : ", len(self.heap))
        if len(nums) == 1:
            return -1
        if len(nums) == 2:
            return nums.pop()
        
        popped = nums[1]
        nums[1] = nums.pop()
        #print("popped element is : ", popped)
        #print("Heap after popping is : ", nums)
        i = 1
        while 2 * i <= len(nums) - 1:
            if 2 * i + 1 <= len(nums) - 1 and nums[2 * i + 1] <= nums[2 * i] and nums[2 * i + 1] < nums[i]:
                nums[2 * i + 1], nums[i] = nums[i], nums[2 * i + 1]
                i = 2 * i + 1
            elif nums[2 * i] < nums[i]:
                nums[2 * i], nums[i] = nums[i], nums[2 * i]
                i = 2 * i
            else:
                break
        print("Heap after popping and bubbling is : ", nums)
        return popped

    def top(self) -> int:
        
        return self.heap[1] if len(self.heap) >= 2 else -1

    def heapify(self, nums: List[int]) -> None:
        #self.heap = self.heap + nums
        #nums = self.heap
        nums1 = [0]
        for x in nums:
            nums1.append(x)
        self.heap = nums1
        nums = nums1
        i = (len(nums) - 1) // 2
        while i >= 1:
            curr = i
            while 2 * curr <= len(nums) - 1:
                if 2 * curr + 1 <= len(nums) - 1 and nums[2 * curr + 1] <= nums[2 * curr] and nums[2 * curr + 1] < nums[curr]:
                    nums[2 * curr + 1] , nums[curr] = nums[curr], nums[2 * curr + 1]
                    curr = 2 * curr + 1
                elif nums[2 * curr] < nums[curr]:
                    nums[2 * curr], nums[curr] = nums[curr], nums[2 * curr]
                    curr = 2 * curr
                else:
                    break
            i -= 1
        print (nums)













