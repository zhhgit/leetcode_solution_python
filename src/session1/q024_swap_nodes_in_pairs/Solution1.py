from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        keep = head.next.next
        second = head.next
        head.next = self.swapPairs(keep)
        second.next = head
        return second

s = Solution1()
arr = [1,2,3,4,5]
listBuilder = ListBuilder(arr)
PrintUtil.print_list(s.swapPairs(listBuilder.get_head()))
