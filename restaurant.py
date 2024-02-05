#CS175

#Lucas Vandenakker

#restaurant

Joes = "Joe's Gourmet Burgers"
Main = "Main Street Pizza Company"
Corner = "Corner Café"
Mamas = "Mama's Fine Italian"
Chefs = "The Chef's Kitchen"

vegetarian = input("Is anyone in your party vegetarian? ")
vegan = input("Is anyone in your party vegan? ")
glutenFree = input("Is anyone in your party gluten-free? ")

v = vegetarian
ve = vegan
g = glutenFree
print("")

if((v == "Yes" and ve == "Yes" and g == "No")or (v == "No" and ve == "Yes" and g == "Yes")or(v == "No" and ve == "Yes" and g == "No")or (v == "Yes" and ve == "Yes" and g == "Yes")):
    print("Here are your restaurant choices.")
    print(Corner)
    print(Chefs)
if(v == "No" and ve == "No" and g == "No"):
    print("Here are your restaurant choices.")
    print(Joes)
    print(Mamas)
    print(Main)
    print(Corner)
    print(Chefs)
if(v == "Yes" and ve == "No" and g == "No"):
    print("Here are your restaurant choices.")
    print(Mamas)
    print(Main)
    print(Corner)
    print(Chefs)
if((v == "Yes" and ve == "No" and g == "Yes")or (v == "No" and ve == "No" and g == "Yes")):
    print("Here are your restaurant choices.")
    print(Main)
    print(Corner)
    print(Chefs)


