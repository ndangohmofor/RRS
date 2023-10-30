from welcome import welcome
from linkedlist2 import LinkedList
from restaurantData import restaurant_data
from restaurantTypes import types


def insert_food_types(food_types_list):
    food_type_list = LinkedList()
    for food_type in food_types_list:
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


my_food_type_list = insert_food_types(types)
my_restaurant_list = insert_restaurant_data(restaurant_data, types)

welcome()

selected_food_type = ""

while len(selected_food_type) == 0:
    user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here\n"
    )).lower()

    food_type_matches = []

    food_type_list_head = my_food_type_list.get_head_node()

    while food_type_list_head:
        if str(food_type_list_head.get_food_type()).startswith(user_input):
            food_type_matches.append(food_type_list_head.get_food_type())
        food_type_list_head = food_type_list_head.get_next_node()

    # print the list of matching food types
    for food_type in food_type_matches:
        print(food_type)

    # if only one type of restaurant is found, ask the user if they would like to display this restaurant