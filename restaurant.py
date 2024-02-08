#CS175

#Lucas Vandenakker

#restaurant



Joes = "Joe's Gourmet Burgers"
Main = "Main Street Pizza Company"
Corner = "Corner Café"
Mamas = "Mama's Fine Italian"
Chefs = "The Chef's Kitchen"

repeat = True
while(repeat == True):
    
    vegetarian = input("Is anyone in your party vegetarian? ")

    while(vegetarian != "yes" and vegetarian != "Yes" and vegetarian != "no" and vegetarian != "No"):
        print("Not a valid input, try again: ")
        vegetarian = input("Is anyone in your party vegetarian? ")
        
    vegan = input("Is anyone in your party vegan? ")

    while(vegan != "yes" and vegan != "Yes" and vegan != "No" and vegan != "no"):
        print("Not a valid input, try again: ")
        vegan = input("Is anyone in your party vegan? ")
        
    glutenFree = input("Is anyone in your party gluten-free? ")

    while(glutenFree != "yes" and glutenFree != "Yes" and glutenFree != "no" and glutenFree !="No"):
        print("Not a valid input, try again: ")
        glutenFree = input("Is anyone in your party gluten-free? ")
       

    v = vegetarian
    ve = vegan
    g = glutenFree
    print("")

    if(((v == "Yes" or v =="yes") and (ve == "Yes" or ve == "yes") and (g == "No" or g == "no"))or ((v == "No" or v == "no") and (ve == "Yes" or ve == "yes") and (g == "Yes" or g == "yes"))or((v == "No" or v == "no") and (ve == "Yes" or ve == "yes") and (g == "No" or g =="no"))or ((v == "Yes" or v == "yes")and (ve == "Yes" or ve == "yes") and (g == "Yes" or g =="yes"))):
        print("Here are your restaurant choices.")
        print(Corner)
        print(Chefs)
    if((v == "No" or v == "no") and (ve == "No" or ve == "no") and (g == "No" or g == "no")):
        print("Here are your restaurant choices.")
        print(Joes)
        print(Mamas)
        print(Main)
        print(Corner)
        print(Chefs)
    if((v == "Yes" or v == "yes") and (ve == "No" or ve== "no") and (g == "No" or g == "no")):
        print("Here are your restaurant choices.")
        print(Mamas)
        print(Main)
        print(Corner)
        print(Chefs)
    if(((v == "Yes" or v == "yes") and (ve == "No" or ve == "no") and (g == "Yes" or g =="yes"))or ((v == "No" or v == "no") and (ve == "No" or ve == "no") and (g == "Yes" or g == "yes"))):
        print("Here are your restaurant choices.")
        print(Main)
        print(Corner)
        print(Chefs)
        
    print("")
    menuRepeat = input("Would you like to see the menu again?: ")
    if(menuRepeat == "yes" or menuRepeat == "Yes"):
        repeat = True
    else:
        repeat = False

print("done")


