# Node Class

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


# Doubly Linked List Class

class DoublyLinkedList:
    def __init__(self):
        self.head = None


# Insertion At The End

    def insert_at_end(self, value):
        temp = Node(value)

        # If Linked List Is Empty

        if self.head is None:
            self.head = temp
            return

        # Traverse To Last Node

        t = self.head

        while t.next is not None:
            t = t.next

        # Connect Last Node With New Node

        t.next = temp
        temp.previous = t


# Print Doubly Linked List

    def print_doubly_linked_list(self):
        t = self.head

        while t is not None:
            print(t.data, end=" <-> ")
            t = t.next

        print("None")


# Insertion At The Beginning

    def insert_at_beginning(self, value):
        temp = Node(value)

        # If Linked List Is Empty

        if self.head is None:
            self.head = temp
            return

        # Connect New Node With Head

        temp.next = self.head
        self.head.previous = temp

        # Move Head To New Node

        self.head = temp


# Insertion In The Middle

    def insert_at_middle(self, value, x):
        # Create New Node

        temp = Node(value)

        # Start From Head

        t = self.head

        # Search For x

        while t is not None:

            if t.data == x:

                # New Node Points To Next Node

                temp.next = t.next

                # If Next Node Exists

                if t.next is not None:
                    t.next.previous = temp

                # Current Node Points To New Node

                t.next = temp

                # New Node Points Back To Current Node

                temp.previous = t

                return

            else:
                t = t.next


# Delete Node

    def delete(self, value):

        # If Linked List Is Empty

        if self.head is None:
            print("Linked List is Empty")
            return

        # Start From Head

        t = self.head

        # Search And Delete Node

        while t is not None:

            if t.data == value:

                # Delete First Node

                if t == self.head:

                    self.head = t.next

                    if self.head is not None:
                        self.head.previous = None

                    return

                # Delete Middle Or Last Node

                if t.previous is not None:
                    t.previous.next = t.next

                if t.next is not None:
                    t.next.previous = t.previous

                return

            else:
                # Move To Next Node

                t = t.next

        print("Value Not Found")


# Create Doubly Linked List

obj = DoublyLinkedList()


# Insert At End

obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)


# Print Linked List

obj.print_doubly_linked_list()


# Insert At Beginning

obj.insert_at_beginning(5)


# Print Linked List

obj.print_doubly_linked_list()


# Insert In Middle

obj.insert_at_middle(50, 20)


# Print Linked List

obj.print_doubly_linked_list()


# Delete First Element

obj.delete(5)


# Print Linked List

obj.print_doubly_linked_list()


# Delete Middle Element

obj.delete(50)


# Print Linked List

obj.print_doubly_linked_list()


# Delete Last Element

obj.delete(40)


# Print Linked List

obj.print_doubly_linked_list()