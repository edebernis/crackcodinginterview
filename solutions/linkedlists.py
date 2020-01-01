#!/usr/bin/python3

from utils import Node


class Q2_1:
    """Remove duplicated from unsorted linked list"""
    tests = None

    def __init__(self):
        self.reset_tests()

    def reset_tests(self):
        l1 = Node(2)
        l1.next = Node(2)
        l2 = Node(2)
        l3 = Node(1)
        l3.next = Node(2)
        l3.next.next = Node(2)
        l4 = Node(1)
        l4.next = Node(2)
        Q2_1.tests = {
            l1: l2,
            l3: l4
        }

    def v1(self, l):
        values = {l.val}
        previous = l
        while previous.next:
            cur = previous.next
            if cur.val in values:
                previous.next = cur.next
            else:
                values.add(cur.val)
                previous = cur
        return l

    def v2(self, l):
        self.reset_tests()
        previous = l
        while previous.next:
            cur = previous.next
            cur2 = l
            dup = False
            while (cur != cur2) and not dup:
                dup = cur.val == cur2.val
                cur2 = cur2.next
            if dup:
                previous.next = cur.next
            else:
                previous = cur
        return l


class Q2_2:
    tests = None

    def __init__(self):
        l1 = Node(1)
        l1.next = Node(2)
        l1.next.next = Node(3)
        l1.next.next.next = Node(4)
        l1.next.next.next.next = Node(5)
        Q2_2.tests = {
            (l1, 1): 4,
            (l1, 2): 3,
            (l1, 3): 2
        }

    def v1(self, l, n):
        values = []
        cur = l
        while cur.next:
            values.append(cur.val)
            cur = cur.next
        return values[-n]

    def v2(self, l, n):
        cur = l
        for _ in range(n):
            cur = cur.next
        if not cur.next:
            return l.val

        return self.v2(l.next, n)

    def v3(self, l, n):
        p1 = l
        p2 = l
        for _ in range(n):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        return p1.val


class Q2_3:
    tests = None

    def __init__(self):
        self.reset_tests()

    def reset_tests(self):
        l1 = Node(1)
        l1.next = Node(2)
        l1.next.next = Node(3)
        l2 = Node(1)
        l2.next = Node(3)
        Q2_3.tests = {
            l1.next: True
        }

    def v1(self, node):
        if not node.next:
            return False

        node.val = node.next.val
        node.next = node.next.next
        return True


class Q2_4:
    tests = None

    def __init__(self):
        l1 = Node(3)
        l1.next = Node(1)
        l1.next.next = Node(5)
        l2 = Node(5)
        l2.next = Node(9)
        l2.next.next = Node(2)
        l3 = Node(8)
        l3.next = Node(0)
        l3.next.next = Node(8)
        Q2_4.tests = {
            (l1, l2): l3
        }

    def v1(self, l1, l2, carry=0):
        if l1 is None and l2 is None:
            return Node(1) if carry else None

        s = carry
        if l1 is not None:
            s += l1.val
        if l2 is not None:
            s += l2.val

        res = Node(s % 10)
        res.next = self.v1(l1.next if l1 else None,
                           l2.next if l2 else None,
                           carry=int(s >= 10))
        return res


class Q2_5:
    tests = None

    def __init__(self):
        l1 = Node(1)
        l1.next = Node(2)
        l1.next.next = Node(3)
        l1.next.next.next = Node(4)
        l1.next.next.next.next = l1.next
        Q2_5.tests = {
            l1: l1.next
        }

    def v1(self, l):
        print(list(Q2_5.tests.keys())[0])
        l1 = l
        l2 = l

        # Meeting point
        while l2.next:
            l1 = l1.next
            l2 = l2.next.next
            if l1 == l2:
                break

        # Check that meeting point exists
        if not l2.next:
            return False

        # Head and meeting point are each at k steps from loop start
        # They must meet at loop start
        l1 = l
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l2
