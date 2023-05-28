class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name+ " is a(n) "+str(self.age)+" old dog."