from pathlib import Path


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
    path = Path("Chapter_10/yamato.txt")
    contents = path.read_text()

    lines = contents.splitlines()
    word_count = 0

    for line in lines:
        word_count = line.lower().count("the ")

    print(word_count)


def main():
    f_10()


if __name__ == "__main__":
    main()
