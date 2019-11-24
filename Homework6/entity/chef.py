from product import Product


class Chef:
    """ Class to create Chef """

    def __init__(self, name, salt):
        """ Initiate our Chef """
        self.name = name
        self.salt = salt

    def get_product_from_salt(self, index):
        return self.salt[index]

    def add_product_in_calt(self, product):
        self.salt.append(product)

    def __str__(self):
        """ Print all parameters """
        return 'Chef:' + self.name + self.salt
