class Node:
    def __init__(self, food_type, name=None, rating=None, price=None, address=None, next_node=None):
        self.food_type = food_type
        self.name = name
        self.rating = rating
        self.price = price
        self.address = address
        self.next_node = next_node

    def set_next_node(self, node):
        self.next_node = node

    def get_next_node(self):
        return self.next_node

    def get_food_type(self):
        return self.food_type

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_price(self):
        return self.price

    def get_address(self):
        return self.address
