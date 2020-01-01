#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse_in_order(self):
        if self.left:
            yield from self.left.traverse_in_order()

        yield self.val

        if self.right:
            yield from self.right.traverse_in_order()

    def traverse_pre_order(self):
        yield self.val

        if self.left:
            yield from self.left.traverse_pre_order()
        if self.right:
            yield from self.right.traverse_pre_order()

    def traverse_post_order(self):
        if self.left:
            yield from self.left.traverse_post_order()
        if self.right:
            yield from self.right.traverse_post_order()

        yield self.val

    def is_balanced(self):
        pass


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def dfs(self, seen=None):
        if seen is None:
            seen = {self}
        else:
            seen.add(self)

        yield self.val
        for n in self.neighbors:
            if n not in seen:
                yield from n.dfs(seen=seen)

    def bfs(self):
        seen = set()
        queue = [self]
        while queue:
            n = queue.pop()
            yield n.val
            seen.add(n)

            for neigh in n.neighbors:
                if neigh not in seen:
                    queue.insert(0, neigh)
