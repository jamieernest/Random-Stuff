from time import sleep

data = ['Abbey', 'Alan', 'Alex', 'Alexander B', 'Alexander C', 'Alice', 'Amelie', 'Amy', 'Angus OC', 'Angus R', 'Anna', 'Annabelle', 'Archie', 'Arianna', 'Arthur', 'Ava', 'Bart', 'Beatrice', 'Benedict', 'Betty', 'Borui', 'Brodie', 'Cade', 'Calum', 'Charles', 'Clementine', 'Connie', 'Connor', 'Dara', 'Dominick', 'Dorian', 'Edo', 'Edward CS', 'Edward M', 'Elise', 'Eliza', 'Emily', 'Eva', 'Favour', 'Fletcher', 'Flora M', 'Flora S', 'Freddie', 'Gabor', 'George', 'Georgia', 'Georgie', 'Greta', 'Harold', 'Harry', 'Hector', 'Henry', 'Holly', 'Honor', 'Hugo', 'Imogen Hannay', 'Imogen Hilleary', 'Iona C', 'Iona M', 'Iona S', 'Ione', 'Isabella', 'Jack', 'James B', 'James M', 'Jamie', 'Jasmine', 'Jayden', 'Jess', 'Kai', 'Kinvara', 'Kurush', 'Lara', 'Lena', 'Leo', 'Liberty', 'Lilly', 'Lily S', 'Lily W', 'Liza', 'Lizzi', 'Lola', 'Louis B', 'Louis DM', 'Luke', 'Magnus K', 'Magnus P', 'Max C', 'Max DP', 'Maya', 'Mehar', 'Melody', 'Mhairi', 'Mitchell', 'Mizuki', 'Mollie', 'Nicholas', 'Nicolas', 'Owen', 'Patrick', 'Percy', 'Pippa', 'Ramsay', 'Rena', 'Robert', 'Robin', 'Romy', 'Rosie', 'Ryan', 'Sandy', 'Seamus', 'Sholto', 'Siena', 'Sirisha', 'Skye F', 'Skye M', 'Sofia R', 'Sofia T', 'Sophie', 'Susannah', 'Tara', 'Thomas', 'Tom', 'Torcal', 'Torin', 'Vincenzo', 'Vinjero', 'Will', 'William H', 'William R', 'Zoe']

search = str(input("Enter a name: "))
searches = 0

def binarySearch(search, first, last):
    global searches
    searches = searches + 1
    if(first > last): return -1

    mid = (first + last) // 2
    print(first, last)
    print(data[first:last + 1])
    print("Is " + data[mid] + " the same as " + search + "?")
    print(data[mid].lower() == search.lower())

    if(data[mid].lower() == search.lower()): return mid

    if(data[mid].lower() > search.lower()):
        print("Overshot!")
        sleep(0.1)
        return binarySearch(search, first, mid - 1)

    if(data[mid].lower() < search.lower()): 
        print("Undershot!")
        sleep(0.1)
        return binarySearch(search, mid + 1, last)
    

index = binarySearch(search, 0, len(data) - 1)

if index == -1:
    print("No have\n" + f"Searches: {str(searches)}")

else:
    print(f"Found at index {index}\n" + f"Searches: {str(searches)}")