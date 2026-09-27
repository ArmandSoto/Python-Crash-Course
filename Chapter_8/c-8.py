from printing_functions import print_models as pm, show_completed_models as scm
from sandwich_functions import print_sandwich_order


def display_message():
    """A function to display a message"""
    print("We are learning about functions in this chapter")


def f_1():
    display_message()


def favorite_book(title):
    title = title.title()
    print(f"One of my favorite books is {title}")


def f_2():
    favorite_book("alice in wonderland")


def make_shirt(size="lg", message="I love Python"):
    print(f"The size is : {size} that says {message}")


def f_3():
    make_shirt("xl", "I love coding.")
    make_shirt(message="I love coding", size="xl")


def f_4():
    make_shirt()
    make_shirt("medium")
    make_shirt(message="I love C")


def describe_city(city, country="USA"):
    print(f"{city} is in {country}")


def f_5():
    describe_city("New York")
    describe_city("London", "UK")
    describe_city("Tokyo", "Japan")


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


def f_6():
    print(city_country("santiago", "chile"))
    print(city_country("London", "UK"))
    print(city_country("Tokyo", "Japan"))


def make_album(artist_name, album_title, num_of_songs="None"):
    album = {
        "artist": artist_name,
        "album": album_title,
    }
    if num_of_songs:
        album["num_of_songs"] = num_of_songs
    return album


def f_7():
    album_1 = make_album("Michael Jackson", "Thriller")
    album_2 = make_album("Pink Floyd", "The Dark Side of the Moon")
    album_3 = make_album("The Beatles", "Abbey Road")
    album_4 = make_album("Nirvana", "Nervermind", 12)

    albums = [album_1, album_2, album_3, album_4]

    for album in albums:
        for k, v in album.items():
            print(f"{k}: {v}")


def f_8():

    while True:
        artist = input("Enter artist name: ")
        if artist == "q":
            break
        title = input("Enter title: ")
        if title == "q":
            break

        album = make_album(artist, title)
        print(album)


def show_messages(messages):
    for msg in messages:
        print(msg)


def f_9():
    messages = ["Hi", "how are you", "ttyl"]
    show_messages(messages)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending Message {current_message}")
        sent_messages.append(current_message)


def f_10():
    messages = ["Hi", "how are you", "ttyl"]
    sent_messages = []
    # [:] means copy via slice shorthand
    send_messages(messages, sent_messages)

    print("------------ Messages --------------------")
    show_messages(messages)
    print("------------ Sent Messages --------------------")
    show_messages(sent_messages)


def f_11():
    messages = ["Hi", "how are you", "ttyl"]
    sent_messages = []
    # [:] means copy via slice shorthand
    send_messages(messages[:], sent_messages)

    print("------------ Messages --------------------")
    show_messages(messages)
    print("------------ Sent Messages --------------------")
    show_messages(sent_messages)


def f_12():
    print_sandwich_order("ham", "cheese")
    print_sandwich_order("bacon", "egg", "lettuce")
    print_sandwich_order("turkey", "tomato", "lettuce", "cheese")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


def f_13():
    user_profile = build_profile(
        "armand", "soto", location="new york", field="compsci", eye_color="brown"
    )

    print(user_profile)


def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info


def f_14():
    car = make_car("subaru", "outback", color="blue", tow_package=True)
    print(car)


def f_15():
    unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
    completed_models = []

    pm(unprinted_designs, completed_models)
    scm(completed_models)


def f_16():
    print_sandwich_order("turkey", "tomato", "lettuce", "cheese")


def main():
    f_16()


if __name__ == "__main__":
    main()
