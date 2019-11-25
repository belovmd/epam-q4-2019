from materials import Hometask
from materials import Lecture
from persons import Group
from persons import Lector
from persons import Student


def main():
    lector = Lector("Max", 33)
    stu1 = Student("Nick", 20)
    stu2 = Student("Ada", 19)
    group = Group("Q19")
    group.add_member(stu1)
    group.add_member(stu2)
    lect1 = Lecture("Lecture 1")
    lect1.prepare("Basics")
    hometask1 = Hometask("Hw1")
    hometask1.prepare(3)

    lector.greet()
    group.greet()
    lector.teach(lect1)
    group.listen(lect1)
    group.do_homework(hometask1)


main()
