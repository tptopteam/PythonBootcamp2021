#readcsv.py

import os
print(os.listdir())

import csv

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
        #print(data)
        return data #return คือ การส่งข้อมูลไปใช้ต่อ

alldata = ReadCSV()
#print(alldata)

for dt in alldata:
    print(dt[1])


'''
#โหลดข้อมูลจาก csv เข้าไปในโปรแกรม
alldata = ReadCSV() #เรียกฟังชันอ่าน csv จากด้านบนมา
for row in alldata:
    table.insert('','end',value=row)
'''
