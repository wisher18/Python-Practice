class Library:
    def __init__(self, books, name):
        self.bookList = books
        self.name = name
        self.lendDict = {}
    def display(self):
        print(f"Welcome to the {self.name} Library")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book : user})
            print("Lender book data has been updated, Now you can take ur book.")
        else:
            print(f"the book is already taken by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    bhushan = Library(["Rich dad", "Poor dad", "Python", "Pycharm", "Java"], "wisher's")
    while(True):
        print(f"Welcome to the {bhushan.name} Library. \n Enter Your Choice to Continue.")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. Add Books")
        print("4. Return Books")
        choice = int(input("Enter the choice here:"))
        if choice== 1:
            bhushan.display()
        elif choice== 2:
            book = input("Enter the book name u want to take.")
            user = input("Enter your name.:")
            bhushan.lendBook(user,book)
        elif choice == 3:
            book = input("Enter the book name you want to Danate:")
            bhushan.addBook(book)
        elif choice == 4:
            book = input("Enter the book name your returning")
            bhushan.returnBook(book)
        else: print("Invalid Input!!!")

        print("Press q to quit() and c to continue().")
        choice2 = ""
        while (choice2!= "q" and choice2 != "c"):
            choice2 = input("Enter ur choice now:")
            if choice2 == "q":
                exit()
            elif choice2 == "c":
                continue