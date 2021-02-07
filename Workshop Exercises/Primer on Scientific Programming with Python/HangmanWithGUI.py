#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:26:01 2020

@author: Matthew
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:52:26 2020

@author: Matthew
"""
from tkinter import *
top = Tk()
frame1 = Frame(top)
frame1.pack()

def CallBack():
   word = E1.get()
   print(word)
   frame1.destroy()
   frame2 = Frame(top)
   frame2.pack()
   L2 = Label(frame2, text ='Guess', )
   L2.pack(side = BOTTOM)
   E2 = Entry(frame2)
   E2.pack(side = BOTTOM)
   B2 = Button(frame2, text='Enter', command = Guess)
   B2.pack(side = RIGHT)
   def Guess():
       
B1 = Button(frame1, text ="Enter", command = CallBack)
L1 = Label(frame1, text='Player 1 word')
L1.pack( side = LEFT)
E1 = Entry(frame1)
E1.pack(side = RIGHT)




B1.pack()
top.mainloop()
