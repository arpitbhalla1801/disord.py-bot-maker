from tkinter import *
import tkinter.font as font

import events
'''
import screen4
import screen5
import screen6
'''
def offMenu():

    root = Tk()
    root.title('MENU')
    root.geometry('500x500')
    root.configure(bg='white')

    myFont = font.Font(size=14)
    myButton=Button(root,text="turn on bot",font=myFont,bg="GREEN",width=10,height=2,command=lambda: [root.destroy(),onMenu()])
    myButton1=Button(root,text="Events",font=myFont,command=lambda: [root.destroy(),events.event_menu()],bg="#f9bf8f",width=10,height=3)
    # myButton2=Button(root,text="Commands",font=myFont,command=lambda: [root.destroy(),screen4.Screen4()],bg="#f9bf8f",width=10,height=3)
    # myButton3=Button(root,text="Settings",font=myFont,command=lambda: [root.destroy(),screen5.Screen5()],bg1="#f9bf8f",width=10,height=3)
    #myButton4=Button(root,text="Action",font=myFont,command=lambda: [root.destroy(),screen6.Screen6()],bg="#f9bf8f",width=10,height=3)

    myButton.place(relx=0.15,rely=0.1,x=3,y=7,anchor=CENTER)
    myButton1.place(relx=0.35,rely=0.35,x=10,y=10,anchor=CENTER)
    # myButton2.place(relx=0.35,rely=0.35,x=150,y=10,anchor=CENTER)
    # myButton3.place(relx=0.35,rely=0.35,x=10,y=120,anchor=CENTER)
    #myButton4.place(relx=0.35,rely=0.35,x=150,y=120,anchor=CENTER)

    Back=Button(root,text="Exit",bg="red",fg="white",command=root.destroy)
    Back.place(relx=0.35,rely=0.35,x=230,y=250)

    root.mainloop()
def onMenu():

    root = Tk()
    root.title('MENU')
    root.geometry('500x500')
    root.configure(bg='white')

    myFont = font.Font(size=14)
    myButton=Button(root,text="turn off bot",font=myFont,bg="RED",width=10,height=2,command=lambda: [root.destroy(),offMenu()])
    myButton1=Button(root,text="Events",font=myFont,command=lambda: [root.destroy(),events.event_menu()],bg="#f9bf8f",width=10,height=3)
    # myButton2=Button(root,text="Commands",font=myFont,command=lambda: [root.destroy(),screen4.Screen4()],bg="#f9bf8f",width=10,height=3)
    # myButton3=Button(root,text="Settings",font=myFont,command=lambda: [root.destroy(),screen5.Screen5()],bg="#f9bf8f",width=10,height=3)
    #myButton4=Button(root,text="Action",font=myFont,command=lambda: [root.destroy(),screen6.Screen6()],bg="#f9bf8f",width=10,height=3)

    myButton.place(relx=0.15,rely=0.1,x=3,y=7,anchor=CENTER)
    myButton1.place(relx=0.35,rely=0.35,x=10,y=10,anchor=CENTER)
    # myButton2.place(relx=0.35,rely=0.35,x=150,y=10,anchor=CENTER)
    # myButton3.place(relx=0.35,rely=0.35,x=10,y=120,anchor=CENTER)
    #myButton4.place(relx=0.35,rely=0.35,x=150,y=120,anchor=CENTER)

    Back=Button(root,text="Exit",bg="red",fg="white",command=root.destroy)
    Back.place(relx=0.35,rely=0.35,x=230,y=250)

    root.mainloop()
