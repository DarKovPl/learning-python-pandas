import pandas as pd

print('1')
path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'
first_series = pd.read_csv(path_to_file, usecols=['Name', 'Attack'], index_col='Name').squeeze()



print('------------------------------------------------')