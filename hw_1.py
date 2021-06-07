# 1_approach
stars = {
    "Alnilam": 27000, 
    "Spica": 22000, 
    "Sun": 6000, 
    "Artur": 4000, 
    "Betelgeuse": 3000
}

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

# 2_approach

key_list = list(stars.keys())
val_list = list(stars.values())

print(list(stars.keys())[list(stars.values()).index(27000)], "is blue")
print(list(stars.keys())[list(stars.values()).index(22000)], "is white")
print(list(stars.keys())[list(stars.values()).index(6000)], "is yellow")
print(list(stars.keys())[list(stars.values()).index(4000)], "is orange")
print(list(stars.keys())[list(stars.values()).index(3000)], "is red")

# 3 approach

def get_color(temper, color='Currently no name star'):  # get_color function in order to get color name based on value of temperature
    if temper ==22000:
        color = "white"
    elif temper == 27000:
        color = 'blue'
    elif temper== 6000:
        color = 'yellow'
    elif temper == 4000:
        color = 'orange'
    elif temper == 3000:
        color = 'red'
    return color

for star in stars:               # output
   star_color=get_color(stars[star])
   print( f'{star} - {stars[star]} - is {star_color}' )
