#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_database(filename='movie_dataset.txt'):
    """ Reading from a text file and creating a database using a dictionary 

    This function reads a text file with movies, each entry on a new line with the following format : 
                    "_title_of_the_movie_" _rating_ _duration_in_minutes_
    The title of the movie might be several words long. 
    The rating is a float and the duration is a whole number representing minutes
    The function creates a dictionary with keys the movie titles and value a tuple of 
    the respective rating and diration. If two movie entries have the same title, 
    the movie with the longer duration should be kept. If the filename is invalid the 
    program returns None

    params : 
            filename - string - the name of the file to be read, default = "movie_dataset.txt"
    returns : 
            list of lists with name, rating and duration of each movie as strings
    """

    return


def movie_title_list(movies: dict):
    """
        ToDo Write the documentation of this function similarly to the function above
    """
    return


def avg_duration(movies: dict, rating: float):
    """
        ToDo Write the documentation of this function similarly to the function above
    """
    return


def best_rated_movie(movies: dict, min_dur: int, max_dur: int, choose_shortest: bool):
    """
        ToDo Write the documentation of this function similarly to the function above
    """
    return


def main():
    """
        ToDo Write the documentation of this function similarly to the function above
    """

    movie_dict = read_database("movie_dataset.txt")
    
    print("Choose one of the below options",
          "1: print all the movie titles in our dataset",
          "2: compute average duration above a rating (e.g. '2 8.8')",
          "3: find the rating of a movie (e.g. '3 Coco')",
          "4: find the best rated movie within a given duration range (e.g. '4 60 120 True')",
          sep='\n ')
    user_input = input()
    user_input = user_input.split()
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
        print("Wrong input")
        return

if __name__ == '__main__':    
    main()


