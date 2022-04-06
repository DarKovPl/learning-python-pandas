import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)

print('1 - to dict')
print(f"dict(pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head(5)) : "
      f"\n{dict(one_series.head(5))}")
print('------------------------------------------------')

print('2 - max')
print(f"max(pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))) : "
      f"\n{max(one_series)}")
print('------------------------------------------------')

print('3 - min')
print(f"min(pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))) : "
      f"\n{min(one_series)}")
print('------------------------------------------------')

print('4 - change name of column')
one_series.name = 'Pok name'

print(f"one_series.name = 'Pok name' : "
      f"\n\n{one_series}")
print('------------------------------------------------')