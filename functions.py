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




