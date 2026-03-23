import heapq
import itertools

class Solution:
    def mergeKLists(self, lists):
        heap = []
        unique = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, unique, node))
                unique += 1
        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val,unique, node.next))
                unique += 1

        return dummy.next