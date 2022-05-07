from datetime import timedelta

import pandas as pd


products = pd.read_csv(
    '../files_to_process/course-files/WA_Sales_Products_2012-14.csv'
)

print(f"{products.head()}")
print('------------------------------------------------')

print('1')

groups = products.groupby(by='Retailer country')

print("groups = products.groupby(by='Retailer country')")
print(f"type(groups) : \n{type(groups)}")
print('------------------------------------------------')

print('2')

print(f"groups.size() : \n{groups.size()}")
print('------------------------------------------------')

print('2')

print(f"groups.first() : \n{groups.first()}")
print('------------------------------------------------')

print('3')

print(f"groups.groups : \n{groups.groups}")
print('------------------------------------------------')

print('4')

print(f"products.loc[groups.groups['Belgium']].head() : \n{products.loc[groups.groups['Belgium']].head()}")
print('------------------------------------------------')

print('5')

print(f"groups.get_group('Belgium').head() : \n{groups.get_group('Belgium').head()}")
print('------------------------------------------------')

# Laboratory


print('1')

df = pd.read_csv('../files_to_process/course-files/marathon_results_2016.csv', index_col='Bib',
                 usecols=['Bib', '40K', 'Half', 'Pace', 'Age', 'M/F', 'Country', 'State', 'City']
)

print(f"df.head() : \n{df.head()}")
print(f"df.info() : \n{df.info()}")
print('----------')

df['40K'] = pd.to_timedelta(df['40K'], errors='coerce', unit='H')
df['Half'] = pd.to_timedelta(df['Half'], errors='coerce', unit='H')

df.dropna(inplace=True)

df['TotalSeconds'] = df['40K'].apply(lambda x: timedelta.total_seconds(x))
df['HalfSeconds'] = df['Half'].apply(lambda x: timedelta.total_seconds(x))


print("df['40K'] = df['40K'].apply(pd.to_timedelta)")
print("df['Half'] = df['Half'].apply(pd.to_timedelta)")
print("df['TotalSeconds'] = df['40K'].apply(lambda x: timedelta.total_seconds(x))")
print("df['HalfSeconds'] = df['Half'].apply(lambda x: timedelta.total_seconds(x))")
print(f"df.head() : \n{df.head()}")
print('**********************************************')

print('4')

group_city = df.groupby(by='City')

print("group_city = df.groupby(by='City')")
print(f"group_city.groups : \n{group_city.groups}")
print('**********************************************')

print('5')

print(f"df.loc[group_city.groups['San Francisco']].head() : "
      f"\n{df.loc[group_city.groups['San Francisco']].head().to_string()}")
print('**********************************************')

print('6')

print(f"group_city.get_group('San Francisco')['40K'].mean(): "
      f"\n{group_city.get_group('San Francisco')['40K'].mean()}")
print('**********************************************')

print('8')

print(f"group_city.first() : \n{group_city.first()}")
print('**********************************************')

print('8')

group_age = df.groupby('Age')

print(f"group_age.get_group(20)['40K'].mean() : \n{group_age.get_group(20)['40K'].mean()}")
print('**********************************************')

print('9')

print(f"group_age.get_group(40)['40K'].mean() : \n{group_age.get_group(40)['40K'].mean()}")
print('**********************************************')

print(f"group_age.first() : \n{group_age.first()}")
print('**********************************************')
