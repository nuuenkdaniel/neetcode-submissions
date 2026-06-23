# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        seen_dict = {}
        seen_dict[head] = True
        curr = head
        while curr.next:
            curr = curr.next
            if seen_dict.get(curr): return True
            else: seen_dict[curr] = True

        return False
