class Library:
    
    book_list = []
    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)

class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id + 100
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability == True :
            self.__availability = False
    def return_book(self):
        if self.__availability == False :
            self.__availability = True
    def view_book_info(self):
        if(self.__availability):
            avail = "Yes"
        else:
            avail = "No"
        print(f'Book ID: {self.__book_id}, Title: {self.__title},  Author: {self.__author}, Available : {avail}')



books = [
    Book(1, "AI Basics", "John Smith", True),
    Book(2, "Advanced AI", "Jane Doe", True),
    Book(3, "Machine Learning Fundamentals", "Alice Johnson", True),
    Book(4, "Deep Learning with Python", "Robert Brown", True),
    Book(5, "AI for Beginners", "Emily Davis", True),
    Book(6, "Practical Machine Learning", "Michael Wilson", True),
    Book(7, "Python Programming for AI", "Sarah White", True),
    Book(8, "Artificial Intelligence in Practice", "David Harris", True),
    Book(9, "Machine Learning for Developers", "Sophia Martin", True),
    Book(10, "Python for Data Science and AI", "Chris Thompson", True),
]  

while True:
    print(f'1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit.')
    choice = input('Enter your choice: ')
    if choice == '1':
        for book in Library.book_list:
            book.view_book_info()
    elif choice == '2':
        book_id = int(input('Enter Book ID to borrow: '))
        for book in Library.book_list:
            if book._Book__book_id == book_id:
                book.borrow_book()
            print(f'Book ID {book_id} not found.')
    elif choice == '3':
        book_id = int(input('Enter Book ID to return: '))
        for book in Library.book_list:
            if book._Book__book_id == book_id:
                book.return_book()
        print(f'Book ID {book_id} not found.')
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')