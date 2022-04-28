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
print('************************************************')

# Laboratory

print('1')

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=[
        'Vehicle ID',
        'Year',
        'Make',
        'Model',
        'Class',
        'Fuel Type',
        'Combined MPG (FT1)',
        'Start Stop Technology'
    ],
)

print(f"fuel.head().to_string() : \n{fuel.head().to_string()}")
print('************************************************')

print('2')

list_of_cars = ['Renault', 'Toyota', 'Ford']
is_in_list = fuel['Make'].isin(list_of_cars)

print("list_of_cars = ['Renault', 'Toyota', 'Ford']")
print("is_in_list = fuel['Make'].isin(list_of_cars)")
print(f"is_in_list.head() : \n{is_in_list.head()}")
print('************************************************')

print('3')

print(f"fuel.loc[is_in_list].head().to_string() : \n{fuel.loc[is_in_list].head().to_string()}")
print('----------')
print(f"fuel[is_in_list].head().to_string() : \n{fuel[is_in_list].head().to_string()}")
print('************************************************')

print('4')

is_no_start_stop_defined = fuel['Start Stop Technology'].isnull()

print("is_no_start_stop_defined = fuel['Start Stop Technology'].isnull()")
print(f"is_no_start_stop_defined.head() : \n{is_no_start_stop_defined.head()}")
print('************************************************')

print('5')

print(f"fuel[is_no_start_stop_defined] : \n{fuel[is_no_start_stop_defined]}")
print('************************************************')

print('6')

is_start_stop_defined = fuel['Start Stop Technology'].notnull()

print(f"is_start_stop_defined : \n{is_start_stop_defined}")
print('************************************************')

print('7')

print(f"fuel[is_start_stop_defined].head().to_string() : \n{fuel[is_start_stop_defined].head().to_string()}")
print('************************************************')

print('8')

mpg50_60 = fuel['Combined MPG (FT1)'].between(50, 60)

print("mpg50_60 = fuel['Combined MPG (FT1)'].between(50, 60)")
print(f"mpg50_60.head() : \n{mpg50_60.head()}")
print('************************************************')

print('9')

print(f"fuel[mpg50_60] : \n{fuel[mpg50_60]}")
print('************************************************')

print('10')

print(f"There are {len(fuel.loc[is_in_list])} cars within the list: {list_of_cars}")
print(f"There are {len(fuel[is_no_start_stop_defined])} cars where Start/Stop technology is not determinated")
print(f"There are {len(fuel[is_start_stop_defined])} cars where Start/Stop technology is determined")
print(f"There are {len(fuel[mpg50_60])} cars with MPG value between 50 and 60.")
print('************************************************')
