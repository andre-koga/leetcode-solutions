/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode rootResult = new ListNode(0, new ListNode());
        ListNode currResult = rootResult;

        int addOne = 0;
        do {
            int n1 = l1 != null ? l1.val : 0;
            int n2 = l2 != null ? l2.val : 0;
            int digit = (n1 + n2 + addOne) % 10;
            addOne = (n1 + n2 + addOne) / 10;

            currResult.next = new ListNode(digit);

            currResult = currResult.next;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        } while (l1 != null || l2 != null || addOne != 0);

        return rootResult.next;
    }
}