import pandas as pd

class Library:
    def __init__(self):
        self.books = pd.read_csv('books.csv')
        self.members = pd.read_csv('members.csv')
        self.borrowings = pd.read_csv('borrowings.csv')

    def add_book(self, book_id, title, author):
        new_book = {'BookID': book_id, 'Title': title, 'Author': author}
        self.books = self.books.append(new_book, ignore_index=True)
        self.books.to_csv('books.csv', index=False)

    def view_books(self):
        print(self.books)

    def add_member(self, member_id, name):
        new_member = {'MemberID': member_id, 'Name': name}
        self.members = self.members.append(new_member, ignore_index=True)
        self.members.to_csv('members.csv', index=False)

    def view_members(self):
        print(self.members)

    def borrow_book(self, book_id, member_id):
        new_borrowing = {'BookID': book_id, 'MemberID': member_id}
        self.borrowings = self.borrowings.append(new_borrowing, ignore_index=True)
        self.borrowings.to_csv('borrowings.csv', index=False)

    def return_book(self, book_id):
        self.borrowings = self.borrowings[self.borrowings.BookID != book_id]
        self.borrowings.to_csv('borrowings.csv', index=False)

if __name__ == "__main__":
    library = Library()
    while True:
        print("\n1. Add Book\n2. View Books\n3. Add Member\n4. View Members\n5. Borrow Book\n6. Return Book\n7. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(book_id, title, author)
        elif choice == 2:
            library.view_books()
        elif choice == 3:
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(member_id, name)
        elif choice == 4:
            library.view_members()
        elif choice == 5:
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            library.borrow_book(book_id, member_id)
        elif choice == 6:
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)
        elif choice == 7:
            break
