import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',

)

print('1')

print(f'frame.head().to_string() : \n{frame.head().to_string()}')
print('------------------------------------------------')

print('2')

print(f'frame.count() : \n{frame.count()}')
print('------------------------------------------------')

print('3')

print(f'frame.dtypes : \n{frame.dtypes}')
print('-----------------------------------------------')

print('4')

print(f'frame.dtypes : \n{frame.dtypes}')
print('-----------------------------------------------')

print('5')

print(f'frame.dtypes.value_counts() : \n{frame.dtypes.value_counts()}')
print('-----------------------------------------------')

print('6')

print(f'frame.shape : \n{frame.shape}')
print('-----------------------------------------------')

print('7')

print(f'frame.axes : \n{frame.axes}')
print('-----------------------------------------------')

print('8')

print(f'frame.index : \n{frame.index}')
print('-----------------------------------------------')

print('9')

print(f'frame.columns : \n{frame.columns}')
print('-----------------------------------------------')

print('10')

print(f'frame.values : \n{frame.values}')
print('-----------------------------------------------')

print('11')

print(f'frame.info() : \n{frame.info()}')
print('-----------------------------------------------')

print('12')

print(f"frame['Category'].value_counts()  : \n{frame['Category'].value_counts()}")
print('-----------------------------------------------')

print('13')

print(f'frame.sample() : \n{frame.sample()}')
print('-----------------------------------------------')

print('14')

print(f"frame.sample(n=3, axis='columns') : \n{frame.sample(n=3, axis='columns')}")
print('-----------------------------------------------')

print('15')

print(f'frame.sample(frac=0.05) : \n{frame.sample(frac=0.05)}')
print('***********************************************')

# Laboratory

fuel = pd.read_csv(
    '../files_to_process/course-files/fuel.csv',
    low_memory=False,
    usecols=['Vehicle ID', 'Year', 'Make', 'Model', 'Class', 'Fuel Type', 'Combined MPG (FT1)'],
)

print('2')

print(f"fuel.info() : \n{fuel.info()}")
print('***********************************************')

print('3')

print(f"fuel.dtypes : \n{fuel.dtypes}")
print('***********************************************')

print('4')

print(f"fuel.dtypes.value_counts() : \n{fuel.dtypes.value_counts()}")
print('***********************************************')

print('5')

print(f"fuel.value_counts(subset=['Make']) : \n{fuel.value_counts(subset=['Make'])}")
print('***********************************************')

print('6')

print(f"fuel.index : \n{fuel.index}")
print('***********************************************')

print('7')

print(f"fuel.columns : \n{fuel.columns}")
print('***********************************************')

print('8')

print(f"fuel.values : \n{fuel.values}")
print('***********************************************')

print('9')

print(f"fuel.axes : \n{fuel.axes}")
print('***********************************************')

print('10')

print(f"fuel.shape : \n{fuel.shape}")
print('***********************************************')

print('11')

print(f"fuel.count() : \n{fuel.count()}")
print('***********************************************')

print('12')

print(f"len(fuel) : \n{len(fuel)}")
print('***********************************************')
