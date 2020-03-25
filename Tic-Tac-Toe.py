#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:50:04 2020

@author: root
"""
#this for interrupted messages
import tkinter.messagebox
from tkinter import *

root = Tk()



#To set vues in the 2 Entries
PXScores=IntVar()
POScores=IntVar()
#Set startup values in the 2 Entries
PXScores.set(0)
POScores.set(0)
#This is for reset all X|O Buttons to default setting
def reset():
    flag = 0
    bclick = True
    
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    btn1.configure(state=NORMAL)
    btn2.configure(state=NORMAL)
    btn3.configure(state=NORMAL)
    btn4.configure(state=NORMAL)
    btn5.configure(state=NORMAL)
    btn6.configure(state=NORMAL)
    btn7.configure(state=NORMAL)
    btn8.configure(state=NORMAL)
    btn9.configure(state=NORMAL)

def disableButton():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)
  

#this is for start a new game loop
def newGame():
    PXScores.set(0)
    POScores.set(0)
    reset()
 
bclick = True
 #if it become 8 this means all 9 buttons are clicked
flag = 0  

#This is for check buttons states & check if there is a winner or not   
def btnClick(buttons):
        global bclick, flag
        
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            #buttons.configure(state=DISABLED)
            bclick = False
            checkForWin()
            flag += 1
    
        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            #buttons.configure(state=DISABLED)
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
        
#This is all probabilities of win
def checkForWin():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] =='X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
        btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X'):
        #set score of how meny playerX wins
        s=float(PXScores.get())
        s=s+1
        PXScores.set(s)
        disableButton() 
        #reset()
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Player X is a Winner" )
        
    elif(flag == 8):
        #this means all 9 buttons are clicked
        disableButton() 
        #reset()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        
    elif(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
         btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
         btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
         btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
         btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
         btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
         btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
         btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O'):
         #set score of how meny playerO wins 
         n=float(PXScores.get())
         n=n+1
         POScores.set(n)
         disableButton()
         #reset()
         tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player O is a Winner")



#This is a GUI code 
root.geometry("660x343+0+0")
root.title("Tec-Tac-Toe")
root.configure(background = 'Cadet Blue')

top = Frame(root,bg = 'Cadet Blue',pady = 2, width = 600, height = 45, relief =RIDGE)
top.grid(row=0,column=0)

LTitle = Label(font= ('arial',25,'bold'),text="Tic-Tac-Toe Game",bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
LTitle.grid(row=0,column=0)

MFram = Frame(root,bg = 'Powder Blue',bd=10, width = 660, height = 255, relief =RIDGE)
MFram.grid(row=1,column=0)

LFram = Frame(MFram,bg = 'Cadet Blue',bd=10, width = 280,pady = 2,padx = 2, height = 255, relief =RIDGE)
LFram.pack(side=LEFT)

RFram = Frame(MFram,bg = 'Cadet Blue',bd=10, width = 280,pady = 2,padx = 2, height = 255, relief =RIDGE)
RFram.pack(side=RIGHT)

RFram1 = Frame(RFram,bg = 'Cadet Blue',bd=10, width = 280,pady = 2,padx = 2, height = 125, relief =RIDGE)
RFram1.grid(row=0,column=0)

PXLabel = Label(RFram1,font= ('arial',20,'bold'),text="PlayerX :",bg='Cadet Blue',fg='Cornsilk')
PXLabel.grid(row=0,column=0)

PXScore=Entry(RFram1,textvariable=PXScores)
PXScore.grid(row=0,column=1)

POLabel = Label(RFram1,font= ('arial',20,'bold'),text="PlayerO :",bg='Cadet Blue',fg='Cornsilk')
POLabel.grid(row=1,column=0)

POScore=Entry(RFram1,textvariable=POScores)
POScore.grid(row=1,column=1)

RFram2= Frame(RFram,bg = 'Cadet Blue',bd=10, width = 280,pady = 2,padx = 2, height = 125, relief =RIDGE)
RFram2.grid(row=1,column=0)

RBtn=Button(RFram2,text="Reset", width = 35, height = 3,pady = 2,padx = 2,command=reset)
RBtn.grid(row=0,column=0)

NGBtn=Button(RFram2,text="New Game", width = 35, height = 3,pady = 2,padx = 2,command=newGame)
NGBtn.grid(row=1,column=0)




btn1=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn1))
btn1.grid(row=1,column=0)

btn2=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn2))
btn2.grid(row=1,column=1)

btn3=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn3))
btn3.grid(row=1,column=2)

btn4=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn4))
btn4.grid(row=2,column=0)

btn5=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn5))
btn5.grid(row=2,column=1)

btn6=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn6))
btn6.grid(row=2,column=2)

btn7=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn7))
btn7.grid(row=3,column=0)

btn8=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn8))
btn8.grid(row=3,column=1)

btn9=Button(LFram,text=" ", width = 8,height =4,command=lambda:btnClick(btn9))
btn9.grid(row=3,column=2)

checkForWin()

root.mainloop()
 