import pandas as pd

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
print('------------------------------------------------')
