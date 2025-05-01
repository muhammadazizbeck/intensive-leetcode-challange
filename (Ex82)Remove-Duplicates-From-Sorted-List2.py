# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val==current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy.next
