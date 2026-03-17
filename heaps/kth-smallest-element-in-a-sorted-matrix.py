class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = []
        rows = len(points)
        cols = len(points[0])

        for x, y in points:
          dist = x*x + y*y
        
          heapq.heappush(heap, (-dist, x, y))

        if len(heap)> k:
                heapq.heappop(heap)


        result = []

        for item in heap:
            _,x,y = item
            result.append([x,y])

        return result    
