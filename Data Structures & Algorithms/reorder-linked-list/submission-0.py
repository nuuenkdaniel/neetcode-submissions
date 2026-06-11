# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None: return

        # Find midpoint list
        mid = head
        tail = head.next
        while tail != None and tail.next != None:
            mid = mid.next
            tail = tail.next.next

        # Reverse list after midpoint
        prev = None
        second = mid.next
        mid.next = None
        while second != None:
            old_next = second.next
            second.next = prev
            prev = second
            second = old_next
        second = prev
        
        # Merge to lists
        while second != None:
            temp_next1, temp_next2 = head.next, second.next
            head.next = second
            second.next = temp_next1
            head = temp_next1
            second = temp_next2

