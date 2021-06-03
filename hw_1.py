stars = {"Alnilam": 27000, "Spica": 22000, "Sun": 6000, "Artur": 4000, "Betelgeuse": 3000}


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


get_key(27000)
get_key(22000)
get_key(6000)
get_key(4000)
get_key(3000)
