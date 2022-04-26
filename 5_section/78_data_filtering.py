import pandas as pd

frame = pd.read_csv(
    '../files_to_process/course-files/Mcdonalds.csv',
    usecols=['Item', 'Category', 'Serving Size', 'Calories', 'TotalFat']
)

print(f"{frame.head().to_string()}")
print('------------------------------------------------')

print('1')

print(f"frame['Calories'] >= 400  : \n{frame['Calories'] >= 400}")
print('------------------------------------------------')

print('2')

print(f"(frame['Calories'] >= 400).head().to_string() : \n{(frame['Calories'] >= 400).head().to_string()}")
print('------------------------------------------------')

print('3')

print(f"(frame['TotalFat'] <= 20).head().to_string() : \n{(frame['TotalFat'] <= 20).head().to_string()}")
print('------------------------------------------------')

print('4')

calories_greater_equal_400 = frame['Calories'] >= 400
total_fat_less_equal_20 = frame['TotalFat'] <= 20
is_breakfast = frame['Category'] == 'Breakfast'

print(f"frame[calories_greater_equal_400].head().to_string()  : "
      f"\n{frame[calories_greater_equal_400].head().to_string()}")

print(f"\nframe[total_fat_less_equal_20].head().to_string() : \n{frame[total_fat_less_equal_20].head().to_string()}")
print(f"\nframe[is_breakfast].head().to_string() : \n{frame[is_breakfast].head().to_string()}")
print('------------------------------------------------')

print('5')

print(f"(frame[is_breakfast & calories_greater_equal_400]).head().to_string(): "
      f"\n{(frame[is_breakfast & calories_greater_equal_400]).head().to_string()}")
print('------------------------------------------------')

print('6')

print(f"(frame[is_breakfast & calories_greater_equal_400 & total_fat_less_equal_20]).head().to_string(): "
      f"\n{(frame[is_breakfast & calories_greater_equal_400 & total_fat_less_equal_20]).head().to_string()}")
print('------------------------------------------------')

print('7')

print(f"(frame[~ is_breakfast]).head().to_string(): "
      f"\n{(frame[~ is_breakfast]).head().to_string()}")
print('************************************************')


# Laboratory


print('1')

fortune = pd.read_csv(
    '../files_to_process/course-files/Fortune_500_2017.csv',
    usecols=['Rank', 'Title', 'Employees', 'Profits', 'Assets'],
    index_col='Rank'
)
print(f"fortune.head().to_string() : \n{fortune.head().to_string()}")
print('************************************************')

print('3')

fortune['RankByEmployees'] = fortune['Employees'].rank(ascending=False)

print("fortune['RankByEmployees'] = fortune['Employees'].rank(ascending=False)")
print(f"{fortune.head().to_string()}")
print('************************************************')

print('5')

fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)

print("fortune['RankByProfits'] = fortune['Profits'].rank(ascending=False)")
print(f"{fortune.head().to_string()}")
print('************************************************')

print('6')

is_employees_rank_first_ten = fortune.RankByEmployees <= 10

print("is_employees_rank_first_ten = fortune.RankByEmployees <= 10")
print(f"fortune[is_employees_rank_first_ten] : "
      f"\n{fortune[is_employees_rank_first_ten].head().to_string()}")
print('************************************************')

print('7')

is_profit_first_ten = fortune.RankByProfits <= 10

print("is_profit_first_ten = fortune.RankByProfits <= 10")
print(f"{fortune[is_profit_first_ten].head(10).to_string()}")
print('************************************************')

print('8')

print(f"fortune[is_employees_rank_first_ten & is_profit_first_ten].head().to_string() : "
      f"\n{fortune[is_employees_rank_first_ten & is_profit_first_ten].head().to_string()}")
print('************************************************')

print('9')

is_employees_rank_more_400 = fortune.RankByEmployees >= 400

print("is_employees_rank_more_400 = fortune.RankByEmployees >= 400")
print(f"fortune[is_employees_rank_first_ten & is_profit_first_ten].head().to_string() : "
      f"\n{fortune[is_employees_rank_more_400].head().to_string()}")
print('************************************************')

print('10')


print(f"fortune[is_employees_rank_more_400 & is_profit_first_ten].head().to_string() : "
      f"\n{fortune[is_employees_rank_more_400 & is_profit_first_ten].head().to_string()}")
print('************************************************')

