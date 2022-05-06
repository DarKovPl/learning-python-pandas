import pandas as pd

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
print('------------------------------------------------')
