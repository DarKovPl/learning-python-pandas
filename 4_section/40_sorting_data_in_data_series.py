import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True).head(5)

print('1')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head(5).sort_values() : "
      f"\n{one_series.sort_values()}")
print('------------------------------------------------')

print('2')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head(5).sort_values(ascending=False) : "
      f"\n{one_series.sort_values(ascending=False)}")
print('------------------------------------------------')

print('3')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head(5).sort_index(): "
      f"\n{one_series.sort_index()}")
print('------------------------------------------------')
