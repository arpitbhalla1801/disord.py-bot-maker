from tkinter import *
import menu_select
def event_menu():
    root=Tk()
    root.title('Events')
    root.geometry('500x500')

    but1=Button(root, text='Add new event')
    but2=Button(root, text='Delete an event')
    but3=Button(root, text='show existing events')

    but1.pack()
    but2.pack()
    but3.pack()

    Back=Button(root,text="go back",bg="red",fg="white",command=lambda:[root.destroy(),menu_select.offMenu()])
    Back.pack()

    root.mainloop()