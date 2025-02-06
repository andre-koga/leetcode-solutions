# extremely slow solution. who cares.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge the first two. repeat.
        n = len(lists)

        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif lists[-1] == None:
            lists.pop()
            return self.mergeKLists(lists)
        elif lists[-2] == None:
            lists.pop(-2)
            return self.mergeKLists(lists)
        else:
            p1 = lists.pop()
            p2 = lists.pop()
            final = None

            if p1.val < p2.val:
                final = p1
                p1 = p1.next
            else:
                final = p2
                p2 = p2.next

            p = final

            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                else:
                    p.next = p2
                    p2 = p2.next
                    p = p.next

            if p1:
                p.next = p1
            elif p2:
                p.next = p2

            lists.append(final)

            return self.mergeKLists(lists)