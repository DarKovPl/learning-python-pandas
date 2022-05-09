import pandas as pd
from datetime import timedelta

products = pd.read_csv(
    '../files_to_process/course-files/WA_Sales_Products_2012-14.csv'
)

print(f"{products.head()}")
print('------------------------------------------------')

print('1')

groups = products.groupby(by=['Retailer country', 'Year'])

print("groups = products.groupby(by=['Retailer country', 'Year'])")
print(f"groups.size().head(10) : \n{groups.size().head(10)}")
print('------------------------------------------------')

print('2')

print(f"groups.get_group(('Australia', 2012)).head() : \n{groups.get_group(('Australia', 2012)).head()}")
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

country_city = df.groupby(["Country", "City"])

print("country_city = df.groupby(['Country', 'City'])")
print(f"{country_city.head()}")
print('**********************************************')

print('4')

print(f"country_city.size() : \n{country_city.size()}")
print('**********************************************')

print('5')

print(f"country_city.mean() : \n{country_city.mean()}")
print('**********************************************')

print('6')

print(f"country_city.get_group(('USA', 'San Francisco')) : \n{country_city.get_group(('USA', 'San Francisco'))}")
print('**********************************************')

print('7')

sex_age = df.groupby(["M/F", "Age"])

print("sex_age = df.groupby(['M/F', 'Age'])")
print(f"sex_age.head() : \n{sex_age.head()}")
print('**********************************************')

print('8')

print(f"sex_age.size() : \n{sex_age.size()}")
print('**********************************************')

print('9')

print(f"sex_age.mean() : \n{sex_age.mean()}")
print('**********************************************')

print(f"{sex_age.get_group(('M', 25))}")
print('**********************************************')
