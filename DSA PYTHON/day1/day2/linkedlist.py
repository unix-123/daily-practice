# Node Class

class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


# Singly Linked List Class

class SinglyLinkedList:
    def __init__(self):
        self.head = None


# Insertion At The End

    def insert_at_end(self, value):
        temp = Node(value)

        if self.head is not None:
            t1 = self.head

            while t1.next is not None:
                t1 = t1.next

            t1.next = temp

        else:
            self.head = temp


# Print Linked List / Traversal

    def print_linked_list(self):
        t1 = self.head

        while t1.next is not None:
            print(t1.data, end=" ")
            t1 = t1.next

        print(t1.data)


# Insertion At The Beginning

    def insert_at_beginning(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp


# Insertion In The Middle

    def insert_in_middle(self, value, x):
        t1 = self.head
        temp = Node(value)

        while t1 is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                break
            else:
                t1 = t1.next


# Delete Element

    def delete_linked_list(self, value):
        t1 = self.head
        previous = t1

        # Delete First Element

        if t1.data == value:
            self.head = t1.next
            return

        # Search Element

        while t1.next is not None:
            if t1.data == value:
                previous.next = t1.next
                break

            else:
                previous = t1
                t1 = t1.next

        # Delete Last Element

        if t1.next is None and t1.data == value:
            previous.next = None


# Create Linked List

obj = SinglyLinkedList()


# Insert At End

obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)


# Print Linked List

obj.print_linked_list()


# Insert At Beginning

obj.insert_at_beginning(5)


# Print Linked List

obj.print_linked_list()


# Insert In Middle

obj.insert_in_middle(40, 20)


# Print Linked List

obj.print_linked_list()


# Delete Element

obj.delete_linked_list(20)


# Print Linked List

obj.print_linked_list()