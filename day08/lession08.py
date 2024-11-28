number = int(input("შეიყვანეთ რიცხვი: "))
if number < 10:
    print("რიცხვი ნაკლებია 10-ზე.")
else:
    print("რიცხვი არ არის ნაკლები 10-ზე.")

number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("რიცხვი არის კენტი.")
else:
    print("რიცხვი არ არის კენტი.")

number = int(input("შეიყვანეთ რიცხვი: "))
if number > 0:
    print("რიცხვი არის დადებითი.")
elif number < 0:
    print("რიცხვი არის უარყოფითი.")
else:
    print("რიცხვი არის ნულოვანი.")

number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
if number1 == number2:
    print("რიცხვები არიან ერთნაირი.")
else:
    print("რიცხვები არ არიან ერთნაირი.")

number = int(input("შეიყვანეთ რიცხვი: "))
if number > 100 and number % 2 == 0:
    print("რიცხვი არის 100-ზე მეტი და კენტი.")
else:
    print("რიცხვი არ არის 100-ზე მეტი ან არ არის კენტი.")

number = int(input("შეიყვანეთ რიცხვი: "))
if number % 5 == 0 or number % 10 == 0:
    print("რიცხვი არის 5-ის ან 10-ის მულტიპლიკატორი.")
else:
    print("რიცხვი არ არის არც 5-ის, არც 10-ის მულტიპლიკატორი.")
