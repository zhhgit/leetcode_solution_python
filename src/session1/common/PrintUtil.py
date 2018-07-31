class PrintUtil:

    @staticmethod
    def print_list(head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next

    @staticmethod
    def print_num_array(arr):
        for i in range(0,len(arr)):
            print(arr[i],end=' ')