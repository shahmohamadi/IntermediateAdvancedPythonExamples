# an example of object oriented in Python
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        print('name is', self.name)

    def get_age(self):
        print('age is', self.age)

    def get_info(self):
        print('name is %s and age is %i' % (self.name, self.age))

    def birthday(self):
        self.age += 1
        print('HBD!')

    def return_count(self):
        return Person.count


samane = Person('samane', 31)
samane.get_name()
samane.get_age()
samane.get_info()
samane.birthday()
samane.get_age()
shahab = Person('shahab', 30)
shahab.get_info()

print('\nwe have %i ppl till now' % samane.count)
