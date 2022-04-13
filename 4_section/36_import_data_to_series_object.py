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
print(f"pd.read_csv(path_to_file, usecols=['Name']).squeeze) : "
      f"\n{pd.read_csv(path_to_file, usecols=['Name']).squeeze}")
print('------------------------------------------------')

# print('5')
# data_from_clipboard = pd.read_clipboard(sep=',')
#
# print(f"data_from_clipboard : \n{data_from_clipboard}")
# print('------------------------------------------------')

print('6')
one_series = pd.read_csv(path_to_file, usecols=['Name'])

print(f"pd.read_csv(path_to_file, usecols=['Name']).squeeze().head() : "
      f"\n{one_series.squeeze().head()}")
print('------------------------------------------------')

print('7')
one_series = pd.read_csv(path_to_file, usecols=['Name']).squeeze()

print(f"pd.read_csv(path_to_file, usecols=['Name']).squeeze().tail(10) : "
      f"\n{one_series.tail(10)}")
print('************************************************')

# Laboratory

print('2')

education = pd.read_csv(
      '../files_to_process/course-files/StackOverflowDeveloperSurvey.csv',
      usecols=['FormalEducation']
)
print(education)
print('************************************************')

print('3')

print(type(education))
print('************************************************')

print('4')

print(f'education.head() : \n{education.head()}')
print('************************************************')

print('5')

print(f'education.squeeze() : \n{education.squeeze()}')
print('************************************************')

print('6')

print(f'type(education.squeeze()) : \n{type(education.squeeze())}')
print('************************************************')

print('7')

print(f'education.squeeze().tail(10) : \n{education.squeeze().tail(10)}')
print('************************************************')

print('8')

all_info = pd.read_csv('../files_to_process/course-files/StackOverflowDeveloperSurvey.csv')
print('************************************************')

print('9')

country = all_info['Country'].squeeze()
print(country)
print(type(country))
print('************************************************')

print('10')

print(country.head())
print('************************************************')

print('11')

filter_only_usa = country == 'United States'
print(f"filter_only_usa = country == 'United States' : \n{filter_only_usa}")
print('************************************************')

print('12')

print(f'filter_only_usa.head() : \n{filter_only_usa.head()}')
print('************************************************')

print('13')

print(f'education.where(filter_only_usa) : \n{education.where(filter_only_usa)}')
print('******')
print(f'education.where(filter_only_usa).dropna() : \n{education.where(filter_only_usa).dropna()}')
print('******')
print(f'education.where(filter_only_usa).dropna().head(10) : \n{education.where(filter_only_usa).dropna().head(10)}')
print('************************************************')
