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

        elif userOption == 2:

            if not files:
                print("Please load spreadsheets first.")
                continue

            allPlates = []
            allIssued = []
            allReturned = []
            allSales = []
            allReceptionist = []

            allPlates, allIssued, allReturned, allSales, allReceptionist = loadData(
                files,
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist = removeDuplicates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist, invalidPlates = filterValidPlates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )
    
            report = calculatePlateReport(
                allPlates,
                allIssued,
                allReturned
            )

            sheetReport, workbookReport = createReport()

            saveReport(
                sheetReport,
                workbookReport,
                report,
                "plate"
            )

            print("Plate report generated.")


        elif userOption == 3:

            if not files:
                print("Please load spreadsheets first.")
                continue

            allPlates = []
            allIssued = []
            allReturned = []
            allSales = []
            allReceptionist = []


            allPlates, allIssued, allReturned, allSales, allReceptionist = loadData(
                files,
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist = removeDuplicates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist, invalidPlates = filterValidPlates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )
    

            report = calculateSalesReport(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            sheetReport, workbookReport = createReport()

            saveReport(
                sheetReport,
                workbookReport,
                report,
                "sales"
            )

            print("Sales report generated.")

        elif userOption == 4:

            if not files:
                print("Please load spreadsheets first.")
                continue

            allPlates = []
            allIssued = []
            allReturned = []
            allSales = []
            allReceptionist = []


            allPlates, allIssued, allReturned, allSales, allReceptionist = loadData(
                files,
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist = removeDuplicates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )

            allPlates, allIssued, allReturned, allSales, allReceptionist, invalidPlates = filterValidPlates(
                allPlates,
                allIssued,
                allReturned,
                allSales,
                allReceptionist
            )
    

            generateOutstandingReport(
                allPlates,
                allIssued,
                allReturned,
                allSales
            )

            print("Outstanding report generated.")

        elif userOption == 5:
            print("Goodbye!")

if __name__ == "__main__":
    main()
