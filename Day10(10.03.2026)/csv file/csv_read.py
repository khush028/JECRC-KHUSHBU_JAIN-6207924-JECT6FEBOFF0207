import csv
from datetime import date

file = open('expense.csv','a+',newline='')
r = csv.reader(file)
file.seek(0)
print(list(r))
file.close()