import pandas as pd

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
print('------------------------------------------------')
