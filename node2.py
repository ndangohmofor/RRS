class Node:
    def __init__(self, food_type, name, rating, price, address, next_node=None):
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

    def get_value(self):
        return self.food_type, self.name, self.rating, self.price, self.address
