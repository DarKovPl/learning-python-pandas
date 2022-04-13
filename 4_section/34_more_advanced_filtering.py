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
print('************************************************')

# Laboratory


print('1')

name_list = [
    'Albania', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus',
    'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
    'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
    'Luxembourg', 'Macedonia', 'Malta', 'Montenegro', 'Netherlands', 'Norway',
    'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovenia', 'Spain',
    'Sweden', 'Switzerland', 'United', 'Kingdom', 'Turkey', 'Ukraine'
]

energy_list_1 = [
    1947, 8347, 3564, 8369, 4560, 3814, 4623, 6348, 6328, 6506, 16483, 7736,
    7264, 5318, 3876, 51440, 5911, 5494, 3230, 3471, 16830, 3521, 4171, 5420,
    7010, 24891, 3797, 4959, 2551, 6410, 4359, 6521, 5707, 14934, 8175, 2498,
    3550, 5701
]

energy_list_2 = [
    2118, 8507, 3698, 7987, 4762, 3819, 4057, 6305, 6039, 6689, 15687, 7344, 7270,
    5511, 3919, 53203, 5665, 5398, 3588, 3608, 14696, 3626, 4761, 5416, 6871, 23658,
    3899, 4736, 2604, 6617, 4387, 6778, 5573, 14290, 7886, 2794, 3641, 5452
]

print('1')

name_series = pd.Series(data=name_list)
energy_series_1 = pd.Series(data=energy_list_1)
energy_series_2 = pd.Series(data=energy_list_2)

print(f'name_series : \n{name_series}')
print(f'energy_series_1 : \n{energy_series_1}')
print(f'energy_series_2 : \n{energy_series_2}')
print('**********************************************')

print('2')

mean_1 = energy_series_1.mean()
print(f'mean_1 : \n{mean_1}')
print('**********************************************')

print('3')

mean_2 = energy_series_2.mean()
print(f'mean_2 : \n{mean_2}')
print('**********************************************')

print('4')

filter_above_mean_1 = energy_series_1 > mean_1
print(f'filter_above_mean_1 : \n{filter_above_mean_1}')
print('**********************************************')

print('5')

filter_above_mean_2 = energy_series_2 > mean_2
print(f'filter_above_mean_2 : \n{filter_above_mean_2}')
print('**********************************************')

print('6')

print(f'name_series.where(filter_above_mean_1 & filter_above_mean_2) : '
      f'\n{name_series.where(filter_above_mean_1 & filter_above_mean_2).dropna()}')
print('**********************************************')

print('7')

filter_below_mean_1 = energy_series_1 < mean_1
print(f'filter_below_mean_1 : \n{filter_below_mean_1}')
print('**********************************************')

print('8')

print(f'name_series.where(filter_below_mean_1 & filter_above_mean_2) : '
      f'\n{name_series.where(filter_below_mean_1 & filter_above_mean_2)}')
print('**********************************************')
