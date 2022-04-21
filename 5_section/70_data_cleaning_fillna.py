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

fuel.loc[27705, 'Class'] = np.NaN
fuel.loc[26561, 'Class'] = np.NaN
fuel.loc[27550, 'Fuel Type'] = np.NaN
fuel.loc[27705, 'Combined MPG (FT1)'] = np.NaN
fuel.loc[27681, 'Combined MPG (FT1)'] = np.NaN
print(f"fuel.head().to_string() : \n{fuel.head().to_string()}")
print('************************************************')

print('4')

print(f"fuel.fillna(value=-1).head().to_string() : \n{fuel.fillna(value=-1).head().to_string()}")
print('************************************************')

print('5')

replace_rules = {'Class': '---', 'Fuel Type': '---', 'Combined MPG (FT1)': -1}

print("replace_rules = {'Class': '---', 'Fuel Type': '---', 'Combined MPG (FT1)': -1}")
print(f"fuel.fillna(value=replace_rules).head().to_string() : \n{fuel.fillna(value=replace_rules).head().to_string()}")
print('************************************************')

print('7')

avg_MPG = fuel['Combined MPG (FT1)'].mean()

print(f"avg_MPG = fuel['Combined MPG (FT1)'].mean() : {avg_MPG}")
print('************************************************')

print('8')

replace_rules = {'Class': '?', 'Fuel Type': '?', 'Combined MPG (FT1)': avg_MPG}

print("replace_rules = {'Class': '?', 'Fuel Type': '?', 'Combined MPG (FT1)': avg_MPG}")
print(f"fuel.fillna(value=replace_rules).head().to_string() :\n{fuel.fillna(value=replace_rules).head().to_string()}\n")
print("OR:   fuel['Class'].fillna('?',inplace=True)")
print('************************************************')

print('10')

fuel['Combined MPG (FT1)'].fillna(method='ffill', inplace=True)

print(f"fuel['Combined MPG (FT1)'].fillna(method='ffill').head().to_string() : \n"
      f"{fuel.head().to_string()}")
print('************************************************')
