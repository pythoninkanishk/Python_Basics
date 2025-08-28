# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __str__(self):
        print("This is an animal.")
    
class Pets(Animals):
    def __str__(self):
        print("This is a pet animal.")
class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof! Woof!")
    
d = Dog()
d.bark()  # Calling the bark method