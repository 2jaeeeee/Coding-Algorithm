class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next, node = head, head
        while node and node.next:
            #바꿀 pair 저장
            pair = node.next
            node.next, pair.next = pair.next, node

            #전 노드의 next 변경
            prev.next = pair

            prev = node
            node = node.next

        return root.next