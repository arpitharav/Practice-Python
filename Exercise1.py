import datetime
now = datetime.datetime.now()
CurrentYear = now.year
x = input("Enter Your Name: ")
y = int(input("Enter your age: "))
Year100 = CurrentYear - y + 100
print("The year you will turn 100 years is " + str(Year100))
