# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        list3 = None
        if list1.val <= list2.val:
            list3 = list1
            list1 = list1.next
        else:
            list3 = list2
            list2 = list2.next

        head = list3

        while True:
            if list1 == None:
                head.next = list2
                return list3
            elif list2 == None:
                head.next = list1
                return list3
            
            # neither list1 or list2 are null
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
    
        return list3