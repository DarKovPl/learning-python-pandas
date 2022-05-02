import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/PublicTransitExpenses.csv',
    usecols=['Agency', 'Reporter Type', 'Total Operating Expenses']
)

print(f"{frame.head().to_string()}")
print('------------------------------------------------')

print('1')

print(f"frame['Agency'].str.contains('Washington') : \n{frame['Agency'].str.contains('Washington')}")
print('------------------------------------------------')

print('2')

print(f"frame[frame['Agency'].str.contains('Washington')] : \n{frame[frame['Agency'].str.contains('Washington')]}")
print('------------------------------------------------')

print('3')

print(f"frame['Agency'].str.lower() : \n{frame['Agency'].str.lower()}")
print('------------------------------------------------')

print('4')

print(f"frame['Agency'].str.lower().str.endswith('ferries') : \n{frame['Agency'].str.lower().str.endswith('ferries')}")
print('------------------------------------------------')

print('5')

print(f"frame[frame['Agency'].str.lower().str.endswith('ferries')] : "
      f"\n{frame[frame['Agency'].str.lower().str.endswith('ferries')]}")
print('------------------------------------------------')

print('6')

ends_with_ferries = frame['Agency'].str.lower().str.strip().str.endswith('ferries')

print("ends_with_ferries = frame['Agency'].str.lower().str.strip().str.endswith('ferries')")
print(f"frame[ends_with_ferries] : \n{frame[ends_with_ferries]}")
print('------------------------------------------------')

print('7')

frame.set_index('Agency', inplace=True)

print("frame.set_index('Agency', inplace=True)")
print(f"frame.head() : \n{frame.head()}")
print('------------------------------------------------')

print('8')

frame.index = frame.index.str.strip().str.upper()

print("frame.index = frame.index.str.strip().str.upper()")
print(f"frame.head() : \n{frame.head()}")
print('------------------------------------------------')

print('9')

print(f"frame['Reporter Type'].value_counts().head() : \n{frame['Reporter Type'].value_counts().head()}")
print('------------------------------------------------')

print('10')

print(f"frame['Reporter Type'].str.split(' ').head() : \n{frame['Reporter Type'].str.split(' ').head()}")
print('------------------------------------------------')

print('11')

print(f"frame['Reporter Type'].str.split(' ', expand=True).head() : "
      f"\n{frame['Reporter Type'].str.split(' ', expand=True).head()}")
print('------------------------------------------------')

print('12')

frame[['Reporter_Type_1', 'Reporter_Type_2']] = frame['Reporter Type'].str.split(' ', expand=True)

print("frame[['Reporter_Type_1', 'Reporter_Type_2']] = frame['Reporter Type'].str.split(' ', expand=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('13')

frame['Agency_2'] = frame.index
frame['Agency_2'].str.split(' ', expand=True, n=10)

print("frame['Agency_2'] = frame.index")
print(f"(frame['Agency_2'].str.split(' ', expand=True, n=10)).head().to_string() : "
      f"\n{(frame['Agency_2'].str.split(' ', expand=True, n=10)).head().to_string()}")
print('------------------------------------------------')

print('14')


def get_comment(row):
    reporter_type = row['Reporter Type']
    cost = float(row['Total Operating Expenses'].replace('$', ''))

    if cost > 200000:
        comment = 'CLASS A'
    else:
        comment = 'CLASS B'
    return reporter_type + '/' + comment


print(f"(frame.apply(get_comment, axis=1)).head().to_string() : "
      f"\n{(frame.apply(get_comment, axis=1)).head().to_string()}")
print('------------------------------------------------')
