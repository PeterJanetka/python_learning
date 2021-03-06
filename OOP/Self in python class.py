"""
### Self in Python class

self represents the instance of the class.
By using the “self” keyword we can access the attributes and
methods of the class in python.
It binds the attributes with the given arguments.

The reason you need to use self,
is because Python does not use the @ syntax to refer to instance attributes.
Python decided to do methods in a way
that makes the instance to which the method belongs,
be passed automatically but not received automatically:
the first parameter of methods is the instance the method is called on.
"""


class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


# both objects have different self which
# contain their attributes

audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
