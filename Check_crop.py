from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from joblib import dump, load

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    from tkinter import ttk
    from PIL import Image ,ImageTk
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("soil and crop")
    root.configure(background="pink")
    
    
    
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    bg = Image.open(r"image5.jpg")
    bg.resize((1800,h),Image.ANTIALIAS)
    print(w,h)
    bg_img = ImageTk.PhotoImage(bg)
    bg_lbl = tk.Label(root,image=bg_img)
    bg_lbl.place(x=80,y=300)
   
    
    N_SOIL = tk.IntVar()
    P_SOIL = tk.IntVar()
    K_SOIL = tk.IntVar()
    TEMPERATURE = tk.IntVar()
    HUMIDITY = tk.IntVar()
    ph= tk.IntVar()
    

    #certifications= tk.StringVar()
    RAINFALL= tk.IntVar()
    STATE= tk.StringVar()
    
    
    # import requests 
    # api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    
    # import json
    # location_req_url='http://api.ipstack.com/103.51.95.183?access_key=4b0f43bbd8b7a123d8b9d6cde128e6ca'
    # r = requests.get(location_req_url)
    # location_obj = json.loads(r.text)
    
    # lat = location_obj['latitude']
    # lon = location_obj['longitude']
    # latitude = lat
    # longitude = lon
    
    
    # location2 = "%s, %s" % (location_obj['city'], location_obj['region_code'])
    # location2 = location2.replace(',','')
    # print(location2.split()[0])
    # city =location2.split()[0] 
    
    # location_label = tk.Label(root,text="At location  "+str(location2),font=('Times New Roman',35,'italic'),bg="cyan3",fg="white")
    # location_label.place(x=850,y=580)
  
    #===================================================================================================================

    def Detect():
        e1= N_SOIL.get()
        print(e1)
        e2= P_SOIL.get()
        print(e2)
        e3=  K_SOIL.get()
        print(e3)
        #print(type(e3))
        e4= float(TEMPERATURE.get())
        print(float(e4))
        
        e5=  float(HUMIDITY.get())
        print(float(e5))
      
        e6= float(ph.get())
        print(float(e6))
        
        e7= float(RAINFALL.get())
        print(float(e7))
        
        
        e8= STATE.get()
        if e8=="Andaman and Nicobar":
           e8=0
        elif e8=="Andhra Pradesh ": 
             e8=1      
        elif e8=="Assam":
             e8=2
        elif e8=="Chattisgarh":
             e8=3
        elif e8=="Goa":
              e8=4
               
        elif e8=="Gujarat ":    
             e8=5                 
        elif e8=="Haryana":
             e8=6
        elif e8=="Himachal Pradesh":
             e8=7
        
        elif e8=="Jammu and Kashmir":
             e8=8
        elif e8=="Karnataka":
             e8=9
             
            
        elif e8=="Kerala":
             e8=10
        elif e8=="Madhya Pradesh":
             e8=11
   
            
        elif e8=="Maharashtra":
             e8=12
        elif e8=="Manipur":
             e8=13
             
             
             
        elif e8=="Meghalaya":
              e8=14
             
        elif e8=="Nagaland":
               e8=15
        elif e8=="Odisha":
               e8=16
        elif e8=="Pondicherry":
               e8=17
        elif e8=="Punjab":
               e8=18
        elif e8=="Rajasthan":
               e8=19
        elif e8=="Tamil Nadu":
               e8=20
    
        elif e8=="Telangana":
              e8=21
        elif e8=="Tripura":
          e8=22
        elif e8=="Uttar Pradesh":
               e8=23
        elif e8=="Uttrakhand":
              e8=24
              
        elif e8=="West Bengal":
             e8=25
        
        
        else:
             e8=26
        print(e8)
        
       
        #########################################################################################
        
        from joblib import dump , load
        a1=load('SVM.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8]])
        print(v)
        if v[0]=="Apple":
            print("Apple")
            yes = tk.Label(root,text="Apple",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150)
            
            
        if v[0]=="Banana":
            print("Banana")
            yes = tk.Label(root,text="Banana",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150)

        if v[0]=="Blackgram":
            print("Blackgram")
            yes = tk.Label(root,text="Blackgram",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150)
            
        if v[0]=="ChickPea":
            print("ChickPea")
            yes = tk.Label(root,text="ChickPea",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150) 
            
        if v[0]=="Coconut":
            print("Coconut")
            yes = tk.Label(root,text="Coconut",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150) 
            
            
        if v[0]=="Coffee":
             print("Coffee")
             yes = tk.Label(root,text="Coffee",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)
             
        if v[0]=="Cotton":
            print("Cotton")
            yes = tk.Label(root,text="Cotton",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150)  
           
        if v[0]=="Grapes":
            print("Grapes")
            yes = tk.Label(root,text="Grapes",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=900,y=150)
            
        if v[0]=="Jute":
              print("Jute")
              yes = tk.Label(root,text="Jute",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)
             
        if v[0]=="Mango":
              print("Mango")
              yes = tk.Label(root,text="Mango",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)
              
        if v[0]=="MothBeans":
             print("MothBeans")
             yes = tk.Label(root,text="MothBeans",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="MungBean":
             print("MungBean")
             yes = tk.Label(root,text="MungBean",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="Orange":
              print("Orange")
              yes = tk.Label(root,text="Orange",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)

        if v[0]=="KidneyBeans":
             print("KidneyBeans")
             yes = tk.Label(root,text="KidneyBeans",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="Lentil":
             print("Lentil")
             yes = tk.Label(root,text="Lentil",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)
        
        if v[0]=="Maize":
             print("Maize")
             yes = tk.Label(root,text="Maize",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="Papaya":
              print("Papaya")
              yes = tk.Label(root,text="Papaya",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)

        if v[0]=="PigeonPeas":
             print("PigeonPeasr")
             yes = tk.Label(root,text="PigeonPeas",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="Pomgranate":
              print("Pomgranate")
              yes = tk.Label(root,text="Pomgranate",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)

        if v[0]=="Rice":
             print("Rice")
             yes = tk.Label(root,text="Rice",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
             yes.place(x=900,y=150)

        if v[0]=="Watermelon":
              print("Watermelon")
              yes = tk.Label(root,text="Watermelon",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
              yes.place(x=900,y=150)
              
        if v[0]=="Muskmelon":
                print("Muskmelon")
                yes = tk.Label(root,text="Muskmelon",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
                yes.place(x=900,y=150)
                
          





    l1=tk.Label(root,text="N_SOIL",background="pink",font=('times', 20, ' bold '),width=10)
    l1.place(x=0,y=1)
    N_SOIL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar= N_SOIL)
    N_SOIL.place(x=300,y=1)
    


    l2=tk.Label(root,text="P_SOIL",background="pink",font=('times', 20, ' bold '),width=10)
    l2.place(x=0,y=50)
    P_SOIL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=P_SOIL)
    P_SOIL.place(x=300,y=50)

    l3=tk.Label(root,text="K_SOIL",background="pink",font=('times', 20, ' bold '),width=10)
    l3.place(x=0,y=100)
    K_SOIL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar= K_SOIL)
    K_SOIL.place(x=300,y=100)
    
   

    l4=tk.Label(root,text="TEMPERATURE",background="pink",font=('times', 20, ' bold '),width=15)
    l4.place(x=0,y=150)
    TEMPERATURE=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar= TEMPERATURE)
    TEMPERATURE.place(x=300,y=150)

    l5=tk.Label(root,text="HUMIDITY",background="pink",font=('times', 20, ' bold '),width=10)
    l5.place(x=400,y=1)
    HUMIDITY=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=HUMIDITY)
    HUMIDITY.place(x=700,y=1)

    l6=tk.Label(root,text="ph",background="pink",font=('times', 20, ' bold '),width=3)
    l6.place(x=400,y=50)
    ph=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar= ph)
    ph.place(x=700,y=50)

    l7=tk.Label(root,text="RAINFALL",background="pink",font=('times', 20, ' bold '),width=10)
    l7.place(x=400,y=100)
    RAINFALL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=RAINFALL)
    RAINFALL.place(x=700,y=100)

 
    l8=tk.Label(root,text="STATE",background="pink",font=('times', 20, ' bold '),width=7)
    l8.place(x=400,y=150)
    monthchoosen = ttk.Combobox(root, width = 27, textvariable = STATE)

   # Adding combobox drop down list
    monthchoosen['values'] = ('Andaman and Nicobar','Andhra Pradesh','Assam','Chattisgarh','Goa','Gujarat','Haryana',
                              'Himachal Pradesh','Jammu and Kashmir','Karnataka','Kerala','Madhya Pradesh','Maharashtra'
                              ,'Manipur','Meghalaya','Nagaland','Odisha','Pondicherry','Punjab','Rajasthan','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttrakhand','West Bengal'
   					
   					  )
    monthchoosen.place(x=700,y=155)
   #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

 
 
    
    l8=tk.Label(root,text="*******crop and soil prediction*******",background="pink",font=('Harlow Solid Italic', 20, ' bold '),width=60)
    l8.place(x=500,y=250)

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=1000,y=70)
    
    # button1 = tk.Button(root,text="train",command=Detect,font=('times', 20, ' bold '),width=10)
    # button1.place(x=300,y=30)


    root.mainloop()

Train()