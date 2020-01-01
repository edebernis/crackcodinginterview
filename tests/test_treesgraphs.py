#!/usr/bin/env python3

from solutions.treesgraphs import TreeNode, GraphNode


def test_tree_traverse_in_order():
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)

    for i, val in enumerate(n1.traverse_in_order()):
        if i == 0:
            assert val == 2
        if i == 1:
            assert val == 1
        if i == 2:
            assert val == 3


def test_tree_traverse_pre_order():
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)

    for i, val in enumerate(n1.traverse_pre_order()):
        if i == 0:
            assert val == 1
        if i == 1:
            assert val == 2
        if i == 2:
            assert val == 3


def test_tree_traverse_post_order():
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)

    for i, val in enumerate(n1.traverse_post_order()):
        if i == 0:
            assert val == 2
        if i == 1:
            assert val == 3
        if i == 2:
            assert val == 1


def test_graph_dfs():
    n1 = GraphNode(1)
    n2 = GraphNode(2)
    n3 = GraphNode(3)
    n4 = GraphNode(4)
    n5 = GraphNode(5)
    n6 = GraphNode(6)
    n7 = GraphNode(7)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n4, n5]
    n3.neighbors = [n6, n7]
    n7.neighbors = [n1]

    for i, val in enumerate(n1.dfs()):
        if i == 0:
            assert val == 1
        if i == 1:
            assert val == 2
        if i == 2:
            assert val == 4
        if i == 3:
            assert val == 5
        if i == 4:
            assert val == 3
        if i == 5:
            assert val == 6
        if i == 6:
            assert val == 7
        assert i < 7


def test_graph_bfs():
    n1 = GraphNode(1)
    n2 = GraphNode(2)
    n3 = GraphNode(3)
    n4 = GraphNode(4)
    n5 = GraphNode(5)
    n6 = GraphNode(6)
    n7 = GraphNode(7)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n4, n5]
    n3.neighbors = [n6, n7]
    n7.neighbors = [n1]

    for i, val in enumerate(n1.bfs()):
        if i == 0:
            assert val == 1
        if i == 1:
            assert val == 2
        if i == 2:
            assert val == 3
        if i == 3:
            assert val == 4
        if i == 4:
            assert val == 5
        if i == 5:
            assert val == 6
        if i == 6:
            assert val == 7
        assert i < 7
