# How big is the room?
# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

length_in_m = float(input('Enter room length in meters: '))
width_in_m = float(input('Enter room width in meters: '))

length_in_ft = 10.7639 * length_in_m
width_in_ft = 10.7639 * width_in_m
area_in_m = length_in_m * width_in_m
area_in_sqft = length_in_ft * width_in_ft

print(f'Area is equals to: {area_in_m} square meters')
print(f'Area is equals to: {round(area_in_sqft, 2)} square feet')


