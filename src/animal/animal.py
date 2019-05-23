class Animal(object):
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def get_name(self):
        return self.name 

    def get_age(self):
        return self.age

if __name__ == '__main__':
    ani = Animal("ani", 5)
    print (ani.get_name())
    print (ani.get_age())
   
