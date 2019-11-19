from abc import ABC
from abc import abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def greet(self):
        pass


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def greet(self):
        print("{}: >>> hello".format(self))

    def __str__(self):
        return "[Stud]{}".format(self.name)

    def listen(self, lecture):
        print("{} listen to {}".format(self, lecture))

    def do_homework(self, homework):
        print("{} do homework {}".format(self, homework))


class Lector(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return "[Lector]{}".format(self.name)

    def greet(self):
        print("{}: >>> hello".format(self))

    def teach(self, lecture):
        print("{} teach {}".format(self, lecture))


class Group(object):
    def __init__(self, id):
        self.id = id
        self.members = []

    def greet(self):
        for student in self.members:
            student.greet()

    def listen(self, lecture):
        for student in self.members:
            student.listen(lecture)

    def do_homework(self, homework):
        for student in self.members:
            student.do_homework(homework)
