import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score

def MarvellousRegression(DataPath):
    Border = "-"*40
    
    #step 1 : Load the data
    print(Border)
    print("step 1 : Load the data")
    print(Border)
    
    df = pd.read_csv(DataPath)
    print(df.head())
    
    #step 2 = Remove unwanted columns
    print(Border)
    print("step 2 : Remove unwanted column")
    print(Border)
    
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
        
    print(df.head())
    #step 3 = Check Missing values
    print(Border)
    print("step  3 = Check Missing values")
    print(Border)
    
    print("Total missing values :")
    print(Border)
    print(df.isnull().sum())
    print(Border)

def main():
    MarvellousRegression("Advertising.csv")




from py_compile import main


if __name__ == "__main__":
    main()