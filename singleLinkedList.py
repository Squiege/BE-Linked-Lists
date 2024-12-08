class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def insertion(self, data):
        # Creating the new node
        new_node = Node(data)
        # If there is no Head Node, make the node the new Head node
        if not self.head:
            self.head = new_node
        # Otherwise insert the new node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def deletion(self, data):
        # Checking if the Node is empty
        if not self.head:
            print("The list is empty. Nothing to delete.")
            return

        # Deleting the head Node
        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted {data} from the list.")
            return

        # Deleting a Node in the middle or at the Tail
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        # Node found
        if current.next:
            current.next = current.next.next
            print(f"Deleted {data} from the list.")
        else:  
            # Node not found
            print(f"{data} not found in the list.")


    def traversal(self):
        # Start at the Head node
        current = self.head
        # While current exists search through each node
        while current:
            # Print data of each node and end with '->'
            print(current.data, end=" -> ")
            # Update current node
            current = current.next
        # Final next that points to an empty node ready for initialization
        print("None")

ll = SinglyLinkedList()
ll.insertion(10)
ll.insertion(20)
ll.insertion(30)
ll.traversal()  
ll.deletion(20)
ll.traversal() 
ll.deletion(40)