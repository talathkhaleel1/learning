import unittest
from application_development.testing.fatima_work import Apple
from application_development.testing.fatima_work import Sum
from application_development.testing.fatima_work import Anagram
from application_development.testing.fatima_work import CountLetters

class FileForTesting(unittest.TestCase):

    def test_to_get_apple_returns_apple(self):
        apple= Apple()# creating an instance for class Apple
        self.assertEqual("apple", apple.get_apple())
        #self.assertEqual("fruit", apple.get_apple())# here test fails as expected value parameter is different.

    def test_to_check_sum_of_elements_with_multiple_elements(self):
        numbers1=Sum()
        self.assertEqual(6, numbers1.sum())

    def test_to_check_sum_of_elements_when_list_is_empty(self):
        numbers1=Sum()
        self.assertEqual(0, numbers1.sum())

    def test_to_check_sum_of_elements_with_one_element_in_the_list(self):
        numbers1=Sum()
        self.assertEqual(1, numbers1.sum())

    def test_to_know_if_values_are_anagrams(self):
        anagram=Anagram()
        self.assertTrue(True, anagram.anagram())

    def test_to_count_letters_in_a_string(self):
        count_letters1=CountLetters()
        self.assertEqual({'a':1, 'p':2, 'l':1, 'e':1} ,count_letters1.count_letters("apple"))