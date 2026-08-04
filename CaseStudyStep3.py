import pandas as pd

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