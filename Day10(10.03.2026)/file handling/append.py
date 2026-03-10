file = open('jecrc.txt' , 'a+')
file.write('JECRC IS OK OK UNIVERSITY')
file.write('There placment is average ')
file.writelines([
    '\n Here food is good',
    '\n taking addmission is very easy',
    '\ngood enivorenment'
])
file.seek(0)
print(file.read())

file.close()