from watchdog.events import FileSystemEventHandler
import os
import time
from PyPDF2 import PdfFileReader
import db_handler
import re
import helper


class Handler(FileSystemEventHandler):
    @staticmethod

    def on_any_event(event):
        # if event.is_directory:
        #     return None
        print(
            "[{}] noticed: [{}] on: [{}] ".format(
                time.asctime(), event.event_type, event.src_path
            )
        )


    def on_modified(self, event):


        for file in os.listdir():

            if file.endswith(".pdf"):
                file_path = f"{helper.desktopFilePath}\{file}"
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
                file_path = f"{helper.desktopFilePath}\{file}"
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
                helper.fileCheck(helper.desktopFilePath,file)