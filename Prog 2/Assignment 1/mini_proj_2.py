#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io


def read_database(filename='movie_dataset.txt'):
    """ Reading from a text file and creating a database using a dictionary 

    This function reads a text file with movies, each entry on a new line with the following format : 
                    "_title_of_the_movie_" _rating_ _duration_in_minutes_
    The title of the movie might be several words long. 
    The rating is a float and the duration is a whole number representing minutes
    The function creates a dictionary with keys the movie titles and value a tuple of 
    the respective rating and duration. If two movie entries have the same title,
    the movie with the longer duration should be kept. If the filename is invalid the 
    program returns None

    params : 
            filename - string - the name of the file to be read, default = "movie_dataset.txt"
    returns : 
            list of lists with name, rating and duration of each movie as strings
    """
    movies = {}
    try:
        with io.open(filename, 'r') as movie_file:
            for line in movie_file:
                closing_idx = line.find("\"", 1)
                title = line[1:closing_idx]
                remaining_line = line[closing_idx + 1:].split()
                if len(remaining_line) != 2:
                    print("Line format wrong", file=sys.stderr)
                    continue
                try:
                    rating = float(remaining_line[0])
                    duration = int(remaining_line[1])
                except ValueError:
                    print("Wrong rating or duration format", file=sys.stderr)
                    continue
                if title in movies:
                    if duration > movies[title][1]:
                        movies[title] = (rating, duration)
                else:
                    movies[title] = (rating, duration)
        return movies
    except OSError as e:
        print("Error opening database: ", e, file=sys.stderr)
        return None


def movie_title_list(movies: dict):
    """
    This function iterates over a dictionary and makes a list of all available keys.
    In the case of the movies dict this then returns a list of all movie names.
    params :
        movies - dict - database of movies contained in the program
    """
    movie_names = []
    for movie in movies.keys():
        movie_names.append(movie)
    return movie_names


def avg_duration(movies: dict, min_rating: float):
    """This function returns the average duration of all movies with a rating higher than the input rating.
   params :
        movies - dict - database of movies contained in the program
        rating - float - all movies with a rating higher that the specified rating will be included in the average duration.
    """
    rating = 0
    rating_check = 0
    number_of_movies = 0
    duration = 1
    avg_dur = 0
    total_duration = 0
    for movie in movies.values():
        if movie[rating] > min_rating:
            rating_check = 1
            if movie[duration] == 0:
                continue
            else:
                number_of_movies += 1
                total_duration += movie[duration]
        else:
            continue
    if number_of_movies != 0:
        avg_dur = total_duration / number_of_movies
    if rating_check == 0:
        return None
    else:
        return avg_dur


def best_rated_movie(movies: dict, min_dur: int, max_dur: int, choose_shortest: bool):
    """
        This function returns the movie title with the highest rating with a duration
between min_dur and max_dur (included). The optional parameter choose_shorter indicates what to do in case of a tie.
- If choose_shortest is True, the shortest movie is returned in case of a tie in the
ratings. Otherwise, the longest one is returned.
- In case no movies in the dictionary fulfill the requirements the function should return

params:
    movies - dict - database of movies contained in the program
    min_dur - int - minimum duration of all movies that should be considered
    max_dur - int - maximum duration of all movies that should be considered
    choose_shortest - bool - specifies how to handle two tied ratings. True for choosing the shorter movie and false for the longer one.

    """
    first_movie = next(iter(movies))
    highest_rated_movie = movies[first_movie]
    rating = 0
    duration = 1
    requirements = 0
    for movie in movies:
        if movie[duration] in range(min_dur, max_dur + 1):
            requirements = 1
            if movie[rating] > highest_rated_movie[rating]:
                highest_rated_movie = movie
            elif movie[rating] == highest_rated_movie[rating] and choose_shortest == True:
                if movie[duration] < highest_rated_movie[duration]:
                    highest_rated_movie = movie
            elif movie[rating] == highest_rated_movie[rating]:
                if movie[duration] > highest_rated_movie[duration]:
                    highest_rated_movie = movie
    if requirements == 0:
        return None
    else:
        return highest_rated_movie.key()


def main():
    """
        The function main() is already partially implemented. It first calls the function
        read_data(). Then asks for the user input to choose 1 out of 4 options (which call for
        one of the functions above with the appropriate arguments).

        1: print all the movie titles in the dataset. Usage: (input the following string) ’1’.

        2: show the average duration of all movies with rating of your choice. Usage: enter
        ’2’ and rating separated by space, e.g. ’2 8.8’.

        3: find the rating of a specific movie. Usage: enter ’3’ and movie name separated
        by space, e.g. ’3 Coco’. Note that the movie name can have more than 1 word.

        4: find the best rated movie within a given duration range. Usage: enter ’4’, the
        minimal and maximal wanted duration and a flag which can be either ’True’ or
        ’False’, e.g. ’4 60 120 True’. If you enter ’True’ the shortest best movie will be
        presented, otherwise the longest best movie",
    """

    movie_dict = read_database("movie_dataset.txt")
    
    print("Choose one of the below options",
          "1: print all the movie titles in our dataset",
          "2: compute average duration above a rating (e.g. '2 8.8')",
          "3: find the rating of a movie (e.g. '3 Coco')",
          "4: find the best rated movie within a given duration range (e.g. '4 60 120 True')",
          sep='\n ')
    if len(sys.argv) == 1:
        user_input = input()
        user_input = user_input.split()
    else:
        user_input = sys.argv[1:]
    if len(user_input) == 1 and user_input[0] == '1':
        movie_names = movie_title_list(movie_dict)
        for name in movie_names:
            print(name)

        return
    elif len(user_input) == 2 and user_input[0] == '2':
        print(avg_duration(movie_dict, float(user_input[1])))
        return
    elif len(user_input) >= 2 and user_input[0] == '3':
        movie_name = " ".join(user_input[1:])
        print(movie_name)
        print(movie_dict[movie_name][0])
        return
    elif len(user_input) == 4 and user_input[0] == '4':
        min_duration = int(user_input[1])
        max_duration = int(user_input[2])
        flag = user_input[3].lower() == 'true'
        
        print(best_rated_movie(movie_dict, min_duration, max_duration, flag))
    else: 
        print("Wrong input", file=sys.stderr)
        return

if __name__ == '__main__':    
    main()


