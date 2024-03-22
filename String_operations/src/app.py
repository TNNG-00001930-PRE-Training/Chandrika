import unittest
def concatenate_strings(str1, str2):
    return str1 + " " + str2
def slice_string(s):
    return s[10:20]
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."
def manipulate_string(s):
    upper_str = s.upper()
    lower_str = s.lower()
    stripped_str = s.strip()
    replaced_str = s.replace("Tammineni", "T")
    return upper_str, lower_str, stripped_str, replaced_str
class TestStringOperations(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "World"), "Hello World")

    def test_slice_string(self):
        self.assertEqual(slice_string("Tammineni Chandrika"), "Chandrika")

    def test_format_string(self):
        self.assertEqual(format_string("Chandrika", 21), "My name is Chandrika and I am 21 years old.")

    def test_manipulate_string(self):
        upper_str, lower_str, stripped_str, replaced_str = manipulate_string(" Tammineni Chandrika ")
        self.assertEqual(upper_str, " TAMMINENI CHANDRIKA ")
        self.assertEqual(lower_str, " tammineni chandrika ")
        self.assertEqual(stripped_str, "Tammineni Chandrika")
        self.assertEqual(replaced_str, " T Chandrika ")

if __name__ == '__main__':
    unittest.main()

