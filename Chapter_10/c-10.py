from pathlib import Path
import json


def f_1():
    path = Path("Chapter_10/learning_python.txt")
    contents = path.read_text()
    print(contents)

    lines = contents.splitlines()
    for line in lines:
        print(line)


def f_2():
    path = Path("Chapter_10/learning_python.txt")
    contents = path.read_text()
    # replace the word Python with C
    contents = contents.replace("Python", "C")

    print(contents)


def f_3():
    # using the pi_string.py example
    path = Path("Chapter_10/pi_million_digits.txt")
    contents = path.read_text()

    pi_string = ""
    for line in contents.splitlines():
        pi_string += line.lstrip()

    print(f"{pi_string[:52]}...")


def f_4():
    guest_name = input("Please enter your name: ")
    path = Path("Chapter_10/guest.txt")
    path.write_text(guest_name)


def f_5():
    # create the guest_book file
    path = Path("Chapter_10/guest_book.txt")

    is_more_guests = True
    contents = ""
    while is_more_guests:
        guest_name = input("Please enter your name: ")

        if guest_name == "q":
            is_more_guests = False
        else:
            contents += guest_name + "\n"

    path.write_text(contents)


def f_6():

    first = input("Please enter a first number: ")
    second = input("Please enter a second number: ")
    try:
        result = int(first) + int(second)
    except ValueError:
        print("Either first or second number is not a number")
    else:
        print(result)


def f_7():
    while True:
        first = input("Please enter a first number: ")
        second = input("Please enter a second number: ")
        try:
            result = int(first) + int(second)
        except ValueError:
            print("Either first or second number is not a number")
        else:
            print(result)
            break


def f_8():

    filenames = ["cats.txt", "dogs.txt"]

    contents = ""
    path = ""
    for filename in filenames:
        try:
            path_str = f"Chapter_10/{filename}"
            path = Path(path_str)
            contents = path.read_text()
        except FileNotFoundError:
            print(f"{filename} is missing")
        else:
            print(contents)
            print("------")


def f_9():
    filenames = ["cats.txt", "dogs.txt"]

    contents = ""
    path = ""
    for filename in filenames:
        try:
            path_str = f"Chapter_10/{filename}"
            path = Path(path_str)
            contents = path.read_text()
        except FileNotFoundError:
            pass
        else:
            print(contents)
            print("------")


def f_10():
    """Count the nubmer of times 'the' appears in the text"""

    path = Path("Chapter_10/yamato.txt")
    contents = path.read_text()

    lines = contents.splitlines()
    word_count = 0

    for line in lines:
        word_count = line.lower().count("the ")

    print(word_count)


def f_11_1():
    """Part 1 - Get Favorite Number then store it"""

    favorite_number = input("What is your favorite number?: ")

    # store the number in a json file
    path = Path("Chapter_10/favorite_number.json")

    # convert var to json format
    contents = json.dumps(favorite_number)

    # write the content to the json file
    path.write_text(contents)


def f_11_2():
    """Part 2 - Read the value and and print a message"""

    path = Path("Chapter_10/favorite_number.json")

    # read the content from the json file
    contents = path.read_text()

    # convert the content to python var
    favorite_number = json.loads(contents)

    print(f"I know your favorite number! It's {favorite_number}.")


def f_11_3():
    """Part 3: call parts 1 and 2"""
    f_11_1()
    f_11_2()


def f_12():
    """Combine Part 1 and Part 2"""

    path = Path("Chapter_10/favorite_number.json")
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = input("What is your favorite number?: ")
        contents = json.dumps(favorite_number)
        path.write_text(contents)
        print(f"Your favorite number {favorite_number} has been stored.")


def get_stored_user(path):
    """Get stored username if available"""

    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_user(path):
    """Prompt for a new username."""

    username = input("What is your name?: ")

    age = input("How old are you?: ")

    location = input("Where are you from?: ")

    user = {"username": username, "age": age, "location": location}

    contents = json.dumps(user)
    path.write_text(contents)

    return user


def print_user(user):
    """takes in a dict and prints it out"""
    print("Here is your profile: ")
    for k, v in user.items():
        print(f"{k} : {v}")


def greet_user():
    """Greet the user by name."""

    path = Path("Chapter_10/user.json")

    # get a user | you gone None
    user = get_stored_user(path)

    # if there is a stored user
    if user:

        print(f"Is this your username? {user['username']}")

        answer = input("Please enter y or n: ").lower()

        if answer == "y":
            # if the user stored is same as current user then return info
            print(f"Welcome back, {user['username']}!")
            print("------------")
            print_user(user)

        elif answer == "n":
            # get the info from the user and then print
            user = get_new_user(path)
            print(
                f"We'll remember you when you come back, {user['username']}!"
            )
            print_user(user)

        else:
            print("Invalid response")
    else:
        # there is no user stored yet
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")


def f_13():

    greet_user()


def main():
    f_13()


if __name__ == "__main__":
    main()
