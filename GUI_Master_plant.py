import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModelp 
import webbrowser
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Plant Leaf Disease Detection ")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Plant Leaf Disease Detection ", font=('times', 35,' bold '), height=1, width=60,bg="maroon1",fg="white")
lbl.place(x=0, y=0)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="blue2")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=90)

    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModelp.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s


   
 

def test_model_proc(fn):
    from keras.models import load_model
    #from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('Plant_model.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
     
        
        
        if plant == 0:
            Cd="Apple___Apple_scab\nDiesease is detected\nPrecautions: A well pruned tree with an open canopy allows air to move \nthrough the tree and dry the leaves quickly.  "
           
        elif plant == 8:
            Cd="Apple___Black_rot\nDiesease is detected \nPrecautions: Pruning to maintain an open canopy improves air flow, \n allows faster drying times and enables better coverage with fungicides."
           
        elif plant == 9:
            Cd="Apple___Cedar_apple_rust\nDiesease is detected\nPrecaution: Cedar apple rust is a fungal disease that requires juniper \nplants to complete its two year life-cycle. "
         
        elif plant == 10:            
            Cd="Apple___healthy\nDiesease is detected\nPrecaution: Apples are often treated with pesticides, so consider buying organic or \nwashing them thoroughly before eating to minimize pesticide residue."
        elif plant == 11:
            Cd="Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot\nDiesease is detected\nPrecaution: Avoid planting corn in the same \nfield year after year to reduce the buildup of pathogens in the soil."
            
        elif plant == 12:
            Cd="Corn_(maize)___Common_rust\nDiesease is detected\nPrecaution: Planting resistant varieties is one of \nthe most effective ways to manage the disease."
            
             
        elif plant == 13:
            Cd="Corn_(maize)___healthy\nDiesease is detected\nPrecaution: The health benefits of corn while minimizing potential risks \nand optimizing its nutritional value in your diet."
        elif plant == 14:
            Cd="Corn_(maize)___Northern_Leaf_Blight\nDiesease is detected\nPrecaution: To mitigate Northern Leaf Blight in corn (maize), rotate crops,\n plant resistant varieties "
            
        elif plant == 15:
            Cd="Grape___Black_rot\nDiesease is detected\nPrecaution: To prevent black rot in grapes, employ cultural practices like pruning for good air circulation"
             
        
        elif plant == 1:
            Cd="Grape___Esca_(Black_Measles)\nDiesease is detected\nPrecaution: Maintain their overall health through proper care and management practices."
             
        elif plant == 2:
            Cd="Grape___healthy\nDiesease is detected\nPrecaution: Maintaining grapevines' health is crucial for ensuring optimal\n growth and fruit production."
        elif plant == 3:
            Cd=" Grape___Leaf_blight_(Isariopsis_Leaf_Spot)\nDiesease is detected\nPrecaution: Maintain good vineyard hygiene by removing and destroying infected plant material promptly."   
            
        elif plant == 4:
            Cd="Peach___Bacterial_spot\nDiesease is detected\nPrecaution: This reduces the source of inoculum for bacterial spot."
        elif plant == 5:
            Cd="Peach___healthy\nDiesease is detected\nPrecaution: Maintaining the health of peach trees is crucial for ensuring\n vigorous growth, high fruit quality"
        elif plant == 6:
            Cd="Strawberry___healthy\nDiesease is detected\nPrecaution: Avoid areas prone to waterlogging, as excessive moisture can lead to\n root rot and other diseases."
        elif plant == 7:
            Cd="Strawberry___Leaf_scorch\nDiesease is detected\nPrecaution: Strawberry leaf scorch is a fungal disease caused\n by Diplocarpon earlianum. "
            
            
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=60, font=("bold", 20), bg='bisque2', fg='black')          
    result_label.place(x=250, y=380)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        x2=format(X)+" "
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='C:/crop', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=40)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=100)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=160)
#
button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=160)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=220)



root.mainloop()