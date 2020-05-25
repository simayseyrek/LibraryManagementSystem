from Library_DB import Library_DB
from Book import Book
from User import User

if __name__ == "__main__":
    db = Library_DB()

    user1 = User(20202305,"simay seyrek", "simay@gmail.com", "1254ss",1)
    book2 = Book(5135566, "kavuşamayanlar2", "ayt", 2050, "komed", 50)
    book1 = Book(123345, "kavuşamayanlar", "simay seyrek", 2020, "dram", 90)
    #db.add_user(user1)
    #db.add_book(book2)
    db.add_book(book1)
    myresult = db.get_all_books()  
    for x in myresult:
        print(x)