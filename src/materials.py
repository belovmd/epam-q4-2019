from abc import ABC
from abc import abstractmethod


class Material(ABC):
    """Abstract class for learning material."""

    name = ''

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def prepare(self, *param):
        pass


class Lecture(Material):
    """Representation of lecture."""

    topic = ''

    def __str__(self):
        return "[Lect]{}:{}".format(
            self.name, self.topic
        )

    def prepare(self, topic):
        """Prepare a lecture."""

        self.topic = topic


class Hometask(Material):
    """Representation of hometask."""

    tasks = []

    def __str__(self):
        return "[Ht]{}, tasks:{}".format(
            self.name, len(self.tasks)
        )

    def prepare(self, taskcount):
        """Prepare a hometask"""

        self.tasks = ['task' + str(task) for task in range(taskcount)]
