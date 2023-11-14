from time import sleep

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

search = int(input("Enter a number: "))
searches = 0


def binarySearch(search, first, last):
    global searches 
    searches = searches + 1
    if(first > last): return -1

    mid = (first + last) // 2
    
    print(first, last)
    print(data[first:last + 1])
    print("Is " + str(data[mid]) + " the same as " + str(search) + "?")
    print(str(data[mid]).lower() == str(search).lower())

    if(str(data[mid]).lower() == str(search).lower()): return mid

    if(str(data[mid]).lower() > str(search).lower()):
        print("Overshot!")
        sleep(0.1)
        return binarySearch(search, first, mid - 1)

    if(str(data[mid]).lower() < str(search).lower()): 
        print("Undershot!")
        sleep(0.1)
        return binarySearch(search, mid + 1, last)
    

index = binarySearch(search, 0, len(data) - 1)

if index == -1:
    print("No have\n", f"Searches: {str(searches)}")

else:
    print(f"Found at index {index}\n", f"Searches: {str(searches)}")