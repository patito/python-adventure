# Python Linked List
#
# Hi douchebad, thanks for vising my blog. I have decided that
# I should learn more
# about algorithms and data structure as result I wrote this
# shit post about linked list


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def preppend(self, data):
        new = Node(data)
        if self.is_empty():
            self.last = new
        new.next = self.head
        self.head = new
        self.count += 1

    def append(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new
        self.count += 1

    def _insert_middle(self, data, index):
        current = self.head
        previous = current
        counter = 0
        new = Node(data)
        while (current):
            if (index == counter):
                previous.next = new
                new.next = current
                break
            previous = current
            current = current.next
            counter += 1

    def insert(self, data, index):
        if index <= 0:
            self.preppend(data)
        elif index >= self.count:
            self.append(data)
        else:
            self._insert_middle(data, index)
        self.count += 1

    def print_list(self):
        current = self.head
        while (current):
            l = "[" + current.data + "]"
            print(l, end=' ')
            current = current.next
        print("\n")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove(self, data):
        if self.is_empty():
            return
        elif self.head.data == data:
            self.head = self.head.next
            self.count -= 1
        else:
            current = self.head
            previous = self.head
            while current:
                print("loop")
                if current.data == data:
                    print("Data Entrou if = ", current.data)
                    previous.next = current.next
                    self.count -= 1
                    break
                previous = current
                current = current.next

    def pop(self, index):
        if self.is_empty():
            return
        if index <= 0:
            self.head = self.head.next
            self.count -= 1
        else:
            current = self.head
            previous = self.head
            counter = 0
            while current:
                if index == counter:
                    previous.next = current.next
                    self.count -= 1
                previous = current
                current = current.next
                counter += 1


if __name__ == '__main__':
    l = LinkedList()
    l.preppend("um")
    l.preppend("dois")
    l.preppend("tres")
    l.append("quatro")
    l.append("cinco")
    print("Length: {}".format(len(l)))
    l.print_list()
    print("Removendo = {}".format(l.pop(0)))
    print("Removendo = {}".format(l.pop(1)))
    print("Removendo = {}".format(l.pop(len(l)-1)))

    print("------------------------")
    l.print_list()
