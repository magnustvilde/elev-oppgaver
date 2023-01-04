import unittest

def adder_function(term1, term2):
    return (term1 * term2)


class Test_adder_function(unittest.TestCase):

    def test_number_input(self):
        expected = 4
        actual = adder_function(2, 2)
        self.assertEqual(actual, expected)

























    def test_number_input2(self):
        expected = 8
        actual = adder_function(5, 3)
        self.assertEqual(actual, expected)
























    def test_string_input(self):
        expected = "Hello World"
        actual = adder_function("Hello ", "World")
        self.assertEqual(actual, expected)




















    def test_different_type_inputs(self):
        with self.assertRaises(TypeError):
            adder_function("1", 1)