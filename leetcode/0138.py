"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        dic = {}
        dic[None] = None
        res_head = Node(head.val, None, None)
        dic[head] = res_head
        p, q = head, res_head
        while p.next != None:
            q.next = Node(p.next.val, None, None)
            dic[p.next] = q.next
            p = p.next
            q = q.next
        p, q = head, res_head
        while p != None:
            q.random = dic[p.random]
            p = p.next
            q = q.next
        return res_head
        
