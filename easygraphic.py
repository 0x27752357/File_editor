
import os 
from easygui import *

#choice = choicebox(msg="Choose your meal : " , title="Menu" , choices=["Pizza" , "Burger", "Pasta" , "Nacho"])

#if choice == "Burger" :
#    multi = multchoicebox(msg="Choose Your specs : " , title="Burger" , choices=["Cheese" , "Tomato" , "Fries" , "Meat Juice" ] )
#    print(f"You chose : {multi.__len__()} item")
 
#string = enterbox(msg="Enter string" , title="Shit")
#integer = integerbox(msg="Enter int" , title="Shit")
#value = []
#value = multenterbox(msg="Enter shits" , title="Shit" , fields=["Name" , "Last name" , "Country" , "Sex" , "Phone number"])
#print(value[1])

#passs = passwordbox(msg="Enter pass" , title="Pass" )
#print(passs)

#codebox()
#dir = diropenbox(msg="ENTER")
#print(dir)
            
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
    

    
while True :
    options = buttonbox(msg="What you want to do ? " , choices=["Delete file" , "Direction of the file" , "Read file" , "Exit"])

    if options == "Delete file" :
        deletefile() 
    
    elif options == "Direction of the file" :
        Direction()
    elif options == "Read file" :
        read_file()
    
    elif options == "Exit" :
         break
    
msgbox(msg="GOODBYe")















