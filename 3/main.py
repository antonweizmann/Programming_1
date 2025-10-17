import in_out_handler as ioh

def book_handler_single(word_count):
    print("Simply enter the filepath of the book you would like to measure")
    book_file = ioh.open_book()
    for line in book_file:
        words = line.split()
        word_count += len(words)
    book_file.close()

def book_handler_series(word_count):
    books = []
    books = ioh.open_series()
    for book in books:
        for line in book:
            words = line.split()
            word_count += len(words)
    ioh.close_series(books)

print("Welcome to the Book Measurer! Do you want to measure only a single book [1] or an entire series [2]")
selection = int(ioh.my_input(0))
total_word_count = 0
average_word_count = 90000
if selection == 1:
    book_handler_single(total_word_count)
elif selection == 2:
    book_handler_series(total_word_count)
else:
    print("The input mode does not exist.")
    exit(1)
number_of_books = total_word_count / average_word_count
print("The average word count of a book is \033[1m" + str(average_word_count) + "\033[0m words")
print("In comparison the book or series you entered has \033[1m" + str(total_word_count) + "\033[0m words")
print("This means that your book or series equals \033[1m" + str(number_of_books) + "\033[0m books")
