#writecsv.py

import csv

def WritetoCSV(data):
    with open('test.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
        print('บันทึกไฟล์สำเร็จ')

data = ['print() คืออะไร','aaaaaaaaa']
WritetoCSV(data)
