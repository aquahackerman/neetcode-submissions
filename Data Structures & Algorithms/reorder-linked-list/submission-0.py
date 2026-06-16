# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        iterator = head
        length = 0
        while iterator is not None:
            length += 1
            iterator = iterator.next
        iterator = head
        for i in range(length//2):
            
            print(iterator.val)
            iterator = iterator.next
        reverse_n = iterator.next
        iterator.next = None

        prev, curr = None, reverse_n
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        reverse_n = prev

        oghead = head
        k = 0
        temp = head.next
        while reverse_n and head:
            if k % 2 == 0:
                temp = head.next
                head.next = reverse_n
                head = temp
            else:
                temp2 = reverse_n.next
                reverse_n.next = temp
                reverse_n = temp2
            k+= 1
            if k == length:
                return
        else:
            if reverse_n:
                head.next = reverse_n
            return
        
        
        