import json
from json.decoder import JSONDecoder

class Vehicle:

    def __init__(self, reg_num, prod_year, passenger_vehicle, mass):
        self.reg_num = reg_num
        self.prod_year = prod_year
        self.passenger_vehicle = passenger_vehicle
        self.mass = mass


class VehicleEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self, w)

class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)
    
    def decode_vehicle(self, d):
        return Vehicle(**d)


def get_input():
    print('What can I do for you?\n1 - Produce a Json String describing a vehicle\n2 - Decode a Json string into vehicle data')
    choice = input('Type 1 or 2: ')
    while choice not in ['1', '2']:
        print('Please type 1 or 2 only.')
        choice = input('Type 1 or 2: ')
    
    if choice == '1':
        inputs = ask_for_info()
        try:
            new_json = json.dumps(inputs, cls=VehicleEncoder)
        except Exception as e:
            print(e)
        print(f'Resultant Json String: {new_json}')

    elif choice == '2':
        json_string = input('Enter a Json String to be decoded: ')
        try:
            raw_data = json.loads(json_string, cls=VehicleDecoder)
        except Exception:
            print('Invalid Json String')
        print(f'Output raw data: {raw_data.__dict__}')

def ask_for_info():
    reg_num = input('Enter the vehicle registration number: ')
    try:
        prod_year = int(input('Enter the production year: '))
    except TypeError:
        print('Production year must be integer')

    passenger_vehicle = input('Carries passengers? (y/n): ').lower().strip()
    while passenger_vehicle not in ['y', 'n']:
        print('Invalid input, please press "y" or "n"')
        passenger_vehicle = input('Carries passengers? (y/n): ')
    if passenger_vehicle == 'y':
        passenger_vehicle = True
    else:
        passenger_vehicle = False
    
    try:
        mass = float(input('Enter vehicle mass: '))
    except TypeError:
        print('Invalid mass, please enter a valid float or int.')
    
    return {'reg_num': reg_num, 'prod_year': prod_year, 'passenger_vehicle': passenger_vehicle, 'mass': mass}

get_input()

