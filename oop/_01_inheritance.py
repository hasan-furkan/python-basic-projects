class Animal:
    
    def eat(self):
        print('I can eat')
        
    def sleep(self):
        print('I can sleep')
        
# derived class

class Dog(Animal):
    
    def sound(self):
        print('Hav Hav')

#create object of the dog class
dog1 = Dog()

dog1.eat()
dog1.sleep()

dog1.sound()