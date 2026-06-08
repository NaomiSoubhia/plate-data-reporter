from functions import *
from config import *

def main():
    userOption = 0
    files = []

    while userOption != 5:
        displayMenu()
        userOption = pyip.inputInt("Select option (1-5): ", min=1, max=5)

        if userOption == 5:
            print("Goodbye!")

if __name__ == "__main__":
    main()
