import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name']).squeeze()

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
print('************************************************')

# Laboratory

print('1')

salary = pd.read_csv(
      '../files_to_process/course-files/StackOverflowDeveloperSurvey.csv',
      usecols=['Salary']
).squeeze().dropna()
print(salary.head())
print('************************************************')

print('2')

print(f'salary.count() : \n{salary.count()}')
print('************************************************')

print('3')

print(f'salary.min(), salary.max() : \n{salary.min(), salary.max()} ')
print('************************************************')

print('4')

print(f'list(salary.head()) : \n{list(salary.head())} ')
print('************************************************')

print('5')

print(f'dict(salary.head()) : \n{dict(salary.head())}')
print('************************************************')

print('6')

list_salary_sorted = salary.sort_values(ascending=False)

print(f'salary.sort_values(ascending=False) : \n{list_salary_sorted}')
print('************************************************')

print('7')

print(f'list_salary_sorted.head() : \n{list_salary_sorted.head()}')
print('************************************************')

print('8')

salary.name = 'Salary of a person'
print(f"salary.name = 'Salary of a person' : \n{salary}")
print('************************************************')
