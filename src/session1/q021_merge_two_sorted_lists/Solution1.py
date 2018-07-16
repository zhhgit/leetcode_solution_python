from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode

class Solution1:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            fakeHead = ListNode(0)
            curr = fakeHead
            self.backTracking(curr,l1,l2)
            return fakeHead.next

    def backTracking(self,curr,l1,l2):
        if l1 is None and l2 is None:
            curr.next = None
        elif l1 is None:
            curr.next = l2
        elif l2 is None:
            curr.next = l1
        else:
            if l1.val <= l2.val:
                keep = l1.next
                l1.next = None
                curr.next = l1
                l1 = keep
            else:
                keep = l2.next
                l2.next = None
                curr.next = l2
                l2 = keep
            curr = curr.next
            self.backTracking(curr,l1,l2)

s = Solution1()
nums1 = [1,2,4]
nums2 = [1,3,4]
listBuilder1 = ListBuilder(nums1)
listBuilder2 = ListBuilder(nums2)
listRet = s.mergeTwoLists(listBuilder1.get_head(),listBuilder2.get_head())
PrintUtil.print_list(listRet)

