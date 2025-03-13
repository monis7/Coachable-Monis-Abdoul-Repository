from collections import deque

# ListNode class for linked list operations
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Insert at the front of a linked list
def insert_at_front(head, value):
    new_node = ListNode(value)
    new_node.next = head
    return new_node  # New head of the list

# 2. Merge two sorted linked lists
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# 3. Delete a node given only a pointer to it
def delete_node(node):
    if node is None or node.next is None:
        raise ValueError("Cannot delete the given node")
    node.val = node.next.val
    node.next = node.next.next

# 4. Reverse a singly linked list iteratively
def reverse_list(head):
    prev, curr = None, head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node

    return prev  # New head

# 5. Find the middle node of a linked list in O(n) time and O(1) space
def find_middle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Middle node

# 6. Stack implementation using a singly linked list
class Stack:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = self.Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise IndexError("Stack is empty")
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if not self.top:
            raise IndexError("Stack is empty")
        return self.top.val

# 7. Queue implementation using a singly linked list
class Queue:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        new_node = self.Node(val)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise IndexError("Queue is empty")
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def peek(self):
        if not self.front:
            raise IndexError("Queue is empty")
        return self.front.val

# 8. Queue using two stacks
class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, val):
        self.in_stack.append(val)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack[-1]

# 9. Stack using two queues
class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if not self.q1:
            raise IndexError("Stack is empty")

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

    def peek(self):
        if not self.q1:
            raise IndexError("Stack is empty")

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        val = self.q1.popleft()
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

