import pandas as pd

mc = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',

)
print('1')

print(mc.head().to_string())
print('------------------------------------------------')

print('2')

mc_selected = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Serving Size', 'Calories', 'Calories from Fat', 'TotalFat'],
    index_col='Item'
)

print(mc_selected.head())
print('------------------------------------------------')
