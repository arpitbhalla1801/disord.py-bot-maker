from tkinter import *
def Screen1():
    root = Tk()
    root.title('LOGIN')
    root.geometry('300x150')
    root.configure(bg='white')

    Label1=Label(root,text="enter bot token")

    Label1.grid(row=0,padx=10,pady=10)

    inp1=Entry(root,width=25)

    inp1.grid(row=0,column=1)

    def Onclick():
        print("token",inp1.get())
        
    Login=Button(root,text="START",bg="orange",command=Onclick)
    Login.grid(row=3,column=1,pady=10,ipadx=20,ipady=10)
    
    root.mainloop()
Screen1()
