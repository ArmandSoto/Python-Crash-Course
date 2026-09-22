
def f_1():
    rental = input("What kind of rental car would you like?: ")
    print(f"Let me see if I can find you a {rental}")

def f_2():
    group_size = input("How many people are in your dinner group? ")
    group_size = int(group_size)
    if group_size > 8:
        print("You'll have to wait for a table ...")
    else:
        print("Your table is ready.")

def f_3():
    number = input("Pleae enter a number: ")
    number = int(number)
    if number % 10 == 0:
        print(f"{number} is a multiple of 10")
    else:
        print(f"{number} is not a multiple of 10")

def f_4():
    toppings = []

    active = True
    
    while active:
        topping = input("Please enter a topping: ")
        if topping == 'quit':
            active = False
        else:
            print(f"We will add {topping} to your pizza")
            toppings.append(topping)

def f_5():
    collecting_tickets = True

    while collecting_tickets:
        age = input("Please enter your age: ")
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif age >= 3 and age <= 12:
            print("Your ticket is $10")
        elif age > 12:
            print("Your ticket is $15")
        else:
            collecting_tickets = False

def f_6():
    # use a conditional test in while statement
    toppings = []
    topping = ''
    while topping != 'quit:':
        topping = input("Please enter a topping: ")
        if topping != 'quit':
            print(f"We will add {topping} to your pizza")
            toppings.append(topping)

    # use an active variable to control how long it runs --  done, skip --

    #Use a break statement to exit the loop when user enters quit
    toppings = []
    topping = ''
    while True:
        topping = input("Please enter a topping: ")
        if topping == 'quit':
            break
        print(f"We will add {topping} to your pizza")
        toppings.append(topping)

# 7-7 is just writing an infinte loop -- skip --

def f_8():
    sandwich_orders = ['BLT', 'Italian Sub', 'Club Sandwich']
    finished_sandwiches = []
    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(f"I made your {sandwich} order")

    print("We made the following sandwiches: ")
    for sandwich in finished_sandwiches:
        print(sandwich.title())

def f_9():
    sandwich_orders = ['BLT', 'Pastrami', 'Italian Sub', 'Pastrami', 
                       'Club Sandwich', 'Pastrami']
    finished_sandwiches = []
    print("The deli has run out of Pastrami")
    
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
        
    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(f"I made your {sandwich} order")

    print("We made the following sandwiches: ")
    for sandwich in finished_sandwiches:
        print(sandwich.title())

def f_10():
    responses = {}
    polling_active = True

    while polling_active:
        name = input("\nWhat is your name? ")
        response = input("If you could visit one place in the world, where "
                         "would you go? ")
        
        responses[name] = response
        
        repeat = input("Would you like to let another perosn respond? "
                       "(yes/ no) ")
        if repeat == 'no':
            polling_active = False

    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to visit {response}")

def main():
    f_10()


if __name__ == "__main__":
    main()