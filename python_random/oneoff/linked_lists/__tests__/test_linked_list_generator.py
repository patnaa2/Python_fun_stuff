import unittest
from base import Node, LinkedList, LinkedListHelper 

class LinkedListGenerator(unittest.TestCase):
    def setUp(self):
        self.helper_obj = LinkedListHelper()
        self._linked_list = self.helper_obj.generate_linked_lists(1,1)[0]

    def test_generate_base_linked_list(self):
        # test if object returned is a linked list
        self.assertIs(type(self._linked_list), LinkedList)
        self.assertIs(type(self._linked_list.head), Node)
    
    def test_length_of_linked_list(self):
        self.assertEqual(self._linked_list.length, 1)

if __name__ == '__main__':
    unittest.main()
