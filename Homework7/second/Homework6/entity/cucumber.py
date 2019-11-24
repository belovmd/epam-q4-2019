from product import Product


class Cucumber(Product):
    """Class to create Cucumber """

    def __init__(self, weight, calories, size):
        """Initiate our Cucumber """
        super().__init__(weight, calories)
        self.size = size

    def __str__(self):
        """Print all parameters """
        return 'Cucumber:' + self.weight + self.calories + self.size
