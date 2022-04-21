import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',

)

print('1')


print(f'frame.Calories : \n{frame.Calories}')
print('------------------------------------------------')

print('2')

print(f'type(frame.Calories) : \n{type(frame.Calories)}')
print('------------------------------------------------')

print('3')

print(f'frame.Calories.mean() : \n{frame.Calories.mean()}')
print('------------------------------------------------')

print('4')

print(f'frame.Calories.median() : \n{frame.Calories.median()}')
print('------------------------------------------------')

print('5')

print(f'frame.Calories.max() : \n{frame.Calories.max()}')
print('------------------------------------------------')

print('6')

print(f'frame.Calories.idxmax() : \n{frame.Calories.idxmax()}')
print('------------------------------------------------')

print('7')

print(f"frame.Calories.frame.Item['82'] : \n{frame.Item[82]}")
print('------------------------------------------------')

print('8')

print(f"frame.Item[frame.Calories.idxmax()] : \n{frame.Item[frame.Calories.idxmax()]}")
print('------------------------------------------------')

print('9')

print(f"frame['Calories'].head() : \n{frame['Calories'].head()}")
print('------------------------------------------------')

print('10')

s = frame['Item']
print(f"s[242] : \n{s[242]}")
print('------------------------------------------------')

print('11')

print(f"frame.loc[242] : \n{frame.loc[242]}")
print('------------------------------------------------')

print('12')

print(f"type(frame.loc[242]) : \n{type(frame.loc[242])}")
print('------------------------------------------------')

print('13')

print(f"frame.loc[242].loc['Item'] : \n{frame.loc[242].loc['Item']}")
print('------------------------------------------------')

print('14')

print(f"frame[['Item', 'Calories', 'TotalFat']].head() : \n{frame[['Item', 'Calories', 'TotalFat']].head()}")
print('************************************************')


# Laboratory

print('1')

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
    index_col='Vehicle ID'
)

print(f"fuel.head() : \n{fuel.head()}")
print('************************************************')

print('2')

print(f"fuel['Make'].head() : \n{fuel['Make'].head()}")
print('************************************************')

print('3')

print(f"fuel['Make'].value_counts().head() : \n{fuel['Make'].value_counts().head()}")
print('************************************************')

print('4')

print(f"fuel.loc[1873] : \n{fuel.loc[1873]}")
print('************************************************')

print('5')

print(f"fuel.loc[1873, 'Combined MPG (FT1)'] : \n{fuel.loc[1873, 'Combined MPG (FT1)']}")
print('************************************************')

print('6')

print(f"fuel['Combined MPG (FT1)'].max() : \n{fuel['Combined MPG (FT1)'].max()}")
print('************************************************')

print('7')

print(f"fuel['Combined MPG (FT1)'].idxmax() : \n{fuel['Combined MPG (FT1)'].idxmax()}")
print('************************************************')

print('8')

index = fuel['Combined MPG (FT1)'].idxmax()

print(f"index = fuel['Combined MPG (FT1)'].idxmax()")
print(f"fuel.loc[index] : \n{fuel.loc[index]}")
print('************************************************')

print('10')

short_fuel = fuel[['Make', 'Model']]

print("short_fuel = fuel[['Make', 'Model']]")
print(f"short_fuel.head() : \n{short_fuel.head()}")
print('************************************************')