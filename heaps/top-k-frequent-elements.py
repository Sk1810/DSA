class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = {}
        heap = []

        for n in nums:
            freq[n] = freq.get(n,0)+1


        for key,value in freq.items():
            heapq.heappush(heap,(value,key))

            if len(heap)>k:
                heapq.heappop(heap)


        result = []

        for item in heap:
            _,x = item
            result.append(x)

    
        return result               