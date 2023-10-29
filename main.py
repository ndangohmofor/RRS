from restaurantData import restaurant_data
from restaurantTypes import types
from linkedlist import LinkedList
from welcome import welcome


# Insert food types into a data structure (LinkedList)
def insert_food_types(food_list):
    food_type_list = LinkedList()
    for food_type in food_list:
        food_type_list.insert_beginning(food_type)
    return food_type_list


# Insert restaurant data into a data structure (LinkedList of LinkedList)
def insert_restau_data(restau_data, food_list):
    restaurant_data_list = LinkedList()
    for food_type in food_list:
        restaurant_sublist = LinkedList()
        for restau in restau_data:
            if restau[0] == food_type:
                restaurant_sublist.insert_beginning(restau)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list


my_food_list = insert_food_types(types)
my_restaurant_list = insert_restau_data(restaurant_data, types)

welcome()

selected_food_type = ""

# Code for user prompt
while len(selected_food_type) == 0:
    user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here\n"
    )).lower()

    # Search for user_input in food types data structure
    matches_types = []
    type_list_head = my_food_list.get_head_node()

    while type_list_head:
        if str(type_list_head.get_value()).startswith(user_input):
            matches_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    # print the list of matching food types
    for food in matches_types:
        print(food)

    # Check if only one type of restaurant was found. Ask user if they would like to select this type
    if len(matches_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matches_types[0] + ". \nDo you want to look at " + matches_types[0] + "restaurants?"
            "Enter y for yes and n for no\n"
        )).lower()

        # Retrieve the restaurant data here
        if select_type == "y":
            selected_food_type = matches_types[0]
            print("Selected Food Type: " + selected_food_type)
            restaurant_list_head = my_restaurant_list.get_head_node()

            while restaurant_list_head.get_next_node():
                sublist_head = restaurant_list_head.get_value().get_head_node()

                if sublist_head.get_value()[0] == selected_food_type:
                    while sublist_head.get_next_node():
                        print("-----------------------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("-----------------------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                restaurant_list_head = restaurant_list_head.get_next_node()

            # Ask customer if they will like to search for other types of restaurants
            repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for n.\n")).lower()
            if repeat_loop == 'y':
                selected_food_type = ""