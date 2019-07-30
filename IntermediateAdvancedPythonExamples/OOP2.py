# inheritance and destructors
class Computer:
    count = 0

    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        Computer.count += 1

    def value(self):
        return (self.ram + self.hard + self.cpu) * 100

    def __del__(self):
        Computer.count -= 1


class Laptop(Computer):
    def value(self):
        return (self.ram + self.hard + self.cpu + self.size) * 100


my_pc = Computer(1, 4, 4)
print(my_pc.value())
my_laptop = Laptop(2, 12, 4)
my_laptop.size = 14
print(my_laptop.value())
print(my_laptop.count)
del my_pc
print(my_laptop.count)

