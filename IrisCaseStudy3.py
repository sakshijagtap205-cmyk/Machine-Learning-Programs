from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris classification case study") 
    print("-"*30)
    
    Dataset = load_iris()  #load iris dataset
    
   # Meta Data of the dataset
    print("Independent variables are :")
    print(Dataset.feature_names)
    print("Length of independent variable :", len(Dataset.feature_names))
    
    print("Dependent variables is :")
    print(Dataset.target_names)
    print("Length of dependent variable :", len(Dataset.target_names))
    
    
if __name__ == "__main__":
    main()