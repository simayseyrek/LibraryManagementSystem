import csv
import random
from Library import Library

lib = Library()
category_list = ['Fantasy', 'Adventure', 'Romance', 'Contemporary', 'Dystopian']
# book database from http://www2.informatik.uni-freiburg.de/~cziegler/BX/
with open('books.csv', newline='', encoding="ISO-8859-1") as csvfile:
    line = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in line:
        try:
            isbn = int(row[0].replace('X', '0'))
            title = row[1]
            author = row[2]
            publish_year = int(row[3])
            category = category_list[random.randint(0, 4)]
            page_number = int(random.randint(50, 500))
            lib.add_book(isbn, title, author, publish_year, category, page_number)
            # print(str(isbn) + title + author + str(publish_year) + category + str(page_number))
        except:
            continue
