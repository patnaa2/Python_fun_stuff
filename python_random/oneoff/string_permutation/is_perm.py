#!/usr/bin/python

# STANDARD QUESTION: DETERMINE IF ONE STRING
# IS A PERMUTATION OF ANOTHER NO SLICING ALLOWED

class CharacterMap(object):
    '''
        Helper class that creates a dictionary
        of characters in a given string

        eg. if string = "acndc"
        dict = { "a": 1, "c": 2, "d": 4 "n": 1 }
    '''

    def __init__(self, string):
        self.char_dict = {}
        
        for char in string:
            if char in self.char_dict: 
                self.char_dict[char] += 1
                continue
            self.char_dict[char] = 1

    def __eq__(self, other_char_map):
        # short circuit if its a bad input
        if not isinstance(other_char_map, CharacterMap):
            raise AttributeError("Invalid Comparison Type. Expected object"
                                 " of class CharacterMap, got %s" 
                                 %(other_char_map))

        # simple dict comparison in other case
        return other_char_map.char_dict == self.char_dict

def is_perm(str1, str2):
    '''
        Helper function that takes in a two strings
        and returns a boolean indicate if they are permutations 
        of one another or not
    '''
    char_map1 = CharacterMap(str1)
    char_map2 = CharacterMap(str2)
    return char_map1 == char_map2

def main(): 
    # have some sort of interactive script

    while True:
        string1 = raw_input("Please enter the first string:\n")
        string2 = raw_input("Please enter the second string:\n")
        
        if is_perm(string1, string2):
            print "%s and %s are permutations of each other." \
                            %(string1, string2)
        else:
            print "%s and %s are NOT permutations of each other."\
                            %(string1, string2)
        print "\n\n"

if __name__ == "__main__":
    main()

