def display_message():
    """ A function to display a message """
    print("We are learning about functions in this chapter")

def f_1():
    display_message()


def favorite_book(title):
    title = title.title()
    print(f"One of my favorite books is {title}")

def f_2():
    favorite_book('alice in wonderland')

def make_shirt(size='lg', message='I love Python'):
    print(f"The size is : {size} that says {message}")

def f_3():
    make_shirt('xl', "I love coding.")
    make_shirt(message="I love coding", size="xl")

def f_4():
    make_shirt()
    make_shirt("medium")
    make_shirt(message="I love C")

def describe_city(city, country='USA'):
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
        'artist': artist_name,
        'album': album_title,
    }
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album


def f_7():
    album_1 = make_album("Michael Jackson", "Thriller" )
    album_2 = make_album("Pink Floyd", "The Dark Side of the Moon")
    album_3 = make_album("The Beatles", "Abbey Road")
    album_4 = make_album("Nirvana", "Nervermind", 12)

    albums = [album_1, album_2, album_3, album_4]
    
    for album in albums: 
        for k, v in album.items():
            print(f"{k}: {v}")


def main():
    f_7()

if __name__ == "__main__":
    main()    