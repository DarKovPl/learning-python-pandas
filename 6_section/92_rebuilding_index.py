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
print('------------------------------------------------')
