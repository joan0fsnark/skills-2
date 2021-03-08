"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    1) Encapsulation
        - Data lives close to its functionality
    2) Abstraction
        - Easy to make different, interchangeable types of things
    3) Polymorphism
        - Flexibility of types without conditionals

2. What is a class?

    Classes provide a means of bundling data and functionality together. 
    Creating a new class creates a new type of object, allowing new 
    instances of that type to be made. Each class instance can have 
    attributes attached to it for maintaining its state. Class instances 
    can also have methods (defined by its class) for modifying its state.


3. What is a method?

    A method is a function that “belongs to” an object. In Python, the 
    term "method" is not unique to class instances: other object types 
    can have methods as well. For example, list objects have methods 
    called 'append', 'insert', 'remove', 'sort', and so on.


4. What is an instance in object orientation?

    An instance is an object in a class (an instance of a thing in a 
    particular class)

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    Class attributes are general and applied to everything/every 
    instance in the class. Instance attributes are more specific 
    and can be defined to override class attributes; an instance 
    takes the general attributes as a default.
"""


"""2. Road Class"""

class Road:

    def __init__(self, num_lanes, speed_limit):
        self.num_lanes = 2
        self.speed_limit = 25

        class Road(road_1):
            self.num_lanes = 4
            self.speed_limit = 60
            
        class Road(road_2):
            

            


# """3. Update Password"""


# class User:
#     """A user object."""

#     def __init__(self, username, password):
#         """Create a user with the given username and password."""

#         self.username = username
#         self.password = password


# """4. Build a Library"""


# class Book(object):
#     """A Book object."""

#     def __init__(self, title, author):
#         """Create a book with the given title and author."""

#         self.title = title
#         self.author = author


# """5. Rectangle"""


# class Rectangle:
#     """A rectangle."""

#     def __init__(self, length, width):
#         """Create a rectangle with the given length and width."""

#         self.length = float(length)
#         self.width = float(width)

#     def calculate_area(self):
#         """Return the area of the rectangle."""

#         return self.length * self.width
