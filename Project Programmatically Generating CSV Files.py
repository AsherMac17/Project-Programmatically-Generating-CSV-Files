from datetime import datetime

# The convertData function converts temperature from F to C.
def convertData(data): 
    convertedValue = (data -32) * 5 / 9
    return convertedValue

# The insertData function adds data to a CSV file
def insertData(filePath, data):
    try:
        with open(filePath, "a")as file:
            file.write(data + "\n")
        return True
    except Exception as error:
        print("Error while writing to the file:", error)
        return False

# The viewData function displays the contents of the CSV file and its path
def viewData(filePath):
    try:
        print("\nReading data from:", filePath)
        with open(filePath, "r") as file:
            print(file.read())
    except Exception as error:
        print("Error while reading the file:", error)

# The getInput function gets the user's input and saves each entry to the CSV file
def getInput():
    entries = int(input("How many entries are you inputting?: "))

    for i in range(entries):
        try:
            date = input("\nEnter a date: ")
            temperature = float(input("Enter the highest temp for the inputted date: "))
        
            convertedValue = convertData(temperature)

            data = date + "," + str(convertedValue)

            if insertData("ZooData.csv", data):
                print("The following data was saved at", datetime.now(), ":", data + ".")
        except Exception as error:
            print("Error while entering data:", error)


print("ashmac9358's Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = ["1 Input Data", "2 View Current Data", "3 Generate Report"]

for option in menuOptions:
    print(option)

choice = input()

if choice == "1":
    getInput()
elif choice == "2":
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")

        
