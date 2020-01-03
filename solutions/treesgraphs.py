#!/usr/bin/env python3

from collections import OrderedDict
from solutions.utils import NodeState


class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.to_dict())

    def neighbors(self):
        if self.left:
            yield self.left
        if self.right:
            yield self.right

    def to_dict(self):
        d = OrderedDict({self.val: OrderedDict()})
        if self.left:
            d[self.val].update(self.left.to_dict())
        if self.right:
            d[self.val].update(self.right.to_dict())
        return d

    def traverse_in_order(self):
        if self.left:
            yield from self.left.traverse_in_order()

        yield self.val

        if self.right:
            yield from self.right.traverse_in_order()

    def successor_in_order(self):
        if self.right:
            cur = self.right
            while cur.left:
                cur = cur.left
            return cur

        cur = self
        while cur.parent and cur.parent.left != cur:
            cur = cur.parent
        return cur

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

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max([left_height, right_height])

    def is_balanced(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return abs(left_height - right_height) < 2


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def dfs(self, seen):
        seen.add(self)
        yield self.val

        for n in self.neighbors:
            if n not in seen:
                yield from n.dfs(seen=seen)

    def dfs_iterative(self):
        seen = set()
        stack = [self]
        while stack:
            n = stack.pop()
            if n in seen:
                continue

            yield n.val
            seen.add(n)

            for neigh in n.neighbors:
                stack.append(neigh)

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


def exists_route(node1, node2):
    seen = set()
    queue = [node1]
    while queue:
        n = queue.pop()
        if n == node2:
            return True
        seen.add(n)

        for neigh in n.neighbors:
            if neigh not in seen:
                queue.insert(0, neigh)
    return False


def get_binary_search_tree(l, parent=None):
    if not l:
        return None
    if len(l) == 1:
        return TreeNode(l[0], parent=parent)

    half_index = int(len(l) / 2)
    root = TreeNode(l[half_index], parent=parent)
    root.left = get_binary_search_tree(l[:half_index], parent=root)
    root.right = get_binary_search_tree(l[half_index+1:], parent=root)
    return root


def get_linked_lists_by_depth(tree):
    level = 0
    result = [[tree]]

    while True:
        level_list = []
        for n in result[level]:
            if n.left:
                level_list.append(n.left)
            if n.right:
                level_list.append(n.right)

        if level_list:
            result.append(level_list)
            level += 1
        else:
            break

    return result


def topological_sort_kahn(graph):
    result = []

    # Get all start nodes with no incoming edges
    stack = graph.get_nodes_without_incoming_edges()

    # For each node, remove edges to outgoing nodes. If outgoing node
    # has no more incoming edges, add node to stack
    while stack:
        n = stack.pop()
        result.append(n)
        for e, m in n.outgoing():
            graph.remove_edge(e)
            if not m.incoming():
                stack.add(m)

    # If graph has still edges, not a DAG.
    if graph.has_edges():
        raise Exception('Not a directed acyclic graph')

    return result


def topological_sort_dfs(graph):
    def visit(node, result):
        if node.state == NodeState.VISITING:
            raise Exception('Not a DAG')
        if node.state == NodeState.VISITED:
            return

        node.state = NodeState.VISITING

        # Visit its neighbors
        for m in n.neighbors:
            visit(m, result)

        node.state = NodeState.VISITED
        # Add node to head
        result.insert(0, node)

    # Get unvisited nodes and visit them until no more unvisited nodes
    result = []
    while graph.unvisited_nodes():
        n = graph.unvisited_nodes().pop()
        visit(n, result)

    return result


def dijkstra(start, dest):
    # Get set of unvisited nodes
    stack = [start]
    start.distance = 0

    while True:
        if not stack:
            raise Exception('Destination not found')

        # Get unvisited node with min distance from start
        lengths = [(node, node.length) for node in stack]
        n = sorted(lengths, key=lambda x: x[1])[0]

        # If next node with min distance is dest, stop here
        if n == dest:
            return dest.distance

        # Get all unvisited neighbors
        for e, m in n.outgoing():
            if m.state == NodeState.VISITED:
                continue
            m.distance = min(m.distance, n.distance + e.length)
            stack.append(m)

        n.state = NodeState.VISITED
        stack.remove(n)


def get_next_node(node):
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur

    cur = node
    while cur.parent and cur.parent.left != cur:
        cur = cur.parent
    return cur


def get_first_common_ancestor(node1, node2):
    if node1 is None or node2 is None:
        return None

    if node1 == node2:
        return node1.parent

    if not node1.parent or not node2.parent:
        return None

    p1 = node1.parent
    p2 = node2.parent
    parents1 = set()
    parents2 = set()
    while p1 or p2:
        parents1.add(p1)
        parents2.add(p2)

        if p1 in parents2:
            return p1
        if p2 in parents1:
            return p2

        if p1.parent:
            p1 = p1.parent
        if p2.parent:
            p2 = p2.parent

    return p1


def is_subtree(tree1, tree2):
    if tree1 is None:
        return False
    if tree2 is None:
        return True

    if tree1.val == tree2.val:
        if match_tree(tree1, tree2):
            return True

    return is_subtree(tree1.left, tree2) or is_subtree(tree1.right, tree2)


def match_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False

    if tree1.val != tree2.val:
        return False

    return match_tree(tree1.left, tree2.left) and \
        match_tree(tree1.right, tree2.right)
