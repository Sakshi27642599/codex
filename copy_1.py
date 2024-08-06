import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
# from gui_stuff import *

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------
#from tkinter import END

def Reset():
    for widget in [t1, t2, t3, t4, t5]:
        widget.delete(1.0, END)

    for widget in [NameEn, S1En, S2En, S3En, S4En, S5En]:
        widget.delete(0, END)
        NameEn.delete(first=0,last=100)

def KNN():
    if(Symptom1.get() == "None"):
        t1.delete("1.0", END)
        t1.insert(END, "ENTER SYMPTOM PLEASE!!!!")
        t1.place(x=550, y=420, width=200, height=30)

    else:
        from sklearn.neighbors import KNeighborsClassifier
        clf1 = KNeighborsClassifier()
        clf1 = clf1.fit(X,np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred=clf1.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf1.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            t1.delete("1.0", END)
            t1.insert(END, disease[a])
        else:
            t1.delete("1.0", END)
            t1.insert(END, "Not Found")

        #t1.grid(row=15, column=1, padx=10)
        t1.place(x=550, y=420, width=200, height=30)

def DecisionTree():
    if(Symptom2.get() == "None"):
        t2.delete("1.0", END)
        t2.insert(END, "ENTER SYMPTOM PLEASE!!!!")
        t2.place(x=550, y=460, width=200, height=30)
    else:
        from sklearn import tree

        clf2 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        clf2 = clf2.fit(X,y)

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred=clf2.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            # print (k,)
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf2.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break


        if (h=='yes'):
            t2.delete("1.0", END)
            t2.insert(END, disease[a])
        else:
            t2.delete("1.0", END)
            t2.insert(END, "Not Found")

        #t2.grid(row=17, column=1 , padx=10)
        t2.place(x=550, y=460, width=200, height=30)


def randomforest():
    if(Symptom3.get() == "None"):
        t3.delete("1.0", END)
        t3.insert(END, "ENTER SYMPTOM PLEASE!!!!")
        t3.place(x=550, y=500, width=200, height=30)
    else:
        from sklearn.ensemble import RandomForestClassifier
        clf3 = RandomForestClassifier()
        clf3 = clf3.fit(X,np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred=clf3.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            t3.delete("1.0", END)
            t3.insert(END, disease[a])
        else:
            t3.delete("1.0", END)
            t3.insert(END, "Not Found")
            
        #t3.grid(row=19, column=1 , padx=10)
        t3.place(x=550, y=500, width=200, height=30)

def SVM():
    if(Symptom4.get() == "None"):
        t4.delete("1.0", END)
        t4.insert(END, "ENTER SYMPTOM PLEASE!!!!")
        t4.place(x=550, y=540, width=200, height=30)
    else:
        from sklearn.svm import SVC
        clf4 = SVC()
        clf4 = clf4.fit(X,np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred=clf4.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

        if (h=='yes'):
            t4.delete("1.0", END)
            t4.insert(END, disease[a])
        else:
            t4.delete("1.0", END)
            t4.insert(END, "Not Found")

        #t4.grid(row=21, column=1 , padx=10)
        t4.place(x=550, y=540, width=200, height=30)

def NaiveBayes():
    if(Symptom5.get() == "None"):
         t5.delete("1.0", END)
         t5.insert(END, "ENTER SYMPTOM PLEASE!!!!")
         t5.place(x=550, y=580, width=200, height=30)
    else:
            from sklearn.naive_bayes import GaussianNB
            gnb = GaussianNB()
            gnb=gnb.fit(X,np.ravel(y))

            # calculating accuracy-------------------------------------------------------------------
            from sklearn.metrics import accuracy_score
            y_pred=gnb.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred,normalize=False))
            # -----------------------------------------------------

            psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1

            inputtest = [l2]
            predict = gnb.predict(inputtest)
            predicted=predict[0]

            h='no'
            for a in range(0,len(disease)):
                if(predicted == a):
                    h='yes'
                    break

            if (h=='yes'):
                t5.delete("1.0", END)
                t5.insert(END, disease[a])
            else:
                t5.delete("1.0", END)
                t5.insert(END, "Not Found")

            #t5.grid(row=23, column=1 , padx=10)
            t5.place(x=550, y=580, width=200, height=30)
             
# gui_stuff------------------------------------------------------------------------------------
root=Tk()
root.geometry("500x500")
bg=PhotoImage(file="image2.png")
label1=Label(root,image=bg)
label1.place(x=0,y=0)

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

# Heading
w2 = Label(root, justify="center", text=" Disease Prediction using Machine Learning  ", fg="black",font="bold")
w2.config(font=("ALGERIAN",42))
w2.grid(row=1, column=0, columnspan=4,padx=0.01)

# labels
NameLb = Label(root,text="Name of the Patient", fg="yellow", bg="black",font="bold")
#NameLb.grid(row=6, column=0, pady=20,padx=180, sticky=W)
NameLb.place(x=300, y=80, width=200, height=40)
w3 = Label(root,text=" Please enter the symptoms",bg="grey", fg="cyan",font="bold")
w3.place(x=380,y=130,width=310,height=35)

w4 = Label(root,text=" Please click here.....",bg="grey", fg="black",font="bold")
w4.place(x=950,y=150,width=310,height=35)

S1Lb = Label(root, text="Symptom 1", fg="light grey", bg="black",font="bold")
#S1Lb.grid(row=7, column=0, pady=10,padx=90, sticky=W)
S1Lb.place(x=350, y=170, width=120, height=50)

S2Lb = Label(root, text="Symptom 2", fg="light grey", bg="black",font="bold")
#S2Lb.grid(row=8, column=0, pady=10,padx=90,sticky=W)
S2Lb.place(x=350, y=210, width=120, height=50)

S3Lb = Label(root, text="Symptom 3", fg="light grey", bg="black",font="bold")
#S3Lb.grid(row=9, column=0, pady=10,padx=90 ,sticky=W)
S3Lb.place(x=350, y=250, width=120, height=50)

S4Lb = Label(root, text="Symptom 4", fg="light grey", bg="black",font="bold")
#S4Lb.grid(row=10, column=0, pady=10,padx=90, sticky=W)
S4Lb.place(x=350, y=290, width=120, height=50)

S5Lb = Label(root, text="Symptom 5", fg="light grey" ,bg="black",font="bold")
#S5Lb.grid(row=11, column=0, pady=10,padx=90, sticky=W)
S5Lb.place(x=350, y=330, width=120, height=50)

knnLb = Label(root, text="KNeighborsClassifier", fg="cyan", bg="grey",font="bold")
#knnLb.grid(row=15, column=0, pady=10,padx=90,sticky=W)
knnLb.place(x=260, y=420, width=200, height=30)

lrLb = Label(root, text="DecisionTree", fg="cyan", bg="grey",font="bold")
#lrLb.grid(row=17, column=0, pady=10,padx=90,sticky=W)
lrLb.place(x=260, y=460, width=200, height=30)

destreeLb = Label(root, text="RandomForest", fg="cyan", bg="grey",font="bold")
#destreeLb.grid(row=19, column=0, pady=10,padx=90, sticky=W)
destreeLb.place(x=260, y=500, width=200, height=30)

svmLb = Label(root, text="SVM", fg="cyan", bg="grey",font="bold")
#svmLb.grid(row=21, column=0, pady=10,padx=90,sticky=W)
svmLb.place(x=260, y=540, width=200, height=30)

ranfLb = Label(root, text="NaiveBayes", fg="cyan", bg="grey",font="bold")
#ranfLb.grid(row=23, column=0, pady=10,padx=90, sticky=W)
ranfLb.place(x=260, y=580, width=200, height=30)
# entries 
OPTIONS = sorted(l1)

NameEn = Entry(root,width=40,textvariable=Name)
#NameEn.grid(row=7, column=1)
NameEn.place(x=550, y=87, width=160, height=30)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
#S1En.grid(row=8, column=1)
S1En.place(x=550, y=180, width=160, height=30)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
#S2En.grid(row=10, column=1)
S2En.place(x=550, y=220, width=160, height=30)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
#S3En.grid(row=10, column=1)
S3En.place(x=550, y=260, width=160, height=30)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
#S4En.grid(row=11, column=1)
S4En.place(x=550, y=300, width=160, height=30)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
#S5En.grid(row=12, column=1)
S5En.place(x=550, y=340, width=160, height=30)

knn = Button(root, text="KNeighborsClassifier", command=KNN,bg="grey",fg="cyan",font="bold")
#knn.grid(row=8, column=3,padx=10)
knn.place(x=1000, y=200, width=200, height=30)

dst = Button(root, text="DecisionTree", command=DecisionTree,bg="grey",fg="cyan",font="bold")
#dst.grid(row=9, column=3,padx=10)
dst.place(x=1000, y=240, width=200, height=30)

rnf = Button(root, text="Randomforest", command=randomforest,bg="grey",fg="cyan",font="bold")
#rnf.grid(row=10, column=3,padx=10)
rnf.place(x=1000, y=280, width=200, height=30)

svm = Button(root, text="SVM", command=SVM,bg="grey",fg="cyan",font="bold")
#svm.grid(row=11, column=3,padx=10)
svm.place(x=1000, y=320, width=200, height=30)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="grey",fg="cyan",font="bold")
#lr.grid(row=12, column=3,padx=10)
lr.place(x=1000, y=360, width=200, height=30)

resetbtn = Button(root, text="Reset", command = Reset,bg="grey",fg="cyan",font="bold")
resetbtn.place(x=1000, y=400,width=200, height=30)

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="black")

t2 = Text(root, height=1, width=40,bg="white",fg="black")

t3 = Text(root, height=1, width=40,bg="white",fg="black")

t4 = Text(root, height=1, width=40,bg="white",fg="black")

t5 = Text(root, height=1, width=40,bg="white",fg="black")


def submit():
    Name = entry_name.get()   

    if Name != " ":
        messagebox.showerror("Error", "Please enter your name")
    else:
        # Process the login here
        messagebox.showinfo("Success", "Entered your name successful")

entry_name =Entry(root)
button_submit = tk.Button(root, text="Submit", command=submit,bg="grey",fg="cyan",font="bold")
button_submit.place(x=1060,y=100,width=90,height=40)

root.mainloop()