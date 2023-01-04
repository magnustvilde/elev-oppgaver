import unittest
import methods as ss

class Test_methods(unittest.TestCase):
    # ----- FIZZBUZZ -----
    #Sjekk om input gir riktig svar
    #Her kan det være greit å sjekke alle forskjellige tilfeller (fizz, buzz, fizzbuzz)
    def test_fizzbuzz_fizz(self):
        print('\ntest_fizzbuzz_fizz')
        self.assertEqual(ss.fizzbuzz(9), 'fizz')
        self.assertEqual(ss.fizzbuzz(-9), 'fizz')

    def test_fizzbuzz_buzz(self):
        print('\ntest_fizzbuzz_buzz')
        self.assertEqual(ss.fizzbuzz(5), 'buzz')
        self.assertEqual(ss.fizzbuzz(-5), 'buzz')
         
    def test_fizzbuzz_fizzbuzz(self):
        print('\ntest_fizzbuzz_fizzbuzz')
        self.assertEqual(ss.fizzbuzz(15), 'fizzbuzz')
        self.assertEqual(ss.fizzbuzz(-15), 'fizzbuzz')


    # -----SELECTIONS SORT-----
    # Sjekk om sorteringen gir riktig resultat
    def test_selection_sort_correct_order(self):
        print('\ntest_selection_sort_correct_order')
        self.assertEqual(ss.selection_sort([3, 8, 4, 12, 1]), sorted([1,3,4,8,12]))
        self.assertEqual(ss.selection_sort([3, -1, 6, 0, -2]), sorted([-2,-1,0,3,6]))


    #Hva om typen som sendes inn ikke er en liste? Lag en test for det
    def test_selection_sort_type_of_input_value(self):
        print('\ntest_selection_sort_type_of_input_value')
        with self.assertRaises(TypeError):
            ss.selection_sort(122)
        with self.assertRaises(TypeError):
            ss.selection_sort('hello world')
        with self.assertRaises(KeyError):
            ss.selection_sort({'hei':1, 'no':2})
        


    # Hva om typen som sendes inn kan itereres, men er "immutable"? Lag en test for det
    def test_selection_sort_mutability_of_input_value(self):
        print('\ntest_selection_sort_mutability_of_input_value')
        with self.assertRaises(TypeError):
            ss.selection_sort((1,3,2,6))
            ss.selection_sort('hei')
if __name__ == '__main__':
    unittest.main()