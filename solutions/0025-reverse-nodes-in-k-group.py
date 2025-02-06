# beats 100% in terms of time complexity!

# couldn't solve this one just by myself, ended up seeing some very small hints
# but got 100%!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevGroup = ListNode(0, None) # starts as a dummy
        headToReturn = None

        while True:
            lookAhead = head

            # move ahead k spots to see if we have enough to perform another flip
            for i in range(k):
                if i == k - 1 and headToReturn == None:
                    headToReturn = lookAhead

                # interrupted early, don't touch this last group
                if lookAhead == None:
                    prevGroup.next = head
                    return headToReturn

                lookAhead = lookAhead.next
                
            prevGroup = self.flipFirstK(head, k, prevGroup)
            head = lookAhead

    def flipFirstK(self, head, k, prevGroup) -> ListNode:
        thisGroup = head # we return the original head of this group
        prev = None
        curr = head
        nxt = None
        i = 0
        while curr and i < k:
            i += 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # localPrev = prev
        # for i in range(k):
            # print(localPrev.val)
            # localPrev = localPrev.next

        prevGroup.next = prev

        # print(thisGroup)
        return thisGroup