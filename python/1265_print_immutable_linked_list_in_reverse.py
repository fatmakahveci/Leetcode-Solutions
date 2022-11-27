# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        '''
        head -> 1 -> 2 -> 3 -> 4
        
        4 -> 3 -> 2 -> 1
        '''
        if head.getNext():
            self.printLinkedListInReverse(head.getNext())
        head.printValue()
