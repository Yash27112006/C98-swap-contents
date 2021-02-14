def swapFileData():
    print("!! Welcome to Swap The Data Program !!")

    name = input("Enter your first name: ")
    print("Hi!", name)
    print("Please tell me the name of the files whose data you want to swap :- ")

    firstFile = input("Enter the name of first file: ")
    secondFile = input("Enter the name of second file: ")

    with open(firstFile, 'r') as a:
        dataA = a.read()

    with open(secondFile, 'r') as b:
        dataB = b.read()

    with open(firstFile, 'w') as a:
        a.write(dataB)

    with open(secondFile, 'w') as b:
        b.write(dataA)

    print("Congratulations !!", name)
    print("The data has been swapped. Now you may view it.")

swapFileData()