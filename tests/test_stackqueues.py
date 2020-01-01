#!/usr/bin/env python3

from solutions.stacksqueues \
    import Stack, Queue, TowersOfHanoi, MyQueue


def test_stack_push():
    stack = Stack()
    stack.push(1)


def test_stack_empty_pop():
    stack = Stack()
    assert stack.pop() is None


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.is_empty()


def test_stack_lifo():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_count():
    stack = Stack()
    assert stack.count == 0
    stack.push(1)
    assert stack.count == 1
    stack.pop()
    assert stack.count == 0


def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)


def test_queue_empty_dequeue():
    queue = Queue()
    assert queue.dequeue() is None


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1


def test_queue_fifo():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_tower_of_hanoi():
    pb = TowersOfHanoi()
    pb.setup(5)
    pb.solve()


def test_myqueue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    assert q.pop() == 2


def test_stack_sort():
    stack = Stack()
    stack.push(2)
    stack.push(1)
    stack.push(4)
    stack.push(3)
    stack.sort()
