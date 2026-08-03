#Rough ->1
#smooth -> 0

#tennis ->1
#Cricket ->2

def main():
    print("Ball Classification case study")
    
    features = [[35 , "1"] , [47 , "1"] , [90 , "0"] , [48 , "1"] , [90 , "0"], [35 , "1"] , [92 , "0"] , [35 , "1"] ,[35 , "1"], [35 , "1"], [96 , "0"], [43 , "1"] ,[110 , "0"], [35 , "1"], [95 , "0"]]
    
    Lables = ["1" , "1" , "2" , "1" , "2", "1" , "2" , "1", "1" , "1", "2", "1", "2", "1" , "2"]

    print("features are :", features)
    print("Lables are : ", Lables)
    
if __name__ == "__main__":
       main()