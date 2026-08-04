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

print(df.head(10))  # first 10 rows of the dataset