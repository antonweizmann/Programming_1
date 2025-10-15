This project is for the Programming 1 course in the Artificial Intelligence Bachelor at Radboud University

I will be making an application that evaluates the length of input books. There will be two modes.
The first mode takes a single file name as input.
The second mode takes a list of files as input. This function is meant to be used to evaluate the length of a book series.

The evaluation by reading the file, taking the word count and then comparing that to the "average" length of a book (which I will define)
It will then return the number of "normal" books the input book is equal to, the word count itself.

my_input(int n)
    A function that uses try and except statements to ensure that the entered input is accepted.
    The integer n is used to switch between different input modes (what the program expects to receive).
    0 is used for integers.
    1 is used for strings.

