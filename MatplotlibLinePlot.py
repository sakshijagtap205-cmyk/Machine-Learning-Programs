import matplotlib.pyplot as plt


def main():
    X = [1,2,3,4,5] 
    Y = [10,25,18,35,30]
    
    plt.plot(
        X,                    #values of x axis
        Y,                     # values of Y axis
        marker = "o",
        linestyle = "--",
        linewidth = 1,
        markersize = 4,
        label = "marks"
    )
    
    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")
    plt.grid(True)
    
    plt.legend()
    plt.show()
    
    
if __name__ =="__main__":
    main()