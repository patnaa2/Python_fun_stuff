from functools import partial
import random
import string

def random_letter():
    return random.choice(string.ascii_letters) 

class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node if next_node else None

    @property
    def is_empty():
        return not self.val
    
    def __str__(self):
        if not isinstance(self.val, str):
            return str(self.val)
        return self.val

    def __repr__(self):
        return self.val

class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def __str__(self):
        ret_str = ""

        tmp = self.head
        while True:
            ret_str += str(tmp)
            if not tmp.next:
                break
            ret_str += " -> " 
            tmp = tmp.next

        return ret_str
    
    @property
    def length(self):
        counter = 1

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
            counter += 1

        return counter


class LinkedListHelper(object):
    VALID_VAL_TYPES = [str, int]
    MAX_INT = 100
    MIN_INT = 0

    @classmethod
    def generate_linked_lists(cls, num, length, val_type=int):
        '''
            Returns num LinkedList with a total of length nodes
            in each linked_list. Each node has a random val of
            type val_type

            :num - number of linked lists to return
            :legnth - length of linked lists
            :val_type - type of val in node of linked lists

            returns list of heads of each linked list
        '''
        linked_lists = []
        
        random_int = partial(random.randint, 0, 100)

        random_gen = random_int if val_type == int\
                else random_letter

        for _ in xrange(num):
            head = LinkedList(Node(random_gen()))
            tmp = head.head
            for _ in xrange(length-1):
                tmp.next = Node(random_gen())
                tmp = tmp.next 

            linked_lists.append(head)
    
        return linked_lists