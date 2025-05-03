# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current = head
        total_str = ""
        while current:
            total_str += str(current.val)
            current = current.next
        return int(total_str,2)
        