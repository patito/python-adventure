class Queue(object):

    def __init__(self):
        self.queue = []

    def empty(self):
        return not(self.queue)

    def insert(self, elem):
        self.queue.insert(0, elem)

    def debug(self):
        print self.queue

    def size(self):
        return len(self.queue)

    def remove(self):
        self.queue.pop()

if __name__ == '__main__':
    q = Queue()
    print(q.empty())
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q.empty())
    q.debug()
    print q.size()
    q.remove()
    q.debug()