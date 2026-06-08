from functions import *
from config import *

def main():
    userOption = 0
    files = []

    while userOption != 5:
        displayMenu()

        userOption = pyip.inputInt(
            prompt="Select an option (1-5): ",
            min=1,
            max=5
        )

        if userOption == 1:
            print("Processing spreadsheets...")
            files = getFilePath()

        elif userOption == 5:
            print("Goodbye!")

if __name__ == "__main__":
    main()
