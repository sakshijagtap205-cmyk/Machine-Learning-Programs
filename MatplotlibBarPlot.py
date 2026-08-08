import matplotlib.pyplot as plt


def main():
    language = ["C" , "C++" , "Java" , "Python"]
    Students = [30 , 40 , 35 , 60]
    
    
    plt.bar(
        language,
        Students,
        width = 0.6,                 #width of bar
        edgecolor = "Black",        #border colours of bar
        linewidth = 1,               #width of  border
        alpha = 0.8,                 #transperence 0.0 to 0.1
        label = "Students"           #legend text
    )
    
    plt.title("Marvellous bar plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of students")
    
    plt.legend()
    plt.show()
    
if __name__ =="__main__":
    main()