# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        deleted_elements = set(nums)
        dummy = ListNode()
        dummy.next = head
        current=dummy
        while current and current.next:
            if current.next.val in deleted_elements:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next