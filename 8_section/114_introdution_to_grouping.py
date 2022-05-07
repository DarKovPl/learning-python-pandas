import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import time

products = pd.read_csv(
    '../files_to_process/course-files/WA_Sales_Products_2012-14.csv'
)

print(f"products.head() : \n{products.head()}")
print(f"products.info() : \n{products.info()}")
print('------------------------------------------------')

print('1')

print(f"products.describe() : \n{products.describe()}")
print('------------------------------------------------')

print('2')

print(f"products['Retailer country'].value_counts() : \n{products['Retailer country'].value_counts()}")
print('------------------------------------------------')

print('3')

print(f"products['Retailer country'].nunique() : \n{products['Retailer country'].nunique()}")
print('------------------------------------------------')

print('4')

countries = products['Retailer country'].unique()
my_own_groups = {}

for country in countries:
    my_own_sub_data_frame = products.where(products['Retailer country'] == country).dropna()
    my_own_groups[country] = my_own_sub_data_frame

print(f"countries = products['Retailer country'].unique()\n"
      "my_own_groups = {}")
print("for country in countries:\n"
      "\tmy_own_sub_data_frame = products.where(products['Retailer country'] == country).dropna()\n"
      "\tmy_own_groups[country] = my_own_sub_data_frame)\n"
      )
print(f"my_own_groups : \n{my_own_groups}")
print('------------------------------------------------')

print('5')

print(f"my_own_groups['Belgium'] : \n{my_own_groups['Belgium']}")
print('------------------------------------------------')

print('6')

print(f"{my_own_groups['Mexico'].describe()}")
print('**********************************************')

# Laboratory

print('2')

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

print(f"df.info() : \n{df.info()}")
print('----------')

print(f"df.describe() : \n{df.describe()}")
print('----------')

print(f"df.value_counts() : \n{df.value_counts()}")
print('----------')

print(f"df['City'].unique() : \n{df['City'].unique()}")
print('----------')

print(f"df['City'].nunique() : \n{df['City'].nunique()}")
print('**********************************************')

print('5')

cities = df['City'].unique()
groups = {}

for city in cities:
    tmp = df.loc[df['City'] == city]
    groups[city] = tmp
print(groups)

print(groups["San Francisco"].describe())
print('**********************************************')