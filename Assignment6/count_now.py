def count_now(places):
    for place in places:
        if len(place) > 5:
            print(place)


places = input("Enter a list of place names separated by spaces: ").split()
count_now(places)
