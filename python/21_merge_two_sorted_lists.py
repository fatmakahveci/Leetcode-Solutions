# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in (list1, list2):
            return list1 or list2
        dummy = cur = ListNode()
        while list1 and list2:
            cur.next = list1
            if list1.val < list2.val:
                list1 = list1.next
            else:
                tmp = list2.next
                cur.next = list2
                list2.next = list1
                list2 = tmp
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next 
