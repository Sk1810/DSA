import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes):
        freq = Counter(barcodes)

        # max heap (negative values)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        result = []
        prev = (0, None)

        while heap:
            count, num = heapq.heappop(heap)

            result.append(num)

            # push previous back if still available
            if prev[0] < 0:
                heapq.heappush(heap, prev)

            # decrease count
            count += 1  # since negative

            prev = (count, num)

        return result