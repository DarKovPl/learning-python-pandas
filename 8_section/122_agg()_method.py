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
print('**********************************************')

#  Laboratory

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

sex_age = df.groupby(["M/F", "Age"])

print("sex_age = df.groupby(['M/F', 'Age'])")
print(f"sex_age.head() : \n{sex_age.head()}")
print('**********************************************')

print('4')

print("sex_age.agg({'TotalSeconds': 'mean', 'HalfSeconds': 'mean'}) : "
      f"\n{sex_age.agg({'TotalSeconds': 'mean', 'HalfSeconds': 'mean'})}")
print('**********************************************')

print('5')

print("sex_age.agg({'TotalSeconds': 'sum', 'HalfSeconds': 'sum'}) : "
      f"\n{sex_age.agg({'TotalSeconds': 'sum', 'HalfSeconds': 'sum'})}")
print('**********************************************')

print('6')

print("sex_age.agg({'TotalSeconds': ['mean', 'sum'], 'HalfSeconds': ['mean', 'sum']}) : "
      f"\n{sex_age.agg({'TotalSeconds': ['mean', 'sum'], 'HalfSeconds': ['mean', 'sum']})}")
print('**********************************************')

print('8')

functions = ['mean', 'sum', 'count']

print("functions = ['mean', 'sum', 'count']")
print("sex_age.agg({'TotalSeconds': functions, 'HalfSeconds': functions}) : "
      f"\n{sex_age.agg({'TotalSeconds': functions, 'HalfSeconds': functions})}")
print('**********************************************')
