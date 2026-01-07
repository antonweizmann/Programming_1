import numpy as np
import database as db
import sys

# Dictionary to store all books
database = db.get_database()


def my_input(expected_type: int, msg):
    """Get input from user with type checking"""
    out = None
    while True:
        try:
            if expected_type == 0:
                out = int(input(msg + "\n"))
            elif expected_type == 1:
                out = input(msg + "\n")
            elif expected_type == 2:
                out = float(input(msg + "\n"))
            else:
                print("Error: no known expected type specified", file=sys.stderr)
            break
        except ValueError:
            if expected_type == 0:
                print("Error: expected input is an integer")
            elif expected_type == 2:
                print("Error: expected input is a number")
    return out


def get_new_book():
    """Get book info from user and return as tuple"""
    title = my_input(1, "Please enter the title of the new book")
    authors = my_input(1, "Please enter the name of the author")
    rating = str(my_input(2, "Please enter the average rating"))
    language = my_input(1, "Please enter the language code")
    pages = str(my_input(0, "Please enter the number of pages"))
    ratings_count = str(my_input(0, "Please enter the ratings count"))
    pub_date = my_input(1, "Please enter the publication date")

    # Return tuple for immutability
    book_data = (authors, rating, language, pages, ratings_count, pub_date)
    return title, book_data


def add_book():
    """Add a new book to the database (uses Dictionary and Tuple)"""
    title, book_data = get_new_book()

    if title in database:
        overwrite = input(f"Book '{title}' already exists. Overwrite? (yes/no): ").lower()
        if overwrite != 'yes' and overwrite != 'y':
            print("Book not added.")
            return

    # Convert tuple to list for storage
    database[title] = list(book_data)
    print(f"Book '{title}' added successfully!")


def print_info(book):
    """Print book information"""
    print(f"Author: {book[0]}")
    print(f"Rating: {book[1]}")
    print(f"Language: {book[2]}")
    print(f"Pages: {book[3]}")
    print(f"Ratings Count: {book[4]}")
    print(f"Publication Date: {book[5]}")


def find_book():
    """Search for a book by title (uses Dictionary)"""
    while True:
        search = input("Please enter the title of the book you would like to search\n")
        if search:
            break

    if search in database:
        print(f"\nFound: {search}")
        print_info(database[search])
    else:
        print(f"The book '{search}' was not found")


def authors_books():
    """Find all books by an author (uses Dictionary)"""
    while True:
        author = input("Please enter the name of the author you would like to search\n")
        if author:
            break

    found = False
    print(f"\nBooks by authors matching '{author}':\n")

    for title, book_data in database.items():
        if author.lower() in book_data[0].lower():
            print(f"\nTitle: {title}")
            print_info(book_data)
            found = True

    if not found:
        print(f"No books found by authors matching '{author}'")


def book_recommendation():
    """Get book recommendations by rating and pages (uses Dictionary)"""
    min_rating = my_input(2, "Please enter the minimum rating of the books")
    max_pages = my_input(0, "Please enter the maximum number of pages")

    found = False
    print(f"\nBooks with rating >= {min_rating} and pages <= {max_pages}:\n")

    for title, book_data in database.items():
        try:
            rating = float(book_data[1])
            pages = int(book_data[3])

            if rating >= min_rating and pages <= max_pages:
                print(f"\nTitle: {title}")
                print_info(book_data)
                found = True
        except (ValueError, IndexError):
            continue

    if not found:
        print("No books found matching your criteria")


def database_statistics():
    """Show database statistics (uses NumPy Array)"""
    print("\n" + "=" * 60)
    print("DATABASE STATISTICS")
    print("=" * 60)

    ratings = []
    pages = []
    rating_counts = []

    # Collect data from dictionary
    for title, book_data in database.items():
        try:
            ratings.append(float(book_data[1]))
            pages.append(int(book_data[3]))
            rating_counts.append(int(book_data[4]))
        except (ValueError, IndexError):
            continue

    if not ratings:
        print("No valid data to analyze")
        return

    # Convert to numpy arrays for calculations
    ratings_array = np.array(ratings)
    pages_array = np.array(pages)
    counts_array = np.array(rating_counts)

    print(f"\nTotal books in database: {len(database)}")
    print(f"Books with valid data: {len(ratings)}")

    print("\n--- RATINGS ANALYSIS ---")
    print(f"Average rating: {np.mean(ratings_array):.2f}")
    print(f"Median rating: {np.median(ratings_array):.2f}")
    print(f"Highest rating: {np.max(ratings_array):.2f}")
    print(f"Lowest rating: {np.min(ratings_array):.2f}")
    print(f"Standard deviation: {np.std(ratings_array):.2f}")

    print("\n--- PAGE COUNT ANALYSIS ---")
    print(f"Average pages: {np.mean(pages_array):.0f}")
    print(f"Median pages: {np.median(pages_array):.0f}")
    print(f"Longest book: {np.max(pages_array)} pages")
    print(f"Shortest book: {np.min(pages_array)} pages")

    print("\n--- POPULARITY ANALYSIS ---")
    print(f"Average ratings count: {np.mean(counts_array):.0f}")
    print(f"Most rated book: {np.max(counts_array)} ratings")
    print(f"Least rated book: {np.min(counts_array)} ratings")

    max_rating_idx = np.argmax(ratings_array)
    max_rating_title = list(database.keys())[max_rating_idx]
    print(f"\nHighest rated book: '{max_rating_title}' ({ratings_array[max_rating_idx]:.2f})")

    print("=" * 60)


def exit_program():
    """Save database and exit"""
    db.write_database(database)
    print("Database saved successfully!")
    exit(0)


def main():
    """Main program loop"""
    print("Welcome to the Goodreads Book Database!")

    while True:
        print("\n" + "=" * 60)
        print("Choose an option:")
        print("  [1] Add a new book")
        print("  [2] Find a book by title")
        print("  [3] Get book recommendations")
        print("  [4] Find books by author")
        print("  [5] View database statistics")
        print("  [6] Save and exit")
        print("=" * 60)

        user_option = my_input(0, "Please choose a mode (1-6)")

        match user_option:
            case 1:
                add_book()
            case 2:
                find_book()
            case 3:
                book_recommendation()
            case 4:
                authors_books()
            case 5:
                database_statistics()
            case 6:
                print("Thanks for using the database!")
                exit_program()
            case _:
                print("Invalid option, please choose 1-6")


if __name__ == "__main__":
    main()
