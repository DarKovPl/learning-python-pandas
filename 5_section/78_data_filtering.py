import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(f"{frame.head().to_string()}")
print('------------------------------------------------')

print('1')

print(f"frame['Calories'] >= 400  : \n{frame['Calories'] >= 400}")
print('------------------------------------------------')

print('2')

print(f"(frame['Calories'] >= 400).head().to_string() : \n{(frame['Calories'] >= 400).head().to_string()}")
print('------------------------------------------------')

print('3')

print(f"(frame['TotalFat'] <= 20).head().to_string() : \n{(frame['TotalFat'] <= 20).head().to_string()}")
print('------------------------------------------------')

print('4')

calories_greater_equal_400 = frame['Calories'] >= 400
total_fat_less_equal_20 = frame['TotalFat'] <= 20
is_breakfast = frame['Category'] == 'Breakfast'

print(f"frame[calories_greater_equal_400].head().to_string()  : "
      f"\n{frame[calories_greater_equal_400].head().to_string()}")

print(f"\nframe[total_fat_less_equal_20].head().to_string() : \n{frame[total_fat_less_equal_20].head().to_string()}")
print(f"\nframe[is_breakfast].head().to_string() : \n{frame[is_breakfast].head().to_string()}")
print('------------------------------------------------')

print('5')

print(f"(frame[is_breakfast & calories_greater_equal_400]).head().to_string(): "
      f"\n{(frame[is_breakfast & calories_greater_equal_400]).head().to_string()}")
print('------------------------------------------------')

print('6')

print(f"(frame[is_breakfast & calories_greater_equal_400 & total_fat_less_equal_20]).head().to_string(): "
      f"\n{(frame[is_breakfast & calories_greater_equal_400 & total_fat_less_equal_20]).head().to_string()}")
print('------------------------------------------------')

print('7')

print(f"(frame[~ is_breakfast]).head().to_string(): "
      f"\n{(frame[~ is_breakfast]).head().to_string()}")
print('------------------------------------------------')
