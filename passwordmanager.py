#----------------------------------------------------------------------------------------------------
from tkinter import*
import tkinter.messagebox #for messagebox
import os #for filedialogbox bcoz it is os feature
from tkinter import filedialog
root = Tk()  								#window creation
root.title("Username & Password Manager") #window title
root.configure(bg="#4d4e4f") 			#bg=background color
root.geometry("600x400")
global n,e,p,l 				#declared global for use
#will hold string data in namevar,emailvar,passwordvar----------------------------------------------
namevar=StringVar() #method
emailvar=StringVar()
passwordvar=StringVar()
#methods that get called----------------------------------------------------------------------------
def savemethod():
                  n=namevar.get()	#will fetch value from namevar and hold in n
                  e=emailvar.get()	#similarly
                  p=passwordvar.get()
#----------------------------------------------------------------------------------------------------
                  file=open("D:\\SavedPassWords.txt",'a')#file handling operation read
                  file.write("-----------\n")
                  file.write(n+"\n")		#writing name,email,password to file
                  file.write(e+"\n")
                  file.write(p+"\n")
                  file.write("-----------\n")
                  file.close()			#saving file
				  #using messagebox to show message
                  tkinter.messagebox.showinfo('S A V E D','Data Stored On SavedPassWords.txt')
#-----------------------------------------------------------------------------------------------------
def clearmethod():
#will clear textboxes1,2,3
      tb1.delete(0,END)
      tb2.delete(0,END)
      tb3.delete(0,END)
#-----------------------------------------------------------------------------------------------------
def exitmethod():
#will close window 
      root.destroy()#destructor
#-----------------------------------------------------------------------------------------------------
def openfilemethod():
#used to open file
      fopen=filedialog.askopenfilename(initialdir="D:", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
      ff=open(fopen,'r')
      for c in ff:
#contents of file will be shown in msgbox,every line new msgbox is generated
            tkinter.messagebox.showinfo('Reading File',c)
      ff.close()
#-------------------------------------------------------------------------------------------------------------
def infomethod():#will show info
      tkinter.messagebox.showinfo('I N F O','PYTHON PROJECT\nMADE BY SWAPNIL.S.BARASKAR \nThis program saves Username&Passwords')
#msgbox shows info
#-------------------------------------------------------------------------------------------------------------
#labels & inputs textboxes
#-------------------------------------------------------------------------------------------------------------
name=Label(root,text="Enter Your Name:     ",fg="white",bg="#4d4e4f",font=("Arial Bold",16))
name.grid(row=1,column=1)
tb1=Entry(root,textvariable=namevar,width=30)#namevar will hold this textbox's text
tb1.grid(row=1,column=2)
#similarly,
email=Label(root,text="Enter Your Email ID:  ",fg="white",bg="#4d4e4f",font=("Arial Bold",16))
email.grid(row=2,column=1)
tb2=Entry(root,textvariable=emailvar,width=30)
tb2.grid(row=2,column=2)
password=Label(root,text="Enter Your Password:",fg="white",bg="#4d4e4f",font=("Arial Bold",16))
tb3=Entry(root,textvariable=passwordvar,width=30)
password.grid(row=3,column=1)
tb3.grid(row=3,column=2)
#-------------------------------------------------------------------------------------------------------------
#buttons
openbtn=Button(root,text=" O P E N ",command=openfilemethod,fg="white",bg="blue",font=("Arial Bold",14))
openbtn.grid(row=11,column=1)

clearbtn = Button(root,text=" C L E A R ",command=clearmethod,fg="white",bg="grey",font=("Arial Bold",14))
clearbtn.grid(row=9,column=1)

savebtn = Button(root,text=" S A V E ",command=savemethod,fg="white",bg="green",font=("Arial Bold",14))
savebtn.grid(row=9,column=2)

exitbtn = Button(root,text=" E X I T ",command=exitmethod,fg="white",bg="red",font=("Arial Bold",14))
exitbtn.grid(row=12,column=3)

infobtn=Button(root,text="I N F O ",command=infomethod,fg="white",bg="teal",font=("Arial Bold",14))
infobtn.grid(row=11,column=2)
#-------------------------------------------------------------------------------------------------------------
root.mainloop()
