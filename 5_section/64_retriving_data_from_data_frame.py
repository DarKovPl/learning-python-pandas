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
print('------------------------------------------------')
