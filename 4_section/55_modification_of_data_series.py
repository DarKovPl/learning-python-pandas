import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'
first_series = pd.read_csv(path_to_file, usecols=['Name', 'Attack'], index_col='Name').squeeze()

print('1')

print(f"first_series.head() : \n{first_series.head()}")
print('------------------------------------------------')

print('2')

print(f"first_series * 100 : \n{first_series * 100}")
print('--------------------')

first_series_100 = first_series * 100
print(f'first_series_100 = first_series * 100')
print(f'first_series_100.head() : \n{first_series_100.head()}')
print('------------------------------------------------')

second_series = pd.read_csv(path_to_file, usecols=['Name', 'Type 1'], index_col='Name').squeeze()
print(f"--second_series.head(): \n{second_series.head()}")

print('3')

print(f'second_series.str.upper() : \n{second_series.str.upper()}')
print('------------------------------------------------')

print('5')

print("second_series_upper_TYPE = 'TYPE: ' + second_series.str.upper()")
second_series_upper_TYPE = 'TYPE: ' + second_series.str.upper()

print(f'second_series_upper_TYPE : \n{second_series_upper_TYPE}')
print('------------------------------------------------')

print('6')

print(f"second_series.vale_counts().head() : \n{second_series.value_counts().head()}")
print('--------------------')
print('def replace_type(old_type):\n\n')


def replace_type(old_type):
    if old_type == 'Grass' or old_type == 'Ground':
        return 'Nature'
    else:
        return old_type


print(f'second_series.apply(replace_type) : \n\n{second_series.apply(replace_type)}')
print('------------------------------------------------')

print('7')

print(f'second_series.apply(lambda a_text: a_text.upper()) : \n{second_series.apply(lambda a_text: a_text.upper())}')
print('------------------------------------------------')