import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name']).squeeze()

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
print('************************************************')

#  Laboratory

print('1')

surveys = pd.read_csv(
      '../files_to_process/course-files/StackOverflowDeveloperSurvey.csv',
      usecols=['CompanySize']
).squeeze()

print(f'surveys.head() : \n{surveys.head()}')
print('************************************************')

print('2')

print(f'surveys[3] : \n{surveys[3]}')
print('************************************************')

print('3')

print(f'surveys[1:11] : \n{surveys[1:11]}')
print('************************************************')

print('4')

print(f'surveys[12345] : \n{surveys[12345]}')
print('************************************************')

print('5')

print(f'surveys[12341:123456] : \n{surveys[12341:12351]}')
print('************************************************')

print('6')
surveys_copy = surveys[:]

surveys_copy.sort_values(inplace=True)
print(f'surveys_copy.sort_values(inplace=True) : \n{surveys_copy}')
print('************************************************')

print('7')

print(f'surveys[3] : \n{surveys[3]}')
print('************************************************')

print('8')

print(f'surveys[1:11] : \n{surveys[1:11]}')
print('************************************************')

print('9')
surveys.reset_index(drop=True, inplace=True)
print(f'surveys.reset_index(drop=True, inplace=True) : \n{surveys}')
print('************************************************')

