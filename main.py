from book import Book
from borrwing_order import Borrwing_order
from client import Client
from librarian import Librarian

list_clients = []
list_librarians = []
list_books = []
list_borrowed_order = []

def create_new_client():
    number_clients = int(input("Enter the number of clients: "))
    i = 0
    while i < number_clients:
        id = input(f"Enter the id noumber of client{i+1}: ")
        full_name = input("Enter the full name: ")
        age = input("Enter the age: ")
        id_no = input("id number: ")
        phone_no = input("phone noumber: ")
        client1 = Client(id, full_name, age, id_no, phone_no)
        list_clients.append(client1)
        i += 1

def create_new_librarian():
    id = input("Enter the id noumber of new librarian: ")
    full_name = input("Enter the name: ")
    age = input("Enter the age: ")
    id_no = input("id: ")
    emplyment_type = input("the type of emplyment: ")
    librarian1 = Librarian(id, full_name, age, id_no, emplyment_type)
    list_librarians.append(librarian1)

def borrwing_new_book():
    new_id = ""
    id = input("Enter the id: ")
    date = input("Enter the date: ")
    client_id = input("Enter the client id: ")
    for item in list_clients:
        if item.id == client_id:
            new_id = item.full_name
            break
    book_id = input("Enter the book id: ")
    for item1 in list_books:
        if book_id == item1.id:
            new_id_book = item1.title
            status_book = item1.status

            if item1.status == "active":
                print("The book is active, you can borrow it")

            else:
                print("The book is not active, you can't borrow it")
                break
            client_id = new_id
            book_id = new_id_book
            status = status_book
            borrwing_order1 = Borrwing_order(id, date, client_id, book_id, status)
            list_borrowed_order.append(borrwing_order1)
    for value in list_borrowed_order:
        print(value.id, value.date, value.client_id, value.book_id, value.status)

def create_new_books():
    number_books = int(input("Enter the number of books: "))
    i = 0
    while i < number_books:
        id = input(f"Enter the id noumber book{i+1}: ")
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        author = input("author: ")
        status = input("status (active, not active): ")
        book1 = Book(id, title, description, author, status)
        list_books.append(book1)
        i += 1

#   impliment

create_new_client()
create_new_librarian()
create_new_books()


print("1- If you want to enter as a client press number '1'\n2- if you want to enter as a librarian, press number '2'")
click = input("")

if click  == "1":
    print("1-If you want to inquire about existing books, press '1'\n2- If you want to borrow a book, press number '2'")
    click1 = input("")

    if click1 == "1":
        print("The books are:")
        for name_books in list_books:
            print(f"the title is {name_books.title},the status is {name_books.status}\n\n")

    elif click1 == "2":
        borrwing_new_book()

elif click == "2":
    print("1-If you want to inquire about existing books, press '1'\n2- If you want to add a new book press '2'\n3- If you want to know the orders press '3'\n")
    click2 = input("")
    if click2 == "1":
        print("The books are:")
        for name_books in list_books:
            print(f"the title is {name_books.title}, the status is {name_books.status}\n\n")
    elif click2 == "2":
        create_new_books()
    elif click2 == "3":
        for value in list_borrowed_order:
            print(value.id, value.client_id, value.book_id, value.status)
else:print("wrong entry")

