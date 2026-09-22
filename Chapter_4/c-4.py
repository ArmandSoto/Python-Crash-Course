
#4-3
def f_3():
    for i in range(1, 21):
        print(i)

#4-4
def f_4(): 
    one_mil = list(range(1, 1_000_001))
    for i in one_mil:
        print(i)

#4-5
def f_5():
    one_mil = list(range(1, 1_000_001))

    minimum = min(one_mil)
    maximum = max(one_mil)
    summation = sum(one_mil)

    print(f"Min is: {minimum}, Max is: {maximum}, Sum is: {summation}")

#4-6
def f_6():
    odd_numbers = list(range(1, 21, 2))

    for num in odd_numbers:
        print(num)

#4-7
def f_7():
    multiples_of_3 = list(range(3, 33, 3))

    for num in multiples_of_3:
        print(num)
# 4-8
def f_8():
    cubes = []
    for value in range(1, 11):
        cubes.append(value**3)

    for cube in cubes:
        print(cube)

#4-9
def f_9():
    multiples_of_3 = list(range(3, 33, 3))

    for num in multiples_of_3:
        print(num)
        
#4-10        
def f_10():

    #first
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The first three items in this list are: numbers")
    print(numbers[:3])

    # middle 
    print("Three items from the middle are: ")

    print(numbers[3:6])

    #end
    print("The last three items in the list are:")
    print(numbers[-3:])

#4-11
def f_11():
    pizzas = ['plain', 'pepporoni', 'bacon']
    friend_pizzas = pizzas[:]

    pizzas.append('sausage')
    friend_pizzas.append('hawaiian')

    print("My favorite pizzas are: ")
    for p in pizzas:
        print(p)

    print("My friend's favorite pizzas are: ")
    for p in friend_pizzas:
        print(p)

#4-12:
def f_12():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    
    my_foods.append('cannoli')
    friend_foods.append('ice cream')

    print("My favorite favorite foods are: ")
    for f in my_foods:
        print(f)

    print("My friend's favorite foods are: ")
    for f in friend_foods:
        print(f)

def f_13():
        
    foods = ('pizza', 'pasta', 'pancakes', 'blt', 'burger') 
    for food in foods: 
        print(food)
    
    print('-------')
    # foods[1] = 'cupcake' #change is rejected
    foods = ('pizza', 'cupcake', 'steak', 'blt', 'burger')
    for food in foods:
        print(food)

#4_14 is the pep style guide
#4_15 Code Review

def main():
    f_13()

if __name__ == "__main__":
    main()