import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(frame.head().to_string() + '\n')

print('1')

print(f"frame['Calories'].rank().head() : \n{frame['Calories'].rank().head()}")
print('------------------------------------------------')

print('2')

frame['CaloriesRank'] = frame['Calories'].rank()

print(f"frame['CaloriesRank'] = frame['Calories'].rank():  \n{frame.head().to_string()}")
print('------------------------------------------------')

print('3')

print(f"frame.sort_values(by='Calories').head(20):  \n{frame.sort_values(by='Calories').head(20)}")
print('------------------------------------------------')

print('4')

frame['CaloriesRank'] = frame['Calories'].rank(ascending=False)

print(f"frame['CaloriesRank'] = frame['Calories'].rank(ascending=False):  \n{frame.head().to_string()}")
print(f"frame.sort_values(by='Calories',ascending=False).head(20).to_string():  "
      f"\n{frame.sort_values(by='Calories', ascending=False).head(20).to_string()}")
print('------------------------------------------------')

print('5')

print(f"frame.nlargest(n=3, columns='Calories').to_string() :  \n{frame.nlargest(n=3, columns='Calories').to_string()}")
print('------------------------------------------------')

print('6')

print(f"frame.nsmallest(n=3, columns='Calories').to_string() :\n{frame.nsmallest(n=3, columns='Calories').to_string()}")
print('------------------------------------------------')
