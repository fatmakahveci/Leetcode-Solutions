# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            first_node, second_node = head, head.next
            
            first_node.next = self.swapPairs(second_node.next)
            second_node.next = first_node

            return second_node
        return head
