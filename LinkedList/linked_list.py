class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node is the list
    """
    data = None
    next_node = None

    # Constructor
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "[Node data: %s]" % self.data


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    # check if the linked list is empty
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count

    """
    Inserting
    """
    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Takes O(n)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    """
    Searching
     """
    def search(self, value):
        """
        Search for the first node containing data that matches the value
        Return node or None if not found

        Takes O(n)
        """
        current = self.head

        while current != None:
            if current.data == value:
                return current
            else:
                current = current.next_node
        return None


    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """


        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)


            current = current.next_node
        return '-> '.join(nodes)


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(5)
l.add(6)
l.add(10)
find = l.search(6)

print(l)
print(find)
