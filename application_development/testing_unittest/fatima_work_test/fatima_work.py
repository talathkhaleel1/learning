class Apple:

    def get_apple(self):
        return "apple"

class Sum:

    def sum(self):
        list_of_integers = [1]
        sum_of_integers = sum(list_of_integers)
        return sum_of_integers

class Anagram:
    def anagram(self):
        a = 'race'
        b = 'care'
        if len(a) == len(b)and sorted(a) == sorted(b) :
            return "True"

class CountLetters:
    def count_letters(self, string):
        result ={}
        for i in range(0,len(string)):
            letter=string[i]# to get letter at every iteration
            letter_count = string.count(letter)# to count letter repetition as every iteration occurs
            result[letter] = letter_count# on letter key we are assigning the value from letter_count
        return result