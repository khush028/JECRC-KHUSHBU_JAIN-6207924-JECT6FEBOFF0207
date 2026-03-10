import csv
from datetime import date

file = open('expense.csv' , 'a+' , newline="")
w = csv.writer(file)
w.writerow(['DATE' , 'CATEGORY' , 'AMOUNT'])
w.writerows([
    [date.today() , 'travel' , 2000],
    [date.today() , 'food' , 9000],
    [date.today() , 'Movie' , 200],
    [date.today() , 'Concert' , 2000]
    ]
)
file.close()