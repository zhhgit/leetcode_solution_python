from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode
from src.session1.common.ListBuilder import ListBuilder


class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        len1 = self.get_list_len(l1)
        len2 = self.get_list_len(l2)
        if len1 >= len2:
            l1new = l1
            l2new = self.extend_list(l2,len1-len2)
        else:
            l1new = self.extend_list(l1,len2 - len1)
            l2new = l2
        return self.add_same_len(l1new,l2new)

    #链表长度
    def get_list_len(self,l1):
        ret = 0
        curr = l1
        while curr is not None:
            ret += 1
            curr = curr.next
        return ret

    #用0扩展两个链表到等长
    def extend_list(self,l1,len):
        if len == 0:
            return l1
        curr = l1
        while (curr is not None) and (curr.next is not None):
            curr = curr.next
        for i in range(len):
            curr.next = ListNode(0)
            curr = curr.next
        return l1

    #两个等长链表相加
    def add_same_len(self,l1,l2):
        increase = 0
        fakeHead = ListNode(0)
        curr = fakeHead
        while (l1 is not None) and (l2 is not None):
            sum = l1.val + l2.val + increase
            if sum >= 10:
                increase = sum // 10
                value = sum % 10
            else:
                value = sum
                increase = 0
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if increase == 1:
            curr.next = ListNode(1)
        return fakeHead.next

s = Solution1()
nums1 = [9,1,6]
nums2 = [0]
listBuilder1 = ListBuilder(nums1)
l1 = listBuilder1.get_head()
listBuilder2 = ListBuilder(nums2)
l2 = listBuilder2.get_head()
PrintUtil.print_list(s.addTwoNumbers(l1,l2))