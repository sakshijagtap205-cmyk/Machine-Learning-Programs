import matplotlib.pyplot as plt


def main():
    marks=[10,34,40,45,55,67,80 ,85 ,87,90,92,98]
    
    plt.hist(
        marks,                  #continuous Data
        bins=5,                 #number of groups
        edgecolor="black",      #border color
        alpha=0.8,              # transperancy
        rwidth=0.9,             #relative width of bars
        
    )
    
    plt.title("Marvelllous  Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
   
    
    plt.show()
    
if __name__ =="__main__":
    main()