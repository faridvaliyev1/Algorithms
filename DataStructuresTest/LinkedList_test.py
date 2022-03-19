from DataStructures.LinkedList import LinkedList,Node
import unittest

class NodeTest(unittest.TestCase):
    def test_init(self):
        data="ABC"
        node=Node(data)
        assert node.data is data
        assert node.next is None


class LinkedListTest(unittest.TestCase):
    
    def test_init(self):
        ll=LinkedList()
        assert ll.head is None
    
    def test_init_with_list(self):
        ll=LinkedList(['A','B','C'])
        assert ll.head.data=="A" 
        

if __name__ == '__main__':
    unittest.main()