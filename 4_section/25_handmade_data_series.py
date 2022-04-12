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
print('*************************************************')

# Laboratory

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

week_days_data_series = pd.Series(data=week_days)
print(week_days_data_series)
print('------------------------------------------------')

free_days = [False, False, False, False, False, True, True]
free_days_series = pd.Series(free_days)
print(free_days_series)
print('------------------------------------------------')

holidays = {'New_year': '2022-01-01', 'Epiphany': '2022-01-06', 'Easter': '2022-04-17'}
holidays_series = pd.Series(data=holidays)
print(holidays_series)