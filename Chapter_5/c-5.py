
# 5-1 and 5-2 combined
def f_1():
    # test 1
    food = 'cake'
    print("Is food == 'cake'? I predict True")
    print(food == 'cake')

    #test 2 
    print("Is food == 'pizza'? I predict False")
    print(food == 'pizza')

    #test 3 lower
    food.lower() #this does not change the original food variable
    print("Is food.lower() != food? I predict True")
    print(food.lower() != food)

    # test 4 upper
    food = food.upper()
    print("Is food.upper() != food? I predict False")
    print(food.upper() == food)

    #test 5 comparisons 
    age_1 = 33
    age_2 = 18
    print("Is age_1 > age 2? I predict True")
    print(age_1 > age_2)

    #test 6 logical ops and
    print("Are age_1 and age_2 > 20? I predict False")
    print(age_1 and age_2 > 20)

    #test 7 logical ops or
    print("Are age_1 < 30 or age_2 < 30? I predict True")
    print(age_1 < 30 or age_2 < 30)

    #test 8
    book = "Think!"
    print("Is book.title() != book? I predict False")
    print(book.title() != book)

    #test 9 Not in
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    print("Is pepporoni in requested_toppngs? I predict False")
    print('pepproni' not in requested_toppings)

    # test 10 in
    print("Are onions in requested_toppings? I predict True")
    print('onions' in requested_toppings)

def f_3():
    alien_color = 'red'
    if alien_color == 'green':
        print('You just earned 5 points')
    alien_color = 'green'
    if alien_color == 'green':
        print('You just earned 5 points')
    
def f_4():
    # v1
    alien_color = 'yellow'
    if alien_color == 'green':
        print('You just earned 5 points')
    else:
        print('You just earned 10 points')

    # v2
    alien_color = 'green'
    if alien_color == 'green':
        print('You just earned 5 points')
    else:
        print('You just earned 10 points')

def f_5():
    # v1
    alien_color = 'red'
    if alien_color == 'green':
        print('You just earned 5 points')
    elif alien_color == 'yellow':
        print('You just earned 10 points')
    else:
        print('You just earned 15 points')

    # v2
    alien_color = 'green'
    if alien_color == 'green':
        print('You just earned 5 points')
    elif alien_color == 'yellow':
        print('You just earned 10 points')
    else:
        print('You just earned 15 points')
    
    # v3
    alien_color = 'yellow'
    if alien_color == 'green':
        print('You just earned 5 points')
    elif alien_color == 'yellow':
        print('You just earned 10 points')
    else:
        print('You just earned 15 points')

def f_6():
    age = 34
    
    if age < 2:
        print('The person is a baby')
    elif age < 4:
        print('The person is a toddler')
    elif age < 13:
        print('The person is a kid')
    elif age < 20:
        print('The person is a teenager')
    elif age < 65:
        print('The person is an adult')
    else:
        print('The person is an elder')

def f_7():
    favorite_fruits = ['apple', 'blueberries', 'bananas']
    
    if 'apple' in favorite_fruits:
        print('You really like apples!')
    if 'blueberries' in favorite_fruits:
        print('You really like blueberries!')
    if 'bananas' in favorite_fruits:
        print('You really like bananas')
    if 'mango' in favorite_fruits:
        print('You really like mangos!')
    if 'strawberry' in favorite_fruits:
        print('You really like straberries!')

def f_8():
    usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
    for username in usernames:
        if username == 'admin':
            print('Hello admin would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again')

def f_9():
    usernames = []
    if usernames:
        for username in usernames:
            if username == 'admin':
                print('Hello admin would you like to see a status report?')
            else:
                print(f'Hello {username}, thank you for logging in again')
    else:
        print('We need to find some users!')

def f_10():
    current_users = ['User1', 'User2', 'User3', 'User4', 'User5']
    # homogenize case to make uniqueness depend on characters
    current_users_lower = []

    for current_user in current_users:
        current_users_lower.append(current_user.lower())

    new_users = ['User2', 'User4']

    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f'{new_user}, You will need to enter a new username')
        else:
            print('The username is available')

def f_11():
    ordinals = list(range(1,10))
    ending = ''
    for num in ordinals:
        if num == 1:
            ending = 'st'
        elif num == 2:
            ending = 'nd'
        elif num == 3:
            ending = 'rd'
        else:
            ending = 'th'
        print(f'{num}{ending}')

# f_12 and #f_13 are negligible

def main():
    f_11()

if __name__ == "__main__":
    main()