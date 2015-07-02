import sys

class Node(object):

    def __init__(self, name="", next=None):
        self.name = name
        self.next = next

    def __str__(self):
        return self.name


class LinkedList(object):
    
    def __init__(self):
        self.head = None

    def append(self, name):
        new = Node(name)
        new.next = self.head
        self.head = new

    def prepend(self, name):
        new = Node(name)
        if (not self.head):
            self.head = new
        else:
            current = self.head
            while (current):
                previous = current
                current = current.next
            previous.next = new

    def print_list(self):
        current = self.head
        while (current):
            print current.name
            current = current.next

    def size(self):
        length = 0
        current = self.head
        while (current):
            current = current.next
            length += 1

        return length

    def search(self, name):
        current = self.head
        while (current):
            if (current.name == name):
                return True
            current = current.next

        return False


if __name__ == '__main__':

    l = LinkedList()
    l.prepend("Paulo")
    l.prepend("Leonardo")
    l.prepend("Benatto")
    l.append("Mr.")
    print('Size List = %d' % l.size())
    print('Looking for Benatto = %d' % l.search("Benatto"))
    l.print_list()
