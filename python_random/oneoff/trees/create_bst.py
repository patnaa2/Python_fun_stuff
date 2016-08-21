'''
    Given a sorted array of unique integers, create
    a binary search tree
'''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def create_min_bst(x, start, end):
    if start > end:
        return 

    mid = (start + end) / 2
    root = Node(x[mid])
    root.left = create_min_bst(x, 0, mid-1)
    root.right = create_min_bst(x, mid+1, end)
    return root

def main():
    array = [3, 4, 6, 7, 9]
    x = create_min_bst(array, 0, 4)

if __name__ == '__main__':
    main()
