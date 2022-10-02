# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
        '''
        dummy = Node
        list1 -> 1 -> 4 -> 5
                 ^
                 |
                curr
                 
        list2 -> 1 -> 3 -> 4
        
        '''
        cur = ListNode()
        dummy = cur
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = None
        for l in lists:
            dummy = self.merge2Lists(dummy, l)

        return dummy
