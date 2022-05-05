import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/PublicTransitExpenses.csv'
)

print(frame.head())
print(frame.info(memory_usage='deep'))
print('------------------------------------------------')

print('2')

frame = pd.read_csv(
    '../files_to_process/course-files/PublicTransitExpenses.csv',
    usecols=[
        'Agency',
        'Reporter Type',
        'Organization Type',
        'Service Area Population',
        'Rail (Y/N)',
        'Fixed Route (Y/N)',
        'Service Costs',
        'Tires and Tubes',
        'Total Operating Expenses'
    ]
)

print(f"frame.head().to_string() : \n{frame.head().to_string()}")
print('------------------------------------------------')

print('3')

new_column_names = {
    'Agency': 'Agency',
    'Reporter Type': 'ReporterType',
    'Organization Type': 'OrgType',
    'Service Area Population': 'Population',
    'Rail (Y/N)': 'IsRail',
    'Fixed Route (Y/N)': 'IsFixedRoute',
    'Service Costs': 'ServiceCosts',
    'Tires and Tubes': 'TiresTubesCost',
    'Total Operating Expenses': 'TotalExpenses'
}

frame.rename(columns=new_column_names, inplace=True)

print(f"frame.rename(columns=new_column_names, inplace=True)")
print(f"frame.head().to_string() : \n{frame.head().to_string()}")

print('--------------')
print(f"{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('4-----')

print(f"frame['ReporterType'].nunique() : \n{frame['ReporterType'].nunique()}")
print('--------------')

print(f"frame['ReporterType'].count(): \n{frame['ReporterType'].count()}")
print('--------------')

print(f"frame['ReporterType'].value_counts() : \n{frame['ReporterType'].value_counts()}")
print('------------------------------------------------')

print('5')

frame['ReporterType'] = frame['ReporterType'].astype('category')

print(f"frame['ReporterType'] = frame['ReporterType'].astype('category')\n")
print(f"frame.info(memory_usage='deep') : \n")
print(f"{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('6')

frame['Agency'] = frame['Agency'].astype('category')
frame['OrgType'] = frame['OrgType'].astype('category')

print("frame['Agency'] = frame['Agency'].astype('category')")
print("frame['OrgType'] = frame['OrgType'].astype('category')\n")
print(f"frame.info(memory_usage='deep') : \n{frame.info(memory_usage='deep')}")
print('------------------------------------------------')

print('7')

frame['Population'].fillna(0, inplace=True)
frame['Population'] = frame['Population'].astype('int')

print("frame['Population'].fillna(0, inplace=True)")
print("frame['Population'] = frame['Population'].astype('int')\n")
print("frame.info(memory_usage='deep') : \n")
print(f"{frame.info(memory_usage='deep')}")
print('---------')

print(f"frame[frame['Population'] > 0].head() : \n{frame[frame['Population'] > 0].head()}")
print('------------------------------------------------')

print('8')

frame['IsRail'].replace(('Y', 'N'), (True, False), inplace=True)
frame['IsFixedRoute'].replace(('Y', 'N'), (True, False), inplace=True)

frame['IsRail'].fillna(False, inplace=True)
frame['IsFixedRoute'].fillna(False, inplace=True)


print("frame['IsRail'].replace(('Y', 'N'), (True, False), inplace=True)")
print("frame['IsFixedRoute'].replace(('Y', 'N'), (True, False), inplace=True)")
print('---------')

print("frame['IsRail'].fillna(False, inplace=True)")
print("frame['IsFixedRoute'].fillna(False, inplace=True)")
print('------------------------------------------------')

print('9')

frame['IsRail'] = frame['IsRail'].astype('bool')
frame['IsFixedRoute'] = frame['IsFixedRoute'].astype('bool')

print("frame['IsRail'] = frame['IsRail'].astype('bool')")
print("frame['IsFixedRoute'] = frame['IsFixedRoute'].astype('Bool')")
print('---------')

print(f"frame.head().to_string() : \n{frame.head().to_string()}\n")

print("frame.info(memory_usage='deep') : \n")
print(f"{frame.info(memory_usage='deep')}")
print('************************************************')


# Laboratory

print('1')

fb = pd.read_csv(
    '../files_to_process/course-files/mrbean_facebook_statuses_with_nulls.csv'
)

print(f"fb.head().to_string() : \n{fb.head().to_string()}")
print('************************************************')

print('2')

print(f"fb.info(memory_usage='deep') : \n{fb.info(memory_usage='deep')}")
print('************************************************')

print('3')

fb = pd.read_csv(
    '../files_to_process/course-files/mrbean_facebook_statuses_with_nulls.csv',
    usecols=["status_message", "status_type", "link_name", "num_reactions", "num_shares", "num_likes"]
)

print(f"fb.info(memory_usage='deep') : \n{fb.info(memory_usage='deep')}")
print('************************************************')

print('4')

print(f"fb.count() : \n{fb.count()}")
print('---------')

print(f"fb['status_type'].nunique() : \n{fb['status_type'].nunique()}")
print('---------')
print(f"fb['status_type'].value_counts() : \n{fb['status_type'].value_counts()}")
print('---------')

fb['status_type'] = fb['status_type'].astype('category')
print(f"{fb.info(memory_usage='deep')}")
print('--------------------------------------------------')

print(f"fb['link_name'].nunique() : \n{fb['link_name'].nunique()}")
print('---------')
print(f"fb['link_name'].value_counts() : \n{fb['link_name'].value_counts()}")
print('---------')

fb['link_name'] = fb['link_name'].astype('category')
print(f"{fb.info(memory_usage='deep')}")
print('************************************************')

print('5')
fb['num_reactions'].fillna(value=0, inplace=True)
fb['num_shares'].fillna(value=0, inplace=True)

fb['num_reactions'] = fb['num_reactions'].astype('int')
fb['num_shares'] = fb['num_shares'].astype('int')
fb['num_shares'] = fb['num_shares'].astype('int')

print(f"fb.head(10).to_string() : \n{fb.head(10).to_string()}")
print(f"{fb.info(memory_usage='deep')}")
print('************************************************')
