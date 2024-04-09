# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        left = 0
        leftHead = head
        right = 0
        rightHead = head
        while True:
            # reached end - leftHead is one before the node to be removed
            if rightHead.next == None:
                if right == n - 1:
                    return head.next

                leftHead.next = leftHead.next.next
                return head
            # didn't reach end - increase right, check if should increase left
            else:
                rightHead = rightHead.next
                if right - left >= n:
                    leftHead = leftHead.next
                    left += 1
                right += 1