import numpy as np
import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv'
)


print('1')
frame.loc[1, 'TotalFat'] = np.NaN
frame.loc[1, 'Saturated Fat'] = np.NaN
frame.loc[2, 'Saturated Fat'] = np.NaN
frame.loc[3, 'Category'] = np.NaN

print(f"frame.loc[1, 'Calories'] = np.NaN")
print(f"frame.loc[1, 'Saturated Fat'] = np.NaN")
print(f"frame.loc[2, 'Saturated Fat'] = np.NaN")
print(f"frame.loc[3, 'Category'] = np.NaN")

print(f'frame.head() : \n{frame.head().to_string()}')
print('------------------------------------------------')

print('2')

print(f'frame.fillna(value=0).head().to_string() : \n{frame.fillna(value=0).head().to_string()}')
print('------------------------------------------------')

print('3')

replace_definition_table = {'Category': 'UNKNOWN', 'TotalFat': 0, 'Saturated Fat': 0}

print(f'frame.fillna(value=replace_definition_table).head().to_string() :'
      f'\n{frame.fillna(value=replace_definition_table).head().to_string()}')
print('------------------------------------------------')

print('4')

print(f"frame['Saturated Fat'].fillna(value=0).head().to_string() : "
      f"\n{frame['Saturated Fat'].fillna(value=0).head().to_string()}")
print('------------------------------------------------')

print('5')

average_total_fat = frame['TotalFat'].mean()
frame["TotalFat"].fillna(average_total_fat, inplace=True)

print(f"average_total_fat = frame['TotalFat'].mean(): "
      f"average_total_fat : {average_total_fat}"
      f"frame['TotalFat'].fillna(average_total_fat, inplace=True)"
      f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('6')

print(f"frame['Saturated Fat'].fillna(method='ffill').head().to_string() : "
      f"\n{frame['Saturated Fat'].fillna(method='ffill').head().to_string()}")
print('------------------------------------------------')

