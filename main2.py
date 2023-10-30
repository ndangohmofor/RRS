from linkedlist2 import LinkedList
from restaurantData import restaurant_data
from restaurantTypes import types
from welcome import welcome


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
                restaurant_data_sublist.insert_beginning(restaurant[0], restaurant[1], restaurant[2], restaurant[3],
                                                         restaurant[4])
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
    if len(food_type_matches) == 1:
        selected_input = str(input(
            "\nThe only matching type for the specified input is " + food_type_matches[
                0] + ". \nDo you want to look at " +
            food_type_matches[0] + "restaurants?"
                                   " Enter y for yes and n for no\n"
        )).lower()
        # if user selects yes, retrieve the restaurant data here
        if selected_input == 'y':
            selected_food_type = food_type_matches[0]
            print("Selected Food Type: " + selected_food_type)
            restaurant_list_head = my_restaurant_list.get_head_node()

            while restaurant_list_head.get_next_node():
                sublist_head = restaurant_list_head.get_food_type().get_head_node().get_next_node()

                if sublist_head.get_food_type() == selected_food_type:
                    while sublist_head.get_next_node():
                        print("-----------------------------------------------------")
                        print("Name: " + sublist_head.get_name())
                        print("Price: " + sublist_head.get_price() + "/5")
                        print("Rating: " + sublist_head.get_rating() + "/5")
                        print("Address: " + sublist_head.get_address())
                        print("-----------------------------------------------------\n")
                        sublist_head = sublist_head.get_next_node()

                restaurant_list_head = restaurant_list_head.get_next_node()

            # Ask the customer if they would like to search for other types of restaurants
            repeat_loop = str(input(
                "\nDo you want to find other restaurants? Enter y for yes and n for no.\n"
            )).lower()
            if repeat_loop == 'y':
                selected_food_type = ''
