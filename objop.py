# ? ABSTRACT CLASSES


from abc import ABC, abstractmethod

class Vechile(ABC):
    
    @abstractmethod
    def go (self):
        pass


    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):

    def go (self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vechile):
    
    def go (self):
        print("You drive the motocycle")

    def stop(self):
        print("You stop the motocycle")

class Boat(Vechile):
    
    def go (self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")
    

#? POLYMORPHISM

    #! 1. INHERINTANCE
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('Peporoni', 15)]

for shape in shapes:
    print(f"{shape.area()}cm")

    #! 2. DUCK TYPING

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = True

    def speak(self):
        print("HORN!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


#? AGGREGATION: Represents a relationship where one object (the whole) contains reference to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

    

class Book: 
    def  __init__(self, title , author):
        self.title = title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit...", "J. R. R. Tolken")
book3 = Book("The Colour of Magic", "Terry Pratchet")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.name)

for book in library.list_books():
    print(book)



# ?Composition = The composed object directly owns its own components, which cannot exist independently "owns - a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make  = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())



# ? NESTED CLASSES

class Company:
    class Employee:
        def __init__(self, name , position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company("Krusty Krab")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

for employee in company2.list_employees():
    print(employee)


# ? STATIC METHODS = A method that belongs to a class rather than any object from that class (instance), usually used for general utilities functions

# ! INSTANCE METHODS  = Best for operations on instances of a class (objects) 
# * STATIC METHODS = Best for utility that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod

    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cahier")
employee3 = Employee("Spongebob", "Cook")
  
print(Employee.is_valid_position("Rocket Scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())



# ? CLASS METHODS = Allow operations related to itself, Take (cls) as the first parameter, which represents the class itself.

# ! INSTANCE METHODS = Best for operations on instances of the class of the object
# ! STATIC METHODS = Best for utility functions that do not need access to class data 
# ! CLASS METHODS = Best for class-level data or requires access to the class itself

class Students:

    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"
    

student1 = Students("Spongebob", 3.2)
student1 = Students("Patrick", 3.2)
student1 = Students("Sandy", 4.0)
    
print(Students.get_count())
print(Students.get_average_gpa())


# ? MAGIC METHODS = Dunder methods (double underscore) __init__, __str__, __eq__. They are automatically called by Python's built-in operations. They allow developers to define or customize the behaviour of objects.

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
           return self.title

        elif key == "author":
            return self.author
        
        elif key == "num_pages":
            return self.num_pages
        
        else:
            return f"Key '{key}' was not found"
        


book1 = Book("The Hobbit", "J.R.R. Tokien", 310)
book2 = Book("Harry Potter and The Philospher Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
    
    
print(book3["audio"])



# ? @property = Decorators used to define a method as a property (it can be accessed like an attribute)
            # ? Benefits: Add additional logic when read, write, or delete attributes. Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
       return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3,4)

rectangle.width = 5
rectangle.height = 6


del rectangle.width
del rectangle.height

