class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        up = 0
        head = node = ListNode()
        while l1 and l2:
            sum = l1.val + l2.val + up
            node.next, up = ListNode(sum % 10), sum // 10

            l1, l2, node = l1.next, l2.next, node.next

        while l1:
            sum = l1.val + up
            node.next, up = ListNode(sum % 10), sum // 10
            l1, node = l1.next, node.next
        while l2:
            sum = l2.val + up
            node.next, up = ListNode(sum % 10), sum // 10
            l2, node = l2.next, node.next

        if up > 0:
            node.next = ListNode(up)

        return head.next