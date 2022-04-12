import pandas as pd

numbers = [1, 2, 3, 11, 12, 13]
print(numbers)
print('------------------------------------------------')

print('1')
num_series = pd.Series(numbers)
print(f'num_series > 10: \n{num_series > 10}')
print('------------------------------------------------')

print('2')
print(f'num_series.where(num_series > 10) : \n{num_series.where(num_series > 10)}')
print('------------------------------------------------')

print('3')
print(f'num_series.where(num_series > 10, other=-1) : \n{num_series.where(num_series > 10, other=-1)}')
print('------------------------------------------------')

print('4')
print(f'num_series.where(num_series > 10).dropna() : \n{num_series.where(num_series > 10).dropna()}')
print('------------------------------------------------')

print('5')
num_series.where(num_series > 10, inplace=True)
print(f'num_series.where(num_series > 10, inplace=True) : \n{num_series}')
print('------------------------------------------------')

print('6')
num_series.dropna(inplace=True)
print(f'num_series.dropna(inplace=True) : \n{num_series}')
print('------------------------------------------------')

num_series = pd.Series(numbers)
print('-------After rebuild num_series------')

print('7')
print(f'num_series.filter(items=[0, 2, 4]) : \n{num_series.filter(items=[0, 2, 4])}')  # filtering by index
print('------------------------------------------------')

print('8')
print(f'num_series.filter(items=[0, 2, 4]) : \n{num_series.filter(items=[0, 2, 4])}')
print('****************First************************')

# Laboratory

numbers = [14, 334, 312, 5823, 9491, 7486, 4343]
age = ['6', '7-14', '15-17', '18-24', '25-39', '40-59', '60']

incidents = pd.Series(index=age, data=numbers)
print(incidents)
print('**************')

print('1')

print(f'incidents.where(incidents > 1000) : \n{incidents.where(incidents > 1000)}')
print(f'incidents.where(incidents > 1000, other=-1) : \n{incidents.where(incidents > 1000, other=-1)}')
print('**************')

print('2')

incidents_1000 = incidents.where(incidents > 1000, other=-1)
print(incidents_1000)
print('**************')

print('3')

print(incidents)
print(f"incidents.filter(items=['18-24', '25-39', '40-59']) : \n{incidents.filter(items=['18-24', '25-39', '40-59'])}")
print('**************')

print('4')

print(f"incidents.where(incidents <= 1000).dropna() : \n{incidents.where(incidents <= 1000).dropna()}")
print('**************')
