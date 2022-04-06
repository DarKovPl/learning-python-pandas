import pandas as pd

numbers = [1, 2, 3, 11, 12, 13]
num_series = pd.Series(numbers)

print('1')
print(f'num_series > 10 : {num_series > 10}')
print('------------------------------------------------')

print('2')
print(f'num_series % 2 == 1 : {num_series % 2 == 1}')
print('------------------------------------------------')

print('3')
print(f'num_series.where(num_series > 10).dropna() : \n{num_series.where(num_series > 10).dropna()}')
print('------------------------------------------------')

print('4')
print(f'num_series.where(num_series % 2 == 1).dropna() : \n{num_series.where(num_series % 2 == 1).dropna()}')
print('------------------------------------------------')

print('5')
numbers_greater_10 = num_series > 10
numbers_odd = num_series % 2 == 1


print(f'num_series.where(numbers_greater_10 & numbers_odd) : \n{num_series.where(numbers_greater_10 & numbers_odd)}\n')

print(f'num_series.where(numbers_greater_10 & numbers_odd).dropna() : '
      f'\n{num_series.where(numbers_greater_10 & numbers_odd).dropna()}')
print('------------------------------------------------')

print('6')
print(f'num_series.between(3, 12) : \n{num_series.between(3, 12)}')
print('------------------------------------------------')

print('7')
print(f'num_series.where(num_series.between(3, 12)): \n{num_series.where(num_series.between(3, 12))}')
print('------------------------------------------------')
