import sys, io, os

def my_input(expected_type: int, msg):
    """Makes sure the correct variable type is input
     :param expected_type: The type of variable expected for this input. 0 means integer and 1 means string.
     :param msg: The message the users is show with the input statement
     :return: the input variable of correct type
     """
    out = None
    while True:
        try:
            if expected_type == 0:
                out = int(input(msg + "\n"))
            elif expected_type == 1:
                out = input(msg + "\n")
            else:
                print("Error: no known expected type specified", file=sys.stderr)
            break
        except ValueError:
            if expected_type == 0:
                print("Error: expected input is an integer")
    return out

def create_log_file():
    """ Creates a logfile called logfile.txt in write mode
     :return: opened logfile in write mode
     """
    try:
        logfile = io.open("logfile.txt", "w", encoding="utf-8")
        return logfile
    except OSError as e:
        print("Error opening logfile:", e)
        return None

def open_book(logfile):
    """Asks the uses for the filepath of the book and opens it. In case of error it asks again and wrties into the logfile
    :param logfile: Opened logfile which errors and status messages will be written into
    :return: opened book_file in read mode
    """
    while True:
        book_path = my_input(1, "Simply enter the filepath of the book you would like to measure")
        try:
            book_file = io.open(book_path, "r", encoding="utf-8")
            break
        except OSError:
            error_msg = "The input filepath was not correct. Please enter the path again."
            print(error_msg)
            if logfile:
                logfile.write(error_msg + "\n")
                logfile.flush()
    if logfile:
        logfile.close()
    return book_file

def get_folder_cont(logfile):
    """Asks the uses for the filepath of the folder containing the series and gets a list containing all files contained in the folder.
    In case of error it asks again and wrties into the logfile
     :param logfile: Opened logfile which errors and status messages will be written into
     :returns: the path of the folder, a list containing all closed books
     """
    while True:
        folder_path = my_input(1, "Please enter the filepath of the folder containing the solely series you would like to measure.")
        try:
            closed_books = os.listdir(folder_path)
            break
        except OSError as e:
            error_msg = "Error: " + str(e) + ". Please enter the path again."
            print(error_msg)
            if logfile:
                logfile.write(error_msg + "\n")
                logfile.flush()
    return folder_path, closed_books

def open_series(logfile, closed_books, folder_path):
    """Iterates over the closed books, opens them and adds them to a list containing all opened books
     :param logfile: Opened logfile which errors and status messages will be written into
     :param closed_books: A list containing all closed books
     :param folder_path: The path of the folder containing the series
     :return: A list containing all opened books
     """
    opened_books = []
    for book in closed_books:
        status_msg = "Opening book number " + str(closed_books.index(book)) + ": " + str(book)
        print(status_msg)
        if logfile:
            logfile.write(status_msg + "\n")
            logfile.flush()
        try:
            book_path = folder_path + "/" + book
            book_file = io.open(book_path, "r", encoding="utf-8")
            opened_books.append(book_file)
        except OSError:
            print(book, " could not be opened")
            continue
    return opened_books

def get_series(logfile):
    """Handles the process of getting a list of all opened books by calling functions.
     :param logfile: Opened logfile which errors and status messages will be written into
     :return: a list with all opened books
     """
    folder_path, closed_books = get_folder_cont(logfile)
    opened_books = open_series(logfile, closed_books, folder_path)
    if logfile:
        logfile.close()
    return opened_books

def close_series(books):
    """Closes all opened books and removes them from the list books
     :param books: A list of all opened books
     """
    for book in books:
        book.close()
        books.remove(book)
