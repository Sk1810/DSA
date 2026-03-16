class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        i = 0

        while i < len(nums):
    
            while len(heap)>k:
                    heapq.heappop(heap)


            heapq.heappush(heap,nums[i])
            i = i+1

        while len(heap)>k:
                    heapq.heappop(heap)

        return heapq.heappop(heap)
    
    
    #could have done like
    
    import heapq

class Solution:
    def kthLargestElementInAnArray(self, nums, k):

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]