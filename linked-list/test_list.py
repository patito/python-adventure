import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        l = LinkedList()
        l.append("crazy")
        l.append("life")
        l.append("forever")
        self.assertEqual(len(l), 3)
        self.assertEqual(l.last.data, "forever")

    def test_preppend(self):
        l = LinkedList()
        l.preppend("bug")
        self.assertEqual(l.head.data, "bug")
        l.preppend("tatuuuu")
        self.assertEqual(l.head.data, "tatuuuu")
        self.assertEqual(len(l), 2)
        self.assertEqual(l.last.data, "bug")


if __name__ == '__main__':
    unittest.main()
