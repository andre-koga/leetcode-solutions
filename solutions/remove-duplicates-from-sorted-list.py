# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the first element always stays.
        # we track the current element as X and set its next to null
        # then we go to the next element. if it is the same, we skip
        # we keep skipping until we find a different element Y
        # then we just connect X to Y.
        # if we reach the end, X is already pointing to null so all is good
        # we just return the head now.

        if head == None or head.next == None:
            return head

        x = head
        y = head.next
        x.next = None

        while y:
            if x.val == y.val:
                y = y.next
            else:
                x.next = y
                x = y
                y = y.next
                x.next = None
                

        return head
