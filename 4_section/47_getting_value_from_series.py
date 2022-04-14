import pandas as pd

index = ['a', 'b', 'c', 'd', 'e', 'e']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(values, index)

print('1 - operator []')

print(f"s = pd.Series(values, index) : \n"
      f"\ns[1] getting value by position: value - \n{s[1]}\n"
      f"\ns['b'] getting value by index: value - \n{s['b']}\n"
      f"\ns['e'] getting multiple values: series - \n{s['e']} \n"
      # f"\n{s['f']} non existing values:  error"
      )

print('------------------------------------------------')

print('2 - method get()')

print(f"s = pd.Series(values, index) : \n"
      f"\ns.get(1) getting value by position: value - \n{s.get(1)}\n"
      f"\ns.get('b') getting value by index: value - \n{s.get('b')}\n"
      f"\ns.get('e') getting multiple values: series - \n{s.get('e')} \n"
      f"\ns.get('f') getting non existing value: - {s.get('f')}\n"
      )

print('------------------------------------------------')

print('3 - method at() - getting value by value of index')

print(f"s = pd.Series(values, index) : \n"
      # f"\ns.at[1]getting value by position: ERROR - \n{s.at[1]}\n"
      f"\ns.at['b'] getting value by index: value - \n{s.at['b']}\n"
      f"\ns.at['e'] getting multiple values: series - \n{s.at['e']} \n"
      # f"\ns.at['f'] getting non existing value: ERROR- {s.at['f']}\n"
      )

print('------------------------------------------------')

print('4 - method iat() - getting value by position in index')

print(f"s = pd.Series(values, index) : \n"
      f"\ns.iat[1] getting value by position: value - \n{s.iat[1]}\n"
      # f"\ns.iat['b'] getting value by index: ERROR only integers - \n{s.iat['b']}\n"
      # f"\ns.iat[[0, 1]] getting multiple values: ERROR no multiple - \n{s.iat[[0, 1]]} \n"
      # f"\ns.iat['f'] getting non existing value: ERROR - {s.iat['f']}\n"
      )

print('------------------------------------------------')

print('5 - method loc() - getting value by value of the index')

print(f"s = pd.Series(values, index) : \n"
      #f"\ns.loc[1] getting value by position: ERROR - \n{s.loc[1]}\n"
      f"\ns.loc['b'] getting value by value of index: - \n{s.loc['b']}\n"
      f"\ns.loc['e'] getting multiple values: Series- \n{s.loc['e']} \n"
      # f"\ns.loc['f'] getting non existing value: ERROR - {s.loc['f']}\n"
      )

print('------------------------------------------------')

print('6 - method iloc() - getting value by position in index')

print(f"s = pd.Series(values, index) : \n"
      f"\ns.iloc[1] getting value by position: value - \n{s.iloc[1]}\n"
      # f"\ns.iloc['b'] getting value by index: ERROR only integers - \n{s.iloc['b']}\n"
      f"\ns.iloc[[0, 1]] getting multiple values: Series - \n{s.iloc[[0, 1]]} \n"
      # f"\ns.iloc['f'] getting non existing value: ERROR - {s.iloc['f']}\n"
      )

print('*************************************************')

#  Laboratory

print('2')

countries = pd.read_csv(
      '../files_to_process/course-files/countries.csv',
      usecols=['Symbol', 'Name'],
      index_col='Symbol'
).squeeze()
print(f'countries : \n{countries}')
print('*************************************************')

print('3')

print(f'countries.head(20) : \n{countries.head(20)}')
print('*************************************************')

print('4')

print(f"countries.loc['FR'] : \n{countries.loc['FR']}")
print('*************************************************')

print('5')

print(f"countries.iloc[13] : \n{countries.iloc[13]}")
print('*************************************************')

print('6')

nordic = countries.loc[['FI', 'SE', 'NO']]
print(f"nordic = countries.loc[['FI', 'SE', 'NO']] : \n{nordic}")
print('*************************************************')

print('7')


print(f"countries[nordic.index] : \n{countries[nordic.index]}")
print('*************************************************')

print('8')


print(f"countries.loc[nordic.index] : \n{countries.loc[nordic.index]}")
print('*************************************************')
