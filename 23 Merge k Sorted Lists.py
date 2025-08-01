# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        lists_filtered:List[Optional[ListNode]] = []
        for list in lists:
            if not list:
                continue
            lists_filtered.append(list)
        lists = lists_filtered
        if not lists:
            return None
        
        lists.sort(key=lambda x:x.val)
        first_node = lists.pop(0)
        if first_node.next:
            lists.append(first_node.next)
        curr_el = first_node
        while lists:
            lists.sort(key=lambda x:x.val)
            next_el = lists.pop(0)
            if next_el.next:
                lists.append(next_el.next)
            curr_el.next = next_el
            curr_el = next_el
        
        return first_node