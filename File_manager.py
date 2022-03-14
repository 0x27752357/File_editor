
import os 
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
        msgbox(f"{file_name} succesfuly chenged to {rename} ! ")
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
        
    
while True :
    options = buttonbox(msg="What you want to do ? " , choices=["Delete file" , "Direction of the file" , "Read file" , "Rename file" , 
                                                                "Make folder" , "Make file" ,"Exit"])

    if options == "Delete file" :
        deletefile() 
    
    elif options == "Direction of the file" :
        Direction()
    elif options == "Read file" :
        read_file()
    elif options == "Rename file" :
        rename_file()
    elif options == "Make folder" :
        Make_folder()
    elif options == "Make file" :
        Make_file()
    elif options == "Exit" :
         break
    
msgbox(msg="GOODBYe")















