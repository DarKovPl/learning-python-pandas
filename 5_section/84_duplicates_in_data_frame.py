import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

color = ['green', 'green', 'blue', 'blue', 'red', 'red', 'white']
size = ['S', 'S', 'S', 'M', 'M', 'M', 'L']
gender = ['M', 'W', 'M', 'W', 'M', 'W', 'U']

clothes = pd.DataFrame({'color': color, 'size': size, 'gender': gender})

print(clothes)
print('------------------------------------------------')

print('1')

print(f"clothes['color'].is_unique : \n{clothes['color'].is_unique}")
print('------------------------------------------------')

print('2')

print(f"clothes['color'].unique() : \n{clothes['color'].unique()}")
print('------------------------------------------------')

print('3 - nunique !')

print(f"clothes['color'].nunique() : \n{clothes['color'].nunique()}")
print('------------------------------------------------')

print('4')

print(f"clothes['color'].duplicated(keep='first') : \n{clothes['color'].duplicated(keep='first')}")
print('------------------------------------------------')

print('5')

print(f"clothes['color'].duplicated(keep=False) : \n{clothes['color'].duplicated(keep=False)}")
print('------------------------------------------------')

print('6')

not_unique_values = clothes['color'].duplicated(keep='first')

print(f"unique_values = clothes['color'].duplicated(keep='first')")
print(f"clothes[unique_values] : \n{clothes[not_unique_values]}")
print('------------------------------------------------')

print('7')

print(f"clothes[~ not_unique_values] : \n{clothes[~ not_unique_values]}")
print('------------------------------------------------')

print('8')

print(f"clothes.drop_duplicates(subset=['color'], keep='first') : "
      f"\n{clothes.drop_duplicates(subset=['color'], keep='first')}")
print('------------------------------------------------')

print('9')

print(f"clothes.drop_duplicates(subset=['color', 'size]) : "
      f"\n{clothes.drop_duplicates(subset=['color', 'size'])}")
print('************************************************')

# Laboratory

print('1')

surveys = pd.read_csv(
    '../files_to_process/course-files/StackOverflowDeveloperSurvey2018.csv',
    usecols=['Country', 'Gender', 'OperatingSystem'],
    low_memory=False
)

print(f"{surveys.head().to_string()}")
print('************************************************')

print('2')

print(f"surveys['Country'].is_unique : \n{surveys['Country'].is_unique}")
print('************************************************')

print('3')

countries = surveys['Country'].duplicated()

print("countries = surveys['Country'].duplicated()")
print(f"surveys[~ countries].head(20).to_string() : \n{surveys[~ countries].head(20).to_string()}")
print('************************************************')

print('4')

print(f"surveys['Country'].nunique() : without NaN : \n{surveys['Country'].nunique()}\n")
print(f"len(surveys['Country'].unique()) : with NaN : \n{len(surveys['Country'].unique())}")
print('************************************************')

print('5')

duplicated_keep_first = surveys.duplicated(subset='Country')

print("duplicated_keep_first = surveys['Country'].duplicated(keep='first')")
print(f"duplicated_keep_first : \n{duplicated_keep_first}")
print('************************************************')

print('6')

print(f"surveys[~ duplicated_keep_first] : \n{surveys[~ duplicated_keep_first]}")
print('************************************************')

print('7')

no_duplicates = surveys.drop_duplicates(subset=['Country', 'OperatingSystem'], keep='first')

print("no_duplicates = surveys.drop_duplicates(subset=['Country', 'OperatingSystem'], keep='first')")
print(f"no_duplicates : \n{no_duplicates}")
print('************************************************')

print('9')

condition = "Country == 'Poland'"
print(f"{no_duplicates.query(condition)}")
print('************************************************')
