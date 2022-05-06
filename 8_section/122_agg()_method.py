import pandas as pd

products = pd.read_csv(
    '../files_to_process/course-files/WA_Sales_Products_2012-14.csv'
)

print(f"{products.head()}")
print('------------------------------------------------')

print('1')

groups = products.groupby(by=['Retailer country', 'Year'])

print("groups = products.groupby(by=['Retailer country', 'Year'])")
print(f"groups['Revenue'].sum().head() : \n{groups['Revenue'].sum().head()}")
print('------------------------------------------------')

print('2')

print(f"groups['Quantity'].sum().head() : \n{groups['Quantity'].sum().head()}")
print('------------------------------------------------')

print('3')

print(f"groups['Gross margin'].mean().head() : \n{groups['Gross margin'].mean().head()}")
print('------------------------------------------------')

print('4')

print(r"groups.agg({'Revenue': 'sum'}).head()" + f": \n{groups.agg({'Revenue': 'sum'}).head()}")
print('------------------------------------------------')

print('5')

print(r"groups.agg({'Gross margin': 'sum'}).head() : " + f" \n{groups.agg({'Gross margin': 'sum'}).head()}")
print('------------------------------------------------')

print('6')

print(r"groups.agg({'Revenue': 'sum', 'Quantity': 'sum', 'Gross margin': 'mean'}))" +
      f"{groups.agg({'Revenue': 'sum', 'Quantity': 'sum', 'Gross margin': 'mean'})}")
print('------------------------------------------------')

print('7')

print(r"groups.agg({'Revenue': ['sum', 'min', 'max'], 'Quantity': ['sum', 'min', 'max'], 'Gross margin': 'mean'}" +
      f"{groups.agg({'Revenue': ['sum', 'min', 'max'], 'Quantity': ['sum', 'min', 'max'], 'Gross margin': 'mean'})}")
print('------------------------------------------------')
