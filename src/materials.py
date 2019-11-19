from abc import ABC
from abc import abstractmethod


class Material(ABC):
    name = ''

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def prepare(self, *param):
        pass


class Lecture(Material):
    topic = ''

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "[Lect]{}:{}".format(
            self.name, self.topic
        )

    def prepare(self, topic):
        self.topic = topic


class Hometask(Material):
    tasks = []

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "[Ht]{}, tasks:{}".format(
            self.name, len(self.tasks)
        )

    def prepare(self, taskcount):
        self.tasks = ['task' + str(task) for task in range(taskcount)]
