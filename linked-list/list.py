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

    def _add_begin(self, name):
        new = Node(name)
        new.next = self.head
        self.head = new

    def _add_end(self, name):
        if (not self.head):
            new = Node(name)
            self.head = new
        else:
            current = self.head
            while (current):
                previous = current
                current = current.next

            new = Node(name)
            previous.next = new

    def add(self, name, first):
        if (first):
            self._add_begin(name)
        else:
            self._add_end(name)

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
        found = False
        pos = 0
        while (current and found == False):
            if (current.name == name):
                found = True
            current = current.next
            pos += 1

        return found, pos


if __name__ == '__main__':

    l = LinkedList()
    l.add("Paulo", False)
    l.add("Leonardo", False)
    l.add("Benatto", False)
    l.add("Mr.", True)
    print('Size List = %d' % l.size())
    found, pos = l.search("Benatto")
    print('Looking for Benatto found %d at %d' % (found, pos))
    l.print_list()
