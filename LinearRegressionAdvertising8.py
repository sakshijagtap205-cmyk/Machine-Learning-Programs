import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score



def MarvellousRegression(DataPath):
    Border = "-"*50
    
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
    
    #step 4 = stastitical summary
    print(Border)
    print("step  4 =  stastitical summary")
    print(Border)
    
    df.describe()
    
    #step 5 = correlation
    print(Border)
    print("step  5 =  Corellation")
    print(Border)

    print(df.corr())
    
    #step 6 = seprate Independent and dependent variables
    print(Border)
    print("step  6 = seprate Independent and dependent variables")
    print(Border)
    
    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("Independent variables:")
    print(X.head())
    
    print("Dependent variables:")
    print(Y.head())
    
    #step 7 = split the dataset
    print(Border)
    print("step  7 = split the dataset ")
    print(Border)
    
    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    
    print("Training data :", X_train.shape)
    print("Testing the data ", X_test.shape)
    
    
    
    #step 8 = create and train the model
    print(Border)
    print("step 8 = create and train the model ")
    print(Border)
    
    model = LinearRegression()
    
    model = model.fit(X_train , Y_train)
    print("model trained succesfully") 
    
    #Step 9 = test the model
    
    print(Border)
    print("step 9 = test the model ")
    print(Border)
    
    Y_pred = model.predict(X_test)
    
    print("Expected answer :")
    print(Y_test[:3])
    
    print("predected answer :")
    print(Y_pred[:3])
    
    
    #step 10 = Evaluate the model
    print(Border)
    print("step 10 = Evaluate the model ")
    print(Border)
    
    MSE = mean_squared_error(Y_test, Y_pred)
    
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)
    print("MSE:", MSE)
    print("RMSE:", RMSE)
    print("R2:", R2)
    
    #step 11 = Display the coefficient
    print(Border)
    print("step 11 = Display the coefficient ")
    print(Border)
    
    print("Tv coefficient :", model.coef_[0])
    print("radio coefficient :", model.coef_[1])
    print("newspaper coefficient :", model.coef_[2])
    
    print("Intercept :", model.intercept_)
    
    
    
def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()