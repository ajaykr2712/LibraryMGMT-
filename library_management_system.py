import pandas as pd

class LibraryManagementSystem:
    def __init__(self):
        self.books_df = pd.read_csv('books.csv')
        self.members_df = pd.read_csv('members.csv')
        self.borrowings_df = pd.read_csv('borrowings.csv')

    def add_book(self, book_id, book_title, book_author):
        new_book_entry = {'BookID': book_id, 'Title': book_title, 'Author': book_author}
        self.books_df = self.books_df.append(new_book_entry, ignore_index=True)
        self.books_df.to_csv('books.csv', index=False)

    def display_books(self):
        print(self.books_df)

    def add_member(self, member_id, member_name):
        new_member_entry = {'MemberID': member_id, 'Name': member_name}
        self.members_df = self.members_df.append(new_member_entry, ignore_index=True)
        self.members_df.to_csv('members.csv', index=False)

    def display_members(self):
        print(self.members_df)

    def borrow_book(self, book_id, member_id):
        new_borrowing_entry = {'BookID': book_id, 'MemberID': member_id}
        self.borrowings_df = self.borrowings_df.append(new_borrowing_entry, ignore_index=True)
        self.borrowings_df.to_csv('borrowings.csv', index=False)

    def return_book(self, book_id):
        self.borrowings_df = self.borrowings_df[self.borrowings_df.BookID != book_id]
        self.borrowings_df.to_csv('borrowings.csv', index=False)

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    
    while True:
        print("\n1. Add Book\n2. View Books\n3. Add Member\n4. View Members\n5. Borrow Book\n6. Return Book\n7. Exit")
        user_choice = int(input("Enter choice: "))
        
        if user_choice == 1:
            book_id = input("Enter Book ID: ")
            book_title = input("Enter Book Title: ")
            book_author = input("Enter Book Author: ")
            library_system.add_book(book_id, book_title, book_author)
        
        elif user_choice == 2:
            library_system.display_books()
        
        elif user_choice == 3:
            member_id = input("Enter Member ID: ")
            member_name = input("Enter Member Name: ")
            library_system.add_member(member_id, member_name)
        
        elif user_choice == 4:
            library_system.display_members()
        
        elif user_choice == 5:
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            library_system.borrow_book(book_id, member_id)
        
        elif user_choice == 6:
            book_id = input("Enter Book ID to return: ")
            library_system.return_book(book_id)
        
        elif user_choice == 7:
            break
