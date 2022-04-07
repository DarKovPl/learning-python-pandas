import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True).head()

print('1')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head().index : "
      f"\n{one_series.index}")
print('------------------------------------------------')

print('2')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head().values : "
      f"\n{one_series.values}")
print('------------------------------------------------')

print('3')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head().values : "
      f"\n{one_series.values}\n")

print(f"'Venusaur' in one_series.values : "
      f"\n{'Venusaur' in one_series.values}")
print('------------------------------------------------')
