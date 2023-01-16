from datetime import datetime
print(":: Enter the date in DD/MM/YYYY format ::")
print()
str_d1=str(input("Enter the date of your birth :: "))
str_d2=str(input("Enter todays date :: "))
print()
date1 = datetime.strptime(str_d1, "%d/%m/%Y")
date2 = datetime.strptime(str_d2, "%d/%m/%Y")
d=date2-date1
print(f'Person survived {d.days} days')


