import pandas as pd
import random as rd

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

print('*************************************************')

# Laboratory


print('1')

plane_dict = {'PYT001': 'Airbus 320', 'PYT002': 'Boeing 737', 'PYT003': 'Airbus 321'}

aircraft = pd.Series(plane_dict)
print(type(aircraft), aircraft)
print('*************************************************')

print('2')

flights_list = [rd.choice(aircraft.index) for _ in range(100)]
print(flights_list[:5])
print('*************************************************')

print('3')

flights = pd.Series(flights_list)
print(f'flights = pd.Series(flights_list) : \n{flights}')
print('*************************************************')

print('4')

flights_aircrafts = flights.map(aircraft)
print(f'flights_aircrafts = pd.Series(flights_list).map(aircraft).head() : \n{flights_aircrafts.head()}')
print('*************************************************')
