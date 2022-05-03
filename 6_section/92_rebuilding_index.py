import pandas as pd


frame = pd.read_csv(
    '../files_to_process/course-files/mammals.csv'

)

print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('1')

frame.set_index('name', inplace=True)

print("frame.set_index('name')")
print(f"frame.head() : \n{frame.head()}")
print('------------------------------------------------')

print('2')

frame.reset_index(inplace=True)

print("frame.reset_index(inplace=True)")
print(f"{frame.head()}")
print('------------------------------------------------')

print('3')

frame.set_index('name', inplace=True)
frame.sort_index(inplace=True)

print("frame.set_index('name', inplace=True)")
print("frame.sort_index(inplace=True)")
print(f"frame.head(10) : \n{frame.head(10)}")
print('------------------------------------------------')

print('4')

print(f"frame['Cat': 'Donkey'] : \n{frame['Cat': 'Donkey']}")
print('------------------------------------------------')

print('5')

print(f"frame[:'Cat'] : \n{frame[:'Cat']}")
print('------------------------------------------------')

print('6')

print(f"frame['B': 'G'] : \n{frame['B': 'G']}")
print('************************************************')

# Laboratory

print('1')

fortune = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv'
)

print(f"fortune.head(7) : \n{fortune.head(7)}")
print('************************************************')

print('2')

fortune.set_index('Rank', inplace=True)
print(f"fortune.head() : \n{fortune.head()}")
print('************************************************')

print('3')

print(f"fortune[99:105] : \n{fortune[99:105]}")
print('************************************************')

print('4 -----LOC-------')


print(f"fortune.loc[99: 105][['Title', 'Employees']] : \n{fortune.loc[99: 105][['Title', 'Employees']]}")
print('************************************************')

print('5')

fortune.reset_index(inplace=True)
fortune.set_index('Title', inplace=True)

print("fortune.reset_index(inplace=True)")
print("fortune.set_index('Title', inplace=True)")
print(f"fortune.head() : \n{fortune.head()}")
print('************************************************')

print('6')

fortune.sort_index(inplace=True)

print("fortune.sort_index(inplace=True)")
print(f"fortune.head() : \n{fortune.head()}")
print('************************************************')

print('7')

print(f"fortune['X': 'Y'] : \n{fortune['X': 'Y']}")
print('************************************************')
