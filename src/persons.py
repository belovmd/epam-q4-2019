from abc import ABC
from abc import abstractmethod


class Person(ABC):
    """Representation of abstract person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def greet(self):
        pass


class Student(Person):
    """Representation of a student."""

    def greet(self):
        """Simple greeting from a student."""

        print("{}: >>> hello".format(self))

    def __str__(self):
        return "[Stud]{}".format(self.name)

    def listen(self, lecture):
        """Listen to a lecture."""

        print("{} listen to {}".format(self, lecture))

    def do_homework(self, homework):
        """Doing a homework."""

        print("{} do homework {}".format(self, homework))


class Lector(Person):
    """Representation of a lector"""

    def __str__(self):
        return "[Lector]{}".format(self.name)

    def greet(self):
        """Simple greeting from a lector."""

        print("{}: >>> hello".format(self))

    def teach(self, lecture):
        """Teaching a lecture."""

        print("{} teach {}".format(self, lecture))


class Group(object):
    """Representation of a group of students"""

    def __init__(self, id):
        self.id = id
        self.members = []

    def add_member(self, student):
        self.members.append(student)

    def greet(self):
        """Greeting from a group."""

        for student in self.members:
            student.greet()

    def listen(self, lecture):
        """Listening to a lecture by a group."""
        for student in self.members:
            student.listen(lecture)

    def do_homework(self, homework):
        """Doing a homework by a group."""

        for student in self.members:
            student.do_homework(homework)
