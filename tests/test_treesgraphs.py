#!/usr/bin/env python3

from solutions.treesgraphs \
    import TreeNode, GraphNode, exists_route, get_binary_search_tree, \
    get_linked_lists_by_depth, get_next_node, get_first_common_ancestor


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

    for i, val in enumerate(n1.dfs(seen=set())):
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


def test_graph_dfs_iterative():
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

    for i, val in enumerate(n1.dfs_iterative()):
        if i == 0:
            assert val == 1
        if i == 1:
            assert val == 3
        if i == 2:
            assert val == 7
        if i == 3:
            assert val == 6
        if i == 4:
            assert val == 2
        if i == 5:
            assert val == 5
        if i == 6:
            assert val == 4
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


def test_balanced_tree():
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)
    assert n1.is_balanced() is True


def test_unbalanced_tree():
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)
    n1.left.left = TreeNode(4)
    n1.left.left.left = TreeNode(5)
    assert n1.is_balanced() is False


def test_exists_route_in_directed_graph():
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
    assert exists_route(n1, n7) is True


def test_exists_route_in_directed_graph_2():
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
    assert exists_route(n2, n7) is False


def test_get_binary_search_tree():
    get_binary_search_tree(list(range(1, 10)))


def test_get_linked_lists_by_depth():
    bst = get_binary_search_tree(list(range(1, 10)))
    for l in get_linked_lists_by_depth(bst):
        pass  # print([n.val for n in l])


def test_get_next_node():
    bst = get_binary_search_tree(list(range(1, 10)))
    assert get_next_node(bst).val == 6
    assert get_next_node(bst.right).val == 9


def test_get_first_common_ancestor():
    bst = get_binary_search_tree(list(range(1, 10)))
    print(get_first_common_ancestor(bst.left, bst.right.left).val)
