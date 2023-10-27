from restaurantData import restaurant_data
from restaurantTypes import types
from linkedlist import LinkedList
from welcome import welcome

welcome()


# Insert food types into a data structure (LinkedList)
def insert_food_types(food_list):
    food_type_list = LinkedList()
    for food_type in food_list:
        food_type_list.insert_beginning(food_type)
    return food_type_list


# Insert restaurant data into a data structure (LinkedList of LinkedList)
def insert_restau_data(restau_data, foot_list):
    restaurant_data_list = LinkedList()
    for food_type in foot_list:
        restaurant_sublist = LinkedList()
        for restau in restau_data:
            if restau[0] == food_type:
                restaurant_sublist.insert_beginning(restau)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list


my_food_list = insert_food_types(types)
my_restaurant_list = insert_restau_data(restaurant_data, types)


selected_food_type = ""

# Code for user prompt