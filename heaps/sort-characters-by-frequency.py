import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        result = []

        while heap:
            count, ch = heapq.heappop(heap)
            count = -count

            result.extend([ch] * count)

        return "".join(result)