# functions.py

import os
import pyinputplus as pyip
import openpyxl
from datetime import datetime
import re
from config import get_report_path


def displayMenu():
    print("\n1-Load Files\n2-Plate Report\n3-Sales Report\n4-Outstanding Report\n5-Exit")


def getFilePath():
    files = []
    filePath = ""

    while filePath.lower() != "done":
        filePath = pyip.inputStr("Enter file path or done: ")

        if filePath.lower() == "done":
            break

        if not filePath.endswith(".xlsx"):
            print("Invalid file")
            continue

        if not os.path.exists(filePath):
            print("File not found")
            continue

        files.append(filePath)

    return files

def openFile(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    return readSpreadsheet(sheet)


def readSpreadsheet(sheet):
    plate, issued, returned, sales, rec = [], [], [], [], []

    row = 2
    cols = ["A","B","C","D","E"]

    while sheet["A" + str(row)].value:
        plate.append(sheet["B" + str(row)].value)
        issued.append(sheet["C" + str(row)].value)
        returned.append(sheet["D" + str(row)].value)
        sales.append(sheet["A" + str(row)].value)
        rec.append(sheet["E" + str(row)].value)
        row += 1

    return plate, issued, returned, sales, rec



def loadData(files, allPlates, allIssued, allReturned, allSales, allReceptionist):
    for file in files:
        plate, issued, returned, sales, rec = openFile(file)

        allPlates += plate
        allIssued += issued
        allReturned += returned
        allSales += sales
        allReceptionist += rec

    return allPlates, allIssued, allReturned, allSales, allReceptionist


def isValidPlate(plate):
    if not plate:
        return False

    plate = str(plate).strip().upper()

    return (
        re.match(r"^[A-Z]{3}$", plate[:3]) and
        re.match(r"^[0-9]{3}$", plate[3:6])
    )


def filterValidPlates(allPlates, allIssued, allReturned, allSales, allReceptionist):
    valid = []

    vp, vi, vr, vs, vrx = [], [], [], [], []

    for i in range(len(allPlates)):
        if isValidPlate(allPlates[i]):
            vp.append(allPlates[i])
            vi.append(allIssued[i])
            vr.append(allReturned[i])
            vs.append(allSales[i])
            vrx.append(allReceptionist[i])

    return vp, vi, vr, vs, vrx


def createReport():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Plate", "Uses", "Days", "Hours", "Minutes", "Seconds"])
    return ws, wb


def calculateTime(i, r):
    if not i or not r:
        return 0
    diff = r - i
    return diff.days * 86400 + diff.seconds


def convertTime(s):
    d = s // 86400
    s %= 86400
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return d,h,m,s

# Generate plate report
def calculatePlateReport(allPlates, allIssued, allReturned):
    report = []
    printed = []

    for i in range(len(allPlates)):
        plate = allPlates[i]
        if plate in printed:
            continue
        printed.append(plate)
        count = 0
        total_seconds = 0
        for j in range(len(allPlates)):
            if allPlates[j] == plate:
                count += 1
                issued = allIssued[j]
                returned = allReturned[j]
                total_seconds += calculateTime(issued, returned)
        days, hours, minutes, seconds = convertTime(total_seconds)
        report.append([plate, count, days, hours, minutes, seconds])
    return report

# Generate sales report
def calculateSalesReport(allPlates, allIssued, allReturned, allSales, allReceptionist):
    report = []
    processed = []
    for i in range(len(allSales)):
        salesperson = allSales[i]
        if salesperson in processed:
            continue
        processed.append(salesperson)
        count = 0
        total_seconds = 0
        for j in range(len(allSales)):
            if allSales[j] == salesperson:
                count += 1
                issued = allIssued[j]
                returned = allReturned[j]
                total_seconds += calculateTime(issued, returned)
        days, hours, minutes, seconds = convertTime(total_seconds)
        report.append([salesperson, count, days, hours, minutes, seconds])
    return report

# Generate outstanding plates report (TXT)
def generateOutstandingReport(allPlates, allIssued, allReturned, allSales):
    path = get_report_path("outstanding_report.txt")
    with open(path, "w") as file:
        file.write("Outstanding Plates Report\n")
        file.write("=========================\n\n")
        found = False
        for i in range(len(allPlates)):
            plate = allPlates[i]
            issued = allIssued[i]
            returned = allReturned[i]
            salesperson = allSales[i]
            if returned is None:
                found = True
                file.write("Plate: " + plate + "\n")
                file.write("Issued by: " + salesperson + "\n")
                file.write("Issued Date:" + str(issued) + "\n")
                file.write("Status: NOT RETURNED\n")
                file.write("Report generated at:" + str(datetime.now()) + "\n")
                file.write("-------------------------\n")
        if not found:
            file.write("No outstanding plates found.\n")
    print("Outstanding report generated successfully!")

