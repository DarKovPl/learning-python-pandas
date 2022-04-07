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