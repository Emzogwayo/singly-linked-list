# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the value
        self.next = None  # Pointer to the next node (None by default)

# LinkedList class to manage the entire list
class LinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Goes to the last node
            current = current.next
        current.next = new_node  # Link the new node at the end

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to the old head
        self.head = new_node  # New node becomes the new head

    # Insert a new node at a specific index
    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    # Delete a node at a specific index
    def delete_at_index(self, index):
        if index < 0:
            print("Invalid index")
            return
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next is not None and count < index - 1:
            current = current.next
            count += 1
        if current.next is None:
            print("Index out of bounds")
            return
        current.next = current.next.next

    # Search for a value and return its index
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # Not found

    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Test code
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_start(5)
    ll.insert_at_index(1, 7)
    ll.display()  

    print("Index of 10:", ll.search(10))

    ll.delete_at_index(1)
    ll.display()  
