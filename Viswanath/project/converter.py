#importing the Libraries
from gtts import gTTS          
import PIL              
import gtts                   
import pytesseract           
from tkinter import filedialog 
from tkinter import *
from PIL import Image,ImageTk  
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print("All Libraries Imported")
#defining the Window
window = Tk()
window.geometry('1280x832')
window.resizable(0, 0)
window.title("Text Recognition System for Visually Impaired")
image=Image.open("space-background-6.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(image=photo,bg='#8fb5c2') 
lab.pack()

#Defining the Labels
message = Label(window, text="Text Recognition System for Visually Impaired" ,bg="#000000"  ,fg="white"  ,width=50  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=10)
message = Label(window, text="" ,bg="white"  ,fg="black"  ,width=50  ,height=12, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=180, y=170)
lbl2 = Label(window, text="Enter the text :",width=16  ,fg="white"  ,bg="#00008B"    ,height=2 ,font=('Helvetica', 20 , ' bold '))  # #000000
lbl2.place(x=90, y=490)
txt2 = Entry(window,width=40  ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
txt2.place(x=330, y=505)


def Picture_to_Text():
    window.filename =  filedialog.askopenfilename()
    img= PIL.Image.open(window.filename)      
    result= pytesseract.image_to_string(img) 
    res = "***Successfully Converted to Text***\n" + result
    pyperclip.copy(res)
    message.configure(text= res)
    if(result==""):
        res = "Oops, No Text Recognized"
        message.configure(text= res)

def Picture_to_Speech():
    window.filename =  filedialog.askopenfilename()
    img= PIL.Image.open(window.filename)     
    result= pytesseract.image_to_string(img)  
    if(result==""):
        res = "Oops, No Text Recognized"
        message.configure(text= res)   
    res= gTTS(result)                #Internet required
    window.filename =  filedialog.asksaveasfilename()
    res.save(window.filename+ '.mp3') 
    res = "Audio Saved Successfully"
    message.configure(text= res)  

def Text_to_Speech(): 
    textInp= (txt2.get())
    res= gTTS(textInp)
    window.filename =  filedialog.asksaveasfilename()
    res.save(window.filename+ '.mp3')
    res = "Audio Saved Successfully"
    message.configure(text= res)

#Defining the buttons
pictext = Button(window, text="Picture_to_Text", command=Picture_to_Text  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "yellow" ,font=('Helvetica', 15 , ' bold '))
pictext.place(x=1000, y=170)

picspeech = Button(window, text="Picture_to_Speech", command=Picture_to_Speech  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "yellow" ,font=('Helvetica', 15 , ' bold '))
picspeech.place(x=1000, y=270)

textspeech = Button(window, text="Text_to_Speech", command=Text_to_Speech  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "yellow" ,font=('Helvetica', 15 , ' bold '))
textspeech.place(x=1000, y=370)

quitWindow = Button(window, text="QUIT", command=window.destroy  ,fg="red"  ,bg="white"  ,width=17  ,height=2, activebackground = "yellow" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1005, y=500)

window.mainloop()
