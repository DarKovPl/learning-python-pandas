import pandas as pd

team = pd.Series(
    data=[5, 3, 2, 4, 3, 4, 4, 5],
    index=['Andy', 'Bob', 'Chris', 'Drik', 'Francis', 'George', 'Henry', 'Ivan']
)
print(f'team : \n{team}', '\n')

notes = pd.Series(data=['C', 'B', 'A', 'A+', 'A++'], index=[1, 2, 3, 4, 5])
print(f'notes : \n{notes}\n')

print('1')

print(f'team.map(notes) : \n{team.map(notes)}')
print('------------------------------------------------')

print('2')
notes_dict = {1: 'C', 2: 'B', 3: 'A', 4: 'A+', 5: 'A++'}

print(f'notes_dict : \n{notes_dict}')
print('----------')

print(f'team.map(notes_dict) : \n{team.map(notes_dict)}')

print('------------------------------------------------')
