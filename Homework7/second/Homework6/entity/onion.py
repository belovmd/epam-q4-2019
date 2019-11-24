from product import Product


class Onion(Product):
    """Class to create Onion """

    def __init__(self, weight, calories, color):
        """Initiate our Onion """
        super().__init__(weight, calories)
        self.color = color

    def __str__(self):
        """Print all parameters """
        return 'Onion:' + self.weight + self.calories + self.color
