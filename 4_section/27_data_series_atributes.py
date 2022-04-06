import pandas as pd

cities = ['London', 'Berlin', 'Warsaw', 'Paris']

cities_series = pd.Series(cities)
print(cities_series)
print('------------------------------------------------')

print(f'size: {cities_series.size}')
print('------------------------------------------------')

print(f'nbytes:  {cities_series.nbytes}')
print('------------------------------------------------')

print(f'is_uniqe:  {cities_series.is_unique}')
print('------------------------------------------------')

print(f'is_monotonic:  {cities_series.is_monotonic}')
print('------------------------------------------------')

print(f'index:  {cities_series.index}')
print('------------------------------------------------')

print(f'.vales :  {cities_series.values}')
print('------------------------------------------------')

print(f'.dtype :  {cities_series.dtype}')
print('------------------------------------------------')

print(f'.shape :  {cities_series.shape}')
print('------------------------------------------------')

print(f'.axes :  {cities_series.axes}')
print('------------------------------------------------')

string_list = ['Cola', 'Redbull', 'Sprite']
string_series = pd.Series(string_list)
print(string_series)

print('-----')
print(f'.is_monotonic :  {string_series.is_monotonic}')
print(f'.is_monotonic_increasing :  {string_series.is_monotonic_increasing}')
print(f'.is_monotonic_decreasing :  {string_series.is_monotonic_decreasing}')
print('------------------------------------------------')


