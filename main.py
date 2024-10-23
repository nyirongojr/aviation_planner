from FlightRoutes import FlightRoutes


class Main:
    # Data scrapped from provided graph
    airport_list = ['JFK', 'HND', 'ICN', 'EWR', 'LGA', 'BGI', 'ORD', 'DSM', 'SFO', 'SAN', 'EYW', 'LHR', 'TLV', 'DEL',
                    'DOH', 'CDG', 'SIN', 'BUD']  # Airport list scrapped from the graph given

    flight_routes = [('EWR', 'HND'), ('HND', 'ICN'), ('ICN', 'JFK'), ('HND', 'JFK'), ('JFK', 'LGA'), ('BGI', 'LGA'),
                     ('ORD', 'BGI'), ('DSM', 'ORD'),
                     ('SFO', 'DSM'), ('SFO', 'SAN'), ('SAN', 'EYW'), ('EYW', 'LHR'), ('LHR', 'SFO'),
                     ('TLV', 'DEL'), ('DEL', 'DOH'), ('DEL', 'CDG'), ('CDG', 'BUD'), ('CDG', 'SIN'), ('SIN', 'CDG')
                     ]  # Routes taken from the graph given

    loop_control = 0

    while loop_control == 0:
        # To ensure the code a user enter is converted to capital and reduce errors
        start_airport = input("\nEnter Starting Airport id using the airport code for me to analyse for you: ").upper()

        if start_airport not in airport_list:
            print(f'Oops!!! {start_airport} airport is not in list. Try another airport code \n')
        else:
            flight_planner = FlightRoutes(airport_list, flight_routes, start_airport)
            result = flight_planner.find_min_routes_to_reach_all()
            # Display result to the user with friendly message
            print(f'Starting from {start_airport}, minimum additional one-way routes needed are: {result} \n')
            user_choice = input('type Q to exit. Or type any letter to  Try again ').upper()

            if user_choice == 'Q':
                loop_control = 1
