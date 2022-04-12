import pandas as pd
import random as rnd

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
print('***********************FIRST*************************')

# Laboratory

data_as_float_list = [i * rnd.random() for i in range(100000)]
data_as_float_series = pd.Series(data_as_float_list)

print('1')
print(f'data_as_float_series.size : \n{data_as_float_series.size}')
print('************')

print('2')
print(f'data_as_float_series.nbytes : \n{data_as_float_series.nbytes}')
print(f'data_as_float_series.memory_usage(deep=True) : \n{data_as_float_series.memory_usage(deep=True)}')
print('************')

print('3')
print(f'data_as_float_series.shape : \n{data_as_float_series.shape}')
print('************')

print('4')
print(f'data_as_float_series.axes : \n{data_as_float_series.axes}')
print('************')

print('5')
print(f'data_as_float_series.dtype : \n{data_as_float_series.dtype}')
print('************')

print('6')
print(f'data_as_float_series.index : \n{data_as_float_series.index}')
print('************')

print('7')
print(f'data_as_float_series.is_unique : \n{data_as_float_series.is_unique}')
print('************')

print('8')
print(f'data_as_float_series.is_monotonic : \n{data_as_float_series.is_monotonic}')
print('********************SECOND****************************')

data_as_string_list = [str(i * rnd.random()) for i in range(100000)]
data_as_string_series = pd.Series(data_as_string_list)

print('1')
print(f'data_as_string_series.size : \n{data_as_string_series.size}')
print('************')

print('2')
print(f'data_as_string_series.nbytes: \n{data_as_string_series.nbytes}')
print(f'data_as_string_series..memory_usage(deep=True): \n{data_as_string_series.memory_usage(deep=True)}')
print('************')

print('3')
print(f'ata_as_string_series.dtype : \n{data_as_string_series.dtype}')
print('************')
