import unittest
from base import Node, LinkedList, LinkedListHelper 
from copy import deepcopy 

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
   
    def test_reverse_linked_list(self):
        linked_list = LinkedList()
        linked_list.insert(0)
        linked_list.insert(1)
        linked_list.insert(2)
        
        orig = deepcopy(linked_list)

        linked_list.reverse()

        self.assertEqual(linked_list.length, 3)
        self.assertEqual(linked_list.head.val, 2)
        self.assertEqual(linked_list.head.next.val, 1)
        self.assertEqual(linked_list.head.next.next.val, 0)
    
    def test_remove_duplicates(self):
        linked_list = LinkedList()
        linked_list.insert(0)
        linked_list.insert(1)
        linked_list.insert(1)
        linked_list.insert(2)

        reversed_head = \
        LinkedListHelper.remove_duplicates_from_sorted_list(linked_list.head)

        self.assertEqual(reversed_head.val, 0)
        self.assertEqual(reversed_head.next.val, 1)
        self.assertEqual(reversed_head.next.next.val, 2)

if __name__ == '__main__':
    unittest.main()
