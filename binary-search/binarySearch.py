from time import sleep

data = ["Charles", "Dara", "James M", "Jamie", "Sholto"]

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