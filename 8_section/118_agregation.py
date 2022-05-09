import pandas as pd
from datetime import timedelta

products = pd.read_csv(
    '../files_to_process/course-files/WA_Sales_Products_2012-14.csv'
)

print(f"{products.head()}")
print('------------------------------------------------')

print('1')

groups = products.groupby(by='Retailer country')

print("groups = products.groupby(by='Retailer country')")
print(f"groups.head() : \n{groups.head()}")
print('------------------------------------------------')

print('2')

print(f"groups.mean() : \n{groups.mean()}")
print('------------------------------------------------')

print('3')

print(f"groups.sum() : \n{groups.sum()}")
print('------------------------------------------------')

print('4')

print(f"groups.count().head() : \n{groups.count().head()}")
print('------------------------------------------------')

print('5')

print(f"groups.min().head() : \n{groups.min().head()}")
print('------------------------------------------------')

print('6')

print(f"groups['Revenue'].sum().head() : \n{groups['Revenue'].sum().head()}")
print('------------------------------------------------')

print('7')

print(f"groups[['Revenue', 'Quantity']].mean().head() : \n{groups[['Revenue', 'Quantity']].mean().head()}")
print('**********************************************')


# Laboratory

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

print('3')

group_city = df.groupby(by='City')

print("group_city = df.groupby(by='City')")
print(f"group_city.head() : \n{group_city.head()}")
print('**********************************************')

print('4')

print(f"group_city.agg(func='mean') : \n{group_city.agg(func='mean')}")
print('**********************************************')

print('5')

print(f"group_city[['TotalSeconds','HalfSeconds']].mean() : \n{group_city[['TotalSeconds','HalfSeconds']].mean()}")
print('**********************************************')

print('6')

print(f"group_city['TotalSeconds'].sum() : \n{group_city['TotalSeconds'].sum()}")
print('**********************************************')

group_age = df.groupby('Age')

print("group_age = df.groupby('Age')")
print(f"group_age.count() : \n{group_age.count()}")
print('**********************************************')

print('7')

print(f"group_age['TotalSeconds'].count() : \n{group_age['TotalSeconds'].count()}")
print('**********************************************')
