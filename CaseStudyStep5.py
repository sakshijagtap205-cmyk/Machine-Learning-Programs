import pandas as pd  # for EDA

import matplotlib.pyplot as plt  #2 imports for visualization
import seaborn as sns

from sklearn.model_selection import train_test_split

Border =  "-"*30

#############################################
# step1 : load the dataset
############################################

print(Border)
print("step 1 : Load the dataset")
print(Border)

Datapath = "iris.csv"

 # data frame df
df = pd.read_csv(Datapath)
print("Data set loaded successfully")
print("Initial entries from dataset are :")

print(df.head())  # rows of the dataset

#############################################
# step2 :  Data Analysis (EDA) 
############################################

print(Border)
print("step2 :  Data Analysis (EDA) ")
print(Border)

print("Shape of dataset :", df.shape)

print("Column name :", list(df.columns))

print("Missing values per column :")

print(df.isnull().sum())      #isnull is a method

print("Class Distribution(species count)")
print(df["species"].value_counts())

print("Stastitical report of dataset :")
print(df.describe())

########################################################
# step3 :  Decide independent and dependent variables 
########################################################

print(Border)
print("Step 3 :  Decide independent and dependent variables ")
print(Border)

# x : Independent variables / features
# Y :  Dependent variables / lable

feature_columns = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)", 
    "petal width (cm)"
]

X = df[feature_columns]  #independent variables        2d areay df
Y = df["species"] #dependent variable

print("X Shape :", X.shape)
print("Y shape :", Y.shape)

#######################################################
# step4 : Visualization of Dataset 
########################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)


#Scatter plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]== sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"] ,label = sp)
    
plt.title("Marvellous iris case study")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

######################################################
# step5 : split the dataset for training and testing
######################################################

print(Border)
print("step5 : split the dataset for training and testing")
print(Border)

X_train , X_test , Y_train , Y_test = train_test_split(X ,Y, test_size=0.5 , random_state=42)

print("X :", X.shape)   # 150, 4
print("Y :", Y.shape)   # 150 ,  

print("Dataset spliting activity done")

print("X_train:", X_train.shape)   #75 , 4
print("X_test:", X_test.shape)     # 75, 4

print("Y_train:", Y_train.shape)   # 75 ,
print("Y_test:", Y_test.shape)     # 75 , 