from node2 import Node


class LinkedList:
    def __init__(self, food_type=None, name=None, rating=None, price=None, address=None):
        self.head_node = Node(food_type, name, rating, price, address)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_food_type, new_name=None, new_rating=None, new_price=None, new_address=None):
        new_node = Node(new_food_type, new_name, new_rating, new_price, new_address)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, name):
        current_node = self.head_node
        if current_node.get_name() == name:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_next_name() == name:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        string_list += current_node.get_food_type() + " " + current_node.get_name() + " " + current_node.get_rating() + " " + current_node.get_price() + " " + current_node.get_address() + "\n"

