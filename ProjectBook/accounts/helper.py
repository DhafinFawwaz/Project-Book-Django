import re
class AutoSubmit:
    def submit():
        print("------------------")
        print("Starting...")
        print("------------------")

        txt = """Title : "A Logical Introduction to Proof"\n
        Genre : Mathematic\n
        Description: The book is intended for students who want to learn how to prove theorems and be better prepared for the rigors required in more advance mathematics. One of the key components in this textbook is the development of a methodology to lay bare the structure underpinning the construction of a proof, much as diagramming a sentence lays bare its grammatical structure. Diagramming a proof is a way of presenting the relationships between the various parts of a proof. A proof diagram provides a tool for showing students how to write correct mathematical proofs.\n
        Price : 360000\n
        Thumbnail : ./images/A_Logical_Introduction_to_Proof.jpg\n
        Pdf: ./pdf/A_Logical_Introduction_to_Proof.pdf\n
        Rating: [0, 0, 0, 0, 0]"""

        book_data = re.split(r"Title: |Genre: |Description: |Price: |Thumbnail: |Pdf: |Rating: |Title : |Genre : |Description : |Price : |Thumbnail : |Pdf : |Rating : |\n", txt)
        book_data = list(filter(None, book_data))
        book_data = list(filter(re.compile('[^\s]').match, book_data))

        book_data[0] = book_data[0][1:-1] # remove ""
        book_data[4] = book_data[4].replace('./images/', '') # remove ./images/
        book_data[5] = book_data[5].replace('./pdf/', '') # remove ./pdf/
        print(book_data)
        print("------------------")

        title = book_data[0]
        genre = book_data[1]
        description = book_data[2]
        quantity = 1
        price = int(book_data[3])
        thumbnail = book_data[4]
        pdf = book_data[5]

        from accounts.models import Book
        book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
        book.save()
        print("------------------")
        print("Saved")
        print("------------------")
        print("Current Data:")
        print(Book.objects.all())

    def submit_all_txt():
        import os
        
        print("------------------")
        print("Starting...")

        import glob, os
        os.chdir(r"C:\Users\sppAghetti\Documents\ITB\Pengkom\Django\Project-Book\ProjectBook\accounts\static\txt")
        
        first_time = False
        for file in glob.glob("*.txt"):
            text_file = open(file, "r", encoding='utf8', errors="replace")
            txt = text_file.read()
            
            print("------------------")
            print(txt)
            print("------------------")

            # book_data = re.split(r"Title: |Genre: |Description: |Price: |Thumbnail: |Pdf: |Rating: |Title : |Genre : |Description : |Price : |Thumbnail : |Pdf : |Rating : |\n", txt)
            # book_data = list(filter(None, book_data))
            
            # if first_time == False:
            #     first_time = True            
            #     book_data.pop(0) # remove weird first element
            # # book_data = list(filter(None, book_data))
            
            # book_data = list(filter(re.compile('[^\s]').match, book_data))

            # book_data[0] = book_data[0][1:-1] # remove ""
            # book_data[4] = book_data[4].replace('./images/', '') # remove ./images/
            # book_data[5] = book_data[5].replace('./pdf/', '') # remove ./pdf/
            # print(book_data)
            # print("------------------")
            # # return

            # title = book_data[0]
            # genre = book_data[1]
            # description = book_data[2]
            # quantity = 1
            # price = int(book_data[3])
            # thumbnail = book_data[4]
            # pdf = book_data[5]

            # from accounts.models import Book
            # book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
            # book.save()
            # print("------------------")
            # print("Current Data:")
            # print(Book.objects.all())

            # print(file, "saved successfully")
            # print("------------------")



            book_data = re.split(r"tiltle: |genre: |quantity: |description: |price: |thumbnail: |pdf: |rating : |\n", txt)
            book_data = list(filter(None, book_data))
            book_data = list(filter(re.compile('[^\s]').match, book_data))

            book_data[0] = book_data[0][1:-1] # remove ""
            book_data[1] = book_data[1][1:-1] # remove ""
            book_data[3] = book_data[3][1:-1] # remove ""
            book_data[5] = book_data[5].replace('./images/', '') # remove ./images/
            book_data[5] = book_data[5][1:-1] # remove ""
            book_data[6] = book_data[6].replace('./pdf/', '') # remove ./pdf/
            book_data[6] = book_data[6][1:-1] # remove ""
            print(book_data)
            print("------------------")

            title = book_data[0]
            genre = book_data[1]
            description = book_data[3]
            quantity = 1
            price = int(book_data[4])
            thumbnail = book_data[5]
            pdf = book_data[6]

            from accounts.models import Book
            book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
            book.save()
            print("------------------")
            print("Saved")
            print("------------------")
            print("Current Data:")
            print(Book.objects.all())


        print("------------------")

    def submit_manual():
        print("------------------")
        print("Starting...")
        print("------------------")

        txt = """tiltle: “Kimia Brady James Jilid 2”
genre: “Chemistry”
quantity: 1
description: “This text provides the forum for problem solving and concept mastery of chemical phenomena that leads to proficiency and success in the General Chemistry course.”
price: 56000
thumbnail: “./images/KimiaBradyJamesJilid2.jpg“
pdf: “./pdf/KimiaBradyJamesJilid2.pdf”
rating: [0, 0, 0, 0, 0]"""

        # book_data = re.split(r"Title: |Genre: |Description: |Price: |Thumbnail: |Pdf: |Rating: |Title : |Genre : |Description : |Price : |Thumbnail : |Pdf : |Rating : |\n", txt)
        book_data = re.split(r"tiltle: |genre: |quantity: |description: |price: |thumbnail: |pdf: |rating : |\n", txt)
        book_data = list(filter(None, book_data))
        book_data = list(filter(re.compile('[^\s]').match, book_data))

        book_data[0] = book_data[0][1:-1] # remove ""
        book_data[1] = book_data[1][1:-1] # remove ""
        book_data[3] = book_data[3][1:-1] # remove ""
        book_data[5] = book_data[5].replace('./images/', '') # remove ./images/
        book_data[5] = book_data[5][1:-1] # remove ""
        book_data[6] = book_data[6].replace('./pdf/', '') # remove ./pdf/
        book_data[6] = book_data[6][1:-1] # remove ""
        print(book_data)
        print("------------------")

        title = book_data[0]
        genre = book_data[1]
        description = book_data[3]
        quantity = 1
        price = int(book_data[4])
        thumbnail = book_data[5]
        pdf = book_data[6]

        from accounts.models import Book
        book = Book(title=title, genre=genre, quantity=quantity, description=description, thumbnail=thumbnail, pdf=pdf, price=price)
        book.save()
        print("------------------")
        print("Saved")
        print("------------------")
        print("Current Data:")
        print(Book.objects.all())

