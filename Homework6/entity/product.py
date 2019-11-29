class Product(object):
    """The base class"""

    def __init__(self, weight, calories):
        """Initiate our Onion """
        self.weight = weight
        self.calories = calories

    def __str__(self):
        """Print all parameters """
        return 'Weight:' + self.weight + 'Calories:' + self.calories
