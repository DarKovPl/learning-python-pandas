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
