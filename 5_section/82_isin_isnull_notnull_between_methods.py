import numpy as np
import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']

clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})

is_color_blue = clothes['color'] == 'blue'
is_color_green = clothes['color'] == 'green'
is_color_red = clothes['color'] == 'red'

print(f"frame.head().to_string()  : \n{frame.head().to_string()}")
print(f"\nclothes : \n{clothes}")
print('------------------------------------------------')

print('1')

print(f"clothes[is_color_blue | is_color_red | is_color_green] : "
      f"\n{clothes[is_color_blue | is_color_red | is_color_green]}")
print('------------------------------------------------')

print('2')

print(f"clothes['color'].isin(['blue', 'green', 'red']) : "
      f"\n{clothes['color'].isin(['blue', 'green', 'red'])}")
print('------------------------------------------------')

print('3')

my_colors = clothes['color'].isin(['blue', 'green', 'red'])

print("my_colors = clothes['color'].isin(['blue', 'green', 'red'])")
print(f"clothes[my_colors]: "
      f"\n{clothes[my_colors]}")
print('------------------------------------------------')

print('4')

clothes.loc[6, 'size'] = np.NaN

print(f"clothes.loc[6, 'size'] = np.NaN : \n{clothes}")
print(f"\nclothes['size'].notnull() :"
      f"\n{clothes['size'].notnull()}")
print('------------------------------------------------')

print('5')

has_size = clothes['size'].notnull()

print("has_size = clothes['size'].notnull()")
print("clothes[has_size] : "
      f"\n{clothes[has_size]}")
print('------------------------------------------------')

print('6')

size_unknown = clothes['size'].isnull()

print("size_unknown = clothes['size'].isnull()")
print(f"clothes[size_unknown] : \n{clothes[size_unknown]}")
print('------------------------------------------------')

print('7')

print(f"frame.head().to_string()  : \n{frame.head().to_string()}")
print('----------')

calories_between_300_and_400 = frame['Calories'].between(300, 400)

print(f"calories_between_300_and_400.head().to_string() : \n{calories_between_300_and_400.head().to_string()}")
print(f"frame[calories_between_300_and_400].head().to_string() : "
      f"\n{frame[calories_between_300_and_400].head().to_string()}")
print('------------------------------------------------')

