import numpy as np
import pandas as pd

frame = pd. read_csv(
    '../files_to_process/course-files/Mcdonalds.csv'
)

print('1')

print(f'frame.head() : \n{frame.head()}')
print('------------------------------------------------')

print('2')
frame.loc[1, 'Calories'] = np.NaN
frame.loc[2, 'TotalFat'] = np.NaN
print(f"frame.loc[1, 'Calories'] = np.NaN\n")
print(f"frame.loc[1, 'Calories'] = np.NaN\n")
print(f'frame.head() : \n{frame.head().to_string()}')
print('------------------------------------------------')

print('3')

print(f'frame.dropna().head().to_string() : \n{frame.dropna().head().to_string()}')
print('------------------------------------------------')

print('4')

print(f"frame.dropna(how='all').head().to_string() : \n{frame.dropna(how='all').head().to_string()}")
print('------------------------------------------------')

print('5')

print(f"frame.dropna(subset=['TotalFat']).head().to_string() : "
      f"\n{frame.dropna(subset=['TotalFat']).head().to_string()}")
print('------------------------------------------------')

print('6')

print(f"frame.dropna(axis='rows').head().to_string() : 0-rows; 1-columns : "
      f"\n{frame.dropna(axis='rows').head().to_string()}")
print('------------------------------------------------')

print('7')

print(f"frame.dropna(axis='columns').head().to_string() : 0-rows; 1-columns : "
      f"\n{frame.dropna(axis='columns').head().to_string()}")
print('------------------------------------------------')
