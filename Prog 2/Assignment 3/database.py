import csv


def get_database() -> dict:
    """Read database from file and return as dictionary"""
    database = {}
    try:
        with open("goodreads.txt", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 7:
                    title = row[0]
                    database[title] = row[1:]
    except FileNotFoundError:
        print("Error: goodreads.txt file not found")
        exit(1)
    except OSError as e:
        print(f"Error opening database: {e}")
        exit(1)
    return database


def write_database(database):
    """Write database dictionary back to file"""
    try:
        with open("goodreads.txt", 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow(['title', 'authors', 'average_rating', 'language_code',
                             'num_pages', 'ratings_count', 'publication_date'])

            # Write all books
            for title, fields in database.items():
                writer.writerow([title] + fields)
    except OSError as e:
        print(f"Error writing database: {e}")
        exit(1)
