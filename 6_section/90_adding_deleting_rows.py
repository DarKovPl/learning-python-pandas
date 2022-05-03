import numpy as np
import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/sleep_time.csv',
    index_col='ID'
)

print('1')

print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('2')

frame.drop(axis=1, columns=['awake', 'brainwt'], inplace=True)

print("frame.drop(axis=1, columns=['awake', 'brainwt'], inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('3')

frame.drop(axis='columns', columns='sleep_cycle', inplace=True)

print("frame.drop(axis='columns', columns='sleep_cycle', inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('4')

frame.drop(columns='sleep_rem', inplace=True)

print("frame.drop(columns='sleep_rem', inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('5')

frame.drop(axis=0, labels=[1, 2], inplace=True)

print("frame.drop(axis=0, labels=[1, 2], inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('6')

frame.drop(axis='rows', labels=3, inplace=True)

print("frame.drop(axis='rows', labels=3, inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('7')

frame.drop(labels=4, inplace=True)

print("frame.drop(labels=4, inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('8')

frame = frame.append(
    {'name': 'Panda_4', 'genus': np.NaN, 'vore': np.NaN, 'order': np.NaN, 'conservation': np.NaN, 'sleep_total': 10},
    ignore_index=True,

)

print("frame = frame.append("
      "{'name': 'Panda_4', 'genus': np.NaN, 'vore': np.NaN, 'order': np.NaN, 'conservation': np.NaN, 'sleep_total': "
      "10}, "
      " ignore_index=True,)")
print(f"frame : \n{frame}")
print('------------------------------------------------')

print('9')

subset = frame[0:5]
frame = frame.append(subset)

print("subset = frame[0:5]")
print("frame = frame.append(subset)")
print(f"frame: \n{frame}")
print('************************************************')

# Laboratory

print('1')

professions = pd.read_csv(
    '../files_to_process/course-files/Prestige.csv'
)

print(f"professions.head() : \n{professions.head()}")
print('************************************************')

print('2')

profession_dict = {
    'name': 'data scientist',
    'education': np.NaN,
    'income': np.NaN,
    'women': np.NaN,
    'prestige': np.NaN,
    'census': np.NaN,
    'type': np.NaN
}

print(f"profession_dict : \n{profession_dict}")
print('************************************************')

print('3')

professions = professions.append(profession_dict, ignore_index=True)

print("professions = professions.append(profession_dict, ignore_index=True)")
print(f"professions.tail() : \n{professions.tail()}")
print('************************************************')

print('4')

taxi = professions[professions['name'] == 'taxi.drivers']

print(f"taxi : \n{taxi}")
print('************************************************')

print('5')

professions.drop(int(taxi.index.values), inplace=True)

print("professions.drop(int(taxi.index.values), inplace=True)")
print(f"professions.tail() : \n{professions.tail()}")
print('************************************************')

print('6')

professions = professions.append(taxi)
professions.sort_index(inplace=True)

print("professions = professions.append(taxi)")
print("professions.sort_index(inplace=True)")
print(f"professions.tail() : \n{professions.tail()}")
print('************************************************')

print('7')

professions.drop(columns='census', inplace=True)

print("professions.drop(columns='census', inplace=True)")
print(f"professions.head() : \n{professions.head()}")
print('************************************************')

print('8')

del professions['type']

print("del professions['type']")
print(f"professions.head() : \n{professions.head()}")
print('************************************************')
