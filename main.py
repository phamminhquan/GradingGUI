#---------GRADING GUI---------#

import os
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.simpledialog as sd

#---List Init--#
#--Entry Boxes--#
section_entry=[]
lab_entry=[]
score_entry=[]
comment_entry=[]
check_box=[]
check_box_var=[]

#---Functions--#
def sub_input():
    # Initialization
    section=[]
    score=[]
    comment=[]
    check=[]
    final_comment=''
    final_score = max_score
    
    # Data acquisition and processing
    for se,sc,co,ch in zip(section_entry,score_entry,comment_entry,check_box_var):
        if ch.get() == 0:
            final_comment = final_comment + '-' + sc.get() + ' for ' + se.get() + ', ' + co.get() + '\n'
            final_score = final_score - int(sc.get())
            
    # Output
    # Create a new window
    out_win = Tk()
    
    # Put the output as text on window
    out = Text(out_win, bg='white', fg='black', relief='flat')
    out.insert(END, 'Comments:\n' + final_comment + '\n' + 'Score: ' + str(final_score))
    out.config(state=DISABLED) # forbid text edition
    out.pack()


#---Start GUI---#    
root = Tk()

#---Message Box---#
sec_num = sd.askinteger('Question Real Quick','How many sections do you want rubric to have?')
while type(sec_num) is not int:
    sec_num = sd.askinteger('Question Real Quick','How many sections do you want rubric to have?')
    
max_score = sd.askinteger('Question Real Quick','Max Points?')
while type(max_score) is not int:
    max_score = sd.askinteger('Question Real Quick','Max Points?')
    

#---Title---#
title_frame = Frame(root)
title_frame.pack(side=TOP)
title = Label(title_frame, text='RUBRIC', fg='red', font=("Georgia", 14))
title.pack()

#---Body---#
outline_frame = Frame(root)
outline_frame.pack()

#--Submit Button--#
sub_but = Button(outline_frame, text='Submit', bg='white', fg='green', command=sub_input)
sub_but.grid(row=0, column=4)

#--Outline--#
section_title = Label(outline_frame, text='Section', font=("Georgia", 12))
section_title.grid(row=1, column=0, padx=(100,100))
laboutline_title = Label(outline_frame, text='Lab Outline', font=("Georgia", 12))
laboutline_title.grid(row=1, column=1, padx=(100,100))
score_title = Label(outline_frame, text='Score', font=('Georgia',12))
score_title.grid(row=1, column=2, padx=(100,100))
comment_title = Label(outline_frame, text='Comment', font=('Georgia',12))
comment_title.grid(row=1, column=3, padx=(100,100))

# Creating entry boxes according to the sections number inputted
for i in range(sec_num):
    #--Entry--#
    section_entry.append(Entry(outline_frame))
    section_entry[i].grid(row=2+i, column=0)
    lab_entry.append(Entry(outline_frame))
    lab_entry[i].grid(row=2+i, column=1)
    score_entry.append(Entry(outline_frame))
    score_entry[i].grid(row=2+i, column=2)
    comment_entry.append(Entry(outline_frame))
    comment_entry[i].grid(row=2+i, column=3)

    #--Check Button--#
    check_box_var.append(IntVar(value=1))
    check_box.append(Checkbutton(outline_frame, variable=check_box_var[i]))
    check_box[i].grid(row=2+i,column=4)
    

root.mainloop()