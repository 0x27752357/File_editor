import os
from tkinter import * 
from easygui import *


            
def deletefile() : 
    file_name = fileopenbox(msg="Enter the file name you want to be deleted : ")
    try :
        os.remove(file_name) 
    except  :
         msgbox(msg="File can not be found")
         
                
def Direction():
    file_name = diropenbox(msg="Choose file pass")
    msgbox(msg=f"Direction of your file is : {file_name}")


def read_file() :
    file_name = fileopenbox(msg="Enter your file name : ")

    with open(file_name) as file :
        try :
            codebox(text=file.read())
        except :
            msgbox(msg="Faild") 
            
            
def rename_file() :
    file_name = fileopenbox(msg="Choose the name of the file you want to rename : ")
    rename = enterbox(msg="Enter your new name : (With format) ")
    
    try :
        os.rename(file_name , rename)
        msgbox(f"{file_name} succesfuly chenged to {rename} ! \nYour renamed files will be saved in the same direction of program")
    except :
        msgbox(msg="Could not find the file")
    
        
def Make_folder() :
    file_name = diropenbox(msg="Choose your path : " , default="/Users/amir")
    new_folder = enterbox(msg="Enter the new folder name : ")
    try :
        os.mkdir(path=file_name + "/" + new_folder)
        msgbox("Done ! ")
    except :
        msgbox(msg="Can not find the file ! ")
        
    
def Make_file() :
    file_name = diropenbox(msg="Enter the direction : " ,  default="/Users/amir")
    new_file_name  = enterbox(msg="Enter your file name : (with format)")  
    print(file_name + "\n" + new_file_name)
    try :
        os.system(command=f"touch {file_name}/{new_file_name}")
        
    except :
        msgbox("FAILD")
        
    
window = Tk()
window.geometry("126x450")

text_1 = Label(text="Welcome" , fg="#4285F4")
text_1.grid(row=0 , column=0)

button_1 = Button(text="Delete file" , command=deletefile , width=10 , height=3)
button_1.grid(row=1 , column=0)

button_2 = Button(text="Direction of the file" , command=Direction , width=10 , height=3)
button_2.grid(row=2 , column=0)

button_3 = Button(text="Reading file" , command=read_file , width=10 , height=3 )
button_3.grid(row=3 , column=0)

button_4 = Button(text="Renaming file" , command=rename_file , width=10 , height=3)
button_4.grid(row=4 , column=0)

button_5 = Button(text="Making folder" , command=Make_folder , width=10 , height=3)
button_5.grid(row=5 , column=0)

button_6 = Button(text="Making file" , command=Make_file , width=10 , height=3 )
button_6.grid(row=6, column=0)

button_7 = Button(text="Exit" , command=window.destroy , width=10 , height=3 )
button_7.grid()


window.mainloop()


