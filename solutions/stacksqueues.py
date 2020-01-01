#!/usr/bin/env python3

from solutions.utils import Node


class Stack:
    """Top -> Node -> Node -> Node"""
    def __init__(self):
        self.top = None
        self.count = 0

    def __str__(self):
        s = ''
        cur = self.top
        while cur:
            s += '->{}'.format(cur.val)
            cur = cur.next
        return s[2:] if s else 'empty'

    def pop(self):
        if not self.top:
            return

        res = self.top.val
        self.top = self.top.next
        self.count -= 1
        return res

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.count += 1

    def peek(self):
        return self.top.val if self.top else None

    def is_empty(self):
        return self.top is None

    def sort(self):
        tmp = Stack()
        while not self.is_empty():
            e = self.pop()

            while not tmp.is_empty() and tmp.peek() < e:
                self.push(tmp.pop())

            tmp.push(e)

        while not tmp.is_empty():
            self.push(tmp.pop())


class Queue:
    """Front -> Node -> Node -> Back"""
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, val):
        node = Node(val)
        if self.front:
            self.back.next = node
            self.back = node
        else:
            self.back = node
            self.front = self.back

    def dequeue(self):
        if not self.front:
            return

        res = self.front.val
        self.front = self.front.next
        return res


class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def _add_stack(self):
        stack = Stack()
        self.stacks.append(stack)
        return stack

    def _get_stack(self):
        if not self.stacks:
            return

        return self.stacks[-1]

    def _remove_stack(self):
        self.stacks.pop()

    def push(self, val):
        stack = self._get_stack()

        if not stack or stack.count == self.threshold:
            stack = self._add_stack()

        stack.push(val)

    def pop(self):
        stack = self._get_stack()
        if not stack:
            return

        if stack.is_empty():
            self._remove_stack()
            stack = self._get_stack()
            if not stack:
                return

        return stack.pop()

    def pop_at(self, index):
        """TODO"""
        pass


class Disk:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size


class Rod:
    def __init__(self):
        self.stack = Stack()

    def __str__(self):
        return str(self.stack)

    def move_disk(self, dest_rod):
        if self.stack.is_empty():
            raise Exception('Empty rod')

        disk = self.stack.pop()
        dest_rod.push(disk)

    def push(self, disk):
        peek = self.stack.peek()
        if peek and peek < disk:
            raise Exception('Invalid push. Disk size is too big')

        self.stack.push(disk)

    def count(self):
        return self.stack.count


class TowersOfHanoi:
    def __init__(self):
        self.rods = None

    def __str__(self):
        s = []
        for i, rod in enumerate(self.rods, start=1):
            s.append('Rod {} : {}'.format(i, rod))
        return '\n'.join(s)

    def setup(self, total_disks):
        if total_disks < 2:
            raise Exception('Total disks must be at least 2')

        self._init_rods()
        self._init_disks(total_disks)

    def _init_rods(self):
        self.rods = []
        for _ in range(3):
            self.rods.append(Rod())

    def _init_disks(self, total_disks):
        for size in range(total_disks, 0, -1):
            disk = Disk(size)
            self.rods[0].push(disk)

    def _move(self, n, from_rod, to_rod, tmp_rod):
        if n == 2:
            from_rod.move_disk(tmp_rod)
            from_rod.move_disk(to_rod)
            tmp_rod.move_disk(to_rod)
            return

        self._move(n-1,
                   from_rod=from_rod,
                   to_rod=tmp_rod,
                   tmp_rod=to_rod)
        from_rod.move_disk(to_rod)
        self._move(n-1,
                   from_rod=tmp_rod,
                   to_rod=to_rod,
                   tmp_rod=from_rod)

    def solve(self):
        self._move(self.rods[0].count(),
                   from_rod=self.rods[0],
                   to_rod=self.rods[2],
                   tmp_rod=self.rods[1])


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, val):
        self.s1.push(val)

    def pop(self):
        if not self.s2.is_empty():
            return self.s2.pop()

        while True:
            e = self.s1.pop()
            if self.s1.is_empty():
                return e
            self.s2.push(e)

    def peek(self):
        if not self.s2.is_empty():
            return self.s2.peek()

        while not self.s1.is_empty():
            e = self.s1.pop()
            self.s2.push(e)

        return self.s2.peek()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()
