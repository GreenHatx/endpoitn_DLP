import ctypes, sys
import db_handler
import os
from PyPDF2 import PdfFileReader
import re

desktopFilePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def fileCheck(path,file):
    dirPath = f"{path}\{file}"

    if os.path.isdir(dirPath):
        os.chdir(dirPath)
        for file in os.listdir():
            # Check whether file is in text format or not

            if file.endswith(".pdf"):
                file_path = f"{dirPath}\{file}"
                pdf = PdfFileReader(file_path)
                for page_num in range(pdf.numPages):

                    pageObj = pdf.getPage(page_num)
                    txt = pageObj.extractText()

                    if re.search(r'[\w\.-]+@[\w\.-]+', txt):
                        print(file_path + " credential information founded ")
                        mycursor = db_handler.mydb.cursor()

                        sql = "INSERT INTO alerts (filePath, eventType) VALUES (%s, %s)"
                        val = (file_path, "E-Mail Credential---------")
                        mycursor.execute(sql, val)

                        db_handler.mydb.commit()

                        print(mycursor.rowcount, "record inserted.")
                        print("mail found")


                    else:
                        print("not found")

            elif file.endswith(".txt"):
                file_path = f"{dirPath}\{file}"
                with open(file_path, 'r') as f:
                    lines = f.read()
                    if re.search(r'[\w\.-]+@[\w\.-]+', lines):
                        mycursor = db_handler.mydb.cursor()

                        sql = "INSERT INTO alerts (filePath, eventType) VALUES (%s, %s)"
                        val = (file_path, "E-Mail Credential----------")
                        mycursor.execute(sql, val)

                        db_handler.mydb.commit()

                        print(mycursor.rowcount, "record inserted.")
                        print(file_path + " credential information founded ")

                        print("mail found")


                    else:
                        print("not found")

            else:
                return fileCheck(dirPath,file)