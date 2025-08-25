# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

#using stack
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <2:
            return head
        
        tail = None
        new_head = None
        while head:
            count = 0
            stack = []
            while count < k and head:
                stack.append(head)
                head = head.next
                count+=1
            
            if count == k:
                if not tail:
                    tail = stack.pop()
                    new_head = tail
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
                tail.next = None
            
            else:
                if not tail:
                    tail = stack.pop(0)
                    new_head = tail
                for item in stack:
                    tail.next = item
                    tail = item
                
        return new_head
