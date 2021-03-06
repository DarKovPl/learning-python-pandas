import pandas as pd

index = ['a', 'b', 'c', 'd', 'e1', 'e2']
values = ['Austria', 'Belgium', 'Canada', 'Denmark', 'England', 'Estonia']
s = pd.Series(values, index)

print('1')

search_list = ['a', 'b']
print(f"s.loc[search_list]"
      f"\n{s.loc[search_list]}\n"
      )
print('------------------------------------------------')

print('2')

searched_list_not_found = ['a', 'b', 'f']

# s.loc[searched_list_not_found]
# print(f" s.loc[searched_list_not_found]: \n"
#       f"ERROR : \n{s.loc[searched_list_not_found]}\n"
#       )
print('------------------------------------------------')

print('3')

print(f"s.reindex(searched_list_not_found)--"
      f"\n{s.reindex(searched_list_not_found)}\n"
      )
print("reindex doesn't handle duplicates ['e', 'e']")
print('------------------------------------------------')

print('4')

print(f"s.index"
      f"\n{s.index}\n\n"
      
      f"s.index.intersection(searched_list_not_found)--"
      f"\n{s.index.intersection(searched_list_not_found)}\n\n"
      
      f"s.loc[s.index.intersection(searched_list_not_found)]--"
      f"\n{s.loc[s.index.intersection(searched_list_not_found)]}\n"
      )
print('Intersection handles duplicates, but if you add the existing value again, this value will be multiplexed.')
print('*************************************************')

# Laboratory

print('2')

countries = pd.read_csv(
      '../files_to_process/course-files/countries.csv',
      usecols=['Symbol', 'Name'],
      index_col='Symbol'
).squeeze()

print(f'{countries.to_string()}')
print('*************************************************')

print('3')

countries.dropna(inplace=True)
print(f'countries.dropna(inplace=True) : \n{countries}')
print('*************************************************')

print('4')

print(f'countries.head(20) : \n{countries.head(20)}')
print('*************************************************')

print('5')

to_find = ['BB', 'AA', 'BS']
print(f'countries.reindex(to_find) : \n{countries.reindex(to_find)}')
print('*************************************************')

print('6')

print(f'countries.loc[countries.index.intersection(to_find)] : '
      f'\n{countries.loc[countries.index.intersection(to_find)]}')
print('*************************************************')

