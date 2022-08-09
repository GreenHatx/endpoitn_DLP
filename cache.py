if file.endswith(".pdf"):
    file_path = f"{path}\{file}"
    pdf = PdfFileReader(file_path)
    for page_num in range(pdf.numPages):


                    pageObj = pdf.getPage(page_num)
                    txt = pageObj.extractText()

        if re.search(r'[\w\.-]+@[\w\.-]+', txt):
            # print(file_path + " credential information founded ")
            mycursor = mydb.cursor()

            sql = "INSERT INTO alerts (filePath, eventType) VALUES (%s, %s)"
            val = (file_path, "E-Mail Credential---------")
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            print("mail found")


                    else:
                        print("not found")

elif file.endswith(".txt"):
    file_path = f"{path}\{file}"
    with open(file_path, 'r') as f:
        lines = f.read()
        if re.search(r'[\w\.-]+@[\w\.-]+', lines):
            mycursor = mydb.cursor()

                        sql = "INSERT INTO alerts (filePath, eventType) VALUES (%s, %s)"
                        val = (file_path, "E-Mail Credential----------")
                        mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            print(file_path + " credential information founded ")

            print("mail found")


        else:
            print("not found")
