from tkinter import *
root = Tk()
root.geometry('450x450')
root.config(bg = 'cyan')
root.title('ContactBook')
root.resizable(0,0)
contactlist = [
    ['Sai Vineela','987654321'],
    ['Vishwanath','9753124680'],
    ['Navya Sri','9631246870'],
    ['Kranthi Kiran','9453723323'],
    ['Shruthi', '9636976789'],
    ['Nithin','9345345345'],
    ]
Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame,orient=VERTICAL)
listbox = Listbox(frame,yscrollcommand=scroll.set,height=12)
scroll.config (command=listbox.yview)
scroll.pack(side=RIGHT,fill=Y)
listbox.pack()

def Selected():
    return listbox.curselection()[0]
    
def Add():
    contactlist.append([Name.get(),Number.get()])
    Select_set()

def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EDIT():
    contactlist[Selected()] = [Name.get(),Number.get()]
    Select_set()
    
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
def RESET():
    Name.set('')
    Number.set('')

def EXIT():
    root.destroy()

def Select_set() :
    contactlist.sort()
    listbox.delete(0,END)
    for name,phone in contactlist :
        listbox.insert (END,name)
        
Select_set()

Label(root, text = 'NAME', font='arial 12 bold', bg='cyan').place(x=30,y=20)
Entry(root, textvariable = Name).place(x=100,y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold', bg='cyan').place(x=30,y=70)
Entry(root, textvariable = Number).place(x=130,y=70)
Label(root, text = 'CONTACTS', font='arial 12 bold', bg='cyan').place(x= 330, y=100)

Button(root,text="ADD", font='arial 12 bold', command = Add).place(x=30,y=110)
Button(root,text="VIEW", font='arial 12 bold',command = VIEW).place(x=30,y=160)
Button(root,text="EDIT", font='arial 12 bold',command = EDIT).place(x=30,y=210)
Button(root,text="DELETE", font='arial 12 bold',command = DELETE).place(x=30,y=260)
Button(root,text="RESET", font='arial 12 bold', command = RESET).place(x=30,y=310)
Button(root,text="EXIT", font='arial 12 bold', command = EXIT, bg='red').place(x= 310,y=340)

mainloop()
