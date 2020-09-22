# https://www.freestudentprojects.com/java-projects/library-management-system-project-report/
# Library management system - planning, organizing and managing the library tasks


class Books:

    def __init__(self, bookname, booknumber):
        self.bookname = bookname
        self.booknumber = booknumber


class Students:

    def __init__(self, stdname, rollnumber, studentbooklist):
        self.stdname = stdname
        self.rollnumber = rollnumber
        self.studentbooklist = studentbooklist


class LibraryManagement:

    def __init__(self, studentlist, bookstock):
        self.studentlist = studentlist
        self.bookstock = bookstock

    def addBook(self, book, bookstock):
        self.book = book
        self.bookstock = bookstock
        bookstock.append(book)

    def removeBook(self, book, bookstock):
        self.book = book
        self.bookstock = bookstock
        bookstock.remove(book)

    def borrowBook(self, book, bookstock, student):
        self.book = book
        self.bookstock = bookstock
        for i in range(len(studentlist)):
            if student == studentlist[i]:
                self.studentlist[i].studentbooklist.append(book)
        self.removeBook(book, bookstock)

    def submitBook(self, book, bookstock, student):
        self.book = book
        self.bookstock = bookstock
        self.addBook(book, bookstock)
        for i in range(len(studentlist)):
            if student == studentlist[i]:
                self.studentlist[i].studentbooklist.remove(book)


book1 = Books("Black Hole Theory", 1210)
book2 = Books("Puss in Boots", 1232)
book3 = Books("Modern Biology", 1989)
book4 = Books("Quantum Physics", 9001)
book5 = Books("Sherlok Holmes", 4521)
book6 = Books("Brief History of Time", 9081)
book7 = Books("Alice in Wonderland", 1909)
book8 = Books("Theory of Relativity", 6771)
bookstock = [book1, book2, book3, book5, book6, book7, book8]

student1 = Students("Harry Graham", 1200919, [])
student2 = Students("Jack Pierce", 1304250, [])
studentlist = [student1, student2]

# Adding book 4 to library
LibraryManagement(studentlist,bookstock).addBook(book4, bookstock)

# Removing book 2 to library
LibraryManagement(studentlist,bookstock).removeBook(book2, bookstock)

# Borrowing book 1 by student 1
LibraryManagement(studentlist,bookstock).borrowBook(book3, bookstock, student1)
LibraryManagement(studentlist,bookstock).borrowBook(book1, bookstock, student1)
LibraryManagement(studentlist,bookstock).submitBook(book3, bookstock, student1)
LibraryManagement(studentlist,bookstock).borrowBook(book3, bookstock, student2)
LibraryManagement(studentlist,bookstock).borrowBook(book4, bookstock, student1)
LibraryManagement(studentlist,bookstock).borrowBook(book5, bookstock, student1)
LibraryManagement(studentlist,bookstock).submitBook(book1, bookstock, student1)
LibraryManagement(studentlist,bookstock).borrowBook(book7, bookstock, student2)


# Printing library state
print ("----------------------- Library Management System -----------------------")
print ("-------------------------------------------------------------------------")
print ("----------------------- Current books in the library -----------------------")
for i in range(len(bookstock)):
    print (str(bookstock[i].bookname) + "\t \t" + str(bookstock[i].booknumber))

print ("----------------------- Current books with students -----------------------")
for i in range(len(studentlist)):
    print (str(studentlist[i].stdname) + ": -----")
    for j in range(len(studentlist[i].studentbooklist)):
        print ("\t \t" + str(studentlist[i].studentbooklist[j].bookname) + "\t \t" + str(studentlist[i].studentbooklist[j].booknumber))
