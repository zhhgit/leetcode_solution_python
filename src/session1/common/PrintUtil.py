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

    @staticmethod
    def print_2d_num_array(matrix):
        rowLen = len(matrix)
        columnLen = len(matrix[0])
        for i in range(0,rowLen):
            for j in range(0,columnLen):
                print(matrix[i][j],end=" ")
            print("")
