class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node
        
    def __repr__(self) -> str:
        return f"<Node : {self.data}>"

class LinkedList:
    def __init__(self, head=None) -> None:
        self.__head = head

    def append(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node

    def prepend(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
        else:
            node.next_node = self.__head
            self.__head = node

    def insert_after(self, target, data):
        if self.__head is None:
            print("< linked list is empty >")
            return

        node = Node(data)
        current = self.__head
        while current is not None and current.data != target:
            current = current.next_node
            
        if current is None:
            print(f"< Node with target {target} not found >")
        else:
            node.next_node = current.next_node
            current.next_node = node
            
    def insert_before(self, target, data):
        if self.__head is None:
            print("< linked list is empty >")
            return
        
        if self.__head.data == target:
            self.prepend(data)
            return
        
        node = Node(data)
        current = self.__head.next_node
        previous = self.__head
        
        while current is not None and current.data != target:
            previous = current
            current = current.next_node
            
        if current is None:
            print(f"< Node with target {target} not found >")
        else:
            previous.next_node = node
            node.next_node = current

    def find(self, data):
        if self.__head is None:
            print("< linked list is empty >")
            return
        
        if self.__head.data == data:
            print(f"< Node with data {data} found at position 1>")
            return
        
        current = self.__head.next_node
        position = 2
        while current is not None and current.data != data:
            position += 1
            current = current.next_node
        
        if current is None:
            print(f"< Node with data {data} not found >")
            return
        else:
            print(f"< Node with data {data} found at position {position} >")

    def delete_node(self, data):
        if self.__head is None:
            print("< linked list is empty >")
            return
        
        if self.__head.data == data:
            self.__head = self.__head.next_node
            return
        
        current = self.__head.next_node
        previous = self.__head
        while current is not None and current.data != data:
            previous = current
            current = current.next_node 

        if current is None:
            print(f"< Node with data {data} not found >")
        else:
            previous.next_node = current.next_node

    def length(self):
        if self.__head is None:
            return 0
        else:
            length = 0
            current = self.__head
            while current is not None:
                length += 1
                current = current.next_node
            return length

    def get_list(self):
        if self.__head is None:
            return "< linked list is empty >"
        else:
            nodes = []
            current = self.__head
            while current is not None:
                nodes.append(current.data)
                current = current.next_node
            return nodes
        
    def reverse(self):
        if self.__head is None:
            print("< linked list is empty >")
            return
        
        previous = None
        current = self.__head
        while current is not None:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        
        self.__head = previous
        
    def get_head(self):
        if self.__head is None:
            print("< linked list is empty >")
            return
        return self.__head.data

    def display(self):
        if self.__head is None:
            print("< linked list is empty >")
        else:
            nodes = []
            current = self.__head
            while current is not None:
                nodes.append(str(current.data))
                current = current.next_node
            print("[ " + " -> ".join(nodes) + " -> None ]")
