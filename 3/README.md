This project is for the Programming 1 course in the Artificial Intelligence Bachelor at Radboud University

I will be making an application that evaluates the length of input books. There will be two modes.
The first mode takes a single file-path as input. This has to be a .txt file
The second mode takes a folder-path as input. The folder should contain only .txt. This function is meant to be used to evaluate the length of a book series.

In case of mode 1, the evaluation is done by reading the file line by line, taking the word count and then comparing that to the "average" length of a book (which is set to 90 000)
In case of mode 2, first all files contained in the input folder will be scanned into a list. 
    The program will then iterate over every single file and again evaluate by reading the file line by line and taking the word count (which is added to a global total word count)
    After the program has finished iterating over every file in the folder, it will then compare the global word count against the "average" length of a book again.
Both modes will then return the number of "normal" books the input book or series is equal to and the word count itself.

Project requirements:
    Comparisons and logical operations
        In the global namespace the program uses a comparison to determine what mode to start.
    if statements (with elif and else)
        In function book_measurer the program uses a if statement (with elif and else) to determine which mode to start and it also handles the case in which a wrong mode was specified.
    Lists and at least 3 different list manipulations
        In open_series the index of each element is used in a status message and a list containing all opened books is created using append.
        In get_series the opened list is iterated over and in close_series all elements of the list are removed one by one.
    for and while loops 
        In get_series a while loop is used to ensure the input filepath is correct.
        In open_series a for loop is used to iterate over a list of closed books, which are then opened.
    Calls for input() and print() functions
        In my_input input is called.
        Print is used in to show the results in the global namespace
    try statements
        The my_input function uses try and except to check that the correct value was assigned to a variable (like a number to an int)
    Typecasting between different types
        In the global namespace the word count and other numbers are converted to string so that they can be printed out.
    At least 2 well-designed functions (Lecture 5)
        The function get_folder_cont 
        The function open_series iterates over the list of closed_books, opens every books and adds the opened book to the opened_books list.
    Write and read information from files (Lecture 6)
        The function get_folder_cont writes an error_msg into a logfile in case of an error.
        The function open_series opens files in the read mode.
        The function create_logfile opens and creates a logfile in write mode
        The function book_handler_series iterates over all books and reads them line by line.

Authorship:
I declare that the work submitted here is from my authorship only. I haven’t used any generative AI to help with
any code/text included in my work. I have given credit for the help I had conceptualizing my project. My work
respects the university and course code of conduct

