import argparse
'''
    Problem: Given a list of n intengers of positive size,
             create the largest possible number by combining the numbers.
             eg. [4, 5, 9, 95 ] -> 99554
'''

def make_largest_int(*args):
    args = sorted([str(x) for x in args], 
                  key= lambda x: (x[0], -len(x)),
                  reverse=True)
    return "".join(args)

def main():
    parser = argparse.ArgumentParser(description='Print the largest int possible.')
    parser.add_argument("-n", "--nums",
                        help="List of numbers to concetante",
                        nargs='+')  
    args = parser.parse_args()
    print make_largest_int(*args.nums)

if __name__ == "__main__":
    main()

