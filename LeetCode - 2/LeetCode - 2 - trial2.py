class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev

    def convertInt(self, head: ListNode) -> int:
        result, node = [], head

        while node:
            result.append(node.val)
            node = node.next

        return int(''.join(str(e) for e in result))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = self.convertInt(self.reverseList(l1))
        val2 = self.convertInt(self.reverseList(l2))

        sum_str = str(val1 + val2)

        prev: ListNode = None
        for c in sum_str:
            node = ListNode(c)
            node.next = prev
            prev = node

        return node