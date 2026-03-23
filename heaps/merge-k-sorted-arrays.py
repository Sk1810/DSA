class Solution:
    def mergeArrays(self, mat):
        # Code here
        
        row = 0
        heap = []
        
        for rows in mat:
            heapq.heappush(heap,(mat[row][0],row,0))
            row = row+1
            
        result = []
        
        while heap:
            val,ro,col = heapq.heappop(heap)
            
            result.append(val)
            
            if col + 1 < len(mat[ro]):
                heapq.heappush(heap, (mat[ro][col + 1], ro, col + 1))
                
        
        
        return result        
        