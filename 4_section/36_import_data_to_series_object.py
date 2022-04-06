import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

pok_csv = pd.read_csv(path_to_file)

print('1 - DataFrame')
print(f'pok_csv = pd.read_csv(path_to_file) : \n{pok_csv}')
print('------------------------------------------------')

print('2 - DataFrame')
print(f"pd.read_csv(path_to_file, usecols=['Name']) : \n{pd.read_csv(path_to_file, usecols=['Name'])}")
print('------------------------------------------------')

print('3 - DataFrame')
print(f"pd.read_csv(path_to_file, usecols=['Name']) : \n{pd.read_csv(path_to_file, usecols=['Name'])}")
print('------------------------------------------------')

print('4 - DataSeries')
print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)) : "
      f"\n{pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)}")
print('------------------------------------------------')

# print('5')
# data_from_clipboard = pd.read_clipboard(sep=',')
#
# print(f"data_from_clipboard : \n{data_from_clipboard}")
# print('------------------------------------------------')

print('6')
one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).head() : "
      f"\n{one_series.head()}")
print('------------------------------------------------')

print('7')
one_series = pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)

print(f"pd.read_csv(path_to_file, usecols=['Name'], squeeze=True)).tail(10) : "
      f"\n{one_series.tail(10)}")
print('------------------------------------------------')
