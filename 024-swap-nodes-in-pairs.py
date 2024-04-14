# This solution is very bad. But who cares. One of the cleanest solutions
# I saw in the submissions is as follows by "meurudesu" (not my solution):
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         temp = head.next
#         head.next = self.swapPairs(head.next.next)
#         temp.next = head
#         return temp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 or 1
        if head == None or head.next == None:
            return head

        # 2 or more - flip the first two
        first = head
        second = head.next
        third = head.next.next
        head = second
        head.next = first
        first.next = third

        prev = first
        pointer = third

        while pointer != None:
            if pointer.next == None:
                # nothing else to flip
                return head

            first = pointer
            second = pointer.next
            third = pointer.next.next
            prev.next = second
            second.next = first
            first.next = third

            pointer = third
            prev = first

        return head
        