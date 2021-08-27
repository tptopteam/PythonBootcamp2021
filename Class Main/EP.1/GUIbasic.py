from tkinter import *
from tkinter import ttk # ttk is them of tk
import csv

#csv File
def WritetoCSV(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
        print('บันทึกไฟล์สำเร็จ')
        
#เครื่องหมาย # คือการคอมเมนท์

# main program
GUI = Tk() # Tk()คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมของฉัน')
GUI.geometry('700x700') # 500 = กว้าง, 300 = สูง

# font
FONT1 = ('Angsana New',15,'bold')
FONT2 = ('Angsana New',15)

# title
L1 = ttk.Label(GUI,text='หัวข้อ',font=FONT1,foreground='green')
L1.pack() #นำ L1 ไปติดกับโปรแกรมหลัก

# text box 1
v_title = StringVar() # เป็นตัวแปรพิเศษ ไว้เก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_title,font=FONT2,width=30)
E1.pack()

# detail
L2 = ttk.Label(GUI,text='รายละเอียด',font=FONT1,foreground='green')
L2.pack()

#สร้างฟังชั่นชื่อ UpdateTable
def UpdateTable():
    alldata = ReadCSV() #เรียกฟังชั่นอ่าน CSV จากด้านบนมา
    for row in alldata:
        table.insert('','end',value=row)

# text box 2
v_detail = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_detail,font=FONT2,width=40)
E2.pack()

# Button save

def SaveButton(event=None):
    title = v_title.get() # .get() ดึงข้อมูลจากตัวแปร v_title
    detail = v_detail.get()
    print(title)
    print(detail)
    dt = [title,detail] # dt = data
    WritetoCSV(dt)
    print('save...')
    # clear ข้อมูล
    v_title.set('') #สั่งเคลียร์ข้อมูลให้ว่าง
    v_detail.set('')#สั่งเคลียร์ข้อมูลให้ว่าง
    E1.focus() #ทำให้เคอร์เซอร์ไปอยู่ตำแหน่งช่องกรอกแรก
    UpdateTable() #อัพเดตข้อมูลทุกครั้งที่มีการบันทึก
    
E2.bind('<Return>',SaveButton)
E2.bind('<Control-s>',SaveButton)
 #เช็คในช่องกรอกที่ 2 ว่ามีการกดปุ่ม Return หรือ Enter หรือไม่หากกดให้ทำการเรียก ฟังก์ชัน SaveButton
B1 = ttk.Button(GUI,text='Save',command=SaveButton)
B1.pack(ipadx=30,ipady=20,pady=20)
# ipadx = ระยะห่างภายในปุ่ม แนวแกน x
# pady = ระยะห่างด้านนอกปุ่ม ทั้งบนและล่างแนวแกน y

#table
header = ['Title','Detail']

table = ttk.Treeview(GUI,height=10,column=header, show='headings')
table.place(x=20,y=300)

table.heading('Title',text='หัวข้อ') #โชว์คำว่าหัวข้อที่คอลัมน์ Title
table.column('Title',width=200) #ปรับความกว้าง
table.heading('Detail',text='รายละเอียด') #โชว์คำว่ารายละเอียดที่คอลัมน์ Title
table.column('Detail',width=460) #ปรับความกว้าง

#test insert data


row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)

row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)

row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)

row = ['.insert()','คือการใส่ข้อมูลเข้าไป']
table.insert('','2',value=row)


#print(help(ttk.Treeview))


    





GUI.mainloop()
# GUI.mainloop() จาก GUI จะทำให้โปรแกรมรันตลอด
