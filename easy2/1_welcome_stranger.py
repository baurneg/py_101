# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, 
# when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", 
# and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions 
# the person's title.

# ExampleCopy Code
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# # Hello, John Q Doe! Nice to have a Master Plumber around.


def greetings(my_list, my_dict):
    name = ''
    occupation = ''
    for word in my_list:
        name += word
        print(name)
    for key in my_dict:
        occupation += key

greeting = ( 
        ["John", "Q", "Doe"],
        {"title": "Master", "occupation": "Plumber"},
)
print(greetings(["John", "Q", "Doe"],
        {"title": "Master", "occupation": "Plumber"}))