import pandas as pd


frame = pd.read_csv(
    '../files_to_process/course-files/mammals.csv'
)

print("1")

print(f"{frame.info(memory_usage='deep')}")
print(f"{frame.head().to_string()}")
print('------------------------------------------------')

print("2")

print(f"frame.columns : \n{frame.columns}")
print('------------------------------------------------')

print("3")

frame.columns = ['name', 'bodyKg', 'brainKg']

print("frame.columns = ['name', 'bodyKg', 'brainKg']")
print(f"frame.head().to_string(): \n{frame.head().to_string()}")
print('------------------------------------------------')

print("4")

new_column_names = {'bodyKg': 'body_kg', 'brainKg': 'brain_kg'}
frame.rename(columns=new_column_names, inplace=True)

print("new_column_names = {'bodyKg': 'body_kg', 'brainKg': 'brain_kg'}")
print("frame.rename(columns=new_column_names, inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print("5")

frame = pd.read_csv(
    '../files_to_process/course-files/mammals.csv',
    index_col='name'
)

print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('6')

frame.rename(index={'Cow': 'Land cow'}, inplace=True)
print("frame.rename(index={'Cow': 'Land cow'}, inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('7')

frame_copy = frame.copy()
frame_copy.loc["Grey wolf", "body"] = 40

print("frame_copy = frame.copy()")
print('frame_copy.loc["Grey wolf", "body"] = 40')
print(f"frame_copy.head().to_string() : \n{frame_copy.head().to_string()}")
print('************************************************')

# Laboratory

print('1')

professions = pd.read_csv(
    '../files_to_process/course-files/Prestige.csv',
    index_col='name'
)

print(f"professions.head() : \n{professions.head()}")
print('************************************************')

print('2')

professions_original = professions.copy()

print(f"professions_original.head(): \n{professions_original.head()}")
print('************************************************')

print('3')

professions.rename(columns={'income': 'income_dollars_per_year'}, inplace=True)

print("professions.rename(columns={'income': 'income_dollars_per_year'}, inplace=True)")
print(f"professions.head().to_string() : \n{professions.head().to_string()}")
print('************************************************')

print('4')

new_column_names_lab = {
    'women': 'women_percent',
    'prestige': 'prestige_indicator'
}

professions.rename(columns=new_column_names_lab, inplace=True)

print("professions.rename(columns=new_column_names_lab, inplace=True)")
print(f"{professions.head().to_string()}")
print('************************************************')

print('5')

index_rename_lab = {
    'accountants': 'bookkeepers',
    'general.managers': 'managers'
}

professions.rename(index=index_rename_lab, inplace=True)

print("professions.rename(index=index_rename_lab, inplace=True)")
print(f"professions.head().to_string() : \n{professions.head().to_string()}")
print('************************************************')

print('6')

print(f"professions.head().to_string() : \n{professions.head().to_string()}\n")
print(f"professions_original.head().to_string() : \n{professions_original.head().to_string()}")
print('************************************************')
