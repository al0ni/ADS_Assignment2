class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add an element to the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Add an element to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3. Remove the last element
    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    # 4. Print all elements
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    # 5. Search for a specific element
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    # 6. Insert an element at a given position
    def insert_at(self, data, pos):
        if pos == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if curr:
                curr = curr.next
        if curr:
            new_node.next = curr.next
            curr.next = new_node

    # 7. Remove an element by its value
    def remove_value(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    # 8. Combine two singly linked lists
    def combine(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other_list.head

    # 9. Reverse a singly linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # 10. Sort a singly linked list (Insertion Sort)
    def sort(self):
        sorted_head = None
        curr = self.head
        while curr:
            next_node = curr.next
            if not sorted_head or sorted_head.data >= curr.data:
                curr.next = sorted_head
                sorted_head = curr
            else:
                temp = sorted_head
                while temp.next and temp.next.data < curr.data:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
            curr = next_node
        self.head = sorted_head
