from FlightRoutes import FlightRoutes


class Main:
    
    # dummy runs
    airport_list = ['JFK', 'HND', 'ICN', 'EWR', 'LGA', 'BGI', 'ORD', 'DSM', 'SFO', 'SAN', 'EYW', 'LHR', 'TLV', 'DEL',
                    'DOH',
                    'CDG', 'SIN', 'BUD']  # Airport list scrapped from the graph given

    flight_routes = [('EWR', 'HND'), ('HND', 'ICN'), ('ICN', 'JFK'), ('HND', 'JFK'), ('JFK', 'LGA'), ('BGI', 'LGA'),
                     ('ORD', 'BGI'), ('DSM', 'ORD'),
                     ('SFO', 'DSM'), ('SFO', 'SAN'), ('SAN', 'EYW'), ('EYW', 'LHR'), ('LHR', 'SFO'),
                     ('TLV', 'DEL'), ('DEL', 'DOH'), ('DEL', 'CDG'), ('CDG', 'BUD'), ('CDG', 'SIN'), ('SIN', 'CDG')
                     ]  # Routes taken from the graph given

    start_airport = 'ICN'

    flight_planner = FlightRoutes(airport_list, flight_routes, start_airport)

    result = flight_planner.find_min_routes_to_reach_all()

    print(result)
