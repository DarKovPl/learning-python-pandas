import pandas as pd

cities = ['London', 'Berlin', 'Warsaw', 'Paris']

print(pd.Series(cities))
print('------------------------------------------------')

prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19)
print(pd.Series(prime_numbers))
print('------------------------------------------------')

logical_values = [True, True, False]
print(pd.Series(logical_values))
print('------------------------------------------------')

spilberg_filmography = {
    '1941': 1979,
    'E.T': 1982,
    'Indiana Jones': 1981,
    'Jaws': 1975
}
print(pd.Series(spilberg_filmography))


