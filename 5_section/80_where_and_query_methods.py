import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(f"frame.head().to_string()  : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('1')

has_more_than_400_cal = frame['Calories'] >= 400

print(f"has_more_than_400_cal.head().to_string() : \n{has_more_than_400_cal.head().to_string()}")
print('------------------------------------------------')

print('2')

print(f"frame.where(has_more_than_400_cal).head().to_string() : "
      f"\n{frame.where(has_more_than_400_cal).head().to_string()}")
print('------------------------------------------------')

print('3 - without where()')

print(f"frame[has_more_than_400_cal].head().to_string() : "
      f"\n{frame[has_more_than_400_cal].head().to_string()}")
print('------------------------------------------------')

print('4')

z = frame.query("Category == 'Desserts'").head().to_string()

print("frame.query('Category == 'Desserts'').head().to_string() : "
      f"\n{z}")
print('------------------------------------------------')

print('5')

z = frame.query("Category in ['Desserts', 'Beverages']").head().to_string()

print("frame.query('Category in ['Desserts', 'Beverages']').head().to_string() : "
      f"\n{z}")
print('------------------------------------------------')

print('6')

z = frame.query("Category == 'Desserts' and Calories < 200").head().to_string()

print("frame.query('Category == 'Desserts' and Calories < 200').head().to_string(): "
      f"\n{z}")
print('------------------------------------------------')
