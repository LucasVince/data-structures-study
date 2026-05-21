class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def append (self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        else:
            last = self.head

            while last.next != None:
                last = last.next
            last.next = new_node

    def insert_after (self, prev_data, data):
        new_node = Node(data)

        current = self.head

        while current:
            if current.data == prev_data:
                new_node = Node(data)

                new_node.next = current.next
                current.next = new_node
                return

            current = current.next

    def prepend (self, data):
        new_node = Node(data)
        next_data = self.head

        self.head = new_node

        self.head.next = next_data

    def delete (self, delete_data):
        current = self.head

        while current:
            if current.data == delete_data:
                
                return

            current = current.next

ll = LinkedList()

ll.append(20)
ll.append(40)
ll.prepend(10)
ll.insert_after(20, 30)
ll.append(50)
ll.display()
ll.delete(50)
ll.display()
