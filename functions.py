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
