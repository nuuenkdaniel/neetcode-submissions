# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        distance = 1
        prev = None
        curr = head
        tail = head
        while tail.next:
            if distance == n:
                prev = curr
                curr = curr.next
            else:
                distance += 1
            tail = tail.next

        if prev == None: return curr.next
        else: prev.next = curr.next
        return head

