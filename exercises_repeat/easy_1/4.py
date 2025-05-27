# How big is the room?
# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet
def valid_input_float(my_input):
    while True:
        try:
            return float(input(my_input))
        except ValueError:
            print('Enter a valid number!')

width = valid_input_float('Enter the width of the room in meters: ')
length = valid_input_float('Please enter the length of the room in meters: ')
area_in_sqm = width * length
area_in_sqft = area_in_sqm * 10.7639

print(f'The room area is {area_in_sqm:.2f} square meters and {area_in_sqft:.2f} square ft.')