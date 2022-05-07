import pandas as pd

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
print('------------------------------------------------')