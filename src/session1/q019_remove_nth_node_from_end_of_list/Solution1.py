from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode

class Solution1:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        fakeHead = ListNode(0)
        fakeHead.next = head
        fast = fakeHead
        slow = fakeHead
        for i in range(0,n):
            fast = fast.next
        while fast is not None and fast.next is not None \
            and slow is not None and slow.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return fakeHead.next

s = Solution1()
arr = [1,2,3,4,5]
nArr = [1,2,3,4,5]
for i in range(0,len(nArr)):
    listBuilder = ListBuilder(arr)
    PrintUtil.print_list(s.removeNthFromEnd(listBuilder.get_head(), nArr[i]))
    print("-----------------")