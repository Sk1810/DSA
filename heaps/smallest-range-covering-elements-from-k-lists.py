class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []
        max_value = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i][0],i,0))
            max_value = max(nums[i][0],max_value)

        best_range = [float('-inf'),float('inf')]

        while True:

            min_value,row,col = heapq.heappop(heap)

            if max_value - min_value < best_range[1]-best_range[0]:
                best_range = [min_value,max_value]
            

            if col+1 == len(nums[row]):
                break

            value = nums[row][col+1]
            max_value = max(max_value,value)    

            heapq.heappush(heap,(value,row,col+1))

        return best_range    