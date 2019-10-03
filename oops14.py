#########abstract base class and abstract method###############
#You can't create object of abstract class,it'll throw error
#from abc import ABCMeta,abstractmethod
#either you can pass "metaclass=ABCMeta" as an argument to shape class or only "ABC"(FOR ABOVE 3.4)
#whichever class inherit ABCMeta class,it'll enforce its child to include methods in them anyhow
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="rectangle"
    side=4
    def __init__(self):
        self.length=5
        self.breadth=4
    def printarea(self):
        return f"area of rectangle is :", self.length*self.breadth

rect1=Rectangle()
print(rect1.printarea())
#tryobj=Shape()
