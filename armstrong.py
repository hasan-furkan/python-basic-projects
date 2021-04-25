while True:
  number = input("enter a number: ")
  if number.isdigit():
    number.split()
    a = 0
    for i in range(len(number)):
      a+=int(number[i])**len(number)
    if a == int(number):
        print(number, "is an Armstrong number")
        break
    else:
        print(number, "is not an Armstrong number")
        break
  else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")