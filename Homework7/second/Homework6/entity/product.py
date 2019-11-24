class Product(object):

    def __init__(self, weight, calories):
        self.weight = weight
        self.calories = calories

    def __str__(self):
        return 'Weight:' + self.weight + 'Calories:' + self.calories
