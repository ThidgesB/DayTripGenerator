destinations = ['New Orleans', 'Malibu', 'Manhattan', 'Kansas City']
restaurants = ['Big Bubbas Bad BBQ', 'Umi Steakhouse', 'GW Fins', 'Irenes']
transportation = ['Plane', 'Train', 'Automobile', 'Bicycle']
entertainments = ['Art Museum', 'Surfing', 'Musical Concert', 'Escape Room']

import random

#randomizer: takes argument, returns random value
def random_selection(selection):
    random_index = random.randint(0,len(selection)-1)
    result = selection[random_index]
    #print(result)
    return result


#prints random destination, allows user to re-roll destination and returns value
def user_destination_selector():
    destination_complete = False
    keep_destination = False
    while destination_complete == False:
        if keep_destination == False:
            random_destination = random_selection(destinations)
        print(f'The random destination for your generated day trip is : {random_destination}.')
        user_input = input(f'Are you happy with {random_destination} as the selected destination? \nYes or No: ').lower().strip()
        if user_input == 'no':
            print('Okay, let\'s try another.')
            destination_complete = False
            keep_destination = False
        elif user_input == 'yes':
            destination_complete = True 
            print(f'Great! We\'ll lock {random_destination} in as your preferred destination.')
            return random_destination
        else:
            print('Unrecognized input. Please enter Yes or No. Starting over.')
            destination_complete = False
            keep_destination = True

#prints random restaurant, allows user to re-roll restaurant and returns value
def user_restaurant_selector():
    keep_restaurant = False
    restaurant_complete = False
    while restaurant_complete == False:
        if keep_restaurant == False:
            random_restaurant = random_selection(restaurants)
        print(f'The random restaurant for your generated day trip is : {random_restaurant}.')
        user_input = input(f'Are you happy with {random_restaurant} as the selected restaurant? \nYes or No: ').lower().strip()
        if user_input == 'no':
            print('Okay, let\'s try another.')
            restaurant_complete = False
            keep_restaurant = False
        elif user_input == 'yes':
            restaurant_complete = True 
            print(f'Great! We\'ll lock {random_restaurant} in as your preferred restaurant.')
            return random_restaurant
        else:
            print('Unrecognized input. Please enter Yes or No. Starting over.')
            restaurant_complete = False
            keep_restaurant = True

#prints random transportation, allows user to re-roll transportation and returns value
def user_transportation_selector():
    keep_transportation = False
    transportation_complete = False
    while transportation_complete == False:
        if keep_transportation == False:
            random_transportation = random_selection(transportation)
        print(f'The random mode of transportation for your generated day trip is : {random_transportation}.')
        user_input = input(f'Are you happy with {random_transportation} as the selected mode of transportation? \nYes or No: ').lower().strip()
        if user_input == 'no':
            print('Okay, let\'s try another.')
            transportation_complete = False
            keep_transportation = False
        elif user_input == 'yes':
            transportation_complete = True 
            print(f'Great! We\'ll lock {random_transportation} in as your preferred mode of transportation.')
            return random_transportation
        else:
            print('Unrecognized input. Please enter Yes or No. Starting over.')
            transportation_complete = False
            keep_transportation = True

#prints random entertainment, allows user to re-roll entertainment and returns value
def user_entertainment_selector():
    keep_entertainment = False
    entertainment_complete = False
    while entertainment_complete == False:
        if keep_entertainment == False:
            random_entertainment = random_selection(entertainments)
        print(f'The random entertainment for your generated day trip is : {random_entertainment}.')
        user_input = input(f'Are you happy with {random_entertainment} as the selected entertainment? \nYes or No: ').lower().strip()
        if user_input == 'no':
            print('Okay, let\'s try another.')
            entertainment_complete = False
            keep_entertainment = False
        elif user_input == 'yes':
            entertainment_complete = True 
            print(f'Great! We\'ll lock {random_entertainment} in as your preferred entertainment.')
            return random_entertainment
        else:
            print('Unrecognized input. Please enter Yes or No. Starting over.')
            entertainment_complete = False
            keep_entertainment = True

#generates random day trip, allows user to re-roll specific values, confirms trip
def finalize_day_trip():

    day_trip_finalized = False
    final_destination = user_destination_selector()
    final_restaurant = user_restaurant_selector()
    final_transportation = user_transportation_selector()
    final_entertainment = user_entertainment_selector()

    while day_trip_finalized == False:

        print('Your randomly generated day trip is as follows:')
        print(f'Destination: {final_destination}. \nRestaurant: {final_restaurant}. \nTransportation: {final_transportation}. \nEntertainment: {final_entertainment}.')
        user_answer = input('Are you ready to confirm your Day Trip? Yes or No. ')

        if user_answer == 'no':
            valid_input = False
            while valid_input == False:
                user_input = input('What would you like to change? Please type 1 for Destination, 2 for restaurant, 3 for transportation, and 4 for entertainment.')
                if user_input == '1':
                    final_destination = user_destination_selector()
                    valid_input = True
                elif user_input == '2':
                    final_restaurant = user_restaurant_selector()
                    valid_input = True
                elif user_input == '3':
                    final_transportation = user_transportation_selector()
                    valid_input = True
                elif user_input == '4':
                    final_entertainment = user_entertainment_selector()
                    valid_input = True
                else:
                    print('Input not recognized. please enter a number that is 1-4.')
                    valid_input = False

        elif user_answer == 'yes':
            day_trip_finalized = True
            print('Okay! Your randomly generated Day Trip has been confirmed.')
            print(f'Destination: {final_destination}. \nRestaurant: {final_restaurant}. \nTransportation: {final_transportation}. \nEntertainment: {final_entertainment}.')
            print('Have Fun!')

        else:
            print('Unrecognized input. Please enter Yes or No.')
            day_trip_finalized = False

finalize_day_trip()