"""__Pronlem Statement__:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1 or list2):
                return None
        op = ListNode()
        opptr = op
        while list1 and list2:
            if(list1.val < list2.val):
                opptr.val = list1.val
                list1 = list1.next
            else:
                opptr.val = list2.val
                list2 = list2.next
            if not(list1 or list2):
                return op
            opptr.next = ListNode()
            opptr = opptr.next
        while list1:
            opptr.val = list1.val
            list1 = list1.next
            if not(list1 or list2):
                return op
            opptr.next = ListNode()
            opptr = opptr.next
        while list2:
            opptr.val = list2.val
            list2 = list2.next
            if not(list1 or list2):
                return op
            opptr.next = ListNode()
            opptr = opptr.next
        opptr = None
        return op

# Improved Solution : 
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1 or list2):
                return None
        if (list1 or list2) and not(list1 and list2):
            return list1 if list1 else list2
        op = ListNode()
        opptr = op
        while list1 and list2:
            if(list1.val < list2.val):
                opptr.val = list1.val
                list1 = list1.next
            else:
                opptr.val = list2.val
                list2 = list2.next
            if list1 and list2:
                opptr.next = ListNode()
                opptr = opptr.next
        if list1 or list2:
            opptr.next = list1 if list1 else list2
        return op