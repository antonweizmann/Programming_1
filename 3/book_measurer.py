import in_out_handler as ioh

average_word_count = 90000

def book_handler_single():
    print("Simply enter the filepath of the book you would like to measure")
    word_count = 0
    book_file = ioh.open_book()
    for line in book_file:
        words = line.split()
        word_count += len(words)
    number_of_books = word_count / average_word_count
    print("The average word count of a book is \033[1m" + str(average_word_count) + "\033[0m words")
    print("In comparison the book you entered has \033[1m" + str(word_count) + "\033[0m words")
    print("This means that you book equals \033[1m" + str(number_of_books) + "\033[0m books")
    book_file.close()

def book_handler_series():
    total_word_count = 0
    books = []
    books = ioh.open_series()
    for book in books:
        word_count = 0
        for line in book:
            words = line.split()
            word_count += len(words)
        total_word_count += word_count

    number_of_books = total_word_count / average_word_count
    print("The average word count of a book is \033[1m" + str(average_word_count) + "\033[0m words")
    print("In comparison the book you entered has \033[1m" + str(total_word_count) + "\033[0m words")
    print("This means that you book equals \033[1m" + str(number_of_books) + "\033[0m books")
    ioh.close_series(books)


def book_measurer():
    print("Welcome to the Book Measurer! Do you want to measure an entire series [1] or only a single book [2]")
    selection = int(input())
    if selection == 1:
        book_handler_series()
    elif selection == 2:
        book_handler_single()

book_measurer()