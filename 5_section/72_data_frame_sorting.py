import numpy as np
import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(f'frame.head().to_string() : {frame.head().to_string()}')

print('1')

print(f"frame.sort_values(by='Calories').head().to_string() : "
      f"\n{frame.sort_values(by='Calories').head().to_string()}")
print('------------------------------------------------')

print('2')

frame['Calories'] = frame['Calories'].astype('float')
frame.loc[82, 'Calories'] = np.NaN

print(f"frame['Calories'] = frame['Calories'].astype('float') : \n"
      f"frame.loc[82, 'Calories'] = np.NaN\n"
      f"frame.loc[82] : \n{frame.loc[82]}")
print('------------------------------------------------')

print('3')

print(f"frame.sort_values(by='Calories', na_position='first').head().to_string() : "
      f"\n{frame.sort_values(by='Calories', na_position='first').head().to_string()}")
print('------------------------------------------------')

print('4')

print(f"frame.sort_values(by=['Category', 'Item']).head(20).to_string() : "
      f"\n{frame.sort_values(by=['Category', 'Item']).head(20).to_string()}")
print('------------------------------------------------')

print('5')

print(f"frame.sort_values(by=['Category', 'Item'], ascending=[True, False]).head(20).to_string() : "
      f"\n{frame.sort_values(by=['Category', 'Item'], ascending=[True, False]).head(20).to_string()}")
print('------------------------------------------------')

print('6')

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat'],
    index_col='Item'
)

print(f"frame.sort_index(ascending=True).head().to_string() : "
      f"\n{frame.sort_index(ascending=True).head().to_string()}")
print('------------------------------------------------')
