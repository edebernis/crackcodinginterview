#!/usr/bin/python3


class NodeState:
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __eq__(self, node):
        if node is None:
            return False
        return self.val == node.val

    def __hash__(self):
        return hash(self.val)

    def __str__(self):
        n = self.is_circular()
        if n:
            cur = self
            res = ''
            not_in_loop_yet = True
            while cur != n or not_in_loop_yet:
                if cur == n:
                    not_in_loop_yet = False
                res += ', %s' % cur.val
                cur = cur.next
            res += ', %s' % cur.val
            return res[2:]

        return '%s%s' % (self.val, ',%s' % str(self.next) if self.next else '')

    def is_circular(self):
        """Returns node at the beginning of the loop"""
        l1 = l2 = self
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
            if l1 == l2:
                break

        if not l2 or not l2.next:
            return False

        l1 = self
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1
