import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Insurance.csv'
)

print('1')

print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('2')

print(f"frame.loc[2, 'Claims'] : \n{frame.loc[2, 'Claims']}")
print('------------------------------------------------')

print('3')

frame.loc[2, "Claims"] = 19

print('frame.loc[2, "Claims"] = 19')
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('4')

frame.loc[2, "Claims"] += 1

print('frame.loc[2, "Claims"] += 1')
print(f"{frame.head().to_string()}")
print('------------------------------------------------')

print('5')

print(f"frame['Age'] == '<25'  : \n{frame['Age'] == '<25'}")
print('------------------------------------------------')

print('6')

is_younger_than_25 = frame['Age'] == '<25'

print("is_younger_than_25 = frame['Age'] == '<25'")
print(f"frame.where(is_younger_than_25) : \n{frame.where(is_younger_than_25)}")
print('------------------------------------------------')

print('7')

print(f"frame.where(is_younger_than_25).dropna()  : \n{frame.where(is_younger_than_25).dropna()}")
print('------------------------------------------------')

print('8')

print(f"frame[is_younger_than_25].head() : \n{frame[is_younger_than_25].head()}")
print('------------------------------------------------')

print('9')

print(f"frame.loc[is_younger_than_25, 'Holders'].head() : \n{frame.loc[is_younger_than_25, 'Holders'].head()}")
print('------------------------------------------------')

print('10')

print(f"(frame.loc[is_younger_than_25, 'Holders'] + 100).head() : "
      f"\n{(frame.loc[is_younger_than_25, 'Holders'] + 100).head()}")
print('------------------------------------------------')

print("11")

frame.loc[is_younger_than_25, "Holders"] += 1000

print('frame.loc[is_younger_than_25, "Holders"] += 1000')
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')
