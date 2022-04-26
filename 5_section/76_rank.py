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
print('************************************************')


#  Laboratory

print('1')

fortune = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv',
    usecols=['Rank', 'Title', 'Employees', 'Profits', 'Assets'],
    index_col='Rank'
)
print(f"fortune.head().to_string() : \n{fortune.head().to_string()}")
print('************************************************')


print('2')

fortune['EmployeesRank'] = fortune['Employees'].rank(ascending=False)

print("fortune['EmployeesRank'] = fortune['Employees'].rank(ascending=False) :")
print(f"{fortune.head().to_string()}")
print('************************************************')

print('4')

fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)

print("fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)  :")
print(f"fortune.head().to_string() : \n{fortune.head().to_string()}")
print('************************************************')


print('6')


print(f"fortune.nlargest(n=3, columns='Assets').head().to_string()  : "
      f"\n{fortune.nlargest(n=3, columns='Assets').head().to_string()}")
print('************************************************')

print('7')

print(f"fortune.nsmallest(n=3, columns='Assets').head().to_string() : "
      f"\n{fortune.nsmallest(n=3, columns='Assets').head().to_string()}")
print('************************************************')
