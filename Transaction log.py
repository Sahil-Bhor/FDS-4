print("Welcom to SaHll's Bank \nInstructions :\nTo deposite your Money = D amount \
      \nTo withdraw = W amount \nFor Example :- D 200,W 100\n")

data = input("********STM*******\n")
ls = []
ls.append(data.split(','))
ls = ls[0]

print("\n")
balance = 0
for item in ls:
    item = item.split(" ")
    action = item[0]
    amount = int(item[1])
    if action == "D":
      balance = balance+amount
      print(f"You Deposited {amount}.00 Rs")
    elif action == "W":
      balance = balance-amount
      if balance < 0:
        print("No sufficient balance to withdraw..!")
      else:
        print(f"You Withdraw {amount}.00 Rs")    
      
print("-----------------------------------")
print(f"Your balance is : {balance}.00 Rs")
print("-----------------------------------")