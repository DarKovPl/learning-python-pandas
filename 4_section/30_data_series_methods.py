import pandas as pd

monotonic_list = (1, 2, 4, 67, 99)
monotonic_series = pd.Series(monotonic_list)
print(f'monotonic_series:  \n{monotonic_series}')
print('------------------------------------------------')

print('1')
print(f'.sum(): {monotonic_series.sum()}')
print('------------------------------------------------')

print('2')
print(f'.min(): {monotonic_series.min()}')
print('------------------------------------------------')

print('3')
print(f'.max(): {monotonic_series.max()}')
print('------------------------------------------------')

print('4')
print(f'.mean(): {monotonic_series.mean()}')  # average
print('------------------------------------------------')

print('5')
print(f'.count(): {monotonic_series.count()}')
print('------------------------------------------------')

print('6')
print(f'.product(): {monotonic_series.product()}')  # multiply
print('------------------------------------------------')

print('7')
print(f'.to_list(): {monotonic_series.tolist()}')
print('------------------------------------------------')

print('8')
print(f'.add(): \n{monotonic_series.add(10)}')
print('------------------------------------------------')


currencies = ['USD', 'EUR', 'PLN', 'EUR', 'EUR']
countries = ['USA', 'Spain', 'Poland', 'Portugal', 'Italy']
cur_series = pd.Series(countries, currencies)
print(f'Table series: \n{cur_series}')
print('------------------------------------------------')

dict_country = {'USD': 'USA', 'USD': 'USA'}
print(dict_country)

print('------------------------------------------------')
dict_country = {'USD': 'USA', 'USD': 'Ecuador'}
print(dict_country)
print('********************FIRST*****************************')

# Laboratory

cities = ['Shanghai', 'Beijing', 'Istanbul']
population = [24183300, 20794100, 15030000]

print('1')

city_pop_series = pd.Series(population, cities)
print(f'city_pop_series : \n{city_pop_series}')
print('**************')

print('2')

city_pop_series = pd.Series(index=cities, data=population)
print(f'city_pop_series : \n{city_pop_series}')
print('**************')

print('3')

print(f'city_pop_series.sum() : \n{city_pop_series.sum()}')
print('**************')

print('4')

print(f'city_pop_series.mean() : \n{city_pop_series.mean()}')
print('**************')

print('5')

print(f'city_pop_series.index : \n{city_pop_series.index}')
print(f'city_pop_series.keys() : \n{city_pop_series.keys()}')
print('**************')

print('6')

print(f'city_pop_series.values : \n{city_pop_series.values}')
print(f'pd.__version__ : \n{pd.__version__}')
print('**************')

