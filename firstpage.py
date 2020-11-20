#import module from tkinter for UI
import os
from tkinter import *

#creating instance of TK
root = Tk()
root.configure(background="white")


def function1():
    
    os.system("python3 DetectShapes.py")
    
def function2():
    
    os.system("python3 simple_shape_detection.py")

def function3():

    os.system("python3 Shape_Detection.py")


def function4():

    os.system("python3 Detect3DShape.py")

def function5():

    os.system("python3 ContourWebcam.py")

def function5():

    os.system("python3 blurring_webcam.py")

def function7():

    os.system("python3 ColorDetectionObj.py")

def function8():

    os.system("python3 AboutUs.py")

def function9():

    root.destroy()

def attend():
    # os.startfile(os.getcwd() + "/developers/dietslideshow.html");
    os.system("python3 simple_shape_detection1.py")

#stting title for the window
root.title("AUTOMATIC SHAPE AND COLOUR DETECTION SYSTEM")

#creating a text label
Label(root, text="AUTOMATIC SHAPE AND COLOUR DETECTION SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating buttons
Button(root,text="Detecting Shapes & Highlighting Them",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Shape Recognition & Display its Name",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Count, Detect Shapes & Display their Names",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Detect 3D Contours of Shapes",font=('times new roman',20),bg="#0D47A1",fg="white",command=function4).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Detect Contours using Webcam",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Detecting and recognizing shapes using Webcam",font=('times new roman',20),bg="#0D47A1",fg="white",command=function6).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Colour Detection",font=('times new roman',20),bg="#0D47A1",fg="white",command=function7).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="About us",font=('times new roman',20),bg="#0D47A1",fg="white",command=function8).grid(row=10,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function9).grid(row=11,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
