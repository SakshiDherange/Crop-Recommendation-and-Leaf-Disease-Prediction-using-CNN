import seaborn as sns
#import tkinter as tk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.naive_bayes import GaussianNB

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


root = tk.Tk()
root.title("soil and Crop Prediction Using Machine Learning")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('bg1.jpg')


image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Soil and Crop Prediction Using Machine Learning  ", font=('times', 30,' bold '), height=1, width=65,bg="green",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("C:/crop/indiancrop_dataset.csv")




le = LabelEncoder()


        
def Model_Training():
    data = pd.read_csv("C:/crop/indiancrop_dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    #data['Auto_Theft_Stolen'] = le.fit_transform(data['Auto_Theft_Stolen'])
    data['N_SOIL'] = le.fit_transform(data['N_SOIL'])
    data['P_SOIL'] = le.fit_transform(data['P_SOIL'])
    data['K_SOIL'] = le.fit_transform(data['K_SOIL'])
    data['TEMPERATURE'] = le.fit_transform(data['TEMPERATURE'])
    data['HUMIDITY'] = le.fit_transform(data['HUMIDITY'])
    data['ph'] = le.fit_transform(data['ph'])
    data['RAINFALL'] = le.fit_transform(data['RAINFALL'])
    data['STATE'] = le.fit_transform(data['STATE'])
    
    
    #print(data['fractal_dimension_mean'])
    #data['Thal'] = le.fit_transform(data['Thal'])
    #print("thal Encoding")
   

    #data['Thal'] = le.fit_transform(data['Thal'])
    #data['ChestPain'] = le.fit_transform(data['ChestPain'])

    """Feature Selection => Manual"""
    x = data.drop(['CROP'], axis=1)
    
    data = data.dropna()

    print(type(x))
    y = data['CROP']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=9999)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    #label4 = tk.Label(root,text =str(repo),width=40,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    #label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Model Traning is Completed \nModel cropSVM.joblib",width=40,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=300,y=200)
    from joblib import dump
    dump (svcclassifier,"cropSVM.joblib")
    print("Model Traning is Completed \n Model saved as cropSVM.joblib")



    
def call_file():
    import Check_crop
    Check_crop.Train()




check = tk.Frame(root, w=100)
check.place(x=700, y=100)


def window():
    root.destroy()



# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text=" Training ", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=200)
# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="SVM prediction ", command=call_file, width=15, height=2)
# button3.place(x=5, y=300)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="CNN prediction  ", command=call_file, width=15, height=2)
# button3.place(x=5, y=200)

# exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
# exit.place(x=5, y=450)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''