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
