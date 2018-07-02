price = 0
import sqlite3
mylibrary=sqlite3.connect('mylibrary.db')
print("OPENEND DATABASE")
title=input("ENTER THE BOOK TITLE : ")
cur=mylibrary.cursor()
x=cur.execute('''SELECT * FROM BOOKS
WHERE NAME == {} '''.format(title))
for row in x:
    print (" ID = ",row[0])
    print (" NAME = ",row[1])
    print (" AUTHOR = ",row[2])
    print (" PRICE = ",row[3]),"\n"
    amt=row[3]
n=int(input("ENTER THE NO.COPIES : "))
price = price  + n*amt
ans=input("ANYTHING ELSE [Y/N] : ")
while ans=='Y' :
    title=input("ENTER THE BOOK TITLE : ")
    cur=mylibrary.cursor()
    x=cur.execute('''SELECT * FROM BOOKS
    WHERE NAME == {} '''.format(title))
    for row in x:
        print (" ID = ",row[0])
        print (" NAME = ",row[1])
        print (" AUTHOR = ",row[2])
        print (" PRICE = ",row[3]),"\n"
        amt=row[3]
    n=int(input("ENTER THE NO.COPIES : "))
    price = price  + n*amt
    ans=input("ANYTHING ELSE [Y/N] : ")

print("TOTAL AMOUNT TO BE PAID : {}".format(price))    
mylibrary.close()



      

