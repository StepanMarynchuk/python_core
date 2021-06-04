stars = {"Alnilam": 27000, "Spica": 22000, "Sun": 6000, "Artur": 4000, "Betelgeuse": 3000}

# todo: try to use as a key star name from the stars list, it's a more convenient approach
# or combine this function with for loop to iterate trough the list if stars
def get_key(val):
    for key, value in stars.items():
        if val == value & val == 22000:
            print(key, ', is white')
        elif val == value & val == 27000:
            print(key, ', is blue')
        elif val == value & val == 6000:
            print(key, ', is yellow')
        elif val == value & val == 4000:
            print(key, ', is orange')
        elif val == value & val == 3000:
            print(key, ', is red')
    return 'Currently, it is undefined star'


# todo: to avoide code duplicating you can use for loop for all items in the list
'''
# for item in list:
#     your_fucntion(item)
'''
get_key(27000)
get_key(22000)
get_key(6000)
get_key(4000)
get_key(3000)


# todo: read about PEP8 -> https://www.python.org/dev/peps/pep-0008/ and write your code 
# accordingly to it, code will be more readeble and easy to understand
