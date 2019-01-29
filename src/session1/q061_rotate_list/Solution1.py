from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def rotateRight(self, head, k):
        listLen = self.getListLen(head)
        if head is None:
            return None
        realK = k % listLen
        if realK == 0:
            return head
        moveStep = listLen - realK - 1
        curr = head
        for i in range(0,moveStep):
            curr = curr.next
        keep = curr.next
        curr.next = None
        curr = keep
        while curr.next is not None:
            curr = curr.next
        curr.next = head
        return keep

    def getListLen(self, head):
        ret = 1
        curr= head
        if head is None:
            return 0
        while curr.next is not None:
            curr = curr.next
            ret = ret + 1
        return ret

s = Solution1()
arr = [1,2,3,4,5]
kArr = [1,2,3,4,5,6]
for i in range(0,len(kArr)):
    listBuilder = ListBuilder(arr)
    PrintUtil.print_list(s.rotateRight(listBuilder.get_head(),kArr[i]))
    print("----------------")



