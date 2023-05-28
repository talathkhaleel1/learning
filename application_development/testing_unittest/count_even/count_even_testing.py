import unittest
from application_development.test.count_even.count_even import CountEven


class TestForCountEven(unittest.TestCase):

    def test_toKnowTheCountOfEvenNumbers_whenNumberStated_isAnEvenNumber_20(self):
        count_even1 = CountEven()
        self.assertEqual(9, count_even1.count_even())

    def test_toKnowTheCountOfEvenNumbers_whenNumberStated_isAnOddNumber_11(self):
        count_even2 = CountEven()
        self.assertEqual(5, count_even2.count_even())

    def test_toKnowTheCountOfEvenNumbers_whenNumberStated_isOutOfSpecifiedRange_101(self):
        count_even3 = CountEven()
        self.assertEqual(0, count_even3.count_even())

    def test_toKnowTheCountOfEvenNumbers_whenNumberStatedIsA_NegativeInteger(self):
        count_even4 = CountEven()
        self.assertEqual(0, count_even4.count_even())

