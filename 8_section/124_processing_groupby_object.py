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

print("for country in groups:\n"
      "\tprint(country[0])\n")

for country in groups:
    print(country[0])
print('------------------------------------------------')

print('2')

print("for country, country_data in groups:\n"
      "\tprint(country, len(country_data))\n")

for country, country_data in groups:
    print(country, len(country_data))
print('------------------------------------------------')

print('3')

print("for country, country_data in groups:\n"
      "\tprint(country, country_data['Revenue'].max() - country_data['Revenue'].min())\n")

for country, country_data in groups:
    print(country, country_data['Revenue'].max() - country_data['Revenue'].min())
print('------------------------------------------------')

print('4')

print("for country, country_data in groups:\n"
      "\tprint(country, \n\t\tcountry_data['Revenue'].max(), "
      "\n\t\tcountry_data['Revenue'].idxmax(), \n\t\tcountry_data.loc[country_data['Revenue'].idxmax()])")

for country, country_data in groups:
    print(country,
          country_data['Revenue'].max(),
          country_data['Revenue'].idxmax(),
          country_data.loc[country_data['Revenue'].idxmax()]
          )
print('------------------------------------------------')

print('5')

print("the_biggest = pd.DataFrame() \n"
      "for country, country_data in groups:\n"
      "\n\t\tthe_biggest = the_biggest.append(country_data.loc[country_data['Revenue'].idxmax()])")

the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest = the_biggest.append(country_data.loc[country_data['Revenue'].idxmax()])

print(f"the_biggest.head() : \n{the_biggest.head()}")
print('------------------------------------------------')

print('6 - the same as upper but easily')

print("the_biggest = pd.DataFrame() \n"
      "for country, country_data in groups:\n"
      "\n\t\tthe_biggest = the_biggest.append(country_data.nlargest(1, 'Revenue'))")

the_biggest = pd.DataFrame()
for country, country_data in groups:
    the_biggest = the_biggest.append(country_data.nlargest(1, 'Revenue'))

print(f"the_biggest.head() : \n{the_biggest.head()}")
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

group_city = df.groupby('City')

print("group_city = df.groupby('City')")
print(f"group_city.head() : \n{group_city.head()}")
print('**********************************************')

print('4')

# for city, city_data in group_city:
#     print(city)
print('**********************************************')

# for city, city_data in group_city:
#     print(f"{city, city_data['Age'].count()}")
print('**********************************************')

print('7')

for city, city_data in group_city:
    print(city, city_data['TotalSeconds'].min())
print('**********************************************')

print('8')

the_best_per_city = pd.DataFrame()

for city, data_city in group_city:
    the_best_per_city = the_best_per_city.append(data_city.nsmallest(1, 'TotalSeconds'))

print(the_best_per_city)