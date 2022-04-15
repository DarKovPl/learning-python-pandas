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
print('------------------------------------------------')
