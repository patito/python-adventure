import sys

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def insert_start(self, data):
        """Insertion at the beginning of a linked list the complexity
        will be O(1)."""

        new = Node(data)
        new.next_node = self.head
        self.head = new
        self.count += 1

    def insert_end(self, data):
        """Insertion at the beginning of a linked list the complexity
        will be O(N)."""

        new = Node(data)
        if (not self.head):
            self.head = new
        else:
            current = self.head
            while (current):
                previous = current
                current = current.next_node
            previous.next_node = new
        self.count += 1

    def print_list(self):
        current = self.head
        while (current):
            print("data = {}".format(current.data))
            current = current.next_node

    def __len__(self):
        """In this case is necessary one field more (more memory),
           but you have direct access. O(1)"""

        return self.count

    def size(self):
        """In this case is necessary to go through. O(N)"""

        length = 0
        current = self.head
        while (current):
            current = current.next_node
            length += 1

        return length

    def search(self, data):
        """In this case is necessary to go through
        to the whole list O(N)"""

        current = self.head
        while (current):
            if (current.data == data):
                return True
            current = current.next_node
        return False

    def remove(self, data):
        raise Exception("develop me")


if __name__ == '__main__':
    l = LinkedList()
    l.insert_start("Paulo")
    l.insert_end("Leonardo")
    l.insert_end("Benatto")
    l.insert_end("Tesudo")
    l.insert_start("Mr.")
    print('len = {}. size = {}'.format(len(l), l.size()))
    print('Searched Benatto? {}'.format(l.search("Benatto")))
    print('Searched Nani? {}'.format(l.search("Nani")))
    l.print_list()
#    l.remove("Benatto")
