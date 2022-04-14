import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'


print('1')

one_series = pd.read_csv(path_to_file, usecols=['Attack', '#'], index_col='#').squeeze()
print(one_series)

print('------------------------------------------------')

print('2')

second_series = pd.read_csv(path_to_file, usecols=['Name', 'Attack'], index_col='Name').squeeze()
print(second_series)

print('************************************************')

# Laboratory

print('2')

fortune_500 = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv',
    usecols=['Rank', 'Title'],
    index_col='Rank'
).squeeze()

print(f'fortune_500.head() : \n{fortune_500.head()}')
print('************************************************')

print('3')

print(f'fortune_500.head(10) : \n{fortune_500.head(10)}')
print('************************************************')

print('4')

print(f'fortune_500[-20:] : \n{fortune_500[-20:]}')
print('************************************************')
print('5')

fortune_500 = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv',
    usecols=['Title', 'Employees'],
    index_col='Title'
).squeeze()

print(fortune_500)
print('************************************************')

print('6')

print(f"fortune_500.loc[['IBM', 'Alphabet', 'Facebook', 'Apple']] : "
      f"\n{fortune_500.loc[['IBM', 'Alphabet', 'Facebook', 'Apple']]}")
print('************************************************')

print('7')

print(f"fortune_500['IBM':'Intel'] : "
      f"\n{fortune_500['IBM':'Intel']}")
print('************************************************')