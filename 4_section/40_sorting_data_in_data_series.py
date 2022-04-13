import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'

one_series = pd.read_csv(path_to_file, usecols=['Name']).squeeze().head(5)

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
print('************************************************')


# Laboratory

salary = pd.read_csv(
      '../files_to_process/course-files/StackOverflowDeveloperSurvey.csv',
      usecols=['Salary']
).squeeze().dropna()

print('1')

print(f'salary.head() : \n{salary.head()}')
print('************************************************')

print('2')

print(f'salary.sort_values(ascending=False).head() : \n{salary.sort_values(ascending=False).head()}')
print('************************************************')

print('3')

print(f'salary.sort_values().head() : \n{salary.sort_values().head()}')
print('************************************************')

print('4 - salary.sort_values(inplace=True, ascending=False)')

salary.sort_values(inplace=True, ascending=False)
print(f'salary.head() : \n{salary.head()}')
print('************************************************')

print('5 - salary.sort_index(inplace=True, ascending=True) ')

salary.sort_index(inplace=True, ascending=False)
print(f'salary.sort_values().head() : \n{salary}')
print('************************************************')

print('6')

salary.sort_values(inplace=True, ascending=False)
print(f'salary.head() : \n{salary.head()}')
print('************************************************')

print('7')

max_salaries = salary.sort_values(ascending=False).head(100)

print(f'max_salaries = salary.sort_values(ascending=False).head(100) : \n{max_salaries}')
print('************************************************')

print('7')

min_salaries = salary.sort_values().head(100)

print(f'min_salaries = salary.sort_values().head(100) : \n{min_salaries}')
print('************************************************')

print('8')

print(f'max_salaries.mean() : \n{max_salaries.mean()}')
print('************************************************')

print('9')

print(f'min_salaries.mean() : \n{min_salaries.mean()}')
print('************************************************')
