import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)

print('1')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[73] : "
      f"\n{one_series[73]}")
print('------------------------------------------------')

print('2')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[[64, 73]] : "
      f"\n{one_series[[64, 73]]}")
print('------------------------------------------------')

print('3')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[2:7] : "
      f"\n{one_series[2:7]}")
print('------------------------------------------------')

print('4')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[795:] : "
      f"\n{one_series[795:]}")
print('------------------------------------------------')

print('5')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[795:799] : "
      f"\n{one_series[795:799]}")
print('------------------------------------------------')

print('6')

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True))[-2:] : "
      f"\n{one_series[-2:]}")
print('------------------------------------------------')
