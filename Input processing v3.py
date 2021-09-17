import random
try:
    guests = dict()
    amount = int(input("Enter the number of friends joining (including you): \n"))
    if amount <= 0:
        print("No one is joining for the party")
        
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(0, amount):
            guests[input()] = 0
            
        bill = int(input("Enter the total bill value: \n"))
        for i in guests:
            guests[i] = round(bill / len(guests),2)
        #print(guests)
        lucky = input("""Do you want to use the "Who is lucky?" feature? Write Yes/No: \n""")
        if lucky == "Yes":
            print(f"{random.choice(list(guests.keys()))} is the lucky one!")
            
            
        else:
            print("No one is going to be lucky")
except:
    print("No one is joining for the party")
