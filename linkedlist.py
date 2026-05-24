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

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        else:
            last = self.head

            while last.next != None:
                last = last.next
            last.next = new_node

    def insert_after(self, prev_data, data):
        new_node = Node(data)

        current = self.head

        while current:
            if current.data == prev_data:
                new_node = Node(data)

                new_node.next = current.next
                current.next = new_node
                return

            current = current.next

    def inset_before(self, next_data, data):
        new_node = Node(data)

        current = self.head
        prev = None

        while current:
            if current.data == next_data:
                new_node = Node(data)

                new_node.next = current
                prev.next = new_node
                return

            prev = current
            current = current.next

    def prepend(self, data):
        new_node = Node(data)
        next_data = self.head

        self.head = new_node

        self.head.next = next_data

    def delete(self, delete_data):
        current = self.head
        prev = None

        while current:
            if current.data == delete_data:
                
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

    def length(self):
        current = self.head
        count = 0

        while current:
            count += 1

            current = current.next

        return count

    def array_convert(self):
        current = self.head
        array = []

        while current:
            array.append(current.data)

            current = current.next
            
        return array

ll = LinkedList()

ll.append(20)
ll.append(40)
ll.prepend(10)
ll.insert_after(20, 30)
ll.append(50)
ll.display()
ll.delete(50)
ll.display()
ll.inset_before(20,15)
ll.display()

ll_array = ll.array_convert()
print(ll_array)
print(ll.length())
