import in_out_handler as ioh

def book_handler_single(logfile):
    """Iterates over the book and counts its words
    :param logfile: Opened logfile which errors and status messages will be written into
    :return: the number of words counted in this book
    :rtype: int
    """
    word_count = 0
    book_file = ioh.open_book(logfile)
    for line in book_file:
        words = line.split()
        word_count += len(words)
    book_file.close()
    return word_count

def book_handler_series(logfile):
    """Iterates over the book and counts its words
    :param logfile: Opened logfile which errors and status messages will be written into
    :return: the number of words counted in this series
    :rtype: int
    """
    word_count = 0
    books = ioh.get_series(logfile)
    for book in books:
        for line in book:
            words = line.split()
            word_count += len(words)
    ioh.close_series(books)
    return word_count

selection = int(ioh.my_input(0, "Welcome to the Book Measurer! Do you want to measure only a single book [1] or an entire series [2]"))
total_word_count = 0
average_word_count = 90000

logfile = ioh.create_log_file()
if logfile is None:
    print("Failed to create logfile, proceeding without logging to file.")
if selection == 1:
    total_word_count = book_handler_single(logfile)
elif selection == 2:
    total_word_count = book_handler_series(logfile)
else:
    print("The input mode does not exist.")
    exit(1)
number_of_books = total_word_count / average_word_count
print("The average word count of a book is \033[1m" + str(average_word_count) + "\033[0m words")
print("In comparison the book or series you entered has \033[1m" + str(total_word_count) + "\033[0m words")
print("This means that your book or series equals \033[1m" + str(round(number_of_books, 2)) + "\033[0m books")
