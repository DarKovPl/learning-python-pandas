import pandas as pd

path_to_file = r'~/Projects/learning-python-pandas/files_to_process/course-files/pokemon.csv'
first_series = pd.read_csv(path_to_file, usecols=['Name', 'Attack'], index_col='Name').squeeze()

print('1')

print(f"first_series.head() : \n{first_series.head()}")
print('------------------------------------------------')

print('2')

print(f"first_series.count() : \n{first_series.count()}")
print('------------------------------------------------')

print('3')

second_series = pd.read_csv(path_to_file, usecols=['Name', 'Type 2'], index_col='Name').squeeze()
print(f"second_series.value_counts() : \n{second_series.value_counts()}")
print('------------------------------------------------')

print('4')

print(f"first_series.min(): \n{first_series.min()}")
print('------------------------------------------------')

print('5')

print(f"first_series.max(): \n{first_series.max()}")
print('------------------------------------------------')

print('6')

print(f"first_series.idxmin(): \n{first_series.idxmin()}")
print("Returns the index of item with minimal value")

print('-------------------')
print(f'first_series.loc[first_series.idxmin()] : \n{first_series.loc[first_series.idxmin()]}')
print('------------------------------------------------')

print('7')

print(f"first_series.idxmax(): \n{first_series.idxmax()}")
print("Returns the index of item with maximal value")

print('-------------------')
print(f'first_series.loc[first_series.idxmax()] : \n{first_series.loc[first_series.idxmax()]}')
print('------------------------------------------------')

print('8')

print(f"first_series.mean(): \n{first_series.mean()}")
print('------------------------------------------------')

print('9')

print(f"first_series.median(): \n{first_series.median()}")
print('------------------------------------------------')

print('10')

print(f"first_series.std(): \n{first_series.std()}")
print('************************************************')

#  Laboratory

print(2)

programmers = pd.read_csv(
    '../files_to_process/course-files/StackOverflowDeveloperSurvey2018.csv',
    low_memory=False,
    usecols=['ConvertedSalary']
).squeeze().dropna()

print(programmers)
print('************************************************')

print('3')

cleaned_programmers = programmers.where(programmers > 0).dropna()

print(f'cleaned_programmers.mean() : \n{cleaned_programmers.mean()}')
print('************************************************')

print('3')

print(f'cleaned_programmers.median(): \n{cleaned_programmers.median()}')
print('************************************************')

print('3')

print(f'cleaned_programmers.std(): \n{cleaned_programmers.std()}')
print('************************************************')

print('4')

print(f'cleaned_programmers.max(): \n{cleaned_programmers.max()}')
print('************************************************')

print('4')

print(f'cleaned_programmers.max(): \n{cleaned_programmers.max()}')
print('************************************************')

print('5')

fortune_500 = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv',
    usecols=['Title', 'Employees'],
    index_col='Title'
).squeeze()

print(f'fortune_500.head() : \n{fortune_500.head()}')
print('************************************************')

print('6')

print(f'fortune_500.idxmax() : \n{fortune_500.idxmax()}')
print('************************************************')

print('7')

print(f'fortune_500.loc[fortune_500.idxmax()] : \n{fortune_500.loc[fortune_500.idxmax()]}')
print('************************************************')

print('8')

print(f'fortune_500.idxmin() : \n{fortune_500.idxmin()}')
print('************************************************')

print('9')

print(f'fortune_500.loc[fortune_500.idxmin()] : \n{fortune_500.loc[fortune_500.idxmin()]}')
print('************************************************')
