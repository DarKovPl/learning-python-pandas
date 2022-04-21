import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=[
        'Item',
        'Category',
        'Calories',
        'TotalFat',
        'Sugars',
        'Protein',
        'Cholesterol'
    ]

)

print('1')

print(f'frame.head() : \n{frame.head()}')
print('------------------------------------------------')

print('2')

print(f'frame.TotalFat.head() : \n{frame.TotalFat.head()}')
print('------------------------------------------------')

print('3')

print(f'frame.TotalFat.head() : \n{frame.TotalFat.head()}')
print('------------------------------------------------')

print('4')

frame["TotalFat_0"] = 0
print(f'frame.TotalFat_0.head() : \n{frame.TotalFat_0.head()}')
print('------------------------------------------------')

print('5')

sugar_and_fat = frame.Sugars + frame.TotalFat
frame["sugar_and_fat"] = sugar_and_fat

print(f'sugar_and_fat = frame.Sugars + frame.TotalFat : \n'
      f'frame["sugar_and_fat"] = sugar_and_fat : \n{frame.head()}')
print('------------------------------------------------')

print('6')

frame["SugarAndProtein"] = frame.Sugars + frame.Protein
print(f'frame["SugarAndProtein"] = frame.Sugar + frame.Protein : \n{frame.head()}')
print('------------------------------------------------')

print('7')

frame.insert(loc=1, column='SPF', value=frame.Sugars + frame.Protein + frame.TotalFat)
print(f'frame.head() : \n{frame.head()}')
print('------------------------------------------------')

print('8')

del frame["SugarAndProtein"]
print(f'del frame["SugarAndProtein"] : \n{frame.head()}')
print('------------------------------------------------')

print('9')

frame = frame.drop(columns=["sugar_and_fat"])
print(f'frame = frame.drop(columns=["sugar_and_fat"]) : \n{frame.head()}')
print('************************************************')

# Laboratory

print('1')

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)']
)

print(f"fuel.head() : \n{fuel.head()}")
print('************************************************')

print('2')

kilometre_range = fuel['Combined MPG (FT1)'] * 1.609 / 3.78
fuel['Combined KPL'] = kilometre_range

print("kilometre_range = fuel['Combined MPG (FT1)'] * 1.609 / 3.78")
print("fuel['Combined KPL'] = kilometre_range")
print(f"fuel.head(10).to_string() : \n{fuel.head(10).to_string()}")
print('************************************************')

print('4')

fuel.insert(loc=4, column='liters per km', value=100 / fuel['Combined KPL'])

print("fuel.insert(loc=4, column='liters per km', value=100 / fuel['Combined KPL'])")
print(f"fuel.head().to_string() : \n{fuel.head().to_string()}")
print('************************************************')

print('6')

fuel.drop(columns=['Combined MPG (FT1)'], inplace=True)
print(f"{fuel.head().to_string()}")
print('************************************************')

print('7')

del fuel['Combined KPL']
print("del fuel['Combined KPL']")
print(f"fuel.head().to_string() : \n{fuel.head().to_string()}")
