# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        cur = head
        self.length = 0
        while cur:
            cur = cur.next
            self.length += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        i = random.randint(0, self.length - 1)
        cur = self.head
        while i and cur:
            cur = cur.next
            i -= 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
