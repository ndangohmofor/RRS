from welcome import welcome
from linkedlist2 import LinkedList
from restaurantData import restaurant_data
from restaurantTypes import types


def insert_food_types(food_type_list):
    food_type_list = LinkedList()
    for food_type in food_type_list:
        food_type_list.insert_beginning(food_type)
    return food_type_list


def insert_restaurant_data(restau_list, food_type_list):
    restaurant_data_list = LinkedList()
    for food_type in food_type_list:
        restaurant_data_sublist = LinkedList()
        for restaurant in restau_list:
            if restaurant[0] == food_type:
                restaurant_data_sublist.insert_beginning(restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4])
        restaurant_data_list.insert_beginning(restaurant_data_sublist)
    return restaurant_data_list

