# runtime: O(n) (its a singly linked list. we can't do better than that)
# space: O(1) (no extras required)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we gotta make 2 operations:
        # cut the list in the middle
        # attach the second half to the first half

        # then return the head, which is the beginning of the second half

        if head == None or head.next == None or k == 0:
            return head

        size = 1
        leftHead, rightHead = head, head

        for i in range(k):
            if rightHead.next != None:
                rightHead = rightHead.next
                size += 1
            else:
                # the list is smaller than we expected. so we redo with mod of k
                print(size)
                return self.rotateRight(head, k % size)

        # else we know we can just move both left head and right head until end. ggs.
        while rightHead.next != None:
            rightHead = rightHead.next
            leftHead = leftHead.next
        
        newHead = leftHead.next
        leftHead.next = None
        rightHead.next = head

        return newHead