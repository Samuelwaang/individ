InfoDb = []
InfoDb.append({  
 "Fruit": "Apple",  
 "Taste": "Sweet",  
 "Grows": "Tree",  
 "ShelfLife": "3 Weeks",  
 "GrowthConditions":["cold in winter","moderate in summer","medium to high humidity","full sun"]  
})  

InfoDb.append({  
 "Fruit": "Lemon",  
 "Taste": "Sour",  
 "Grade": "Tree",  
 "ShelfLife": "3-4 Weeks",  
 "GrowthConditions":["tropical","subtropical humid","slightly acidic soil","full to partial sun"]  
})  

def print_data(n):
    print(InfoDb[n]["Fruit"], InfoDb[n]["Taste"])
    print("\t", "GrowthConditions: ", end="")
    print(", ".join(InfoDb[n]["GrowthConditions"]))
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

  
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)

    

      