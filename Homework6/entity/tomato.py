from product import Product


class Tomato(Product):
    """Class to create Tomato """

    def __init__(self, weight, calories, sort):
        """Initiate our Tomato """
        super().__init__(weight, calories)
        self.sort = sort

    def __str__(self):
        """Print all parameters """
        return 'Tomato:' + str(self.weight) + str(self.calories) + self.sort
