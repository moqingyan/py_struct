from src.animal.animal import Animal 
print ("here")

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        return "meow~~"

cat = Cat("maomao", 6)
print (cat.meow())