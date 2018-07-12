from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode
import heapq

class Solution2:
    def mergeKLists(self,lists):
        fakeHead = ListNode(0)
        curr = fakeHead
        heap = []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return fakeHead.next

s = Solution2()
numsArr = [[1,4,5],[1,3,4],[2,6]]
lists = []
for nums in numsArr:
    listBuilder = ListBuilder(nums)
    lists.append(listBuilder.get_head())
PrintUtil.print_list(s.mergeKLists(lists))