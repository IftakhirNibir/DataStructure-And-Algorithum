

class animal:
    def __init__(self,name):
        self.name = name

class dog(animal):
    def display(self):
        print("Your dog name is ",self.name)

d1 = dog("Tommy")
d1.display()

