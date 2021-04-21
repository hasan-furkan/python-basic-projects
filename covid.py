age = input("Are you a cigarette addict older than 75 years old? yes or no: ")
if age.title() == "yes":
    age = True
elif age.title() == "No":
    age = False
# 
chronic = input("Do you have a severe chronic disease? yes or no: ")
if chronic.title() == "yes":
    chronic = True
elif chronic.title() == "No":
    chronic = False
#
immune = input("Is your immune system too weak? yes or no: ")
if immune.title() == "Yes":
    immune = True
elif immune.title() == "No":
    immune = False
#
risk = age and chronic or immune
if risk == "yes":
    print("You are in risky group")
else:
    print("You are not in risky group")