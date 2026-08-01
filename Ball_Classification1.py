def main():
    print("Ball Classification case study")
    
    features = [[35 , "Rough"] , [47 , "Rough"] , [90 , "smooth"] , [48 , "Rough"] , [90 , "smooth"], [35 , "Rough"] , [92 , "smooth"] , [35 , "Rough"] ,[35 , "Rough"], [35 , "Rough"], [96 , "Smooth"], [43 , "Rough"], [110 , "smooth"], [35 , "Rough"], [95 , "smooth"]]
    
    Lables = ["Tennis" , "Tennis" , "Cricket" , "Tennis" , "Cricket", "Tennis" , "Cricket" , "Tennis", "Tennis" , "Tennis", "Cricket", "Tennis", "Cricket", "Tennis" , "Cricket"]

    print("features are :" , features)
    print("Lables are :" , Lables)

if __name__ == "__main__":
    main()