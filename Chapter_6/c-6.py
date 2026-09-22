def f_1():
    person = {
        'first_name': 'Criston',
        'last_name': 'Flores',
        'age': 34,
        'city': 'Manhattan',    
    }
    print(f'{person.get('first_name')} {person.get('last_name')} {person.get('age')} {person.get('city')}')

# Accessing a dict, chose to use bracket notation
def f_2():
    favorite_numbers = {
        'Criston': 1,
        'Ali': 2,
        'Mom': 3,
        'Eddie': 4,
        'Armand': 5,
    }
    print(f'Criston: {favorite_numbers['Criston']}')
    print(f'Ali: {favorite_numbers['Ali']}')
    print(f'Mom: {favorite_numbers['Mom']}')
    print(f'Eddie: {favorite_numbers['Eddie']}')
    print(f'Armand: {favorite_numbers['Armand']}')

def f_3():
    #5 programming words you've learned 
    glossary = {
        'Dictionary': 'a collection of key-value pairs',
        'Increment': 'Increase by an amount',
        'Get': 'Retrieve a value from a dictionary, o.w. return None',
        'None': 'A special value which means, no value exists',
        'Key': 'A way to access a dictionary, a value associated with another value'
    }
    print(f' Dictionary - {glossary['Dictionary']}')
    print(f' Increment - {glossary['Increment']}')
    print(f' Get - {glossary['Get']}')
    print(f' None - {glossary['None']}')
    print(f' Key - {glossary['Key']}')

def f_4():
    glossary = {
        'Dictionary': 'a collection of key-value pairs',
        'Increment': 'Increase by an amount',
        'get()': 'Retrieve a value from a dictionary, o.w. return None',
        'None': 'A special value which means, no value exists',
        'Key': 'A way to access a dictionary, a value associated with another value',
        'Value': 'Something you get back when you access a dictionary using a key',
        'items()': 'Returns a sequence of key-value pairs',
        'keys()' : "When you don't need values in a dictionary, returns a sequence of keys",
        'sorted()': "Sorts the value in alphabetical order",
        'values()': "When you don't need keys in a dictionary, returns a sequence of values"

    }
    for key, value in glossary.items():
        print(f'{key} - {value}')
    
def f_5():
    rivers = {
        'nile': 'africa',
        'amazon': 'south america',
        'the yangzte': 'asia'
    }

    for key, value in rivers.items():
        print(f'The {key} runs through {value}')
    for river in rivers.keys():
        print(river)
    for country in rivers.values():
        print(country)

def f_6():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python'
    }
    people_to_poll = ['mary', 'jeff', 'jen', 'phil', 'christie']

    for name in people_to_poll:
        # we can put a for loop in an if statement - very powerful
        if name in favorite_languages.keys():
            print(f'Thank you {name} for responding')
        else:
            print(f'Hi, {name} we invite you to take the favorite languages '
                  'poll')
def f_7():
    people = {
        'cflores' : {
            'first_name': 'Criston',
            'last_name' : 'Flores',
            'age' : '34',
            'city' : 'Manhattan'
        },

        'aelayni' : {
            'first_name': 'Ali',
            'last_name': 'Elayni',
            'age' : 34,
            'city': 'Maspeth'
        },

        'eflores' : {
            'first_name': 'Edwin',
            'last_name': 'Flores',
            'age': 34,
            'city': 'forest hills'
        }

    }

    for person, info in people.items():
        print(f'{person} : ')
        print(f' First: {info['first_name']}, Last: {info['last_name']}, ' 
              f'Age: {info['age']}, City: {info['city']}')

def f_8():
    sidney = {
        'first': 'sidney',
        'type': 'dog',
        'owner': 'madelaine'
    }

    frasier = {
        'first': 'fraisher',
        'type': 'cat',
        'owner': 'madelaine'
    }

    cecil = {
        'first': 'cecil',
        'type': 'turtle',
        'owner': 'madelaine'
    }

    pets = []

    pets.append(sidney)
    pets.append(frasier)
    pets.append(cecil)

    for pet in pets:
        print(f'First: {pet['first']}, type: {pet['type']}, ' 
              f'owner: {pet['owner']}')

def f_9():
    favorite_places = {
        'Criston': ['Tokyo', 'NYC', 'Kyoto'],
        'Ali': ['NYC', 'Machu Picchu', 'Tokyo'],
        'Edwin': ['Rome', 'Paris', 'Sidney']
    }

    for person, places in favorite_places.items():
        print(f"{person}'s favorite places are: ")
        for place in places:
            print(f'\t{place}')

def f_10():
    favorite_numbers = {
        'Criston': [1,5],
        'Ali': [2, 4],
        'Mom': [3,1],
        'Eddie': [4, 2],
        'Armand': [1,7],
    }
    
    for person, numbers in favorite_numbers.items():
        print(f"{person}'s favorite nubmers are: ")
        for number in numbers:
            print(number)

def f_11():
    cities = {
        'tokyo': {
            'country': 'japan',
            'population': 14_000_000,
            'fact': 'Tokyo is the largest metropolitan area in the world'
        },
        'paris': {
            'country': 'france',
            'population': 2_000_000,
            'fact': 'Home to the famous Eiffel Tower'
        },
        'sydney': {
            'country': 'australia',
            'population': 5_000_000,
            'fact': 'known for the iconic Syney Opera House'
        }
    }

    for city, info in cities.items():
        print(f'{city} info: ')
        print(f'Country: {info['country']}, Population: {info['population']}, '
              f'Fact: {info['fact']}')

# 6_12 can be skipped

def main():
    f_11()

if __name__ == "__main__":
    main()