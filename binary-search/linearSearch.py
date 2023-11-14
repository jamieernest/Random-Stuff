from time import sleep

data = ["Charles", "Dara", "James M", "Jamie", "Sholto"]
search = str(input("Enter a name: "))
searches = 0

def loopSearch(search): 
    global searches
    for i in range(len(data)):
        searches = i + 1
        print(f"Checking element {i}")
        print(data[i:len(data)])
        print("Is " + data[i] + " the same as " + search + "?")
        print(data[i].lower() == search.lower())
        if data[i].lower() == search.lower():
            return i
        sleep(0.1)
    return -1

index = loopSearch(search)

if index == -1:
    print("No have\n" + f"Searches: {str(searches)}")
else:
    print(f"Found at index {index}\n" + f"Searches: {str(searches)}")