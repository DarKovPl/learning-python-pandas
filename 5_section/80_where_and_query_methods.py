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
print('*************************************************')

# Laboratory


print('1')

animals = pd.read_csv(
 '../files_to_process/course-files/sleep_time.csv',
 index_col='ID'
).fillna(0)

print(f"{animals.head().to_string()}")
print('*************************************************')

print('4')

herbi = animals['vore'] == 'herbi'
herbi = animals.where(herbi)

print("herbi = animals['vore'] == 'herbi'  :")
print("herbi = animals.where(herbi)")
print(f"len(herbi)  : \n{len(herbi)}")
print(f"len(herbi).dropna()) : \n{len(herbi.dropna())}")
print('*************************************************')

print('5')

carni = animals.where(animals['vore'] == 'carni')

print("carni = animals.where(animals['vore'] == 'carni')")
print(f"len(carni) : \n{len(carni)}")
print(f"len(carni.dropna()) : \n{len(carni.dropna())}")
print('*************************************************')

print('6')

omni = animals['vore'] == 'omni'
omni = animals.where(omni)

print("omni = animals['vore'] == 'omni'")
print("omni = animals.where(omni)")
print(f"len(omni) : \n{len(omni)}")
print(f"len(omni.dropna()) : \n{len(omni.dropna())}")
print('*************************************************')

print('7')

print(f"herbi['sleep_total'].mean() : \n{herbi['sleep_total'].mean()}\n")
print(f"carni['sleep_total'].mean() : \n{carni['sleep_total'].mean()}\n")
print(f"omni['sleep_total'].mean() : \n{omni['sleep_total'].mean()}")
print('*************************************************')

print('8')

print(f"animals.query('sleep_total > 14') : \n{animals.query('sleep_total > 14')}")
print('*************************************************')

print('9')

condition = "sleep_total > 14 & vore == 'herbi'"

print("condition = 'sleep_total > 14 & vore == 'herbi' "' :')
print(f"animals.query(condition) : \n{animals.query(condition)}")
print('*************************************************')


print('9')

condition_1 = "sleep_total > 14 & vore == 'herbi' & bodywt > 1"

print("condition_1 = 'sleep_total > 14 & vore == 'herbi' & bodywt > 1'  :")
print(f"animals.query(condition_1) : \n{animals.query(condition_1)}")
print('*************************************************')
