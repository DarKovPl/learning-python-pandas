import numpy as np
import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(frame.head().to_string() + '\n')

print('1')

print(f'frame.dtypes : \n{frame.dtypes}')
print('------------------------------------------------')

print('2')

print(f"frame.info(memory_usage='deep') : \n{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('3')

frame.loc[1, 'Serving Size'] = np.NaN

print(f"frame.loc[1, 'Serving Size'] = np.NaN : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('4')

frame.loc[2, 'Calories'] = np.NaN

print(f"frame.loc[2, 'Calories'] = np.NaN : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('5')

frame['Calories'].fillna(value=0, inplace=True)

print(f"frame['Calories'].fillna(value=0, inplace=True) : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('6')

frame['Calories'] = frame['Calories'].astype('int32')

print(f"frame['Calories'] = frame['Calories'].astype('int32') : \n{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('7')

frame['Category'] = frame['Category'].astype('category')

print(f"frame['Category'] = frame['Category'].astype('category') : \n{frame.head().to_string()}")
print(f"frame.info(memory_usage='deep') : \n{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('8')

frame['Serving Size'].value_counts()

print(f"frame['Serving Size'].value_counts() : \n{frame['Serving Size'].value_counts()}")
print('------------------------------------------------')

print('9')

frame['Serving Size'] = frame['Serving Size'].astype('category')

print(f"frame['Serving Size'] = frame['Serving Size'].astype('category') : \n{frame.info(memory_usage='deep')}")
print('------------------------------------------------')
