# 07:00 alarm in the morning
clock = float(input("What time is it"))
while True:
     if clock == 07.00:
         print("get ready to go to work")
         break
     elif clock <= 07.30:
          print("you will be late for work")
          break
     else:
         print("You are late for work, you are fired")
         break