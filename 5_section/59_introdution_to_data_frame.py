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
print('**********************************************')

# Laboratory

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False
)

print('1')

print(fuel)
print(fuel.head().to_string())
print('**********************************************')

print('3')

print(fuel.head(10))
print('**********************************************')

print('4')

print(fuel.tail(5))
print('**********************************************')

print('5')

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)']
)

print(fuel.head())
print('**********************************************')

print('7')

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
    index_col='Vehicle ID'
)

print(fuel.head())
print('**********************************************')
