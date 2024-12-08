class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, data):
        new_node = Node(data)
        # If the list is empty, set head to the new node
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  
            # Set the previous pointer of the new node
            new_node.prev = current 

    def deletion(self, data):
        if not self.head:  
            print("The list is empty. Nothing to delete.")
            return

        if self.head.data == data:  
            self.head = self.head.next
            if self.head:  
                # Remove the backward link
                self.head.prev = None
            print(f"Deleted {data} from the list.")
            return

        current = self.head
        while current and current.data != data: 
            current = current.next

        if current: 
            if current.next:  # If it's not the last node
                current.next.prev = current.prev
            if current.prev:  # If it's not the first node
                current.prev.next = current.next
            print(f"Deleted {data} from the list.")
        else:
            print(f"{data} not found in the list.")

    def traversal(self):
        print("Traversing forward:")
        current = self.head
        while current:  # Forward traversal
            print(current.data, end=" -> ")
            last = current  # Keep track of the last node
            current = current.next
        print("None")

        print("Traversing backward:")
        while last:  # Backward traversal from the last node
            print(last.data, end=" -> ")
            last = last.prev
        print("None")


dll = DoublyLinkedList()
dll.insertion(10)
dll.insertion(20)
dll.insertion(30)
dll.traversal()
dll.deletion(20)
dll.traversal()