import sys, io, os

def my_input(expected_type: int):
    out = None
    while True:
        try:
            if expected_type == 0:
                out = int(input())
            elif expected_type == 1:
                out = input()
            else:
                print("Error: no known expected type specified", file=sys.stderr)
            break
        except ValueError:
            if expected_type == 0:
                print("Error: expected input is an integer")
    return out

def open_book():
    logfile = create_log_file()
    if logfile is None:
        print("Failed to create logfile, proceeding without logging to file.")
    while True:
        book_path = my_input(1)
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

def create_log_file():
    try:
        logfile = io.open("logfile.txt", "w", encoding="utf-8")
        return logfile
    except OSError as e:
        print("Error opening logfile:", e)
        return None

def open_series():
    print("Please enter the filepath of the folder containing the solely series you would like to measure.")
    opened_books = []
    logfile = create_log_file()
    if logfile is None:
        print("Failed to create logfile, proceeding without logging to file.")
    while True:
        folder_path = my_input(1)
        try:
            closed_books = os.listdir(folder_path)
            break
        except OSError as e:
            error_msg = "Error: " + str(e) + ". Please enter the path again."
            print(error_msg)
            if logfile:
                logfile.write(error_msg + "\n")
                logfile.flush()
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
    if logfile:
        logfile.close()
    return opened_books

def close_series(books):
    for book in books:
        book.close()
        books.remove(book)
