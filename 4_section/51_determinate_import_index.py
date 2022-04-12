import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'


print('1')

one_series = pd.read_csv(path_to_file, usecols=['Attack', '#'], index_col='#').squeeze()
print(one_series)

print('------------------------------------------------')

print('2')

second_series = pd.read_csv(path_to_file, usecols=['Name', 'Attack'], index_col='Name').squeeze()
print(second_series)

print('------------------------------------------------')