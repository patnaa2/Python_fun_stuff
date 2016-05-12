import unittest
from is_perm import CharacterMap, is_perm

class TestCharacterMap(unittest.TestCase):

    def test_init_with_string_of_unique_characters(self):
        char_map = CharacterMap("bar")
        self.assertEqual(char_map.char_dict["b"], 1)
        self.assertEqual(char_map.char_dict["a"], 1)
        self.assertEqual(char_map.char_dict["r"], 1)

    def test_init_with_non_unique_string(self):
        char_map = CharacterMap("foo")
        self.assertEqual(char_map.char_dict["f"], 1)
        self.assertEqual(char_map.char_dict["o"], 2)

    def test_true_equality(self):
        char_map_1 = CharacterMap("foo")
        char_map_2 = CharacterMap("oof")
        self.assertTrue(char_map_1 == char_map_2)

    def test_false_equality(self):
        char_map_1 = CharacterMap("bar")
        char_map_2 = CharacterMap("rrr")
        self.assertFalse(char_map_1 == char_map_2)

    def test_equality_with_invalid_types(self):
        char_map_1 = CharacterMap("bar")
        with self.assertRaises(AttributeError):
            char_map_1 == "string"

class TestIsPermutationMethod(unittest.TestCase):
    
    def test_is_perm_true(self):
        string1 = "test"
        string2 = "test"
        self.assertTrue(is_perm(string1, string2))
        
        string1 = "testing"
        string2 = "gintset"
        self.assertTrue(is_perm(string1, string2))

    def test_is_perm_false(self):
        string1 = "test"
        string2 = "bar"
        self.assertFalse(is_perm(string1, string2))

if __name__ == '__main__':
    unittest.main()
