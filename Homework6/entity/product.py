class Product(object):
    """The base class"""

    def __init__(self, weight, calories):
        """Initiate our Onion """
        self.weight = weight
        self.calories = calories

    def __str__(self):
        """Print all parameters """
        return 'Weight:' + str(self.weight) + 'Calories:' + str(self.calories)
