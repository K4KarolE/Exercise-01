weight = float(input("What is your weight? "))
weight_type = input("KG or LBS? Type `K` or `L`. ")

if weight_type.upper() != "L" and weight_type.upper() != "K":
    print("Sorry, invalid mass type")
if weight_type.upper() == "L":
    print("Your weight in KGs: " + str(weight * 0.45))
if weight_type.upper() == "K":
    print("Your weight in LBs: " + str(weight / 0.45))


