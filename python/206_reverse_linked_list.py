# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        
        1 -> 2 -> 3 -> 4 -> 5 -> N
        1 -> 2 -> 3 -> 4 <- 5
                       |
                       v
                       N
                       
        N <- 1 <- 2 <- 3 <- 4 <- 5
        '''
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
